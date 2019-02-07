nonTerminals = ["S", "STMT", "STMT1", "STMT2", "CONDITION", "FUNCTION", "MSG", "E", "E1", "T", "T1", "F", "F1", "H"]
terminals = ["int", "main", "(", ")", "begin", "end", "datatype", ";", "id", "=", ",", "if", "printf", "string", "relop", "+", "-", "*", "/", "digits", "$"]
parsingTable = [
    #S
    [["int", "main", "(", ")", "begin", "STMT", "end"], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
    #STMT
    [[], [], [], [], [], [], ["datatype", "STMT", ";"], [], ["id", "=", "E", ";"], [], [], ["CONDITION"], ["FUNCTION"], [], [], [], [], [], [], [], []],
    #STMT1
    [[], [], [], [], [], [], [], [], ["id", "STMT2"], [], [], [], [], [], [], [], [], [], [], [], []],
    #STMT2
    [[], [], [], [], [], [], [], ["EPSILON"], [id], ["=", "E"], [",", "id"], [], [], [], [], [], [], [], [], [], []],
    #CONDITION
    [[], [], [], [], [], [], [], [], [], [], [], ["if", "(", "E", ")", "begin", "STMT", "end"], [], [], [], [], [], [], [], [], []],
    #FUNCTION
    [[], [], [], [], [], [], [], [], [], [], [], [], ["printf", "(", "MSG", ")", ";"], [], [], [], [], [], [], [], []],
    #MSG
    [[], [], [], [], [], [], [], [], ["id"], [], [], [], [], ["string"], [], [], [], [], [], [], []],
    #E
    [[], [], ["T", "E1"], [], [], [], [], [], ["T", "E1"], [], [], [], [], [], [], [], ["T", "E1"], [], [], ["T", "E1"], []],
    #E1
    [[], [], [], ["EPSILON"], [], [], [], ["EPSILON"], [], [], [], [], [], [], ["relop", "T", "E1"], [], [], [], [], [], []],
    #T
    [[], [], ["F", "T1"], [], [], [], [], [], ["F", "T1"], [], [], [], [], [], [], [], ["F", "T1"], [], [], ["F", "T1"], []],
    #T1
    [[], [], [], ["EPSILON"], [], [], [], ["EPSILON"], [], [], [], [], [], [], ["EPSILON"], ["+", "F", "T1"], ["-", "F", "T1"], [], [], [], []],
    #F
    [[], [], ["H", "F1"], [], [], [], [], [], ["H", "F1"], [], [], [], [], [], [], [], ["H", "F1"], [], [], ["H", "F1"], []],
    #F1
    [[], [], [], ["EPSILON"], [], [], [], ["EPSILON"], [], [], [], [], [], [], ["EPSILON"], ["EPSILON"], ["EPSILON"], ["*", "H", "F1"], ["*", "H", "F1"], [], []],
    #H
    [[], [], ["(", "E", ")"], [], [], [], [], [], ["id"], [], [], [], [], [], [], [], ["-", "H"], [], [], ["digits"], []]
]

def parse(inp):
    inp.append("$")
    stack = ["$", "S"]
    i, j = 0, 1
    matched = []
    while(inp[i] != "$"):
        # print(i, j)
        try:
            if(stack[j] == inp[i]):
                print("Match", inp[i])
                matched.append(inp[i])
                stack.pop()
                i += 1
                j -= 1
                # print(stack, inp, i)
            elif(stack[j] in nonTerminals):
                production = parsingTable[nonTerminals.index(stack[j])][terminals.index(inp[i])]
                print(nonTerminals[nonTerminals.index(stack[j])], "->", " ".join(production))
                stack.pop()
                j -= 1
                if(production[0] != "EPSILON"):
                    for ele in production[::-1]:
                        stack.append(ele)
                        j += 1
                    # print(stack)
            # print(stack)
        except:
            break
    # print(matched, inp[:-1], stack)
    if(matched != inp[:-1] or stack != ["$"]):
        print("Invalid input!")
    else:
        print("Valid input!")