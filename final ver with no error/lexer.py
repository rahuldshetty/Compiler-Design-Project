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
		tokens=[]
		lc_no = 1
		lines=[]
		for line in code.split('\n'):
			p=re.findall(tokenSet,line)
			for ele in p:
				for item in ele:
					if item!='':
						tokens.append(item)
						lines.append(lc_no)
			lc_no+=1
		Token=[]
		for i,token in enumerate(tokens):
			if token not in TOKEN_DESC:
				if re.match(r'\".*\"',token):
					Token.append((token,'STRING',lines[i]))
				elif re.match(r'\'.?\'',token):
					Token.append((token,'CHARACTER',lines[i]))
				elif re.match("'",token):
					Token.append((token,'SINGLE_QUOTE',lines[i]))
				elif re.match('"',token):
					Token.append((token,'DOUBLE_QUOTE',lines[i]))
				elif re.match(r'[a-zA-Z][a-zA-Z0-9]*',token):
					Token.append((token,'IDENTIFIER',lines[i]))
				elif re.match(r'[0-9]+',token):
					Token.append((token,'DIGITS',lines[i]))

			else:
				Token.append((token,TOKEN_DESC[token],lines[i]))
		return Token


