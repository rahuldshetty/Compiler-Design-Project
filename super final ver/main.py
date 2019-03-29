from parsegen import *
from myParser import *
from lexer import *
from symb import *
from prettytable import PrettyTable

f=open("Construct.txt","r")
p=f.read()
tokens=Tokenizer.tokenize(p)

table = PrettyTable(["Token", "Lexeme"])

print("Output of Lexer")
for t in tokens:
    table.add_row([t[0], t[1]])
print(table)

symbolTable = SymbolTable()
symbolTable.updateTable(tokens)


p=open("Rules.txt",'r').read()

print("\n\nOutput of Parser")

parser = Parser(p)
parser.processProductions()

symbolTable=parse(tokens,"S",parser.variables,parser.terminals,parser.table,symbolTable)[0]
print("\nSymbol Table")
symTbl = PrettyTable(["Token", "Description", "Size (in bytes)"])
for item in symbolTable.symbTable:
    symTbl.add_row([item, symbolTable.symbTable[item]["DESC"], symbolTable.symbTable[item]["SIZE"]])
print(symTbl)