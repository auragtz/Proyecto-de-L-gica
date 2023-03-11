import pandas as pd

def binOr(a,b):
# both a and b are bool variables
    # 1 1 - 1
    # 1 0 - 1
    # 0 1 - 1
    # 0 0 - 0
    if (a or b ):
        return True
    else :
        return False

def trueFalseFill(len,total):
    tFS = ["T"]*len + ["F"]*len
    tFS = tFS * int(total/(2*len))
    return tFS


def exp_table( table1,table2,operation ):
    #decorators go brrrrrrrr
    
    return operation(table1,table2)


def printTable(variableList,expressionList):
    #the variableArray is a list of all variables
    # 

    # the expressionList is a list. There is no need for it to be a numpy array yet
    # It is a list of all expressions. 
    

    # The array to be printed ought to have at least a column per variable
    # 2^n rows, and a column per expression
    varLen = len(variableList)
    rowNo = (2**len(variableList))
    indexG = [x+1 for x in range(rowNo)]

    trueFalseDictionary = {}
    for x in list(range(varLen)):
        trueFalseDictionary[variableList[x]] = trueFalseFill( 2**x ,rowNo)

    
    table = pd.DataFrame(trueFalseDictionary,columns=variableList, index=indexG)


    
    

    print(table)
    pass


nPremises = int(input("How many premises (2-3)? "))
while nPremises != 2 and nPremises != 3:
    print("Incorrect value")
    nPremises = int(input("How many premises (2-3)? "))

if nPremises == 2:
    printTable(["a","b"],[])
else:
    printTable(["a", "b", "c"], [])
