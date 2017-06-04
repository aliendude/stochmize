from platypus import *
import matplotlib.pyplot as plt

m={}
def belegundu(vars,m):
	x = vars[0]
	y = vars[1]
	return [-2*pow(x,2) + y, 2*x + y], [-x + y - 1, x + y - 7]

problem = Problem(2, 2, 2)
problem.types[:] = [Real(0, 5), Real(0, 5)]
problem.constraints[:] = "<=0"
problem.function = belegundu
problem.model=m

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