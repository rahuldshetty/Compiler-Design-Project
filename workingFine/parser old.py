import re
from lexer import *


class Parser:

    def __init__(self,code="",tokens=[]):
        if len(tokens)!=0:
            self.tokens=tokens
        else:
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
        token=self.getNextToken()
        if token[1] is not "DISPLAY":
            self.currentTokenID=curPos
            return []
        token1=self.getNextToken()
        if token1[1] == "LEFT_PARA" :
            token2=self.getNextToken()
            if token2[1] == "STRING" or token2[1] == "CHARACTER" or token2[1]=="IDENTIFIER":
                    grammar.append(token2)
            elif token2[1]=="RIGHT_PARA":
                grammar.append(("","STRING"))
                self.currentTokenID=self.currentTokenID-1
            else:
                raise Exception("Error parsing function...")
            token3=self.getNextToken()
            if token3[1]=="RIGHT_PARA":
                token4=self.getNextToken()
                if token4[1]=="EOS":
                    return grammar
                else:
                    raise Exception("Error parsing function...")
            else:
                raise Exception("Error parsing function...")
        else:
            raise Exception("Error parsing function...")

    def findEachStmts(self):
        stmts=[]
        temp=[]
        stack=[]
        while self.currentTokenID < len(self.tokens)-1:
            token=self.getNextToken()
            if token[1]=="BLOCK_START":
                stack.append("START")
                temp.append(token)
            elif token[1]=="BLOCK_END":
                stack.pop()
                temp.append(token)
                stmts.append(temp)
                temp=[]

            elif token[1]=="EOS" and len(stack)==0:
                temp.append(token)
                stmts.append(temp)
                temp=[]
            else:
                temp.append(token)
        if len(temp)==0:
            return stmts
        else:
            raise Exception("Invalid Statement Ending...")


    def findMain(self):
        intToken=self.getNextToken()
        if intToken[1] == "INTEGER":
            mainToken=self.getNextToken()
            if mainToken[0]=="main":
                lpara=self.getNextToken()
                rpara=self.getNextToken()
                begin=self.getNextToken()
                last=self.tokens[len(self.tokens)-1]
                if lpara[1]=="LEFT_PARA" and rpara[1]=="RIGHT_PARA" and begin[1]=="BLOCK_START" and last[1]=="BLOCK_END":
                    # MAIN FUNCTION EXISTS OR NOT
                    ParseTree=[]
                    lines=self.findEachStmts()
                    for line in lines:
                        tempParser=Parser(tokens=line)
                        t1=tempParser.checkDeclarative()
                        if t1!=[]:
                            ParseTree.append(t1)
                            continue
                        t1=tempParser.checkPrintStmt()
                        if t1!=[]:
                            ParseTree.append(t1)
                            continue
                        else:
                            raise Exception("Invalid Statment..")
                    for line in ParseTree:print(line)
                    

                else:
                    raise Exception("Main block not found...")
            else:
                raise Exception("Main block not found...")
        else:
            raise Exception("Main block not found...")


    def checkDeclarative(self):
        declarations=['DECLARATION']
        curPos=self.currentTokenID
        token=self.getNextToken()
        if token[1] not in DATATYPES:
            self.currentTokenID=curPos
            return []
        declarations.append(token[1])
        token1=self.getNextToken()
        if token1[1]=='IDENTIFIER':
            declarations.append(token1)
            while (self.currentTokenID)<len(self.tokens):
                token2=self.getNextToken()
                if token2[1]=='SEPERATOR':
                    token3=self.getNextToken()
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
                    
            
        
    def tryfindMain(self):
        try:
            self.findMain()
        except:
            raise Exception("Error in parsing...")

dec_code='float a,b;'
printf_code1 = "printf(n1);"
printf_code = "printf(\"Hello\");"
printf_code2 = "printf(h);"

main="int main() begin int a,b; float c,d; printf(\"hello\");  end"
    
lines="int a,b,c;printf(a);printf('f')"

p=Parser(code=main)
p.tryfindMain()
