from rest_framework import serializers
from pims.models import Product, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        supplier_data = validated_data.pop('supplier')
        supplier_name = supplier_data.get('name')
        supplier, created = Supplier.objects.get_or_create(name=supplier_name, defaults=supplier_data)

        product = Product.objects.create(supplier=supplier, **validated_data)
        return product

    def update(self, instance, validated_data):

        supplier_data = validated_data.pop('supplier')
        instance.supplier.name = supplier_data.get('name', instance.supplier.name)
        instance.supplier.contact_info = supplier_data.get('contact_info', instance.supplier.contact_info)
        instance.supplier.save()
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.images = validated_data.get('images', instance.images)
        instance.save()
        return instance
    