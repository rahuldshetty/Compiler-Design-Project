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

    def findMain(self):
        intToken=Parser.getNextToken(self)
        if intToken[1] == "INTEGER":
            mainToken=Parser.getNextToken(self)
            if mainToken[0]=="main":
                lpara=Parser.getNextToken(self)
                rpara=Parser.getNextToken(self)
                begin=Parser.getNextToken(self)
                last=self.tokens[len(self.tokens)-1]
                if lpara[1]=="LEFT_PARA" and rpara[1]=="RIGHT_PARA" and begin[1]=="BLOCK_START" and last[1]=="BLOCK_END":
                    # MAIN FUNCTION EXISTS OR NOT
                    ParseTree=[]
                    

                else:
                    raise Exception("Main block not found...")
            else:
                raise Exception("Main block not found...")
        else:
            raise Exception("Main block not found...")


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

main="int main() begin int a,b,c; printf(a);  end"
    
p=Parser(main)
print(p.findMain())


        
        

    
    
