from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home' ),
    path('products/', views.products, name='products'),
    path('contact-us/', views.contact, name='contactus'),
    path('about-us/', views.about, name='about'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('<int:product_id>/', views.product_detail, name='product-detail'),
    path("news-info/<int:news_id>/", views.news_info, name="news-info"),
    path('category/<category_id>/', views.category, name='category')
    ]