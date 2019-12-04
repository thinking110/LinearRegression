#coding=utf-8

from  numpy  import *

import  numpy  as np 

import  matplotlib.pyplot  as plt 



filename='./ex0.txt' #文件目录
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




def   RidgeRegress(xMat ,yMat,lam=0.2):

     xTx = xMat.T *xMat

     print("xTx shape==",xTx.shape)



     denom=xTx + eye(shape(xMat)[1])*lam

     print("denom==", denom.shape)

     if  linalg.det(denom) == 0.0:

     	print ("  this  matrix   is singular  cannot do  inverse")

     	return 
     ws = denom.I *(xMat.T *yMat)

     print("ws shape==",ws.shape)

     return  ws 


def   RidgeTest(xArr,yArr):
      
      xMat = mat(xArr)

      yMat = mat(yArr).T
      
      yMen = mean(yMat,0)


      #yMat= yMat - yMen

      xMean = mean(xMat,0)

      #xMat =(xMat - xMean)


      print("xMat==",xMat)

      number =200

      wMat = zeros( (number,shape(xMat)[1]) )

      print("wMat=33=",wMat.shape)

      for  i in range(number):
         ws = RidgeRegress(xMat,yMat, exp(i-15) )


         wMat[i,:] = ws.T 
      return  wMat


def  PlotLine(X,wMat):
    
      fig = plt.figure()

      ax = fig.add_subplot(111)

      #number = 20
      ax.plot(wMat)
      
      print("X",X)


      #ax.plot(mat(X).T[:,1],wMat.T[:,1])

      plt.show()




def regularize(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = mean(inMat,0)   #calc mean then subtract it off
    inVar = var(inMat,0)      #calc variance of Xi then divide by it
    #inMat = (inMat - inMeans)/inVar
    inMat = (inMat - inMeans)

    return inMat


def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()

def stageWise(xArr,yArr,eps=0.01,numIt=10):
    xMat = mat(xArr); yMat=mat(yArr).T
    yMean = mean(yMat,0)
    #yMat = yMat - yMean     #can also regularize ys but will get smaller coef
    #xMat = regularize(xMat)
    m,n=shape(xMat)
    returnMat = zeros((numIt,n)) #testing code remove
    ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()


    print("wsTest==",wsTest)
    for i in range(numIt):
        print( ws.T)
        lowestError = inf; 
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()

                print("wsTest[j]",wsTest[j])
                wsTest[j] += eps*sign
                yTest = xMat*wsTest
                rssE = rssError(yMat.A,yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:]=ws.T

    return returnMat


def TestRidge():

     x,y= loaddataSet(filename)
     wMat = RidgeTest(x,y)
     
     print("wMat==",wMat.shape)

     PlotLine(x,wMat)



def  TestStage():

	x,y= loaddataSet(filename)

	wMat=stageWise(x,y)

	PlotLine(x,wMat)

TestStage()

