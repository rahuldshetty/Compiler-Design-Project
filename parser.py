import re
from lexer import *


class Parser:
    
    def __init__(self,code):
        self.tokens=Tokenizer.tokenize(code)
        self.currentTokenID=0

        

    def getNextToken(self):
        if self.currentTokenID+1 <= len(self.tokens):
            token=self.tokens[self.currentTokenID]
            self.currentTokenID+=1
            return token
        else:
            raise Exception("Error Parsing...")


    def checkPrintStmt(self):
        print(self.tokens)
        grammar=['DISPLAY']
        curPos=self.currentTokenID
        token=Parser.getNextToken(self)
        if token[1] is not "DISPLAY":
            return []
        token1=Parser.getNextToken(self)
        if token1[1] == "LEFT_PARA" :
            token2=Parser.getNextToken(self)
            if token2[1] == "STRING" or token2[1] == "CHARACTER" or token2[1]=="IDENTIFIER":
                    grammar.append(token2)
            else:
                raise Exception("Error parsing function...")
            token3=Parser.getNextToken(self)
            if token3[1]=="RIGHT_PARA":
                token4=Parser.getNextToken(self)
                if token4[1]=="EOS":
                    return grammar
                else:
                    raise Exception("Error parsing function...")
            else:
                raise Exception("Error parsing function...")
        else:
            raise Exception("Error parsing function...")




    def checkDeclarative(self):
        declarations=['DECLARATION']
        curPos=self.currentTokenID
        token=Parser.getNextToken(self)
        if token[1] not in DATATYPES:
            return []
        declarations.append(token[1])
        token1=Parser.getNextToken(self)
        if token1[1]=='IDENTIFIER':
            declarations.append(token1)
            while (self.currentTokenID)<len(self.tokens):
                token2=Parser.getNextToken(self)
                if token2[1]=='SEPERATOR':
                    token3=Parser.getNextToken(self)
                    if token3[1]=='IDENTIFIER':
                        declarations.append(token3)
                        continue
                    else:
                        raise Exception("Error parsing near declaration..")
                elif token2[1]=='EOS':
                    return declarations
                else:
                    raise Exception("Error parsing near declaration..")
        raise Exception("Error parsing near declaration..")      
                    
            
        
       


dec_code='float a,b;'
printf_code1 = "printf(n1);"
printf_code = "printf(\"Hello\");"
printf_code2 = "printf(h);"

    
p=Parser(printf_code2)
print(p.checkPrintStmt())


        
        

    
    
