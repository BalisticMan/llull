# Generated from llull.g4 by ANTLR 4.9
from antlr4 import *
from colored import fg
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
else:
    from llullParser import llullParser

# This class defines a complete generic visitor for a prettifying a llull program produced by llullParser.


class prettierVisitor(ParseTreeVisitor):

    PROTECTED_KEYWORDS = fg('deep_pink_2')
    METHOD_NAME = fg('blue')
    DEFAULT = fg('grey_93')
    BODY_KEYWORDS = fg('magenta')
    TEXT = fg('orange_4b')
    spaces = "    "

    def __init__(self):
        self.level = 0

    def printInline(self, text, fg):
        if fg is None:
            print(self.DEFAULT + text, end='')
        else:
            print(fg + text, end='')

    def printDefault(self, text, fg):
        if fg is None:
            print(self.DEFAULT + text)
        else:
            print(fg + text)

    def getSpaces(self):
        spaces = ""
        for i in range(self.level):
            spaces += f"{self.spaces}"
        return spaces

    # Visit a parse tree produced by llullParser#root.
    def visitRoot(self, ctx: llullParser.RootContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#expr.
    def visitExpr(self, ctx: llullParser.ExprContext):
        l = ctx.getChildren()
        first = True
        for method in l:
            if first:
                first = False
            else:
                self.printDefault("", None)
            self.visit(method)

    # Visit a parse tree produced by llullParser#value.

    def visitValue(self, ctx: llullParser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#number.
    def visitNumber(self, ctx: llullParser.NumberContext):
        self.printInline(ctx.getText(), self.BODY_KEYWORDS)

    # Visit a parse tree produced by llullParser#identifier.
    def visitIdentifier(self, ctx: llullParser.IdentifierContext):
        self.printInline(ctx.getText(), None)

    # Visit a parse tree produced by llullParser#relational.
    def visitRelational(self, ctx: llullParser.RelationalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#string.
    def visitString(self, ctx: llullParser.StringContext):
        l = list(ctx.getChildren())
        text = self.visit(l[1])
        self.printInline(f"\"{text}\"", self.TEXT)

    # Visit a parse tree produced by llullParser#write.
    def visitWrite(self, ctx: llullParser.WriteContext):
        l = list(ctx.getChildren())
        self.printInline("write", self.BODY_KEYWORDS)
        self.printInline("(", None)
        self.visit(l[2])
        self.printInline(")", None)

    # Visit a parse tree produced by llullParser#read.
    def visitRead(self, ctx: llullParser.ReadContext):
        l = list(ctx.getChildren())
        id = l[2].getText()
        self.printInline("read", self.BODY_KEYWORDS)
        self.printInline(f"({id})", None)

    # Visit a parse tree produced by llullParser#assignoperation.
    def visitAssignoperation(self, ctx: llullParser.AssignoperationContext):
        l = list(ctx.getChildren())
        variableName = l[0].getText()
        self.printInline(f"{variableName} = ", None)
        self.visit(l[2])

    # Visit a parse tree produced by llullParser#operation.
    def visitOperation(self, ctx: llullParser.OperationContext):
        l = list(ctx.getChildren())
        size = len(l)

        if size == 1:
            self.visit(l[0])
        elif size == 2:
            self.printInline("-", self.BODY_KEYWORDS)
            self.visit(l[1])
        else:
            if (l[0].getText() != "("):
                self.visit(l[0])
                self.printInline(f" {l[1].getText()} ", None)
                self.visit(l[2])
            else:
                self.printInline("(", None)
                self.visit(l[1])
                self.printInline(")", None)

    # Visit a parse tree produced by llullParser#relatinoaloperation
    def visitRelationaloperation(self, ctx: llullParser.RelationaloperationContext):
        l = list(ctx.getChildren())
        operator = l[1].getText()
        self.visit(l[0])
        self.printInline(f" {operator} ", None)
        self.visit(l[2])

    # Visit a parse tree produced by llullParser#ifconditional.
    def visitIfconditional(self, ctx: llullParser.IfconditionalContext):
        spaces = self.getSpaces()
        self.level += 1

        l = list(ctx.getChildren())
        self.printInline("if", self.PROTECTED_KEYWORDS)
        self.printInline(" (", None)
        self.visit(l[2])
        self.printDefault(") {", None)
        self.visit(l[5])

        self.level -= 1
        self.printInline(spaces, None)
        self.printInline("}", None)

        if len(l) == 8:
            self.visit(l[7])

    # Visit a parse tree produced by llullParser#elseconditional.

    def visitElseconditional(self, ctx: llullParser.ElseconditionalContext):
        spaces = self.getSpaces()
        self.level += 1

        l = list(ctx.getChildren())
        self.printInline(f" else", self.PROTECTED_KEYWORDS)
        self.printDefault(" {", None)
        self.visit(l[2])

        self.level -= 1
        self.printInline(spaces, None)
        self.printInline("}", None)

    # Visit a parse tree produced by llullParser#whileloop.
    def visitWhileloop(self, ctx: llullParser.WhileloopContext):
        spaces = self.getSpaces()
        self.level += 1

        l = list(ctx.getChildren())
        self.printInline("while", self.PROTECTED_KEYWORDS)
        self.printInline(" (", None)
        self.visit(l[2])
        self.printDefault(") {", None)
        self.visit(l[5])

        self.level -= 1
        self.printInline(spaces, None)
        self.printInline("}", None)

    # Visit a parse tree produced by llullParser#forloop.

    def visitForloop(self, ctx: llullParser.ForloopContext):
        spaces = self.getSpaces()
        self.level += 1

        l = list(ctx.getChildren())
        self.printInline("for", self.PROTECTED_KEYWORDS)
        self.printInline(" (", None)
        self.visit(l[2])
        self.printInline("; ", None)
        self.visit(l[4])
        self.printInline("; ", None)
        self.visit(l[6])
        self.printDefault(") {", None)
        self.visit(l[9])

        self.level -= 1
        self.printInline(spaces, None)
        self.printInline("}", None)

    # Visit a parse tree produced by llullParser#method.
    def visitMethod(self, ctx: llullParser.MethodContext):
        self.level += 1

        l = list(ctx.getChildren())
        methodName = l[1].getText()
        self.printInline("void", self.PROTECTED_KEYWORDS)
        self.printInline(f" {methodName}", self.METHOD_NAME)
        self.printInline("(", None)
        self.visit(l[3])
        self.printDefault(f") ""{", None)
        self.visit(l[6])

        self.level -= 1
        self.printDefault("}", None)

    # Visit a parse tree produced by llullParser#call.
    def visitCall(self, ctx: llullParser.CallContext):
        l = list(ctx.getChildren())
        methodName = l[0].getText()
        self.printInline(methodName, self.BODY_KEYWORDS)
        self.printInline("(", None)
        self.visit(l[2])
        self.printInline(")", None)

        # Visit a parse tree produced by llullParser#parameters.
    def visitParameters(self, ctx: llullParser.ParametersContext):
        l = list(ctx.getChildren())
        for argument in l:
            if argument.getText() != ',':
                self.visit(argument)
            else:
                self.printInline(", ", None)

    # Visit a parse tree produced by llullParser#arguments.
    def visitArguments(self, ctx: llullParser.ArgumentsContext):
        l = list(ctx.getChildren())
        for argument in l:
            if argument.getText() != ',':
                self.visit(argument)
            else:
                self.printInline(", ", None)

    # Visit a parse tree produced by llullParser#writearguments.
    def visitWritearguments(self, ctx: llullParser.WriteargumentsContext):
        l = list(ctx.getChildren())
        for argument in l:
            if argument.getText() != ',':
                self.visit(argument)
            else:
                self.printInline(", ", None)

    # Visit a parse tree produced by llullParser#body.
    def visitBody(self, ctx: llullParser.BodyContext):
        spaces = self.getSpaces()
        l = list(ctx.getChildren())
        for node in l:
            self.printInline(spaces, None)
            self.visit(node)
            self.printDefault("", None)

    # Visit a parse tree produced by llullParser#array.
    def visitDeclarearray(self, ctx: llullParser.DeclarearrayContext):
        l = list(ctx.getChildren())
        self.printInline("array", self.BODY_KEYWORDS)
        id = l[2].getText()
        self.printInline(f"({id}, ", None)
        self.visit(l[4])
        self.printInline(")", None)

    # Visit a parse tree produced by llullParser#setarray.
    def visitSetarray(self, ctx: llullParser.SetarrayContext):
        l = list(ctx.getChildren())
        self.printInline("set", self.BODY_KEYWORDS)
        id = l[2].getText()
        self.printInline(f"({id}, ", None)
        self.visit(l[4])
        self.printInline(", ", None)
        self.visit(l[6])
        self.printInline(")", None)

    # Visit a parse tree produced by llullParser#getarray.
    def visitGetarray(self, ctx: llullParser.GetarrayContext):
        l = list(ctx.getChildren())
        self.printInline("get", self.BODY_KEYWORDS)
        id = l[2].getText()
        self.printInline(f"({id}, ", None)
        self.visit(l[4])
        self.printInline(")", None)

    def visitText(self, ctx: llullParser.TextContext):
        text = ""
        g = ctx.getChildren()
        first = True
        for i in range(ctx.getChildCount()):
            w = next(g)
            if not first:
                text += f" {w}"
            else:
                first = False
                text += str(w)
        return text


del llullParser
