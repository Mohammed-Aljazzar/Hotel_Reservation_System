from django.urls import path
from .views import PropertyList, PropertyDetail, PropertyCreate, PropertyUpdate, PropertyDelete
from .api_view import PropertyAPIList,PropertyAPIDetail

app_name = 'property'
urlpatterns = [
    path('create/', PropertyCreate.as_view(), name='property_create'),
    path('<slug:slug>/edit/', PropertyUpdate.as_view(), name='property_update'),
    path('<slug:slug>/delete/', PropertyDelete.as_view(), name='property_delete'),
    path('', PropertyList.as_view(), name='property_list'),
    path('<slug:slug>/', PropertyDetail.as_view(), name='property_detail'),

    path('api/list/', PropertyAPIList.as_view(), name='property_list_api'),
    path('api/list/<int:pk>', PropertyAPIDetail.as_view(), name='property_detail_api'),

]
