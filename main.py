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
                self.IR.exps.append(blk)
            else:
                self.IR.funDefs.append(blk)
        return self.IR

    def visitExpBlk(self, ctx: MoeParser.ExpBlkContext):
        return self.visit(ctx.expr())

    def visitFDBlk(self, ctx: MoeParser.FDBlkContext):
        return self.visit(ctx.fun_def())

    def visitINT(self, ctx: MoeParser.INTContext):
        return MoeIR.intE(int(ctx.INT().getText()))

    def visitVAR(self, ctx: MoeParser.VARContext):
        return MoeIR.idE(ctx.ID().getText())

    def visitADD(self, ctx: MoeParser.ADDContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return MoeIR.plusE(left, right)

    def visitMUL(self, ctx: MoeParser.MULContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return MoeIR.multE(left, right)

    def visitAPP(self, ctx: MoeParser.APPContext):
        fun_name = ctx.ID().getText()
        args = []
        for arg in ctx.expr():
            moeIR_arg = self.visit(arg)
            args.append(moeIR_arg)
        return MoeIR.appE(fun_name, args)

    def visitFun_def(self, ctx: MoeParser.Fun_defContext):
        fun_name = ""
        args = []
        i = 0
        for id in ctx.ID():
            if i == 0:
                fun_name = id.getText()
            else:
                args.append(id.getText())
            i += 1
        return MoeIR.FunDef(fun_name, args, self.visit(ctx.expr()))


with open("input.moe", "r") as file:
    input_file = file.read()
lexer = MoeLexer(InputStream(input_file))
tokens = CommonTokenStream(lexer)
parser = MoeParser(tokens)
tree = parser.file_()
Moetrans = MoeTS()
IR = Moetrans.visit(tree)
MoeIR.intepret(IR)
