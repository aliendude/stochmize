#!/usr/bin/python
import sys
from antlr4 import *
from StochmizeLexer import StochmizeLexer
from StochmizeListener import StochmizeListener
from StochmizeParser import StochmizeParser
from pulp import * 
from platypus import *
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from antlr4.error.ErrorListener import ErrorListener


if (len(sys.argv)<2):
	print("Usage: \npython compiler input.sz --debug");
	sys.exit()

filename = str(sys.argv[1])
debug = False

try:
	debug = str(sys.argv[2]) == "--debug"
except Exception:
	pass
#if (debug): print(filename)

#Map de las variables con respecto a un indice
varIdsIndex = {}

#Map de los rangos de las variables
varRanges = {}

#Coeficientes de las restricciones
varCoefs = []

#Numero condicional de las restricciones
valNumRest = []

#Desigualdades de las restricciones
subgetDefs = []

#Coeficioentes de las funciones objetivos
obgetsDefs = []

pousDefs = []

#Tipo de objetivo por cada funcion
min_maxObject = []

normal_params_m = []
normal_params_v = []

unif_params_a = []
unif_params_b = []

subDict = {}

subIds = []
subgetNumbers = []

MaxMinObj = []
idsObjets = [] 

def expresiones(exp):

	if (debug): print("expresiones")
	if (debug): print(exp.getText())
	index = 0.0
	coefOper = 1.0
	pouVal = 1
	indexOper = 0
	oper = [];
	coefs = [0]*len(varIdsIndex)
	pous = [1]*len(varIdsIndex)
	idv=''
	pouFlag=False
	pouVal = 1
	if (debug): print("***childrens***")
	for child in exp.getChildren():
		if pouFlag:
			index = varIdsIndex[idv]
			pous[index]=int(child.getText())
			pouFlag=False
			idv=''

		if child.getText() in varIdsIndex:
			idv=child.getText()

		if child.getText() == '**':
			pouFlag = True
	if (debug): print(pous)
	if (debug): print("***************")
	oper.append(1.0)
	for oprExp in exp.operators():
		if oprExp.getText() == '-':
			oper.append(-1.0)
		elif oprExp.getText() == '+':
			oper.append(1.0)


	for expCont in exp.expr_content():
		if (debug): print("++++expr_content+++++++")
		if (debug): print(expCont.getText())
		if (debug): print("+++++++++++++++++++++++")
		if expCont.getText() in varIdsIndex:
			index = varIdsIndex[expCont.getText()]
			coefs[index]=coefOper*oper[indexOper]
			indexOper = indexOper+1
			coefOper = 1.0
		else:
			coefOper = float(expCont.getText())
		
	if (debug): print(coefs)
	if (debug): print(oper)
	if (debug): print("=====================")
	if (debug): print("/////     /////////")
	if (debug): print(pous)
	if (debug): print("//////////////")
	return coefs

def expresiones_pous(exp):

	if (debug): print("expresiones")
	if (debug): print(exp.getText())
	index = 0.0
	coefOper = 1.0
	pouVal = 1
	indexOper = 0
	oper = [];
	coefs = [0]*len(varIdsIndex)
	pous = [1]*len(varIdsIndex)
	idv=''
	pouFlag=False
	pouVal = 1
	if (debug): print("***childrens***")
	for child in exp.getChildren():
		if pouFlag:
			index = varIdsIndex[idv]
			pous[index]=int(child.getText())
			pouFlag=False
			idv=''

		if child.getText() in varIdsIndex:
			idv=child.getText()

		if child.getText() == '**':
			pouFlag = True
	if (debug): print(pous)
	if (debug): print("***************")
	oper.append(1.0)
	for oprExp in exp.operators():
		if oprExp.getText() == '-':
			oper.append(-1.0)
		elif oprExp.getText() == '+':
			oper.append(1.0)


	for expCont in exp.expr_content():
		if (debug): print("++++expr_content+++++++")
		if (debug): print(expCont.getText())
		if (debug): print("+++++++++++++++++++++++")
		if expCont.getText() in varIdsIndex:
			index = varIdsIndex[expCont.getText()]
			coefs[index]=coefOper*oper[indexOper]
			indexOper = indexOper+1
			coefOper = 1.0
		else:
			coefOper = float(expCont.getText())
		
	if (debug): print(coefs)
	if (debug): print(oper)
	if (debug): print("=====================")
	if (debug): print("/////     /////////")
	if (debug): print(pous)
	if (debug): print("//////////////")
	return pous

