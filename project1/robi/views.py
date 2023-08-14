from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, SalesOrder, Customer, Invoice, Tables, Attendance
from .serializers import ProductsSerializer, CustomerSerializer, InvoiceSerializer, TablesSerializer, SalesOrderSerializer, AttendanceSerializer

class ProductsListView(APIView):
    def get(self, request):
        sellingprice_filter = request.query_params.get('sellingprice')
        name_filter = request.query_params.get('name')

        products = Products.objects.all()

        if sellingprice_filter:
            products = products.filter(sellingprice__exact=sellingprice_filter)

        if name_filter:
            products = products.filter(name__icontains=name_filter)

        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceListView(APIView):
    def get(self, request):
        order_filter = request.query_params.get('order')
        userid_filter = request.query_params.get('userid')
        totalamount_filter = request.query_params.get('totalamount')
        paymentmode_filter = request.query_params.get('paymentmode')
        approvedby_filter = request.query_params.get('approvedby')
        approvaldate_filter = request.query_params.get('approvaldate')
        type_filter = request.query_params.get('type')
        paid_filter = request.query_params.get('paid')
        balance_filter = request.query_params.get('balance')

        invoices = Invoice.objects.all()

        if order_filter:
            invoices = invoices.filter(order=order_filter)

        if userid_filter:
            invoices = invoices.filter(userid=userid_filter)

        if totalamount_filter:
            invoices = invoices.filter(totalamount=totalamount_filter)

        if paymentmode_filter:
            invoices = invoices.filter(paymentmode=paymentmode_filter)

        if approvedby_filter:
            invoices = invoices.filter(approvedby=approvedby_filter)

        if approvaldate_filter:
            invoices = invoices.filter(approvaldate=approvaldate_filter)

        if type_filter:
            invoices = invoices.filter(type=type_filter)

        if paid_filter:
            invoices = invoices.filter(paid=paid_filter)

        if balance_filter:
            invoices = invoices.filter(balance=balance_filter)

        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

class SalesOrderListView(APIView):
    def get(self, request):
        myinvoice_filter = request.query_params.get('myinvoice')
        code_filter = request.query_params.get('code')
        customer_filter = request.query_params.get('customer')
        userid_filter = request.query_params.get('userid')
        status_filter = request.query_params.get('status')
        date_filter = request.query_params.get('date')
        branch_filter = request.query_params.get('branch')

        sales_orders = SalesOrder.objects.all()

        if myinvoice_filter:
            sales_orders = sales_orders.filter(myinvoice=myinvoice_filter)

        if code_filter:
            sales_orders = sales_orders.filter(code=code_filter)

        if customer_filter:
            sales_orders = sales_orders.filter(customer__icontains=customer_filter)

        if userid_filter:
            sales_orders = sales_orders.filter(userid=userid_filter)

        if status_filter:
            sales_orders = sales_orders.filter(status=status_filter)

        if date_filter:
            sales_orders = sales_orders.filter(date=date_filter)

        if branch_filter:
            sales_orders = sales_orders.filter(branch=branch_filter)

        serializer = SalesOrderSerializer(sales_orders, many=True)
        return Response(serializer.data)

class CustomerListView(APIView):
    def get(self, request):
        first_name_filter = request.query_params.get('first_name')
        surname_filter = request.query_params.get('surname')
        phone_filter = request.query_params.get('phone')

        customers = Customer.objects.all()

        if first_name_filter:
            customers = customers.filter(first_name__icontains=first_name_filter)

        if surname_filter:
            customers = customers.filter(surname__icontains=surname_filter)

        if phone_filter:
            customers = customers.filter(phone__icontains=phone_filter)

        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    
class TablesListView(APIView):
    def get(self, request):
        status_filter = request.query_params.get('status')
        name_filter = request.query_params.get('name')

        tables = Tables.objects.all()

        if status_filter:
            tables = tables.filter(status=status_filter)

        if name_filter:
            tables = tables.filter(name__icontains=name_filter)

        serializer = TablesSerializer(tables, many=True)
        return Response(serializer.data)

class AttendanceListView(APIView):
    def get(self, request):
        idno_filter = request.query_params.get('idno')
        surname_filter = request.query_params.get('surname')
        type_filter = request.query_params.get('type')

        attendance = Attendance.objects.all()

        if idno_filter:
            attendance = attendance.filter(idno=idno_filter)

        if surname_filter:
            attendance = attendance.filter(surname__icontains=surname_filter)

        if type_filter:
            attendance = attendance.filter(type=type_filter)

        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)
