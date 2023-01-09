from django.urls import path
from . import views

app_name = 'bike'

urlpatterns = [
    path('bicycles/', views.product_list, name='product_list'),
    path('accessories/', views.accessories_product_list, name='accessories_product_list'),
    path('parts/', views.parts_product_list, name='parts_product_list'),
    # path('<slug:category_slug>/', views.product_list,
    #      name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', views.product_details,
    #      name='product_detail'),
]