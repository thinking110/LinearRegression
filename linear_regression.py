# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:38:23 2017

@author: John
"""

from numpy import *
import matplotlib.pyplot as plt

def loaddataSet(filename):
    numfeat = len(open(filename).readline().split('\t'))-1
    dataMat = [];labelsVec = []
    file = open(filename)
    for line in file.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numfeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelsVec.append(float(curLine[-1]))
    return dataMat,labelsVec

def standRegression(xArr,yArr):
    xMat = mat(xArr);yMat = mat(yArr)

    print("xMat==", xMat.shape, "yMat",yMat.shape)

    xTx = xMat.T * xMat
    if linalg.det(xTx)==0.0:
        print('this matrix is singular,cannot do inverse\n')
        return
    print("xTx==",xTx.shape )
    sigma = xTx.I * (xMat.T * yMat.T)
    return  xMat,yMat,sigma

def PlotLine(xMat,yMat,sigma):
    ax = plt.subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy*sigma
    ax.plot(xCopy[:,1],yHat)
    plt.show()


def  TestStand():
     
    x,y=loaddataSet("./ex0.txt")


    xMat,yMat,sigma = standRegression(x,y)

    print("sigma=111=",sigma.shape)

    PlotLine(xMat,yMat,sigma)

TestStand()

    
def lwlr(testPoint,xArr,yArr,k = 1.0):
    xMat = mat(xArr);yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    print("weights.shape=",weights.shape)
    for i in range(m):
        diffMat = testPoint - xMat[i,:]
        weights[i,i] = exp(diffMat * diffMat.T/(-2.0*k**2))
    xTWx = xMat.T * (weights*xMat)
    if linalg.det(xTWx)==0.0:
        print('this matrix is singular,cannot do inverse\n')
        return
    sigma = xTWx.I * (xMat.T * (weights * yMat))
    return testPoint * sigma

def lwlrTest(testArr,xArr,yArr,k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    print("m==",m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat
    
def PlotLine1(testArr,xArr,yArr,k = 1.0):
    xMat = mat(xArr)
    yMat = mat(yArr)
    print(xMat.shape,yMat.shape)
    yHat = lwlrTest(testArr,xArr,yArr,k)
    srtInd = xMat[:,1].argsort(0)
    xsort = xMat[srtInd][:,0,:]
    ax = plt.subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0],s = 2,c = 'red')
    ax.plot(xsort[:,1],yHat[srtInd])
    plt.show()
        

def Testlwlr():
    
    x,y=loaddataSet("./ex0.txt")

    print("xMat==",x.__sizeof__())

    x1,y1=loaddataSet("./ex1.txt")

    PlotLine1(x,x,y,0.01)

Testlwlr()