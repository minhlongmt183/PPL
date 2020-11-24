class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Type(AST):
    __metalclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class Program(AST):
    # decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl


    def __str__(self):
        return "Program([" + ','.join(str(j) for i in self.decl for j in i) + "])"

    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl): #variable:Id; varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl("+str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v ,param):
        return v.visitVarDecl(self, param)


class Id(AST): #name:str
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Id(" + str(self.name) + ")"
    def accept(self, v , param):
        return v.visitId(self, param)


class ASTGeneration(MPVisitor):


    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([vardecl.accept(self) for vardecl in ctx.vardecl()])

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        mp_type = ctx.mptype().accept(self)

        return [VarDecl(name, mp_type) for name in ctx.ids().accept(self)]

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return IntType() if ctx.INTTYPE() else FloatType()



    def visitIds(self,ctx:MPParser.IdsContext):

        return [Id(id.getText()) for id in ctx.ID()]