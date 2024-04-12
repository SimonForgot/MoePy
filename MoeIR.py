class Exp:
    pass


class intE(Exp):
    def __init__(self, n: int):
        self.n = n


class idE(Exp):
    def __init__(self, s: str):
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
    def __init__(self, fn: str, args: list):
        self.fn = fn
        self.args = args


class FunDef:
    def __init__(cls, name: str, args: list, body: Exp):
        cls.name = name
        cls.args = args
        cls.body = body


class MoeIR:
    def __init__(self) -> None:
        self.funDefs = []
        self.exps = []


def intepretExp(exp: Exp, fds: list, id_dict: dict):
    if isinstance(exp, idE):
        return id_dict[exp.s]
    elif isinstance(exp, intE):
        return exp.n
    elif isinstance(exp, plusE):
        return intepretExp(exp.l, fds, id_dict) + intepretExp(exp.r, fds, id_dict)
    elif isinstance(exp, multE):
        return intepretExp(exp.l, fds, id_dict) * intepretExp(exp.r, fds, id_dict)
    elif isinstance(exp, appE):
        f = next((fd for fd in fds if fd.name == exp.fn), None)
        if f == None:
            raise Exception("can't find func def: " + exp.fn)
        args_dict = zip(f.args, (intepretExp(e, fds, id_dict) for e in exp.args))
        return intepretExp(f.body, fds, dict(args_dict))


def intepret(moe_ir: MoeIR):
    exps = moe_ir.exps
    for exp in exps:
        r = intepretExp(exp, moe_ir.funDefs, {})
        print(r)
