from antlr4 import *
from StochmizeLexer import StochmizeLexer
from StochmizeListener import StochmizeListener
from StochmizeParser import StochmizeParser
from pulp import * 
import numpy as np
import antlr4
import sys
import os

varIdsIndex = {}
varRanges = {}
varCoefs = []

valNumRest = []
subgetDefs = []
obgetsDefs = []

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

def expreciones(exp):
	print("EXPRECIONES")
	
	index = 0.0;
	coefOper = 1.0
	oper = [];
	coefs = [0]*len(varIdsIndex)
	#print(varIdsIdent)

	for oprExp in exp.operators():
		oper.append(oprExp.getText())

	for expCont in exp.expr_content():
		if expCont.getText() in varIdsIndex:
			index = varIdsIndex[expCont.getText()]
			coefs[index]=coefOper
			coefOper = 1.0
		else:
			coefOper = float(expCont.getText())

	print(coefs)
	print("=====================")
	return coefs

def fixedVal(frr):
	arr = []
	fix = frr.fixed()
	num = fix.NUMBER()
	arr.append(float(num.getText()))
	return arr

def rangVal(frr):
	arr = []
	rang = frr.rang()
	for ran in rang.NUMBER():
		arr.append(float(ran.getText()))
	return arr
"""
def exprecontent(exp):
	print("######## INI #########")
	for child in exp.getChildren():
		print(type(child))
		print(child) 
	print("######### FIN ########")
"""
class StochmizePrintListener(StochmizeListener):

	def enterProgram(self, ctx):
		print(ctx.ID(0))
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
		print(varRanges)
		"""
		print("enterVars_def")
		for child in ctx.getChildren():
			if isinstance(child , antlr4.tree.Tree.TerminalNodeImpl):
				if child.getText() != ';':
					varIds.append(child.getText())

			if isinstance(child , StochmizeParser.FixedContext):
				for childFixer in child.getChildren():
					if childFixer.getText() != '=':
						varNum.append(childFixer.getText())

			if isinstance(child , StochmizeParser.RandomContext):
				for childRandom in child.getChildren():
					if isinstance(childRandom , StochmizeParser.NormalContext):
						normal_params_m.append(childRandom.normal_params().NUMBER(0).getText())
						normal_params_v.append(childRandom.normal_params().NUMBER(1).getText())

					if isinstance(childRandom , StochmizeParser.UnifContext):
						unif_params_a.append(childRandom.unif_params().NUMBER(0).getText())
						unif_params_b.append(childRandom.unif_params().NUMBER(1).getText())
		print("==========================")
		"""

	
	def enterSubjto(self, ctx):
		print("enterSubjto")

		for subg_def in ctx.SUBJTO_DEF():
			subgetDefs.append(subg_def.getText())

		for expr in ctx.expr():
			varCoefs.append(expreciones(expr))

		for valRest in ctx.NUMBER():
			valNumRest.append(float(valRest.getText()))

		print(varCoefs)
		print(subgetDefs)
		print(valNumRest)


	
	def enterObjectives(self, ctx):
		
		"""
		for idsObj in ctx.ID():
			print(idsObj.getText())
			idsObjets.append(idsObj.getText())"""

		for min_max in ctx.min_max():
			min_maxObject.append(min_max.getText())

		for exprObj in ctx.expr():
			obgetsDefs.append(expreciones(exprObj))
		print(min_maxObject)
		print(obgetsDefs)

		"""
		for child in ctx.getChildren():
			print(type(child))
			print(child)
			if isinstance(child , StochmizeParser.ExprContext):
				expreciones(child)"""
		print("==========================")
	

def main():

	lexer = StochmizeLexer(FileStream('input.sz'))
	stream = CommonTokenStream(lexer)
	parser = StochmizeParser(stream)
	tree = parser.program()

	printer = StochmizePrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)
	"""
	arr=[0,0,0,0,0]
	print(arr)
	arr[3]=5
	print(arr)
	"""
	#print(varIds['y'])
	
	"""
	print(varNum)
	print(normal_params_m)
	print(normal_params_v)
	print(unif_params_a)
	print(unif_params_b)
	print(subIds)
	print(subgetDefs)
	print(subgetNumbers)
	print(MaxMinObj)
	print(idsObjets)
	"""

	
	if min_maxObject[0] == 'min':
		prob = LpProblem("test1", LpMinimize)
	else:
		prob = LpProblem("test1", LpMaximize) 

	varsLp = {}
	valProb = 0
	#variables
	index=0
	for var in varIdsIndex:
		ran = varRanges[varIdsIndex[var]]
		if len(ran) == 2:
			varsLp[varIdsIndex[var]]=LpVariable(var, ran[0], ran[1])
			valProb = valProb + varsLp[varIdsIndex[var]]*obgetsDefs[0][varIdsIndex[var]]
		else:
			varsLp[varIdsIndex[var]]=LpVariable(var, ran[0])
			valProb = valProb + varsLp[varIdsIndex[var]]*obgetsDefs[0][varIdsIndex[var]]
		index=index+1

	#print(valProb)

	#objetive	

	prob += valProb

	#restrictions
	rest = 0
	indexRestVal = 0

	for restef in varCoefs:
		index = 0
		valrest = 0
		for coef in restef:
			valrest = valrest + coef*varsLp[index]
			index=index+1

		sub = subgetDefs[indexRestVal]
		print(valrest)
		if sub == '==':
			prob += valrest == valNumRest[indexRestVal]
		elif sub == '<=':
			prob += valrest <= valNumRest[indexRestVal]
		elif sub == '>=':
			prob += valrest >= valNumRest[indexRestVal]
		elif sub == '<':
			prob += valrest < valNumRest[indexRestVal]
		elif sub == '>':
			prob += valrest > valNumRest[indexRestVal]
		indexRestVal=indexRestVal+1

	print(prob)
	GLPK().solve(prob) 
	os.system('clear')
	print(prob)
	for v in prob.variables(): 
		print v.name, "=", v.varValue 

	print "objective=", value(prob.objective) 
	"""
	prob = LpProblem("test1", LpMaximize)
	# Variables 
	x = LpVariable("x", 0, 4) 
	y = LpVariable("y", 1, 1)
	z = LpVariable("z", 0) 

	# Objective
	prob += 1*x + 4*y + 9*z 

	# Constraints 
	prob += x+y <= 5 
	prob += x+z >= 10 
	prob += y+z == 7 
	print("========================")
	print(prob)
	print("========================")
	
	GLPK().solve(prob) 
	os.system('clear')
	# Solution 
	print("========================")
	print(prob)
	print("========================")
	for v in prob.variables(): 
		print v.name, "=", v.varValue 

	print "objective=", value(prob.objective)  
	"""
if __name__ == '__main__':
    main()