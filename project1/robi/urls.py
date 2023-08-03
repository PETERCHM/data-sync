from django.urls import path
from .views import ProductsListView, MainmenuListView, OpenordersListView, OrderlistListView, AttendanceListView,ActivityloggsListView, SalesOrdercancelledListView, SalesOrderkitchenListView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products-list'),
    path('mainmenu/', MainmenuListView.as_view(), name='mainmenu-list'),
    path('openorders/', OpenordersListView.as_view(), name='openorders-list'),
    path('orderlist/', OrderlistListView.as_view(), name='orderlist-list'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('activityloggs/', ActivityloggsListView.as_view(), name='activityloggs-list'),
    path('salesordercancelled/', SalesOrdercancelledListView.as_view(), name='salesordercancelled-list'),
    path('salesorderkitchen/', SalesOrderkitchenListView.as_view(), name='salesorderkitchen-list'),

]
