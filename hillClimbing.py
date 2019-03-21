import numpy as np
from matplotlib import cm
from mpl_toolkits import mplot3d
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import importlib
importlib.reload(plt)

#calculates the value of griewank function of any dimension
def griewank(x):
    #calculating term1 of the equation
    xsq = np.square(x)  #squares all elements of the array x
    xsqdiv4000 = xsq/4000
    term1 = np.sum(xsqdiv4000)
    
    #calculating term2 of the equation
    xbyrooti = np.ones(x.size)
    for i in range(x.size):
        xbyrooti[i] = x[i]/math.sqrt(i+1)
    cosxbyrooti = np.cos(xbyrooti)
    term2 = np.prod(cosxbyrooti)

    return term1-term2+1
    
def hillClimb2d():
    print("Simulating Hill Climbing on First Order Griewank")
    pointx = float(input("Enter x"))
    plt.figure()
    plt.ion()
    x = np.arange(-200,200.1,0.1)
    y = np.array([griewank(np.array([i])) for i in x])
    plt.plot(x,y,'g-',linewidth=1.5,markersize=4)
    (plt.get_current_fig_manager()).full_screen_toggle()
    plt.show()
    plt.pause(1)
    fig = plt.gcf()
    plt.title("Simple Hill Climbing on First Order Griewank Function")
    currentx = pointx
    a = None
    explored_set = set()
    while True:
        plt.pause(0.1)
        if a is not None:
            a.set_visible(False)
        plt.plot(currentx,griewank(np.array([currentx])),'ro',markersize=3)
        leftx = currentx - 0.1
        rightx = currentx + 0.1
        gwleft = griewank(np.array([leftx]))
        gwright = griewank(np.array([rightx]))
        if(gwleft > gwright):
            currentx = leftx 
            string = "Coordinate: ({0:.1f},{0:.1f}) is better".format(currentx,gwleft)
        elif(gwright > gwleft):
            currentx = rightx
            string = "Coordinate: ({0:.1f},{0:.1f}) is better".format(currentx,gwright)
        if currentx in explored_set:
            plt.pause(2)
            plt.close()
            break
        a = fig.text(0.2,0.2,string)
        explored_set.add(currentx)

def hillClimb3d():
    print("Simulating Hill Climbing on Second Order Griewank")
    pointx = float(input("Enter x"))
    pointy = float(input("Enter y"))  
    x = np.arange(-5,5.1,0.1)
    y = np.arange(-5,5.1,0.1)
    x,y = np.meshgrid(x,y)
    z = np.ones(x.shape)
    for i in range(x.shape[0]):
        for j in range(y.shape[0]):
            z[i][j] = griewank(np.array([x[i][j],y[i][j]]))  
    plt.ion() 
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection = '3d')
    surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False,alpha=0.2)
    plt.show()
    plt.pause(1)
    fig = plt.gcf()
    plt.title("Simple Hill Climbing on Second Order Griewank Function")
    a = None
    explored_set = set()
    currentx = pointx
    currenty = pointy
    while True:
        plt.pause(0.1)
        if a is not None:
            a.set_visible(False)
        plt.plot([currentx],[currenty],[griewank(np.array([currentx,currenty]))+0.04],markerfacecolor='g', markeredgecolor='g', marker='o', markersize=8, alpha=1)
        downx = currentx
        downy = currenty - 0.1
        gwdown = griewank(np.array([downx,downy]))
        topx = currentx
        topy = currenty + 0.1
        gwtop= griewank(np.array([topx,topy]))
        leftx = currentx - 0.1
        lefty = currenty
        gwleft = griewank(np.array([leftx,lefty]))
        rightx = currentx + 0.1
        righty = currenty
        gwright = griewank(np.array([rightx,righty]))
        maxgw = max(gwdown,gwtop,gwleft,gwright)
        if maxgw==gwdown:
            currentx = downx
            currenty = downy
        elif maxgw==gwtop:
            currentx = topx
            currenty = topy
        elif maxgw==gwleft:
            currentx = leftx
            currenty = lefty
        elif maxgw==gwright:
            currentx = rightx
            currenty = righty
        if(currentx,currenty) in explored_set:
            plt.pause(2)
            plt.close()
            break
        string = "Coordinate: ({0:.1f},{0:.1f}) is better".format(currentx,currenty)
        a=fig.text(0, 0, string, horizontalalignment='center',verticalalignment='center', transform=ax.transAxes)
        explored_set.add((currentx,currenty))
        
hillClimb2d()
hillClimb3d()
