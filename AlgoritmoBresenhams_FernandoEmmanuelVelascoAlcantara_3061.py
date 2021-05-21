import matplotlib.pyplot as plt

#Algoritmo dado por el docente de bresenhams

def bresen(x1, y1, x2, y2, color):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    p = 2*dy - dx

    x = x1
    y = y1

    for i in range(x, x2):
        plt.plot(round(x), round(y), color)
        x = x + 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + (2*dy) - (2*dx)
            y = y + 1

        print("X:", x)
        print("Y:", y)

        #Aqui se muestra lo correspondiente a matplotlib.
    plt.title("Bresenhams")
    plt.grid()
    plt.plot(marker='s', markersize=10, markerfacecolor='blue')
    plt.show()

    #Ingresar los datos.
def main():
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    color = "y."

    bresen(x1, y1, x2, y2, color)


if __name__ == "__main__":
    main()
