import re
import numpy as np

def loadParams():
    input = open("input.txt", "r")  # otwieranie pliku
    params = input.readlines()  # wczytanie paramertów wejściowych
    for i in range(0,4):
        params[i] = re.sub('[a-zA-z" "="\n"]', '', params[i])  # usuwanie liter a-z, A-Z, spacji i równości, aby zosta ły liczby
    input.close();
    return params

def calculateArea(x, y):
    return (x+1)*(y+1) #wyobraz sobie pole 1x1 to ma ona dwie długości pomiędzy kropkami szerokości i wysokości

def createMatrix(x, y):
    return np.ones( (x, y), dtype=np.int32 )

def circleArea(r):
    return np.pi*np.square(r)

# source: https://www.xarg.org/2016/07/calculate-the-intersection-area-of-two-circles/
def intersectArea(A, B, r):
    d = np.sqrt( np.square(B[0]-A[0]) - np.square(B[1]-A[1]) ) # odleglosc miedzy środkami okręgó
    if (d < (r + r) ):
        a = r * r
        b = r * r

        x = (a - b + d * d) / (2 * d)
        z = x * x
        y = np.sqrt(a - z)

        if (d <= np.abs(r - r)):
            return np.pi * np.min(a, b)
        return a*np.arcsin( (y/r) ) + b*np.arcsin( (y/r) ) - y*( (x+np.sqrt( (z+b-a) )) )
    return 0


#def calculateSprinklerArea(x, y, r):


    
def main():
    params = loadParams()
    x = int(params[0])
    y = int(params[1])
    r = int(params[2])
    eff = int(params[3])
    wholeArea = calculateArea(x, y)
    print("Whole area is " + str(wholeArea))
    matrix = createMatrix(x, y)
    print( intersectArea([0,0], [1,0], r))
    print(circleArea(r))


if __name__== "__main__":
  main()
