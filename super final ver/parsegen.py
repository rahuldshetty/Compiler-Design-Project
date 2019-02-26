#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Rules
1. Always terminate the production with newline.
2. Place space between each symbols(terminals or non terminals).
3. Write LL Grammar rules.
4. Define rules for all variables used.
5. # is used to denote empty string or Epsilon
'''

visited = {}


def first(symb, parser):
    if symb is '|':
        return ['#']
    if symb in parser.terminals:
        return [symb]
    elif symb is '#':
        return ['#']
    ans = []
    body = parser.prods[symb]
    found = 0
    waitKey = 0
    for item in body:
        if item == '|':
            if waitKey == 1:
                ans.append('#')
                waitKey = 0
            found = 0
            continue
        if found == 0:
            if item is '#':
                ans += ['#']
            elif item in parser.terminals:
                waitKey = 0
                ans += [item]
            else:
                subFirst = first(item, parser)
                ans += [x for x in subFirst if x != '#']
                if '#' in subFirst:
                    waitKey = 1
                    continue
            found = 1
    if waitKey == 1:
        ans.append('#')
    return list(set(ans))


def follow(symb,parser,startSymb=""):
    if visited[symb]==-1:
        return parser.followSet[symb]
    if visited[symb]==7:
        visited[symb]=0
        return [] if startSymb!="" else ['$']
    visited[symb]+=1
    ans=[]
    if startSymb!="":
        ans.append('$')
    for prod in parser.prods:
        body=parser.prods[prod]
        if symb in body:
            f=1
            beforeEp=0
            for item in body:
                #open('log.txt','a').write(" ".join([symb,prod,item]) + "\n" )
                if f==0:
                    if item == "#":
                        beforeEp=1
                        continue
                    elif item == "|" and beforeEp==1:
                        ans+=follow(prod,parser,startSymb if prod is startSymb else "")
                        beforeEp=0
                    elif item in parser.terminals:
                        f=1
                        beforeEp=0
                        ans+=[item]
                    elif item in parser.variables:
                        firstSet=parser.firstSet[item]
                        ans += [x for x in firstSet if x != "#"]
                        beforeEp=1
                        f=0
                        if "#" not in firstSet:
                            beforeEp=0
                            f=1


                elif item == symb:
                    f=0
            
            if f==0:
                ans+=follow(prod,parser,startSymb  if prod is startSymb else "")
    visited[symb]=-1
    parser.followSet[symb]=list(set(ans))
    return parser.followSet[symb]





class Parser:

    def __init__(self, code):
        self.code = code

    def createEmptyTable(self):
        self.variables = []
        self.terminals = ["$"]

        # Get the variables

        for var in self.prods.keys():
            self.variables.append(var)
            visited[var] = 0

        self.variables = list(set(self.variables))

        # get the teminals

        for (key, value) in self.prods.items():
            for item in value:
                if item not in self.variables and item != '|' and item \
                    != '#':
                    self.terminals.append(item)

        self.terminals = list(set(self.terminals))
        self.table = []

        # Each row is for one variable

        for e in self.variables:
            self.table.append([])

        # add columns for each row

        for r in range(len(self.variables)):
            for c in range(len(self.terminals)):
                self.table[r].append([])

    def processProductions(self):

        # find each productions by using ; as splitter

        prods = [x.strip() for x in self.code.split('\n')]
        prods = [x for x in prods if len(x) != 0]
        prods = [self.parseProduction(x) for x in prods]

        prodsD = {}
        for item in prods:
            head = item[0]
            body = item[1]
            prodsD[head] = body
        self.prods = prodsD

        self.createEmptyTable()
        ff=open('logparse.txt','w')
        ff.write('First Set:\n')
        firstSet = {}
       	f = 0
        for prod in prodsD:
            if f == 0:
                firstSet[prod] = first(prod, self)
            else:
                firstSet[prod] = first(prod, self)
            ff.write(prod+":  " + str(firstSet[prod])+"\n")
        
       
        self.firstSet = firstSet
        ff.write('\nFollow Set:\n')
        self.followSet = {}
        f = 0
        for prod in prodsD:
            if f == 0 and prod == prods[0][0]:
                self.followSet[prod] = follow(prod, self, prods[0][0])
                f = 1
            else:
                self.followSet[prod] = follow(prod, self,"")
            ff.write(prod+":  " + str(self.followSet[prod])+"\n")

        for prod in self.prods:
        	self.postProcessTable(prod,self.prods[prod])

        for prodIndex,prodH in enumerate(self.followSet):
                prodIndex=self.variables.index(prodH)
                followset = self.followSet[prodH]
                for i in followset:
                    if len(self.table[prodIndex][self.terminals.index(i)])==0:
                        self.table[prodIndex][self.terminals.index(i)]=['sync']       

        ff.write('\nTerminals:'+str(self.terminals)+"\n")
        ff.write('\nNon-Terminals:'+str(self.variables)+"\n")
        ff.write("\nParsing Table:\n")

       	for row in range(len(self.table)):
            ff.write( self.variables[row] +" :   " + str(self.table[row])+"\n\n")


    def postProcessTable(self,head,production):
        subprods=[]
        t=[]
        for i in production:
        	if i!="|":
        		t.append(i)
        	else:
        		subprods.append(t)
        		t=[]
        if len(t)!=0:
            subprods.append(t)
        for body in subprods:
            tempFirst=[]
            found=0
            for item in body:
                if item in self.terminals:
                   tempFirst.append(item)
                   found=0
                   break
                else:
                    if item is "#":
                	    found=1
                	    continue
                    first=self.firstSet[item]
                    tempFirst+=[x for x in first if x!="#"]
                    if "#" in first:
                        found=1
                        continue
                    else:
                   	    found=0
                   	    break
            if found==1:
                tempFirst+=self.followSet[head]
            varIndex=self.variables.index(head)
            for term in tempFirst:
            	termIndex=self.terminals.index(term)
            	self.table[varIndex][termIndex]+=body
            

            

            




    def parseProduction(self, code):

        # Production of the form A -> B | A ;

        (head, body) = code.split('->')
        head = head.strip()
        body = [x.strip() for x in body.split()]
        return (head, body)

