from django.urls import path
from . import views


urlpatterns = [
    path('advertis/', views.AdvertiseListView.as_view(), name='advertise_list'),
    path('advertis/detail/', views.advertis_detail),
    path('advertis/search/', views.SearchAdvertisView.as_view(), name='advertise_search'),
    path('advertis/<category_name>/', views.AdvertiseListByCategory.as_view(), name='category_advertise'),
    path('advertis/<advertisId>/<name>/', views.advertis_detail),
    path('advertis_categories_partial/', views.advertis_categories_partial, name='advertis_categories_partial'),
    path('advertis_register/', views.advertis_register),

]
