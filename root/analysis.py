import array as arr
import math
from math import sqrt,log
import string
import matplotlib.pyplot as plt
import numpy as np 
import sympy as sym
from sympy import symbols,sympify
import re

import matplotlib

from matplotlib.animation import FuncAnimation
from django.http import HttpResponse
from django.shortcuts import render







def calculationOfF_test(modifiedAlpha,size,alpha,fVal):
	meanOfAlpha = 0.0
	
	for j in range (0,size):
		meanOfAlpha = meanOfAlpha + alpha[j]
		
		
	meanOfAlpha = meanOfAlpha/size;
	meanOfAlpha = round(meanOfAlpha,5)
	for i in range (0,17):
		val =0.0
		for j in range(0,size):
			val = val + modifiedAlpha[i][j]
           
		meanOfModifiedAlpha = val/size;
		meanOfModifiedAlpha = round(meanOfModifiedAlpha,5)
		sumOfAlpha = 0.0
		sumOfModifiedAlpha = 0.0
		for j in range(0,size):
			sumOfAlpha = sumOfAlpha + ((alpha[j]-meanOfAlpha)*(alpha[j]-meanOfAlpha));
			sumOfModifiedAlpha = sumOfModifiedAlpha + ((modifiedAlpha[0][j]-meanOfModifiedAlpha)*(modifiedAlpha[0][j]-meanOfModifiedAlpha));

		
		sumOfAlpha = round(sumOfAlpha,5)
		sumOfModifiedAlpha = round(sumOfModifiedAlpha,5)
		SD1 = sumOfAlpha/(size-1)
		SD1 = round(SD1,5)
		SD2 = sumOfModifiedAlpha/(size-1)
		SD1 = round(SD1,5)

		if(SD2!=0):
			f_test = SD1/SD2
		else:
			f_test = SD1
   
		f_test = round(f_test,5)
		fVal.append(abs(f_test));
 
 

   
def calculationOfT_test(modifiedAlpha,size,alpha,tVal):
	meanOfAlpha = 0.0
	
 
	for j in range (0,size):
		meanOfAlpha = meanOfAlpha + alpha[j]
  
	meanOfAlpha = meanOfAlpha/size;
	meanOfAlpha = round(meanOfAlpha,5)
 
	for i in range (0,17):
		val = 0.0
		for j in range(0,size):
			val = val + modifiedAlpha[i][j]
           
		meanOfModifiedAlpha = val/size;
		meanOfModifiedAlpha = round(meanOfModifiedAlpha,5)
		sumOfAlpha = 0.0;
		sumOfModifiedAlpha = 0.0;
		for j in range(0,size):
			sumOfAlpha = sumOfAlpha + ((alpha[j]-meanOfAlpha)*(alpha[j]-meanOfAlpha));
			sumOfModifiedAlpha = sumOfModifiedAlpha + ((modifiedAlpha[i][j]-meanOfModifiedAlpha)*(modifiedAlpha[i][j]-meanOfModifiedAlpha));

		sumOfAlpha = round(sumOfAlpha,5)
		sumOfModifiedAlpha = round(sumOfModifiedAlpha,5)
  
  
		# T test calculation 
		SD1 = round(sumOfAlpha/(size-1),5)
		SD2 = round(sumOfModifiedAlpha/(size-1),5)

		SD = ((size*SD1) + (size*SD2))/(size+size-2)
		SD = 	math.sqrt(SD)
		SD = round(SD,5)
		
		t_test = (meanOfAlpha-meanOfModifiedAlpha)/(SD*math.sqrt(2/size))
		t_test = round(t_test,5)
		
		tVal.append(abs(t_test))
	



			
	
	








		
	
    

    
	


def findingRoot(modifiedGAlpha,equationsWithLog,i,j):
    
    eq = equationsWithLog[0][i]
    exp = sympify(eq)
    x = symbols('x')
    expr_diff = sym.diff(exp,x)
    
    x0 = 0.5
    val2 = round(abs(expr_diff.subs(x,x0)),5)
    
    
    val1 = abs(exp.subs(x,x0))
    
    if modifiedGAlpha[i][j]<0:
        val1 = round(val1+modifiedGAlpha[i][j],5)
    else:
        val1 = round(val1-modifiedGAlpha[i][j],5)
    
    
    #print("val1",val1)
    #print("val2",val2)
    #print("derivative")
    #print(expr_diff)
    if val2 == 0.00:
        return 0.0
    
    x1 = round(abs(x0-(val1/val2)),5)
    
    step = 0
    while ( step<3):
        exp = expr_diff
        print(type(exp))
        if re.search(r'x',str(exp))== False:
            return x1
        
        expr_diff = sym.diff(exp,x)
        
        x0 = x1
        
        #print("derivative in while")
        #print(expr_diff)
		
        
        val1 =abs(exp.subs(x,x0))
        
        val2 = abs(expr_diff.subs(x,x0))
        #print("val1 in while",val1)
        #print("val2 inwhile",val2)
        if val2 == 0.00:
             return 0.0
         
        x1 = round(abs(x0-(val1/val2)),5)
        step = step+1
        
        
    
    return x1
  




			
    
		
