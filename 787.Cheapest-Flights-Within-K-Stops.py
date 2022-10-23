# There are n cities connected by some number of flights. 
# You are given an array flights where flights[i] = [fromi, toi, pricei]
#  indicates that there is a flight from city fromi to city toi with 
#  cost pricei.

# You are also given three integers src, dst, and k, return the cheapest
#  price from src to dst with at most k stops. If there is no such route,
#   return -1.

def findCheapestPrice(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0
    for i in range(k+1):
        tmpPrices = prices.copy()
        for s, d, p in flights: # s=source, d=destination, p=price
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p
        prices = tmpPrices
    
    if prices[dst] == float("inf"):
        return -1
    else:
        return prices[dst]
