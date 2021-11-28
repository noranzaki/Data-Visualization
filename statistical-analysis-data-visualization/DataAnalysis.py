import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean
from sklearn.linear_model import LinearRegression
from tkinter import *
import math
from PIL import ImageTk,Image 
filename = 'Sales.csv'
import tkinter.font as font

# Titles for axes
xTitle = 'Year'
yTitle = 'Unit Sales(in millions)'

plt.style.use('bmh')
df = pd.read_csv(filename)

# All Brands
x = df[xTitle]
y = df[yTitle]

sqrtDataSetSize = math.ceil(math.sqrt(x.size))

# Measures of Central Tendency
# Mean = y.mean()
# print("%.3f" % Mean)
# Median = y.median()
# print(Median)
# Mode = y.mode()[0]
# print(Mode)

#MaxNum = y.max()
# print(MaxNum)
#MinNum = y.min()
# print(MinNum)

# Measures of Dispersion
#Range = MaxNum - MinNum
# print(Range)

root = Tk()
root.geometry("360x620")
root.resizable(False, False)
root.configure(background = '#051626')
#Images
BarImage = PhotoImage(file = 'barImage.png')
PieImage = PhotoImage(file = 'pieImage.png')
HistogramImage = PhotoImage(file = 'histogramImage.png')
ScatterPlotImage = PhotoImage(file = 'scatterPlotImage.png')
BoxPlotImage = PhotoImage(file = 'boxPlotImage.png')
ScatterRegressionImage = PhotoImage(file = 'scatterRegressionImage.png')
MeanImage = PhotoImage(file = 'meanImage.png')
MedianImage = PhotoImage(file = 'medianImage.png')
ModeImage = PhotoImage(file = 'modeImage.png')

GraphsLabel=Label(root,text="Graphs",activebackground='#051626',height=2, width=30)



# Bar chart
def BarChartGraph():
    plt.xlabel(xTitle, fontsize=16)
    plt.ylabel(yTitle, fontsize=16)
    plt.bar(x, y)
    plt.show()


BarButton = Button(root,width=100,command=BarChartGraph,highlightthickness = 0, bd = 0,bg='#051626',image=BarImage,activebackground='#051626')           

BarButton.place(x=100,y=10)
BarButton.pack()


# Pie chart


def PieChartGraph():
    plt.pie(y, labels=x, radius=1.0, autopct='%0.01f%%',shadow=False, explode=(0.1, 0, 0, 0, 0, 0.1, 0, 0, 0))     
    plt.axis('equal')  # Assures it's a circle
    plt.show()


PieButton = Button(root,width=100,command=PieChartGraph,highlightthickness = 0, bd = 0,bg='#051626',image=PieImage,activebackground='#051626')           

PieButton.place(x=200,y=10)
PieButton.pack()

# Histogram


def HistogramGraph():
    plt.hist(y, bins=int(sqrtDataSetSize), ec="black")
    plt.xlabel(xTitle, fontsize=18)
    plt.ylabel(yTitle, fontsize=16)
    plt.show()


HistogramButton = Button(root,width=100,command=HistogramGraph,highlightthickness = 0, bd = 0,bg='#051626',image=HistogramImage,activebackground='#051626')               

HistogramButton.place(x=300,y=20)
HistogramButton.pack()

# Boxplot


def BoxplotGraph():
    plt.boxplot(y, vert=False)
    plt.show()


BoxplotButton = Button(root,width=100,command=BoxplotGraph,highlightthickness = 0, bd = 0,bg='#051626',image=BoxPlotImage,activebackground='#051626')
#BoxplotButton.grid(row=2,column=1)

# Scatter Graph


def ScatterPlotGraph():
    plt.xlabel(xTitle, fontsize=18)
    plt.ylabel(yTitle, fontsize=16)
    plt.plot(x, y, 'o')
    plt.show()


ScatterPlotButton = Button(root,width=100,command=ScatterPlotGraph,highlightthickness = 0, bd = 0,bg='#051626',image=ScatterPlotImage,activebackground='#051626')                
#ScatterPlotButton.grid(row=3,column=0)
# RegressionLine


def RegressionLine():
    X = df.iloc[:, :-1].values.reshape(-1, 1)
    Y = df.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    # Scatter Graph(With Regression Line)
    newX = [[2019], [2020], [2021]]
    newY = linear_regressor.predict(newX)
    print(newY)
    plt.scatter(X, Y, color='#003F72', label='Data')
    plt.plot(X, Y_pred, color='red', label='Regression line')
    plt.scatter(newX, newY, color='green', label='Prediction')
    plt.legend(loc=4)
    plt.show()


ScatterRegressionbutton = Button(root,width=100,highlightthickness = 0, bd = 0,bg='#051626',image=ScatterRegressionImage,activebackground='#051626' , command=RegressionLine)
#ScatterRegressionbutton.grid(row=3,column=1)

def CalculateMean():
    Mean = y.mean()
    #var1.set(Mean)
    
#var1=StringVar()
MeanButton = Button(root,width=100,highlightthickness = 0, bd = 0,bg='#051626',image=MeanImage,activebackground='#051626')
#MeanButton.grid(row=4,column=0)
#MeanLabel =Label(root,textvariable=var1 ) 
#MeanLabel.grid(row=7,column=1)

def CalculateMedian():
    Median = y.median()
    #var2.set(Median)

#var2=StringVar()
MeadianButton = Button(root,width=100,highlightthickness = 0, bd = 0,bg='#051626',image=MedianImage,activebackground='#051626')
#MeadianButton.grid(row=4,column=1)
#MedianLabel =Label(root,textvariable=var2 ) 
#MedianLabel.grid(row=8,column=1)

def CalculateMode():
    Mode = y.mode()[7]
    #var3.set(Mode)

#var3=StringVar()
ModeLabel = Label(root,width=100, highlightthickness = 0, bd = 0,bg='#051626',image=ModeImage,activebackground='#051626')
#ModeLabel.grid(row=4,column=2)
#ModeLabel =Label(root,textvariable=var3 ) 
#ModeLabel.grid(row=9,column=1)
root.mainloop()


