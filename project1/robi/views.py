from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Mainmenu, Openorders, Orderlist, Attendance, Activityloggs, SalesOrdercancelled, SalesOrderkitchen
from .serializers import ProductsSerializer, MainmenuSerializer, OpenordersSerializer, OrderlistSerializer, AttendanceSerializer, ActivityloggsSerializer, SalesOrdercancelledSerializer, SalesOrderkitchenSerializer

class ProductsListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

class MainmenuListView(APIView):
    def get(self, request):
        mainmenu = Mainmenu.objects.all()
        serializer = MainmenuSerializer(mainmenu, many=True)
        return Response(serializer.data)

class OpenordersListView(APIView):
    def get(self, request):
        openorders = Openorders.objects.all()
        serializer = OpenordersSerializer(openorders, many=True)
        return Response(serializer.data)

class OrderlistListView(APIView):
    def get(self, request):
        orderlist = Orderlist.objects.all()
        serializer = OrderlistSerializer(orderlist, many=True)
        return Response(serializer.data)

class AttendanceListView(APIView):
    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

class ActivityloggsListView(APIView):
    def get(self, request):
        activityloggs = Activityloggs.objects.all()
        serializer = ActivityloggsSerializer(activityloggs, many=True)
        return Response(serializer.data)

class SalesOrdercancelledListView(APIView):
    def get(self, request):
        sales_order_cancelled = SalesOrdercancelled.objects.all()
        serializer = SalesOrdercancelledSerializer(sales_order_cancelled, many=True)
        return Response(serializer.data)

class SalesOrderkitchenListView(APIView):
    def get(self, request):
        sales_order_kitchen = SalesOrderkitchen.objects.all()
        serializer = SalesOrderkitchenSerializer(sales_order_kitchen, many=True)
        return Response(serializer.data)