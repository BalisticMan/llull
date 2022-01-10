import sys
from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from antlr4.InputStream import InputStream
from llullVisitor import llullVisitor

sys.tracebacklimit = -1

args_len = len(sys.argv)

activeMethod = 'main'
intialArguments = []

if args_len == 0:
    print("No arguments provided")

input_stream = FileStream(sys.argv[1], encoding='utf-8')

if args_len >= 3:
    activeMethod = sys.argv[2]
    intialArguments = sys.argv[3:]

lexer = llullLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = llullParser(token_stream)
tree = parser.root()
# print(tree.toStringTree(recog=parser))

visitor = llullVisitor(activeMethod, intialArguments)
visitor.visit(tree)
