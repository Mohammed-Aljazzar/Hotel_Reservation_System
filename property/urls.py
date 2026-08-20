from django.urls import path
from .views import PropertyList, PropertyDetail, PropertyCreate, PropertyUpdate, PropertyDelete

app_name = 'property'
urlpatterns = [
    path('create/', PropertyCreate.as_view(), name='property_create'),
    path('<slug:slug>/edit/', PropertyUpdate.as_view(), name='property_update'),
    path('<slug:slug>/delete/', PropertyDelete.as_view(), name='property_delete'),
    path('', PropertyList.as_view(), name='property_list'),
    path('<slug:slug>/', PropertyDetail.as_view(), name='property_detail'),

]
