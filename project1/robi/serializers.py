from rest_framework import serializers
from .models import Products, Mainmenu, Openorders, Orderlist, Attendance, Activityloggs, SalesOrdercancelled, SalesOrderkitchen


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class MainmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainmenu
        fields = '__all__'

class OpenordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Openorders
        fields = '__all__'

class OrderlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderlist
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ActivityloggsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activityloggs
        fields = '__all__'

class SalesOrdercancelledSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrdercancelled
        fields = '__all__'

class SalesOrderkitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderkitchen
        fields = '__all__'