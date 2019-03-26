
class SymbolTable:

    def __init__(self):
        self.symbTable={}
        self.symbolDT=""

    
    def lookup(self,id):
        if id in self.symbTable:
            return self.symbTable[id]
        return None
    
    def insertNewItem(self,id):
        if id not in self.symbTable:
            self.symbTable[id]={}
    
    def setAttribute(self,id,attr,val):
        if id in self.symbTable:
            self.symbTable[id][attr]=val
    
    def getAttribute(self,id,attr):
        if id in self.symbTable:
            return self.symbTable[id][attr]
        else:
            print('Warning',attr,'not found')

    
    def updateTable(self,tokens):
        for token in tokens:
            lexeme = token[0]
            desc = token[1]
            if desc == "IDENTIFIER":
                self.insertNewItem(lexeme)
                self.setAttribute(lexeme,"DESC",desc)


    def updateOutput(self,head,body):
      
        if head=="DATATYPE":
            self.symbolDT=body[0]

    def updateMatch(self,token):
        if token[1] == "IDENTIFIER":
            self.setAttribute(token[0],"TYPE",self.symbolDT)
            size=SymbolTable.mapSize(self.symbolDT)
            self.setAttribute(token[0],"SIZE",size)

    def mapSize(dt):
        if dt=="INTEGER":return 2
        elif dt=="FLOAT":return 4
        elif dt=="CHAR":return 1
        elif dt=="DOUBLE":return 8

    
            

        