def calculationOfModifiedAlpha(modifiedGAlpha,modifiedAlpha,size):
    eqFile = open('eq.txt','r')
    equationsWithLog = [line.split(',') for line in eqFile.readlines()]
    
    
    for i in range(0,17):
        for j in range(0,size):
            modifiedAlpha[i][j] = round(findingRoot(modifiedGAlpha,equationsWithLog,i,j),5)
            
       
 
 
    
   
    

def calculationOfModifiedGAlpha(gAlpha,modifiedGAlpha,timePeriods,regressionEq,size):
	for i in range(0,17):
		for j in range(0,size):
			x = timePeriods[j]
			val = eval(regressionEq[i])
			modifiedGAlpha[i][j]=round(val,5)







def calculateSlopePart(ind,gAlpha,timePeriods,size):
	sy = sum(gAlpha[ind])

	sx = sum(timePeriods)

	sxsy = 0

	sx2 = 0

	for i in range(size):
		sxsy += (gAlpha[ind][i] * timePeriods[i])
		sx2 += (timePeriods[i]*timePeriods[i])
	b = (size * sxsy - sx * sy)/(size * sx2 - sx * sx)
	

	return b






def calculationOfLeastRegLine(gAlpha,timePeriods,regressionEq,size):

	for i in range(0,17):
		slopePart = calculateSlopePart(i,gAlpha,timePeriods,size)
		meanY = int(sum(gAlpha[i])/size)
		meanX  = int(sum(timePeriods)/size)
		
		
		constPart= meanY - (slopePart * meanX)
		
		eq = ""
		c = "{:.5f}".format(constPart)
		eq += c
		s = "{:.5f}".format(slopePart)
		if (s[0]!='-'):
			eq +='+'

		eq += s
		eq +='*x'
		regressionEq.append(eq)
	
		


def calculationOfCorelationCoeff(gAlpha,timePeriods,coRelationCof,size):
    meanTime = 0.0
    
    for i in range(0,size):
        meanTime = meanTime+timePeriods[i]
        
    meanTime = meanTime/size
    for ind in range(0,17):
        meanVal = 0.0
        for i in range(0,size):
            meanVal = meanVal+gAlpha[ind][i]
        meanVal = meanVal/size
        var1 = 0.0
        var2 = 0.0
        var3 = 0.0
        for j in range(0,size):
            var1 = var1 + ((gAlpha[ind][j]-meanVal)*(timePeriods[j]-meanTime))
            var2 = var2 + ((gAlpha[ind][j]-meanVal)*(gAlpha[ind][j]-meanVal))
            var3 = var3 + ((timePeriods[j]-meanTime)*(timePeriods[j]-meanTime))
        sumVal = math.sqrt(var2*var3)
        if sumVal!=0:
            temp = round((var1/sumVal),5)
            coRelationCof.append(abs(temp))
        else:
            coRelationCof.append(abs(var1))
            
            
            
            

def calculationOfGAlpha(gAlpha,alpha,size):
        equationFile = open('equations.txt','r')
        equations = [line.split(',') for line in equationFile.readlines()]
        for i in range(0,17):
            for j in range(0,size):
                
                try:
                    x = alpha[j]
                    val = eval(equations[0][i])
                    
                    gAlpha[i][j]=round(abs(val),5)
                    
			
                    
                except ValueError:
                    gAlpha[i][j] = 0
                    
                
			




def calculationOfAlpha(finalWeights,timePeriods,alpha,initialWeight):
	alphaArray = []
	
	for item in finalWeights:
		alphaVal =  float((initialWeight-item)/initialWeight)
		alphaArray.append(round(alphaVal,5))

	alpha[:] = alphaArray





def dataAnalysis(request):
	
    return render(request,"number") 

  
	








	
	

	


























    

