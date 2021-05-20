from Variable import *

class Grammar:

    def __init__(self, variables):
        self.variables = variables
        if self.validateVariablesDuplicated() == True:
            raise Exception()
        if self.validateVariablePointExistingVariable() == False:
            raise Exception()

    def stringVerifier(self, string):
        matrix = list()

        ## First
        firstColumn = list()
        for c in string:
            cell = set()
            for variable in self.variables:
                for rule in variable.rules:
                    if c == rule:
                        cell.add(variable.name)
            firstColumn.append(cell)
        matrix.append(firstColumn)

        ## Others
        for j in range(1, len(string)):
            print("j:" + str(j))
            column = list()
            for i in range(len(string) - j):
                print("i:" + str(i))
                
                combinations = set()
                for k in range(1, j + 1):
                    print("k:"+str(k))
                    combinations |= Grammar.combine(matrix[k-1][i], matrix[j-k][i+k])
                print("combinations:" + combinations.__str__())

                cell = set()
                for c in combinations:
                    cell |= self.foundVariablesWithrule(c)
                print("cell:" + self.foundVariablesWithrule(c).__str__())
                column.append(cell)
                
            matrix.append(column)
        
        return self.variables[0].name in matrix[len(matrix)-1][0]
    
    def validateVariablesDuplicated(self):
        nameList = list()
        for variable in self.variables:
            nameList.append(variable.name)

        duplicated = True
        if len(nameList) == len(set(nameList)):
            duplicated = False
        return duplicated

    def validateVariablePointExistingVariable(self):
        allPoint = True
        for variable in self.variables:
            for rule in variable.rules:
                for c in rule:
                    if c.isupper():
                        allPoint = allPoint and self.foundVariable(c)
        return allPoint
                        
    def foundVariable(self, name):
        found = False

        for var in self.variables:
            if var.name == name:
                found = True
        
        return found

    def foundVariablesWithrule(self, rule):
        variables = set()
        for var in self.variables:
            for p in var.rules:
                if p == rule:
                    variables.add(var.name)
        return variables

    @staticmethod
    def combine(x1, x2):
        combinations = set()
        for a in x1:
            for b in x2:
                combinations.add(a + b)
        return combinations
                
    def __str__(self):
        string = "G: {"
        for variable in self.variables:
            string += "\n\t" + variable.__str__()
        return string + "\n}"

##Tester
var1 = Variable("S", ["AB", "BS", "b"])
var2 = Variable("A", ["AA","a"])
var3 = Variable("B", ["c","a"])
grammar = Grammar([var1, var2, var3])
print(grammar)
print(grammar.stringVerifier("cacab"))