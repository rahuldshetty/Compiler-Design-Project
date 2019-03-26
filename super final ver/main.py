from parsegen import *
from myParser import *
from lexer import *
from symb import *

f=open("Construct.txt","r")
p=f.read()
tokens=Tokenizer.tokenize(p)

print("Output of Lexer\nToken\t\tLexeme\n------------------------------")
for i in tokens:print("\t\t".join(str(x) for x in i[0:2]))

symbolTable = SymbolTable()
symbolTable.updateTable(tokens)


p=open("Rules.txt",'r').read()

print("\n\nOutput of Parser")

parser = Parser(p)
parser.processProductions()

symbolTable=parse(tokens,"S",parser.variables,parser.terminals,parser.table,symbolTable)[0]
print("\nSymbol Table")
for item in symbolTable.symbTable:
    print(item,symbolTable.symbTable[item],sep=":")