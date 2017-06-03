from platypus import NSGAII, Problem, Real

model = {'objetives':	 {'type':	  ['min'],'coefs':[[-1,4,9]]},
		 'restrictions': {'numCoefs': [5,10,7],        'coefs':[[-1,-1],[1,1],[1,1]]}}

print(Real(0,1))
def fun(vars,model):
	rest= []
	objt = []
	
	for objcf in model['objetives']['coefs']:
		index = 0
		valob = 0
		for coef in objcf:
			valob = valob + coef*vars[index]
			index=index+1
		objt.append(valob)

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
problem = Problem(3, 1, 3)
problem.types[:] = [Real(0, 4), Real(-1, 1),Real(0, 0)]
problem.constraints[:] = "<=0"
problem.function = fun

problem.model = model

algorithm = NSGAII(problem)
algorithm.run(100)

for solution in algorithm.result:
    print(solution.objectives)