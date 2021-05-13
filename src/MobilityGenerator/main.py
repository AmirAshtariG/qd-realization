import random


# Parameter Initilize
Timestep = 500
step = 0.003
reverse = 1

# Valid Dims
MaxX = 10.5
MaxY = 7.9
MaxZ = 4


def randommov():
    #  Generate random Mobility
    f0 = open("NodePosition1.dat", "w")
    if reverse == 1:
        y = 0.3 * random.random() + MaxY*(2/3)
    else:
        y = 3 * random.random()

    z = 2 * random.random()
    x = 5 * random.random()

    for i in range(0, Timestep):

        if x >= MaxX or x <= 0:
            x = MaxX/2
        if y >= MaxY or y <= 0:
            y = MaxY/2
        if z >= MaxZ or z <= 0.7:
            z = MaxZ/2

        if reverse == 1:
            y -= step * random.random()
        else:
            y += step * random.random()
        x += step*random.random()
        z += step*random.random()
        f0.writelines(str(x) + str(',') + str(y) + str(',') + str(z) + str('\n'))
    f0.close()


def determinsticmov():
    # Generate Determinstic Movement Include LOS & NLOS#
    f0 = open("Deterministic/NodePosition0.dat", "w")
    f1 = open("Deterministic/NodePosition1.dat", "w")
    x0 = 2.8
    y0 = 1.55
    z0 = 0.5
    x1 = 7.8
    y1 = 1.55
    z1 = 2.1

    for i in range(0, Timestep):
        x0 -= step * random.random() * 0.03
        y0 += step * random.random()
        z0 += step * random.random() * 2.4
        x1 -= step * random.random() * 1.05
        y1 += step * random.random() * 3.8
        z1 += step * random.random()
        f0.writelines(str(x0) + str(',') + str(y0) + str(',') + str(z0) + str('\n'))
        f1.writelines(str(x1) + str(',') + str(y1) + str(',') + str(z1) + str('\n'))
    f0.close()
    f1.close()


if __name__ == "__main__":
    determinsticmov()



