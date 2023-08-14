from rest_framework import serializers
from .models import Products,  Invoice, Tables, Customer, SalesOrder, Attendance


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['code', 'name', 'description', 'sellingprice', 'imgid', 'category']

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['myinvoice',  'code', 'qty', 'customer', 'userid', 'discountype', 'discountvalue', 'status', 'branch', 'date', 'amount', ]
 
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
