from django.shortcuts import render
from django.http import HttpResponse
from . import ProfitCalculator
from . import chart


# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Result(request):
    buyPrice = float(request.GET['buyprice'])
    sellPrice = float(request.GET['sellprice'])
    token = request.GET['token']
    takerFee = float(request.GET['takerfee'])
    makerFee = float(request.GET['makerfee'])
    investment = float(request.GET['investment'])
    netprofit = round(ProfitCalculator.NetProfitCalculator(token,buyPrice,sellPrice,investment,takerFee,makerFee)[0],2)
    netprofit = "₹" + str(netprofit)

    values = list(ProfitCalculator.NetProfitCalculator(token,buyPrice,sellPrice,investment,takerFee,makerFee))
    keys = ['Net Profit', 'Total Fee', 'Total Investment']
    if values[0] < 0:
        values[0] = abs(values[0])
        keys[0] = 'Total Loss'
        graph = chart.get_plot(values,keys, 'blue')
        netvalue = 'Total Loss:'
    else:
        graph = chart.get_plot(values,keys)
        netvalue = 'Total Profit:'
    return render(request, 'result.html', {'netprofit': netprofit, 'graph': graph, "netvalue": netvalue})
