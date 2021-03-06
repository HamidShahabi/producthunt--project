from django.urls import path

from product import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
    path('<int:product_id>/delete', views.delete, name='delete'),
    path('<int:product_id>/edit', views.edit, name='edit'),
    path('myproducts/', views.myproducts, name='myproducts'),
]
