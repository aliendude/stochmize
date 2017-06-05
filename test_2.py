from antlr4 import *
from StochmizeLexer import StochmizeLexer
from StochmizeListener import StochmizeListener
from StochmizeParser import StochmizeParser
from pulp import * 
from platypus import *
import numpy as np
import antlr4
import sys
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def expreciones(exp):

	print("EXPRECIONES")
	print(exp.getText())
	index = 0.0
	coefOper = 1.0
	pouVal = 1
	indexOper = 0
	oper = [];
	coefs = [0]*len(varIdsIndex)
	pous = [1]*len(varIdsIndex)
	#print(varIdsIdent)
	"""
	for operator in exp.operators():
		print(operator.getText())
	"""
	idv=''
	pouFlag=False
	pouVal = 1
	print("***childrens***")
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
	print(pous)
	print("***************")
	oper.append(1.0)
	for oprExp in exp.operators():
		if oprExp.getText() == '-':
			oper.append(-1.0)
		elif oprExp.getText() == '+':
			oper.append(1.0)


	for expCont in exp.expr_content():
		print("++++expr_content+++++++")
		print(expCont.getText())
		print("+++++++++++++++++++++++")
		if expCont.getText() in varIdsIndex:
			index = varIdsIndex[expCont.getText()]
			coefs[index]=coefOper*oper[indexOper]
			indexOper = indexOper+1
			coefOper = 1.0
		else:
			coefOper = float(expCont.getText())
		
	print(coefs)
	print(oper)
	print("=====================")
	print("/////     /////////")
	print(pous)
	print("//////////////")
	return coefs


def expreciones_pous(exp):

	print("EXPRECIONES")
	print(exp.getText())
	index = 0.0
	coefOper = 1.0
	pouVal = 1
	indexOper = 0
	oper = [];
	coefs = [0]*len(varIdsIndex)
	pous = [1]*len(varIdsIndex)
	#print(varIdsIdent)
	"""
	for operator in exp.operators():
		print(operator.getText())
	"""
	idv=''
	pouFlag=False
	pouVal = 1
	print("***childrens***")
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
	print(pous)
	print("***************")
	oper.append(1.0)
	for oprExp in exp.operators():
		if oprExp.getText() == '-':
			oper.append(-1.0)
		elif oprExp.getText() == '+':
			oper.append(1.0)


	for expCont in exp.expr_content():
		print("++++expr_content+++++++")
		print(expCont.getText())
		print("+++++++++++++++++++++++")
		if expCont.getText() in varIdsIndex:
			index = varIdsIndex[expCont.getText()]
			coefs[index]=coefOper*oper[indexOper]
			indexOper = indexOper+1
			coefOper = 1.0
		else:
			coefOper = float(expCont.getText())
		
	print(coefs)
	print(oper)
	print("=====================")
	print("/////     /////////")
	print(pous)
	print("//////////////")
	return pous



def fixedVal(frr):
	arr = []
	fix = frr.fixed()
	num = fix.NUMBER()
	arr.append(float(num.getText()))
	return arr

def rangVal(frr):
	print("=== RANGE ===")
	arr = []
	rang = frr.rang()

	for ran in rang.limit():
		arr.append(float(ran.getText()))
	print(arr)
	print("===  ===")
	return arr

def exprecontent(exp):
	"""
	factor_signo_numero = []
	print("#####INI####")
	if exp.MINUS():
		factor_signo_numero.append(-1.0)
	else:
		factor_signo_numero.append(1.0)
	print(exp.getText())
	factor_signo_numero.append(exp.ID())
	print(factor_signo_numero)
	print("#####FIN####")
	"""

	""""
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

	
	def enterObjectives(self, ctx):
		
		"""
		for idsObj in ctx.ID():
			print(idsObj.getText())
			idsObjets.append(idsObj.getText())"""

		for min_max in ctx.min_max():
			min_maxObject.append(min_max.getText())

		for exprObj in ctx.expr():
			obgetsDefs.append(expreciones(exprObj))
			pousDefs.append(expreciones_pous(exprObj))
		
		print("$$$ obj $$$$$$")
		print(obgetsDefs)
		print("$$$$$$$$$$$$$$")
	

def main():

	lexer = StochmizeLexer(FileStream('input.sz'))
	stream = CommonTokenStream(lexer)
	parser = StochmizeParser(stream)
	tree = parser.program()

	printer = StochmizePrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)

	model = {'objetives':{'type': min_maxObject, 'coefs':obgetsDefs, 'pous':pousDefs},
			'restrictions':{'numCoefs': valNumRest, 'coefs':varCoefs}}

	print(model)

	
	def fun(vars,model):
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

	print(ranges[0])
	print(ranges[1])
	problem.constraints[:] = "<=0"
	problem.function = fun
	problem.model = model

	algorithm = NSGAII(problem)
	algorithm.run(10000)

	for solution in algorithm.result:
		print(solution.objectives)

	
	plt.scatter([s.objectives[0] for s in algorithm.result],
	            [s.objectives[1] for s in algorithm.result])
	plt.xlim([-10.0, 20.0])
	plt.ylim([-10.0, 20.0])
	plt.xlabel("$f_1(x)$")
	plt.ylabel("$f_2(x)$")

	#fig = plt.figure()
	plt.show()
	
	"""
	#problem = DTLZ2(3)
	algorithms = [NSGAII]
	# run the experiment using Python 3's concurrent futures for parallel evaluation
	with ProcessPoolEvaluator() as evaluator:
		results = experiment(algorithms, problem, seeds=1, nfe=10000, evaluator=evaluator)
		# display the results
	fig = plt.figure()
	for i, algorithm in enumerate(six.iterkeys(results)):
		result = results[algorithm][problem][0]
		ax = fig.add_subplot(2, 5, i+1, projection='3d')
		ax.scatter([s.objectives[0] for s in result],
			[s.objectives[1] for s in result],
			[s.objectives[2] for s in result])
		ax.set_title(algorithm)
		ax.set_xlim([0, 1.1])
		ax.set_ylim([0, 1.1])
		ax.set_zlim([0, 1.1])
		ax.view_init(elev=30.0, azim=15.0)
		ax.locator_params(nbins=4)

	plt.show()
	"""
if __name__ == '__main__':
    main()