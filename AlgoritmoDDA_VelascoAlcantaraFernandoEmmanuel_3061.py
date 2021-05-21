import matplotlib.pyplot as plt

#Algoritmo dado por el docente de dda

def dda(x1, y1, x2, y2, color2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    steps = 0

    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)

    xInc = float(dx / steps)
    yInc = float(dy / steps)

    #Redondeo de los elementos

    xInc = round(xInc, 1)
    yInc = round(yInc, 1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x1), round(y1), color2)
        x1 += xInc
        y1 += yInc

        print("X:",x1)
        print("Y:",y1)

    #Algunos elementos de matplot

    plt.title("DDA")
    plt.grid()
    plt.plot(marker='s', markersize=10, markerfacecolor='blue')
    plt.show()

    #Ingresar los valores

def main():
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    color2 = "r."

    dda(x1, y1, x2, y2, color2)

if __name__ == "__main__":
    main()
