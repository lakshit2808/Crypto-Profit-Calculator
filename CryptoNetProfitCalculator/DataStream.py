import requests

def DataStream(symbol, interval, limit=0):
    data= {}
    try:
        data = requests.get('https://public.coindcx.com/market_data/candles?pair=B-%s&interval=%s'%(symbol, interval))
        if limit == 0:
            data = data.json()[0]
        else:
            data = data.json()[:limit]
    except IndexError:
        try:
            data = requests.get('https://public.coindcx.com/market_data/candles?pair=I-%s&interval=%s'%(symbol, interval))
            if limit == 0:
                data = data.json()[0]
            else:
                data = data.json()[:limit]
        except IndexError:
            try:
                data = requests.get('https://public.coindcx.com/market_data/candles?pair=HB-%s&interval=%s'%(symbol, interval))
                if limit == 0:
                    data = data.json()[0]
                else:
                    data = data.json()[:limit]
            except IndexError:
                try:
                    data = requests.get('https://public.coindcx.com/market_data/candles?pair=H-%s&interval=%s'%(symbol, interval))
                    if limit == 0:
                        data = data.json()[0]
                    else:
                        data = data.json()[:limit]
                except IndexError:
                    data = requests.get('https://public.coindcx.com/market_data/candles?pair=BM-%s&interval=%s'%(symbol, interval))
                    if limit == 0:
                        data = data.json()[0]
                    else:
                        data = data.json()[:limit]
    return data