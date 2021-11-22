from . import DataStream


def NetProfitCalculator(token,buy_price, sell_price, totalamountinrs, takerfee , makerfee):
    token = token.upper()
    token = DataStream.DataStream('%s_INR'%(token), '1m')['close']

    amountIntoken = totalamountinrs / token

    quantity = amountIntoken / buy_price

    changeInPrice = sell_price - buy_price

    profit = changeInPrice * quantity

    buyFee = takerfee/100 * buy_price * quantity
    sellFee = makerfee/100 * sell_price * quantity
    
    buyFeeINR = buyFee * token
    sellFeeINR = sellFee * token

    totalFee = buyFee + sellFee

    totalFeeINR = buyFeeINR + sellFeeINR
    
    netProfitIntoken = profit - totalFee

    netProfitInRS = netProfitIntoken * token

    return netProfitInRS, totalFeeINR, totalamountinrs


