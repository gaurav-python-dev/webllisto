#project level url

from django.urls import path
from .views import (list,createUpdateForm,ProductDetail,ProductUpdateView,
                    product_delete, category_list, create_category, delete_category,
                    update_category)
app_name='products'
urlpatterns = [
    path('create/', createUpdateForm,name='create'),
    path('',list,name='list'),
    path('<int:pk>/',ProductDetail.as_view(),name='detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',product_delete,name='delete'),
    path('category/',category_list,name='category_list'),
    path('category/create/', create_category, name= 'category_create'),
    path('category/<int:id>/delete/',delete_category,name='category_delete'),
    path('category/<int:id>/update/',update_category,name='category_update'),


]
