import myLexer
import myParser

f = open("Construct.txt","r")
p = f.read()
tokens = myLexer.tokenize(p)
print("---Output of Lexer--- \n", tokens, "\n\n---Output of parser---")
myParser.parse(tokens)