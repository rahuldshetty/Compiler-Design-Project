from prettytable import PrettyTable

def parse(inp,startSymbol,nonTerminals,terminals,parsingTable,symbolTable):
    inp.append(("$","$"))
    stack = ["$", startSymbol ]
    i, j = 0, 1
    matched = []
    error=[]
    errorFlag=False
    table = PrettyTable(["Stack top", "Current input symbol", "Action"])

    while(inp[i][1] != "$" and stack[j]!="$"):
        # print(i, j)
        try:
            if(stack[j] == inp[i][1]):
                table.add_row([stack[j], inp[i][1], "Match " + str(inp[i][1])])
                symbolTable.updateMatch(inp[i])
                matched.append(inp[i])
                errorFlag=False
                stack.pop()
                i += 1
                j -= 1
                # print(stack, inp, i)
            elif(stack[j] in nonTerminals):
                production = parsingTable[nonTerminals.index(stack[j])][terminals.index(inp[i][1])]
                if len(production)==0:
                    table.add_row([stack[j], inp[i][1], "ERROR! skip " + inp[i]])
                    if errorFlag==False:
                        error.append("Error near line no. "+str(inp[i][2]))
                        errorFlag=True
                    i+=1
                elif "sync" == production[0]:
                    table.add_row([stack[j], inp[i][1], "ERROR! pop " + stack[j]])
                    if errorFlag==False:
                        error.append("Error near line no. "+str(inp[i][2]))
                        errorFlag=True
                    stack.pop()
                    j-=1 
                elif inp[i][1] != stack[j] and len(production)==0:
                    if len(stack)==2:
                        table.add_row([stack[j], inp[i][1], "ERROR! skip " + inp[i]])
                        if errorFlag==False:
                            error.append("Error near line no. "+str(inp[i][2]))
                            errorFlag=True
                        i+=1
                    else:
                        table.add_row([stack[j], inp[i][1], "ERROR! pop " + stack[j]])
                        if errorFlag==False:
                            error.append("Error near line no. "+str(inp[i][2]))
                            errorFlag=True
                        stack.pop()
                        j-=1
                else:  
                    f=(nonTerminals[nonTerminals.index(stack[j])]+ "->" + " ".join(production))
                    symbolTable.updateOutput(nonTerminals[nonTerminals.index(stack[j])],production)
                    table.add_row([stack[j], inp[i][1],"Output " + str(f)])
                    errorFlag=False
                    stack.pop()
                    j -= 1
                    if("#" not in production):
                        for ele in production[::-1]:
                            stack.append(ele)
                            j += 1
                        # print(stack)
            else:
                # manage error
                table.add_row([stack[j], inp[i][1], "ERROR! skip " + inp[i]])
                if errorFlag==False:
                    error.append("Error near line no. "+str(inp[i][2]))
                    errorFlag=True
                i+=1
                
        except:
            break
    # print(matched, inp[:-1], stack)
    print(table)
    if(matched != inp[:-1] or stack != ["$"] or len(error)!=0):
        print("Result:")
        print("Invalid input!")
        print("Errors:")
        for line in error:
            print(line)

    else:
        print("Result:")
        print("Valid input!")
    return [symbolTable]