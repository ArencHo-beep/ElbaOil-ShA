from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("products/", views.product_list_view, name="products"),
    path("contact/", views.contact_view, name="contact"),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    # path('search/', views.category_search, name='category_search'),
    path('ajax/category-autocomplete/', views.category_autocomplete, name='category_autocomplete'),
    path('search/', views.search_view, name='search'),
    path('ajax/search_suggestions/', views.search_suggestions, name='search_suggestions'),
]
