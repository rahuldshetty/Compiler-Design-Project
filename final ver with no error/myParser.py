def parse(inp,startSymbol,nonTerminals,terminals,parsingTable):
    inp.append(("$","$"))
    stack = ["$", startSymbol ]
    i, j = 0, 1
    matched = []
    while(inp[i][1] != "$"):
        # print(i, j)
        try:
            if(stack[j] == inp[i][1]):
                print("Match", inp[i])
                matched.append(inp[i])
                stack.pop()
                i += 1
                j -= 1
                # print(stack, inp, i)
            elif(stack[j] in nonTerminals):
                production = parsingTable[nonTerminals.index(stack[j])][terminals.index(inp[i][1])]
                print(nonTerminals[nonTerminals.index(stack[j])], "->", " ".join(production))
                stack.pop()
                j -= 1
                if("#" not in production):
                    for ele in production[::-1]:
                        stack.append(ele)
                        j += 1
                    # print(stack)
            else:
                # manage error
                break
        except:
            break
    # print(matched, inp[:-1], stack)
    if(matched != inp[:-1] or stack != ["$"]):
        print("Invalid input!")
    else:
        print("Valid input!")