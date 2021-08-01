def operations(val):
    excl = {'(':0, '-': 1, '+': 1, '*': 2, '/': 2, '^':3}
    if val not in excl:
        return -1;
    return excl[val]
        

def to_postfix(infix):
    operators = []
    output = []
    for item in infix:

        print("_"*10)
        print('output:')
        print(output)
        print('operators:')
        print(operators)

        if item == ')':
            while operations(operators[-1]) != 0:
                elem = operators.pop()
                if elem != '(':
                    output.append(elem)
            continue
        if operations(item) != -1:
            while len(operators) > 0 and operations(item) <= operations(operators[-1]):
                elem = operators.pop()
                if elem != '(':
                    output.append(elem)
            operators.append(item)
        else:
            output.append(item)
    while len(operators) > 0:
        elem = operators.pop()
        if elem != '(':
            output.append(elem)
    return "".join(output)



#print(to_postfix("2+7*5-7"))
print(to_postfix("(5-4)-1+(9/5/2)-7/(1/7)"))

