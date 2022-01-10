import sys
from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from antlr4.InputStream import InputStream
from prettierVisitor import prettierVisitor
if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
else:
    input_stream = InputStream(input('? '))
lexer = llullLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = llullParser(token_stream)
tree = parser.root()
# print(tree.toStringTree(recog=parser))

visitor = prettierVisitor()
visitor.visit(tree)