def fixedVal(frr):
	arr = []
	fix = frr.fixed()
	num = fix.NUMBER()
	arr.append(float(num.getText()))
	return arr

def rangVal(frr):
	if (debug): print("=== RANGE ===")
	arr = []
	rang = frr.rang()

	for ran in rang.limit():
		arr.append(float(ran.getText()))
	if (debug): print(arr)
	if (debug): print("===  ===")
	return arr

class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print str(line) + ":" + str(column) + ": sintax ERROR, " + str(msg)
        sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print "Ambiguity ERROR, " + str(configs)
        sys.exit()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print "Attempting full context ERROR, " + str(configs)
        sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print "Context ERROR, " + str(configs)
        sys.exit()


class StochmizePrintListener(StochmizeListener):

	def enterProgram(self, ctx):
		if (debug): print(ctx.ID(0))
	# Enter a parse tree produced by StochmizeParser#vars_def.
	def enterVars_def(self, ctx):
		index = 0
		for idsVar in ctx.ID():
			varIdsIndex[idsVar.getText()]=index
			index=index+1

		index = 0
		for frr in ctx.fixed_range_random():
			if frr.fixed():
				varRanges[index]=fixedVal(frr)
				index=index+1
			elif frr.rang():
				varRanges[index]=rangVal(frr)
				index=index+1

		
		if (debug): print(varRanges)
	
	def enterSubjto(self, ctx):
		if (debug): print("enterSubjto")

		for subg_def in ctx.SUBJTO_DEF():
			subgetDefs.append(subg_def.getText())

		for expr in ctx.expr():
			varCoefs.append(expresiones(expr))

		for valRest in ctx.NUMBER():
			valNumRest.append(float(valRest.getText()))

	
	def enterObjectives(self, ctx):
		for min_max in ctx.min_max():
			min_maxObject.append(min_max.getText())

		for exprObj in ctx.expr():
			obgetsDefs.append(expresiones(exprObj))
			pousDefs.append(expresiones_pous(exprObj))
		
		if (debug): print("$$$ obj $$$$$$")
		if (debug): print(obgetsDefs)
		if (debug): print("$$$$$$$$$$$$$$")

def main():

	lexer = StochmizeLexer(FileStream(filename))
	stream = CommonTokenStream(lexer)
	parser = StochmizeParser(stream)
	parser._listeners = [ MyErrorListener() ]
	tree = parser.program()
	printer = StochmizePrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)

	model = {'objetives':{'type': min_maxObject, 'coefs':obgetsDefs, 'pous':pousDefs},
			'restrictions':{'numCoefs': valNumRest, 'coefs':varCoefs}}

	if (debug): print(model)

	def fun(vars, model):
		rest= []
		objt = []
		
		idNumObg=0
		for objcf in model['objetives']['coefs']:
			index = 0
			valob = 0
			for coef in objcf:
				valob = valob + coef*pow(vars[index] , model['objetives']['pous'][idNumObg][index])
				index=index+1
			objt.append(valob)
			idNumObg=idNumObg+1

		idNumRest=0
		for restcf in model['restrictions']['coefs']:
			index = 0
			valrest = 0
			for coef in restcf:
				valrest = valrest + coef*vars[index]
				index=index+1
			rest.append(valrest-model['restrictions']['numCoefs'][idNumRest])
			idNumRest=idNumRest+1

		return objt,rest
	#Problem(num variables,num func objetivo, num restric)
	problem = Problem(len(varIdsIndex), len(obgetsDefs), len(varCoefs))

	ranges = [Real(0,0)]*len(varIdsIndex)

	index=0
	for var in varIdsIndex:
		ran = varRanges[varIdsIndex[var]]
		if len(ran) == 2:
			ranges[varIdsIndex[var]]=Real(ran[0],ran[1])
		else:
			ranges[varIdsIndex[var]]=Real(ran[0],ran[0])
		index=index+1

	problem.types[:] = ranges

	if (debug): print(ranges[0])
	if (debug): print(ranges[1])
	problem.constraints[:] = "<=0"
	problem.function = fun
	problem.model = model

	algorithm = NSGAII(problem)
	algorithm.run(10000)

	for solution in algorithm.result:
		if (debug): print(solution.objectives)

	
	plt.scatter([s.objectives[0] for s in algorithm.result],
	            [s.objectives[1] for s in algorithm.result])
	plt.xlim([-10.0, 20.0])
	plt.ylim([-10.0, 20.0])
	plt.xlabel("$f_1(x)$")
	plt.ylabel("$f_2(x)$")

	#fig = plt.figure()
	plt.show()
	
if __name__ == '__main__':
    main()