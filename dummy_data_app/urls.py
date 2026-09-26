from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dummy_data_app.views import finance
from dummy_data_app.views import news

news_router = DefaultRouter()
news_router.register("news", news.NewsViewset, basename="news")

urlpatterns = [
    path("", include(news_router.urls)),
    path("finance/account-numbers", finance.account_numbers),
    path("finance/transactions", finance.transactions),
    path("finance/currencies", finance.currencies),
    path("finance/stocks", finance.stocks)
]