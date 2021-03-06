import re

TOKENS = ["=","==","%","/","\*","-","\+","!=","!","\|\|","&&","<=","<",">=",">","if","main","begin","end","printf","float","char","int",r'\(',r'\)',",",";",r'\".*\"',r'\'.?\'',r'[a-zA-Z][a-zA-Z0-9]*',r'[0-9]+',"'",'"']

DATATYPES = ["INTEGER","FLOAT","CHAR"]

TOKEN_DESC={ "=":"ASSIGN" ,
			 "==":"EQ",
			 "%":"MOD",
			 "/":"DIV",
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
			 "float":"FLOAT",
			 "char":"CHAR",
			 "(":"LEFT_PARA",
			 ")":"RIGHT_PARA",
			 ",":"SEPERATOR",
			 ";":"EOS"
		 }

class Tokenizer:
	def tokenize(code):
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
				if re.match(r'\".*\"',token):
					Token.append((token,'STRING'))
				elif re.match(r'\'.?\'',token):
					Token.append((token,'CHARACTER'))
				elif re.match("'",token):
					Token.append((token,'SINGLE_QUOTE'))
				elif re.match('"',token):
					Token.append((token,'DOUBLE_QUOTE'))
				elif re.match(r'[a-zA-Z][a-zA-Z0-9]*',token):
					Token.append((token,'IDENTIFIER'))
				elif re.match(r'[0-9]+',token):
					Token.append((token,'DIGITS'))

			else:
				Token.append((token,TOKEN_DESC[token]))
		return Token


