from antlr4 import *
from StochmizeLexer import StochmizeLexer
from StochmizeListener import StochmizeListener
from StochmizeParser import StochmizeParser
import sys

"""
class StochmizePrintListener(StochmizeListener):
    def enterProgram(self, ctx):
        print("%s" % ctx.ID('T_0'))

	def enterModel(self, ctx):
		print("%s" % ctx.VARS_DEF(0))
"""
def main():

	lexer = StochmizeLexer(FileStream('input.sz'))
	stream = CommonTokenStream(lexer)
	parser = StochmizeParser(stream)
	tree = parser.program()
	varsd = parser.vars_def()

	"""
	print(tree.ID(0))
	print(varsd.ID())
	
	print(tree.model(0).vars_def().ID())

	print()
	"""
	printer = StochmizeListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)
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