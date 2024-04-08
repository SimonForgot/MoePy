from antlr4 import *
import MoeIR
from antlr.MoeLexer import MoeLexer
from antlr.MoeParser import MoeParser
from antlr.MoeVisitor import MoeVisitor


class MoeTS(MoeVisitor):
    def visitFile(self, ctx: MoeParser.FileContext):
        self.IR = MoeIR.MoeIR()
        for b in ctx.block():
            blk = self.visit(b)
            if isinstance(blk, MoeIR.Exp):
                print("Exp")
            else:
                print("FunDef")
        return self.IR

    def visitExpBlk(self, ctx: MoeParser.ExpBlkContext):
        return MoeIR.intE(3)

    def visitFDBlk(self, ctx: MoeParser.FDBlkContext):
        return MoeIR.FunDef(1,2,3)

    """
    def visitNumber(self, ctx:MoeParser.NumberContext):
        return float(ctx.getText())

    def visitParenthesis(self, ctx:MoeParser.ParenthesisContext):
        return self.visit(ctx.expression())

    def visitMulDiv(self, ctx:MoeParser.MulDivContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == MoeParser.MUL:
            return left * right
        else:
            return left / right
    """


with open("input.moe", "r") as file:
    input_file = file.read()
lexer = MoeLexer(InputStream(input_file))
tokens = CommonTokenStream(lexer)
parser = MoeParser(tokens)
tree = parser.file_()
Moetrans = MoeTS()
IR = Moetrans.visit(tree)
