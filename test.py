from antlr4 import *
from StochmizeLexer import StochmizeLexer
from StochmizeListener import StochmizeListener
from StochmizeParser import StochmizeParser
import antlr4
import sys

varIds = []
varNum = []

normal_params_m = []
normal_params_v = []

unif_params_a = []
unif_params_b = []
class StochmizePrintListener(StochmizeListener):

	def enterProgram(self, ctx):
		print(ctx.ID(0))
	# Enter a parse tree produced by StochmizeParser#vars_def.
	def enterVars_def(self, ctx):
		
		
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


def main():

	lexer = StochmizeLexer(FileStream('input.sz'))
	stream = CommonTokenStream(lexer)
	parser = StochmizeParser(stream)
	tree = parser.program()
	#varsd = parser.vars_def()

	"""
	print(tree.ID(0))
	print(varsd.ID())
	
	print(tree.model(0).vars_def().ID())

	print()
	"""
	printer = StochmizePrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)
	print(varIds)
	print(varNum)
	print(normal_params_m)
	print(normal_params_v)
	print(unif_params_a)
	print(unif_params_b)
	"""
	printer = StochmizeListener()
	res=printer.enterProgram(tree)
	print(res)
	"""
	"""
	walker = ParseTreeWalker()
	walker.walk(printer,tree)
	"""

if __name__ == '__main__':
    main()