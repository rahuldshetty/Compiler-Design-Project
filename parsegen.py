#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Rules
1. Always terminate the production with ;
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


def follow(symb, parser, isStart=False):
    if visited[symb] == 191:
        return []
    visited[symb] += 1

    ans = []
    if isStart == True:
        ans.append('$')
    for prod in parser.prods:
        body = parser.prods[prod]
        if symb in body:
            f = 1
            for item in body:
                if f == 0:
                    if item == '#':
                        continue
                    if item in parser.terminals:
                        f = 1
                        ans += [item]
                        continue
                    elif item == '|':
                        if prod is parser.variables[0]:
                            ans += follow(prod, parser, True)
                        else:
                            ans += follow(prod, parser)

                        continue
                    firstSet = parser.firstSet[item]
                    ans += [x for x in firstSet if x != '#']
                    if '#' in firstSet:
                        continue
                    f = 1
                if item is symb:
                    f = 0
                    continue
            if f == 0:
                if prod is parser.variables[0]:
                    ans += follow(prod, parser, True)
                else:
                    ans += follow(prod, parser)
    visited[symb] = 0	
    return list(set(ans))


class Parser:

    def __init__(self, code):
        self.code = code

    def createEmptyTable(self):
        self.variables = []
        self.terminals = []

        # Get the variables

        for var in self.prods.keys():
            self.variables.append(var)
            visited[var] = -1

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

        prods = [x.strip() for x in self.code.split(';;')]
        prods = [x for x in prods if len(x) != 0]
        prods = [self.parseProduction(x) for x in prods]
        prodsD = {}
        for item in prods:
            head = item[0]
            body = item[1]
            prodsD[head] = body
        self.prods = prodsD

        self.createEmptyTable()

        firstSet = {}
        f = 0
        for prod in prodsD:
            if f == 0:
                firstSet[prod] = first(prod, self)
            else:
                firstSet[prod] = first(prod, self)
        self.firstSet = firstSet
        print ('First set:', firstSet)

        followSet = {}
        f = 0
        for prod in prodsD:
            if f == 0 and prod == prods[0][0]:
                followSet[prod] = follow(prod, self, True)
                f = 1
            else:
                followSet[prod] = follow(prod, self)

        print ('Follow Set:', followSet)

    def parseProduction(self, code):

        # Production of the form A -> B | A ;

        (head, body) = code.split('->')
        head = head.strip()
        body = [x.strip() for x in body.split()]
        return (head, body)


# p="E -> T E1 ;; E1 ->  + T E1 ; | # ;; T -> id ;; "

p = \
    """
	S -> int main ( ) begin STMTS end ;;
	STMTS -> STMT STMTS | # ;;
	STMT -> datatype STMT1 ; | CONDITION | FUNCTION ; | id = E ;;
	STMT1 -> id STMT2 ;;
	STMT2 -> , id STMT2 | = E STMT2 | # ;;
	CONDITION -> if ( E ) begin STMTS end ;;
	FUNCTION -> printf ( MSG ) ;;
	MSG -> string | id ;;
	E -> T E1 ;;
	E1 -> relop T E1 | # ;;
	T -> F T1 ;;
	T1 -> + F T1 | - F T1 | # ;;
	F -> H F1 ;;
	F1 -> * H F1 | / H F1 | # ;;
	H -> ( E ) | - H | id | digits ;;
"""

par = Parser(p)
par.processProductions()

			