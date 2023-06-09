
from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from .signals import order_created

from .models import Product, Banner, MetaLink, Shipping, ProductSpecification, CategoryLevelOne,  ProductHighlight, Collection,  Customer, ProductImage


class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count', 'image']


class ProductImageSerializer(serializers.ModelSerializer):
    images = serializers.ImageField()

    def create(self, validated_data):
        product_id = self.context.get('product_id')
        if product_id is None:
            raise serializers.ValidationError(
                "Product ID not found in context.")
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductImage
        fields = ['id', 'images']


class CategoryLevelOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLevelOne
        fields = "__all__"


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = "__all__"


class ProductHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHighlight
        fields = "__all__"


class MetaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaLink
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    collection = CollectionSerializer()
    specifications = ProductSpecificationSerializer(
        many=True, read_only=True)
    highlights = ProductHighlightSerializer(
        many=True, read_only=True)
    category_level_one = CategoryLevelOneSerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'sales_price',
                  'price', 'unit', 'quantity', 'available', 'brand_name', 'collection', 'description', 'image',  'specifications', 'highlights', 'category_level_one', 'meta_title', 'meta_description', 'meta_keywords']

    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, source='mrp_price')


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'date', 'name', 'description', 'rating', 'product']

#     def create(self, validated_data):
#         product = self.context.get('product')
#         if product:
#             validated_data['product'] = product
#         return super().create(validated_data)


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'sales_price']


# class CartItemSerializer(serializers.ModelSerializer):
#     product = SimpleProductSerializer()
#     total_price = serializers.SerializerMethodField()

#     def get_total_price(self, cart_item: CartItem):
#         return cart_item.quantity * cart_item.product.sales_price

#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity', 'total_price']


# class CartSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only=True)
#     items = CartItemSerializer(many=True, read_only=True)
#     total_price = serializers.SerializerMethodField()

#     def get_total_price(self, cart):
#         return sum([item.quantity * item.product.sales_price for item in cart.items.all()])

#     class Meta:
#         model = Cart
#         fields = ['id', 'items', 'total_price']


# class AddCartItemSerializer(serializers.ModelSerializer):
#     product_id = serializers.IntegerField()

#     def validate_product_id(self, value):
#         if not Product.objects.filter(pk=value).exists():
#             raise serializers.ValidationError(
#                 'No product with the given ID was found.')
#         return value

#     def save(self, **kwargs):
#         cart_id = self.context['cart_pk']
#         product_id = self.validated_data['product_id']
#         quantity = self.validated_data['quantity']

#         try:
#             cart_item = CartItem.objects.get(
#                 cart_id=cart_id, product_id=product_id)
#             cart_item.quantity += quantity
#             cart_item.save()
#             self.instance = cart_item
#         except CartItem.DoesNotExist:
#             self.instance = CartItem.objects.create(
#                 cart_id=cart_id, **self.validated_data)

#         return self.instance

#     class Meta:
#         model = CartItem
#         fields = ['id', 'product_id', 'quantity']


# class UpdateCartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['quantity']


class CustomerSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'membership']


# class OrderItemSerializer(serializers.ModelSerializer):
#     product = SimpleProductSerializer()

#     class Meta:
#         model = OrderItem
#         feilds = ['id', 'product', 'sales_price', 'quantity']


# class UpdateOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['payment_status']


# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True)

#     class Meta:
#         model = Order
#         fields = ['id', 'customer', 'placed_at', 'payment_status', 'items']


# class CreateOrderSerializer(serializers.Serializer):

#     cart_id = serializers.UUIDField()

#     def validate_cart_id(self, cart_id):
#         if not Cart.objects.filter(pk=cart_id).exists():
#             raise serializers.ValidationError(
#                 'No cart with the given ID was found.')
#         if CartItem.objects.filter(cart_id=cart_id).count() == 0:
#             raise serializers.ValidationError('The cart is Empty')
#         return cart_id

#     def save(self, **kwargs):
#         with transaction.atomic():
#             cart_id = self.validated_data['cart_id']
#             customer = Customer.objects.get(
#                 user_id=self.context['user_id'])
#             order = Order.objects.create(customer=customer)

#             cart_items = CartItem.objects \
#                 .select_related('product') \
#                 .filter(
#                     cart_id=cart_id)
#             order_items = [
#                 OrderItem(
#                     order=order,
#                     product=item.product,
#                     sales_price=item.product.sales_price,
#                     quantity=item.quantity
#                 ) for item in cart_items
#             ]

#             OrderItem.objects.bulk_create(order_items)
#             Cart.objects.filter(pk=cart_id).delete()

#             order_created.send_robust(self.__class__, order=order)

#             return order


# class SubscriberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscriber
#         fields = "__all__"


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
