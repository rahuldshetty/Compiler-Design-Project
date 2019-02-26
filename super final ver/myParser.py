def parse(inp,startSymbol,nonTerminals,terminals,parsingTable):
    inp.append(("$","$"))
    stack = ["$", startSymbol ]
    i, j = 0, 1
    matched = []
    error=[]
    errorFlag=False
    rounds=1
    while(inp[i][1] != "$" and stack[j]!="$"):
        print("-"*100)
        print("Round:",rounds)
        rounds+=1
        # print(i, j)
        try:
            if(stack[j] == inp[i][1]):
                print("Stack:  "+",".join(str(x) for x in stack),"Input: " + ",".join(str(x[0]) for x in inp[i:]),"Action: Match "+str(inp[i][1]),sep="\n" )
                matched.append(inp[i])
                errorFlag=False
                stack.pop()
                i += 1
                j -= 1
                # print(stack, inp, i)
            elif(stack[j] in nonTerminals):
                production = parsingTable[nonTerminals.index(stack[j])][terminals.index(inp[i][1])]
                if len(production)==0:
                    print("Error skip:",inp[i])
                    if errorFlag==False:
                        error.append("Error near line no. "+str(inp[i][2]))
                        errorFlag=True
                    i+=1
                elif "sync" == production[0]:
                    print("Error pop:",stack[j])
                    if errorFlag==False:
                        error.append("Error near line no. "+str(inp[i][2]))
                        errorFlag=True
                    stack.pop()
                    j-=1 
                elif inp[i][1] != stack[j] and len(production)==0:
                    if len(stack)==2:
                        print("Error skip:",inp[i])
                        if errorFlag==False:
                            error.append("Error near line no. "+str(inp[i][2]))
                            errorFlag=True
                        i+=1
                    else:
                        print("Error pop:",stack[j])
                        if errorFlag==False:
                            error.append("Error near line no. "+str(inp[i][2]))
                            errorFlag=True
                        stack.pop()
                        j-=1
                else:  
                    f=(nonTerminals[nonTerminals.index(stack[j])]+ "->" + " ".join(production))
                    print("Stack:  "+",".join(str(x) for x in stack),"Input: " + ",".join(str(x[0]) for x in inp[i:]),"Action: Output "+str(f),sep="\n" )               
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
                print("Error skip:",inp[i])
                if errorFlag==False:
                    error.append("Error near line no. "+str(inp[i][2]))
                    errorFlag=True
                i+=1
                
        except:
            break
    # print(matched, inp[:-1], stack)
    if(matched != inp[:-1] or stack != ["$"] or len(error)!=0):
        print("-"*100)
        print("Result:")
        print("Invalid input!")
        print("Errors:")
        for line in error:
            print(line)

    else:
        print("-"*100)
        print("Result:")
        print("Valid input!")