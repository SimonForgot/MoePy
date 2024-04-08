class Exp:
    pass


class intE(Exp):
    def __init__(self, n):
        self.n = n


class idE(Exp):
    def __init__(self, s):
        self.s = s


class plusE(Exp):
    def __init__(self, l, r):
        self.l = l
        self.r = r


class multE(Exp):
    def __init__(self, l, r):
        self.l = l
        self.r = r


class appE(Exp):
    def __init__(self, s, args: list):
        self.s = s
        self.args = args


class FunDef:
    def __init__(cls, name, args: list, body: Exp):
        cls.name = name
        cls.args = args
        cls.body = body


class MoeIR:
    def __init__(self) -> None:
        self.funDefs = []
        self.exps = []