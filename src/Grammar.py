from Variable import *

class Grammar:
    """
    This class is a representation of a grammar in CNF.

    Attributes:
        variables (list): The variables that describes the grammar.
    """

    def __init__(self, variables):
        """
        The constructor of Grammar class.

        Args:
            variables (list): The variables that describes the grammar.
        """
        self.variables = variables

        self.validateDuplicatedVariables()
        self.validatePossibleVariableRules()
        self.validateLambdaRules()

    def stringVerifier(self, string):
        """
        Check if a string can be produced by this grammar.

        Args:
            string (str): The string we want to check.

        Returns:
            bool: Indicates if the string can be produced by the grammar.
        """
        matrix = list()
        
        # First
        firstColumn = list()
        for c in string:
            cell = set()
            for variable in self.variables:
                for rule in variable.rules:
                    if c == rule:
                        cell.add(variable.name)
            firstColumn.append(cell)
        matrix.append(firstColumn)

        # Others
        for j in range(1, len(string)):
            # print("j:" + str(j))
            column = list()
            for i in range(len(string) - j):
                # print("i:" + str(i))
                
                combinations = set()
                for k in range(1, j + 1):
                    # print("k:"+str(k))
                    combinations |= Grammar.combine(matrix[k-1][i], matrix[j-k][i+k])
                # print("combinations:" + combinations.__str__())

                cell = set()
                for c in combinations:
                    cell |= self.foundVariablesWithrule(c)
                # print("cell:" + self.foundVariablesWithrule(c).__str__())
                column.append(cell)
                
            matrix.append(column)

        can = True
        if string:
            can = self.variables[0].name in matrix[len(matrix)-1][0]
        else:
            can = self.variables[0].produceEmptyStrings()
            
        
        return can
    
    def validateDuplicatedVariables(self):
        """
        Validates that there are not variables with the same name.

        Raises:
            DuplicatedVariablesError: If there are two or more variables having the same name.
        """
        nameList = list()
        for variable in self.variables:
            nameList.append(variable.name)

        duplicated = True
        if len(nameList) == len(set(nameList)):
            duplicated = False

        if duplicated:
            raise DuplicatedVariablesError("Corregir")

    def validatePossibleVariableRules(self):
        """
        Validate that all variables have another existing variable in his rules sets.

        Raises:
            NotExistingVariableError: If a variable have another non existing variable in his rules set.
        """
        allPoint = True
        for variable in self.variables:
            for rule in variable.rules:
                for c in rule:
                    if c.isupper():
                        allPoint = allPoint and self.foundVariable(c)

        if not allPoint:
            raise NotExistingVariableError("Corregir")

    def validateLambdaRules(self):
        """
        Validate that all variables (different from the initial variable) can not produce a empty string.

        Raises:
            LambdaInNotInitialVariableError: If a variable (different from the initial variable) produce a empty string.
        """
        for i in range(1, len(self.variables)):
            if self.variables[i].produceEmptyStrings():
                raise LambdaInNotInitialVariableError("Corregir")
            
                        
    def foundVariable(self, name):
        """
        Indicates if a variable is in the grammar by its name.

        Args:
            name (str): The name of the variable.

        Return:
            bool: Indicates if the variables was found.
        """
        found = False

        for var in self.variables:
            if var.name == name:
                found = True
        
        return found

    def foundVariablesWithrule(self, rule):
        """
        Find all variables that contain an specified rule.

        Args:
            rule (str): The specified rule.

        Returns:
            set: A set of names from the variables that contain the specified rule.
        """
        variables = set()
        for var in self.variables:
            for p in var.rules:
                if p == rule:
                    variables.add(var.name)
        return variables

    @staticmethod
    def combine(x1, x2):
        """
        Static.
        Make all the possible combinations between the elements (strings) of two sets.

        Args:
            x1 (set): The first set of strings.
            x2 (set): The second set of strings.

        Returns:
            set: A set that contain all the possible combinations between the first and second set.
        """
        combinations = set()
        for a in x1:
            for b in x2:
                combinations.add(a + b)
        return combinations
                
    def __str__(self):
        """
        Creates a string representation for a Grammar object.

        Returns:
            str: The string representation of the grammar.
        """
        string = "G: {"
        for variable in self.variables:
            string += "\n\t" + variable.__str__()
        return string + "\n}"

## Exceptions
class DuplicatedVariablesError(Exception):
    """Raised when two or more variables have the same name."""
    pass

class NotExistingVariableError(Exception):
    """Raised when a variable have another non existing variable in his rules set."""
    pass

class LambdaInNotInitialVariableError(Exception):
    """Raised when a variable (different from the initial variable) produce a empty string."""
    pass

##Tests
#var1 = Variable("S", {"AB", "BA",""})
#var2 = Variable("A", {"AB","a"})
#var3 = Variable("B", {"b"})
#grammar = Grammar([var1, var2, var3])
#print(grammar)
#print(grammar.stringVerifier("babbb"))
