from multiprocessing import context
from django.shortcuts import render

from stock.models import Stock

def stock_list(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
    }
    return render(request, 'stock/stocks.html', context)
