from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from pims.models import Product, Supplier
from pims.serializers import ProductSerializer, SupplierSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F

# Create your views here.

class ProductView(APIView):

    #get product list based on filters
    def get(self, request):
        products = Product.objects.all()

        # Filter by supplier
        supplier_id = request.query_params.get('supplier_id')
        if supplier_id:
            products = products.filter(supplier_id=supplier_id)
        # Filter by price range
        min_price = request.query_params.get('min_price')
        if min_price:
            products = products.filter(price__gte=min_price)
        max_price = request.query_params.get('max_price')
        if max_price:
            products = products.filter(price__lte=max_price)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    #add products
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):

    #get product details based on primary key
    def get(self, request, pk):

        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    #update product details based on primary key
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #delete product based on primary key
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response("Item deleted successfully!")
        
    
class ProductStockView(APIView):

    #update stock based on product primary key
    def patch(self, request, pk):

        stock_change = request.data.get('stock_change')
        if stock_change and isinstance(stock_change, int):
            try:
                #prevent race condition during stock updation
                product_update = Product.objects.filter(pk=pk).update(stock_quantity=F('stock_quantity') + stock_change)
                return Response("Stock value updated!", status=status.HTTP_200_OK)
            except:
                return Response("Stock change value is invalid", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Stock change value is invalid", status=status.HTTP_400_BAD_REQUEST)


