from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<str:tp>', CompanyListByTypeView.as_view(), name='company_detail'),
    path('reviews/', ReviewList.as_view(), name='create_review'),
    path('reviews-by-rate/<int:rate>', ReviewListByRate.as_view(), name='reviews_by_rate'),
    path('reviews/<int:pk>', UserReviews.as_view(), name='user_reviews'),
]