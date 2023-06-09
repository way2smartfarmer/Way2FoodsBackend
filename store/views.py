# from store.pagination import DefaultPagination
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .permissions import IsAdminOrReadOnly, FullDjangoModelPermissions, ViewCustomerHistoryPermission
from .filters import ProductFilter, SubCollectionFilter
from .models import Collection, Product, MetaLink,  Banner, Shipping,  Customer, ProductImage
from .serializers import CollectionSerializer, MetaLinkSerializer, BannerSerializer, ShippingSerializer, ProductSpecification, ProductSpecificationSerializer, ProductHighlightSerializer, ProductHighlight, ProductSerializer, CustomerSerializer,  ProductImageSerializer
from django.http import JsonResponse


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    # pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['title', 'description']
    ordering_fields = ['sales_price', 'last_update', 'stock']
    ordering = ['id']  # Set a default ordering, in case none is specified
    lookup_field = 'slug'  # Set the lookup field to use the slug instead of id

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by collection, if specified in query params
        collection_id = self.request.query_params.get('collection', None)
        if collection_id:
            queryset = queryset.filter(collection__id=collection_id)
        # Filter by category, if specified in query params
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        # Filter by search query, if specified in query params
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(
                description__icontains=search_query))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Sort by price, if specified in query params
        sort_by_price = request.query_params.get('sort', None) == 'price'
        sort_by_stock = request.query_params.get('sort', None) == 'stock'
        if sort_by_price:
            queryset = queryset.order_by('sales_price')
        elif sort_by_stock:
            queryset = queryset.order_by('stock')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@action(detail=False, methods=['GET'])
def availability(self, request, *args, **kwargs):
    queryset = self.get_queryset().filter(stock__gt=0)
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(title__icontains=query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response([])


class ProductSpecificationList(generics.ListAPIView):
    serializer_class = ProductSpecificationSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ProductSpecification.objects.filter(product_id=product_id)


class ProductHighlightList(generics.ListAPIView):
    serializer_class = ProductHighlightSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ProductHighlight.objects.filter(product_id=product_id)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self):
        return {'request': self.request}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        collection = get_object_or_404(
            Collection, pk=request.data['collection'])
        self.perform_create(serializer, collection)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, collection):
        serializer.save(collection=collection)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        collection = get_object_or_404(
            Collection, pk=request.data['collection'])
        self.perform_update(serializer, collection)
        return Response(serializer.data)

    def perform_update(self, serializer, collection):
        serializer.save(collection=collection)


# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         queryset = Review.objects.all()
#         product_slug = self.kwargs.get('product_slug')
#         if product_slug:
#             product = get_object_or_404(Product, slug=product_slug)
#             queryset = queryset.filter(product=product)
#         return queryset

#     def perform_create(self, serializer):
#         product_slug = self.kwargs.get('product_slug')
#         if product_slug:
#             product = get_object_or_404(Product, slug=product_slug)
#             serializer.save(product=product)
#         else:
#             serializer.save()


# class CartViewSet(CreateModelMixin,
#                   RetrieveModelMixin,
#                   DestroyModelMixin,
#                   GenericViewSet):
#     queryset = Cart.objects.prefetch_related('items__product').all()
#     serializer_class = CartSerializer

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         if 'pk' in self.kwargs:
#             context['cart_pk'] = self.kwargs['pk']
#         return context


# class CartItemViewSet(ModelViewSet):
#     http_method_names = ['get', 'post', 'patch', 'delete']
#     serializer_class = CartItemSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return AddCartItemSerializer
#         elif self.request.method == 'PATCH':
#             return UpdateCartItemSerializer
#         return CartItemSerializer

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['cart_pk'] = self.kwargs.get('cart_pk')
#         return context

#     def get_queryset(self):
#         return CartItem.objects.filter(cart_id=self.kwargs.get('cart_pk')).select_related('product')

#     def perform_create(self, serializer):
#         cart_pk = self.kwargs.get('cart_pk')
#         print(f'cart_pk: {cart_pk}')
#         serializer.save(cart_id=cart_pk)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('Ok')

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


# class OrderViewSet(ModelViewSet):
#     http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

#     # def get_permissions(self):
#     #     if self.request.method in ['PATCH', 'DELETE']:
#     #         return [IsAdminUser()]
#     #     return [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         serializer = CreateOrderSerializer(
#             data=request.data,
#             context={'user_id': self.request.user.id}
#         )
#         serializer.is_valid(raise_exception=True)
#         order = serializer.save()
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return CreateOrderSerializer
#         elif self.request.method == 'PATCH':
#             return UpdateOrderSerializer
#         return OrderSerializer

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff:
#             return Order.objects.all()

#         try:
#             customer_id = Customer.objects.only('id').get(user_id=user.id).id
#         except Customer.DoesNotExist:
#             customer_id = None
#         return Order.objects.filter(customer_id=customer_id)


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):

        context = super().get_serializer_context()
        if 'product_pk' in self.kwargs:
            context['product_id'] = self.kwargs['product_pk']
        return context

    def get_queryset(self):
        if 'product_pk' in self.kwargs:
            return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
        return ProductImage.objects.all()


# class SubscribeToProduct(ModelViewSet):
#     serializer_class = SubscriberSerializer

#     def get_queryset(self):
#         return Subscriber.objects.all()


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class ShippingViewSet(ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class MetaLinkViewSet(ModelViewSet):
    queryset = MetaLink.objects.all()
    serializer_class = MetaLinkSerializer
