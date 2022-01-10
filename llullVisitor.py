# Generated from llull.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
else:
    from llullParser import llullParser

# This class defines a complete generic visitor for a parse tree produced by llullParser.


class llullVisitor(ParseTreeVisitor):

    # methods : {
    #     methodName: {
    #         body: value,
    #         params: {
    #             paramName: value | None
    #         },
    #         paramCount: None
    #     }
    # }

    def __init__(self, activeMethod, initialArguments):
        self.methods = {}
        self.activeMethod = activeMethod
        self.initialArguments = initialArguments
        self.executionQueue = []
        self.currentExecution = 0

    # Visit a parse tree produced by llullParser#root.
    def visitRoot(self, ctx: llullParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#expr.
    def visitExpr(self, ctx: llullParser.ExprContext):
        l = ctx.getChildren()
        for method in l:
            self.visit(method)
        if self.activeMethod in self.methods:
            if (self.activeMethod != 'main'):
                keys_list = list(self.methods[self.activeMethod]['params'])
                i = 0
                if (len(self.initialArguments) != self.methods[self.activeMethod]['paramCount']):
                    raise Exception(
                        "Invalid number of arguments for method '" + self.activeMethod + "'.")
                for argument in self.initialArguments:
                    key = keys_list[i]
                    self.methods[self.activeMethod]['params'][key] = argument
                    i = i + 1

            self.executionQueue.append(self.methods[self.activeMethod])
            self.currentExecution = 0
            self.executionQueue[self.currentExecution]['variables'] = {}
            self.executionQueue[self.currentExecution]['tables'] = {}
            self.visit(self.methods[self.activeMethod]['body'])
        else:
            raise Exception("There is no '" +
                            self.activeMethod + "' method defined.")

    # Visit a parse tree produced by llullParser#value.
    def visitValue(self, ctx: llullParser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#number.
    def visitNumber(self, ctx: llullParser.NumberContext):
        return int(ctx.getText())

    # Visit a parse tree produced by llullParser#identifier.
    def visitIdentifier(self, ctx: llullParser.IdentifierContext):
        id = ctx.getText()
        if id in self.executionQueue[self.currentExecution]['variables']:
            return self.executionQueue[self.currentExecution]['variables'][id]
        elif id in self.executionQueue[self.currentExecution]['params']:
            return self.executionQueue[self.currentExecution]['params'][id]
        elif id in self.executionQueue[self.currentExecution]['tables']:
            return self.executionQueue[self.currentExecution]['tables'][id]
        raise Exception("Variable '" + id + "' does not exist.")

    # Visit a parse tree produced by llullParser#relational.
    def visitRelational(self, ctx: llullParser.RelationalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#string.
    def visitString(self, ctx: llullParser.StringContext):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    # Visit a parse tree produced by llullParser#write.
    def visitWrite(self, ctx: llullParser.WriteContext):
        l = list(ctx.getChildren())
        arguments = self.visit(l[2])
        for arg in arguments:
            print(arg, end=' ')
        print()

    # Visit a parse tree produced by llullParser#read.
    def visitRead(self, ctx: llullParser.ReadContext):
        l = list(ctx.getChildren())
        id = l[2].getText()
        if id in self.executionQueue[self.currentExecution]['variables']:
            raise Exception("Variable '" + id + "' already exists.")
        elif id in self.executionQueue[self.currentExecution]['params']:
            raise Exception("Variable '" + id + "' already exists.")
        elif id in self.executionQueue[self.currentExecution]['tables']:
            raise Exception("Variable '" + id + "' already exists.")
        else:
            self.executionQueue[self.currentExecution]['variables'][id] = int(
                input())

    # Visit a parse tree produced by llullParser#assignoperation.
    def visitAssignoperation(self, ctx: llullParser.AssignoperationContext):
        l = list(ctx.getChildren())
        variableName = l[0].getText()
        if variableName in self.executionQueue[self.currentExecution]['params']:
            raise Exception("There already exists a variable with name '" +
                            variableName + "'.")
        else:
            value = self.visit(l[2])
            self.executionQueue[self.currentExecution]['variables'][variableName] = value

    # Visit a parse tree produced by llullParser#operation.
    def visitOperation(self, ctx: llullParser.OperationContext):
        l = list(ctx.getChildren())
        size = len(l)

        if(size < 3):
            if size == 1:
                return self.visit(l[0])
            else:
                return -1 * self.visit(l[1])
        else:
            operation = self.visit(l[1])
            isOperation = operation == None
            if (isOperation):
                a = self.visit(l[0])
                b = self.visit(l[2])
                operator = l[1].getText()
                result = None
                if operator == '+':
                    result = a + b
                elif operator == '-':
                    result = a - b
                elif operator == '/':
                    if (b == 0):
                        raise Exception("Can't divide by 0")
                    result = a / b
                elif operator == '*':
                    result = a * b
                elif operator == '%':
                    result = a % b
                return result
            else:
                return operation

    # Visit a parse tree produced by llullParser#relatinoaloperation
    def visitRelationaloperation(self, ctx: llullParser.RelationaloperationContext):
        l = list(ctx.getChildren())
        a = self.visit(l[0])
        b = self.visit(l[2])
        operator = l[1].getText()
        result = None
        if operator == '<':
            result = a < b
        elif operator == '>':
            result = a > b
        elif operator == '<=':
            result = a <= b
        elif operator == '>=':
            result = a >= b
        elif operator == '==':
            result = a == b
        elif operator == '<>':
            result = a != b
        if result:
            return 1
        else:
            return 0

    # Visit a parse tree produced by llullParser#ifconditional.
    def visitIfconditional(self, ctx: llullParser.IfconditionalContext):
        l = list(ctx.getChildren())
        fulfillsCondition = self.visit(l[2])
        if fulfillsCondition:
            self.visit(l[5])
        elif not fulfillsCondition and len(l) == 8:
            self.visit(l[7])

    # Visit a parse tree produced by llullParser#elseconditional.
    def visitElseconditional(self, ctx: llullParser.ElseconditionalContext):
        l = list(ctx.getChildren())
        self.visit(l[2])

    # Visit a parse tree produced by llullParser#whileloop.
    def visitWhileloop(self, ctx: llullParser.WhileloopContext):
        l = list(ctx.getChildren())
        fulfillsCondition = self.visit(l[2])
        while (fulfillsCondition):
            self.visit(l[5])
            fulfillsCondition = self.visit(l[2])

    # Visit a parse tree produced by llullParser#forloop.
    def visitForloop(self, ctx: llullParser.ForloopContext):
        l = list(ctx.getChildren())
        self.visit(l[2])

        relationalOperation = l[4]
        body = l[9]
        assignOperation = l[6]

        while (self.visit(relationalOperation)):
            self.visit(body)
            self.visit(assignOperation)

    # Visit a parse tree produced by llullParser#method.
    def visitMethod(self, ctx: llullParser.MethodContext):
        l = list(ctx.getChildren())
        methodName = l[1].getText()

        if methodName in self.methods:
            raise Exception("Method '" + methodName + "' already exists.")

        params = self.visit(l[3])
        paramCount = len(params)
        body = l[6]
        self.methods[methodName] = {}
        self.methods[methodName]['params'] = {}

        for param in params:
            if (param in self.methods[methodName]['params']):
                raise Exception("Parameter '" + param + "' already exists.")
            self.methods[methodName]['params'][param] = None

        self.methods[methodName]['body'] = body
        self.methods[methodName]['paramCount'] = paramCount

    # Visit a parse tree produced by llullParser#call.
    def visitCall(self, ctx: llullParser.CallContext):
        l = list(ctx.getChildren())
        methodName = l[0].getText()
        if methodName in self.methods:
            self.activeMethod = methodName
            arguments = self.visit(l[2])
            tables = []
            for arg in l:
                if arg.getText() in self.executionQueue[self.currentExecution]['tables']:
                    tables.append(arg.getText())
            keys_list = list(self.methods[methodName]['params'])
            i = 0

            if (len(arguments) != self.methods[methodName]['paramCount']):
                raise Exception(
                    "Invalid number of arguments for method '" + methodName + "'.")

            self.currentExecution = self.currentExecution + 1
            self.executionQueue.append(self.methods[methodName])
            self.executionQueue[self.currentExecution]['variables'] = {}
            self.executionQueue[self.currentExecution]['tables'] = {}

            for argument in arguments:
                key = keys_list[i]

                self.executionQueue[self.currentExecution]['params'][key] = argument
                i = i + 1

            # search for modified tables passed by reference
            self.visit(self.executionQueue[self.currentExecution]['body'])
            for table in tables:
                modifiedTable = self.executionQueue[self.currentExecution]['params'][table]
                self.executionQueue[self.currentExecution -
                                    1]['tables'][table] = modifiedTable
            self.currentExecution = self.currentExecution - 1
            self.executionQueue.pop()
        else:
            raise Exception("Method '" + methodName + "' does not exist.")

    # Visit a parse tree produced by llullParser#parameters.
    def visitParameters(self, ctx: llullParser.ParametersContext):
        l = list(ctx.getChildren())
        params = []
        for param in l:
            parsedParam = param.getText()
            if parsedParam != ',':
                params.append(parsedParam)
        return params

    # Visit a parse tree produced by llullParser#arguments.
    def visitArguments(self, ctx: llullParser.ArgumentsContext):
        l = list(ctx.getChildren())
        arguments = []
        for argument in l:
            if argument.getText() != ',':
                arguments.append(self.visit(argument))
        return arguments

    # Visit a parse tree produced by llullParser#writearguments.
    def visitWritearguments(self, ctx: llullParser.WriteargumentsContext):
        l = list(ctx.getChildren())
        arguments = []
        for argument in l:
            if argument.getText() != ',':
                arguments.append(self.visit(argument))
        return arguments

    # Visit a parse tree produced by llullParser#body.
    # We clean all the previous local variables declared
    def visitBody(self, ctx: llullParser.BodyContext):
        l = list(ctx.getChildren())
        for node in l:
            self.visit(node)

    # Visit a parse tree produced by llullParser#array.
    def visitDeclarearray(self, ctx: llullParser.DeclarearrayContext):
        l = list(ctx.getChildren())
        id = l[2].getText()
        if id in self.executionQueue[self.currentExecution]['tables']:
            raise Exception(
                "There already exists a table with name '" + id + "' .")
        elif id in self.executionQueue[self.currentExecution]['variables']:
            raise Exception(
                "There already exists a table with name '" + id + "' .")
        numberOfEntries = self.visit(l[4])
        arr = []
        arr = [0 for i in range(numberOfEntries)]
        self.executionQueue[self.currentExecution]['tables'][id] = arr

    # Visit a parse tree produced by llullParser#setarray.
    def visitSetarray(self, ctx: llullParser.SetarrayContext):
        l = list(ctx.getChildren())
        id = l[2].getText()
        index = self.visit(l[4])
        value = self.visit(l[6])
        if id in self.executionQueue[self.currentExecution]['tables']:
            if index >= len(self.executionQueue[self.currentExecution]['tables'][id]) or index < 0:
                raise Exception("Invalid index to access table.")
            self.executionQueue[self.currentExecution]['tables'][id][index] = value
        elif id in self.executionQueue[self.currentExecution]['params']:
            if index >= len(self.executionQueue[self.currentExecution]['params'][id]) or index < 0:
                raise Exception("Invalid index to access table.")
            self.executionQueue[self.currentExecution]['params'][id][index] = value
        else:
            raise Exception(
                "Table '" + id + "' does not exist.")

    # Visit a parse tree produced by llullParser#getarray.
    def visitGetarray(self, ctx: llullParser.GetarrayContext):
        l = list(ctx.getChildren())
        id = l[2].getText()
        index = self.visit(l[4])
        if id in self.executionQueue[self.currentExecution]['tables']:
            if index >= len(self.executionQueue[self.currentExecution]['tables'][id]) or index < 0:
                raise Exception("Invalid index to access table.")
            return self.executionQueue[self.currentExecution]['tables'][id][index]
        elif id in self.executionQueue[self.currentExecution]['params']:
            if index >= len(self.executionQueue[self.currentExecution]['params'][id]) or index < 0:
                raise Exception("Invalid index to access table.")
            return self.executionQueue[self.currentExecution]['params'][id][index]
        else:
            raise Exception(
                "Table '" + id + "' does not exist.")

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
