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



    def checkDeclarative(self):
        declarations=[]
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
                    
            
        
        

TOKENS=[('int','INTEGER'),('','IDENTIFIER'),('',','),('','IDENTIFIER'),('','EOS')]
code='float a,b;'
        
p=Parser(code)
print(p.checkDeclarative())


        
        

    
    
