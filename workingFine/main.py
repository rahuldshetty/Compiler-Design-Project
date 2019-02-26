from parsegen import *
from myParser import *
from lexer import *

f=open("Construct.txt","r")
p=f.read()
tokens=Tokenizer.tokenize(p)



p=open("Rules.txt",'r').read()


parser = Parser(p)
parser.processProductions()

parse(tokens,"S",parser.variables,parser.terminals,parser.table)
