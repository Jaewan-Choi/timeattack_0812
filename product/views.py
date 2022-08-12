from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductStatus
from user.models import User
from .serializers import ProductSerializer, ProductStatusSerializer
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ActiveProductView(APIView):

    def get(self, request):
        get_active = request.data['is_active']
        if get_active == True:
            active_true = Product.objects.filter(is_active=True)
            product_serializer = ProductSerializer(active_true, many=True)
        else:
            active_false = Product.objects.filter(is_active=False)
            product_serializer = ProductSerializer(active_false, many=True)
        return Response(product_serializer.data)

    def post(self, request):
        get_product = request.data['product']
        get_user = request.user
        find_product = Product.objects.get(name=get_product)
        find_user = User.objects.get(email=get_user)
        start_product = ProductStatus
        start_product.end_date = datetime.now() + relativedelta(years=1)
        start_product.product = find_product.id
        start_product.user = find_user.id
        product_status_serializer = ProductStatusSerializer(data=start_product)
        if product_status_serializer.is_valid():
            print('통과o')
            product_status_serializer.save()
        else:
            print(product_status_serializer)
        return Response()