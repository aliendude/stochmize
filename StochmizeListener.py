# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete listener for a parse tree produced by StochmizeParser.
class StochmizeListener(ParseTreeListener):

    # Enter a parse tree produced by StochmizeParser#program.
    def enterProgram(self, ctx):
        #pass
        print("%s" % ctx.ID(0))
        """
        for child in ctx.getChildren():
            print(child)
        """
        #return ctx.model(0)

    # Exit a parse tree produced by StochmizeParser#program.
    def exitProgram(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#model.
    def enterModel(self, ctx):
        #return ctx.vars_def()
        #print("enterModel")
        #print(ctx.vars_def())
        pass

    # Exit a parse tree produced by StochmizeParser#model.
    def exitModel(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#vars_def.
    def enterVars_def(self, ctx):
        #return ctx.fixed()
        print(ctx.ID())
        #print(ctx.ID(1))
        #print(ctx.ID(2))
        

    # Exit a parse tree produced by StochmizeParser#vars_def.
    def exitVars_def(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#fixed.
    def enterFixed(self, ctx):
        #return ctx.NUMBER
        print(ctx.NUMBER())
        

    # Exit a parse tree produced by StochmizeParser#fixed.
    def exitFixed(self, ctx):
        
        pass


    # Enter a parse tree produced by StochmizeParser#random.
    def enterRandom(self, ctx):
        print(ctx)

    # Exit a parse tree produced by StochmizeParser#random.
    def exitRandom(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#normal.
    def enterNormal(self, ctx):
        print(ctx.NORMAL())
        print(ctx.normal_params().NUMBER(1))

    # Exit a parse tree produced by StochmizeParser#normal.
    def exitNormal(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#unif.
    def enterUnif(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#unif.
    def exitUnif(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#normal_params.
    def enterNormal_params(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#normal_params.
    def exitNormal_params(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#unif_params.
    def enterUnif_params(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#unif_params.
    def exitUnif_params(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#subjto.
    def enterSubjto(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#subjto.
    def exitSubjto(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#objectives.
    def enterObjectives(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#objectives.
    def exitObjectives(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#expr.
    def enterExpr(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#expr.
    def exitExpr(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#expr_content.
    def enterExpr_content(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#expr_content.
    def exitExpr_content(self, ctx):
        pass


    # Enter a parse tree produced by StochmizeParser#operators.
    def enterOperators(self, ctx):
        pass

    # Exit a parse tree produced by StochmizeParser#operators.
    def exitOperators(self, ctx):
        pass


