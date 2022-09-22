from django.urls import path

from stock.views import stock_sell, stock_list, stock_detail_buy, stock_buy, account, stock_detail_sell

urlpatterns = [
    path('list/', stock_list, name='list'),
    path('detail_buy/<int:pk>/', stock_detail_buy, name='detail_buy'),
    path('detail_sell/<int:pk>/', stock_detail_sell, name='detail_sell'),
    path('buy/<int:pk>/', stock_buy, name='buy'),
    path('sell/<int:pk>/', stock_sell, name='sell'),
    path('account/', account, name='account')
]