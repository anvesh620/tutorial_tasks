dict_a = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}
dict_b = {'A':'Hello', 'C': 'Buddy', 'D': 'Welcome'}
expression = input()


if (expression == "A and B"):            # concate A and B
    c = ('A' in dict_a) and ('B' in dict_a)
    if (c):
        print(dict_a["A"],dict_a["B"])
elif (expression == "A and C"):           # concate A and C
    c = ('A' in dict_a) and ('C' in dict_a)
    if (c):
        print(dict_a["A"],dict_a["C"])
        

elif (expression == "D or B"):     # print first variable else second variable
    if ('D' in dict_a):
        print(dict_a["D"])
    else:
        print(dict_a["B"])

elif (expression == "A or B"):  # print first variable else second variable
    if ('A' in dict_a) and ('B' in dict_a):
        print(dict_a["A"])
    elif ('A' in dict_a) and ('B' not in dict_a):
        print(dict_a["A"])
    else:
        print(dict_a["B"])
        
        
elif (expression == "A and B and C"): #concate a and b and c 
    if ('A' in dict_a) and ('B' in dict_a) and ('C' in dict_a):
        print(dict_a['A'],dict_a['B'],dict_a['C'])

    
elif (expression == "A and (B or C)"):
    if ('A' in dict_a) and ('B' in dict_a) and ('C' in dict_a):
        print(dict_a['A'],dict_a['B'])
    else:
        if ('A' in dict_a) and (('B' in dict_a) and ('C' not in dict_a)):
            print(dict_a['A'],dict_a['B'])
        else:
            if ('A' in dict_a) and (('B' not in dict_a) and ('C' in dict_a)):
                print(dict_a['A'],dict_a['C'])

elif (expression == "A and (C or D)"):
    if ('A' in dict_a) and ('C' in dict_a) and ('D' in dict_a):
        print(dict_a['A'],dict_a['C'])
    else:
        if ('A' in dict_a) and (('C' in dict_a) and ('D' not in dict_a)):
            print(dict_a['A'],dict_a['C'])
        else:
            if ('A' in dict_a) and (('C' not in dict_a) and ('D' in dict_a)):
                print(dict_a['A'],dict_a['D'])
                
elif (expression == "A and (B or C) and D"):
    if ('A' in dict_b) and (('B' in dict_b) and ('C' in dict_b)) and ('D' in dict_b):
        print(dict_b['A'],dict_b['B'],dict_b['D'])
    else:
        if (('A' in dict_b) and (('B' not in dict_b) and ('C' in dict_b)) and ('D' in dict_b)):
            print(dict_b['A'],dict_b['C'],dict_b['D'])
        elif(('A' in dict_b) and (('B' in dict_b) and ('C' not in dict_b)) and ('D' in dict_b)):
            print(dict_b['A'],dict_b['B'],dict_b['D'])