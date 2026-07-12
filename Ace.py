import numpy as np

nInst=51
currentPos = np.zeros(nInst)
def getMyPosition (prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape
    if (nt < 2):
        return np.zeros(nins)
    
    
    return currentPos

