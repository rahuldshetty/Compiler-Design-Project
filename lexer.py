import re

TOKENS = ["=","==","%","\*","-","\+","!=","!","\|\|","&&","<=","<",">=",">","if","main","begin","end","printf","int",r'\(',r'\)',",",";",r'[a-zA-Z][a-zA-Z0-9]*',r'[0-9]+']

TOKEN_DESC={ "=":"ASSIGN" ,
			 "==":"EQ",
			 "%":"MOD",
			 "*":"MUL",
			 "-":"SUB",
			 "+":"ADD",
			 "!=":"NE",
			 "!":"NOT",
			 "||":"OR",
			 "&&":"AND",
			 "<=":"LE",
			 "<":"LT",
			 ">=":"GE",
			 ">":"GT",
			 "if":"IF",
			 "main":"PGM_START",
			 "begin":"BLOCK_START",
			 "end":"BLOCK_END",
			 "printf":"DISPLAY",
			 "int":"INTEGER",
			 "(":"LEFT_PARA",
			 ")":"RIGHT_PARA",
			 ",":"SEPERATOR",
			 ";":"EOS"
		 }

class Tokenizer:
	def removeComments(code):
		return re.sub(r'[\n\t \r]',' ',code)
	def tokenize(code):
		code=Tokenizer.removeComments(code)
		tokenSet="("+")|(".join(TOKENS)+")"
		p=re.findall(tokenSet,code)
		tokens=[]
		for ele in p:
			for item in ele:
				if item!='':
					tokens.append(item)
		Token=[]
		for token in tokens:
			if token not in TOKEN_DESC:
				if re.match(r'[a-zA-Z][a-zA-Z0-9]*',token):
					Token.append((token,'IDENTIFIER'))
				elif re.match(r'[0-9]+',token):
					Token.append((token,'DIGITS'))
			else:
				Token.append((token,TOKEN_DESC[token]))
		return Token

f=open("Construct.txt","r")
p=f.read()
tokens=Tokenizer.tokenize(p)
for token in tokens:
	print(token)