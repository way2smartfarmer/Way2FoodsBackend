from rest_framework import generics
from .models import Order, MyImage, Contact
from .serializers import OrderSerializer, ContactSerializer, MyImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MyImageView(generics.CreateAPIView):
    queryset = MyImage.objects.all()
    serializer_class = MyImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        # Parse the request data
        data = request.data
        name = data.get('name')
        place = data.get('place')
        pincode = data.get('pincode')
        phone = data.get('phone')
        message = data.get('message')

        # Create the Contact object
        contact = Contact(name=name, place=place,
                          pincode=pincode, phone=phone, message=message)
        contact.save()

        # Return a response
        return Response({'message': 'Contact created successfully'})
