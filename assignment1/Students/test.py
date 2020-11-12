class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        global lst
        lst = []
        for ele in ctx.decl:
            self.visit()
            isinstance
    def visitVarDecl(self,ctx:VarDecl,o:object):
        glo
    def visitConstDecl(self,ctx:ConstDecl,o:object):pass
        return ctx.name
    def visitIntType(self,ctx:IntType,o:object):
        pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

# class Program: #decl:List[Decl]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str,typ:Type

# class ConstDecl(Decl): #name:str,val:Lit

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class Lit(ABC): #abstract class

# class IntLit(Lit): #val:int