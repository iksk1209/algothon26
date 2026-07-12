import numpy as np

def backtest(prices, getMyPosition):
    """
    Backtest a trading strategy given the price data and a function to get positions.
    """
    nInst, nt = prices.shape
    currentPos = np.zeros(nInst)
    dailyPnL = np.zeros(nt)

    for t in range(1, nt):
        # Get the current position based on prices up to day t
        currentPos = getMyPosition(prices[:, :t])
        
        # Calculate daily PnL
        dailyPnL[t] = np.sum(currentPos * (prices[:, t] - prices[:, t - 1]))

    return dailyPnL