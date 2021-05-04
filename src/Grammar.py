from Variable import *

class Grammar:

    def __init__(self, variables):
        self.variables = variables
        if self.validateVariablesDuplicated() == True:
            raise Exception()
        if self.validateVariablePointExistingVariable() == False:
            raise Exception()

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
            for path in variable.paths:
                for c in path:
                    if c.isupper():
                        allPoint = allPoint and self.foundVariable(c)
        return allPoint
                        
    def foundVariable(self, name):
        found = False

        for var in self.variables:
            if var.name == name:
                found = True
        
        return found

    def __str__(self):
        string = "G: {"
        for variable in self.variables:
            string += "\n\t" + variable.__str__()
        return string + "\n}"

var1 = Variable("S", ["AB", "Ba", "b"])
var2 = Variable("A", ["a"])
var3 = Variable("B", ["c"])
grammar = Grammar([var1, var2, var3])
print(grammar)

