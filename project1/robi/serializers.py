from rest_framework import serializers
from .models import Products, Mainmenu, Invoice, Openorders, Tables, Customer, SalesOrder, Orderlist, Attendance, Activityloggs, SalesOrdercancelled, SalesOrderkitchen


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['code', 'name', 'description', 'sellingprice', 'imgid', 'category']

class MainmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainmenu
        fields = '__all__'

from rest_framework import serializers

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['myinvoice',  'code', 'qty', 'customer', 'userid', 'status', 'branch', 'date', 'amount', ]
 

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
        fields = ['idno', 'surname', 'type']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first name', 'surname', 'phone']

class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ['name', 'description', 'status', 'userid']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['order','userid', 'totalamount', 'paymentmode', 'approvedby', 'approvaldate', 'type', 'paid', 'balance']

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