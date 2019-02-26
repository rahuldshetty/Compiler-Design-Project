from parsegen import *
from myParser import *
from lexer import *

f=open("Construct.txt","r")
p=f.read()
tokens=Tokenizer.tokenize(p)

print("Output of Lexer\nToken\t\tLexeme\n------------------------------")
for i in tokens:print("\t\t".join(str(x) for x in i[0:2]))



p=open("Rules.txt",'r').read()

print("\n\nOutput of Parser")

parser = Parser(p)
parser.processProductions()

parse(tokens,"S",parser.variables,parser.terminals,parser.table)
