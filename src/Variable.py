class Variable:
    """
    This class is a representation of a variable in a grammar.

    Attributes:
        name (str): The name of the variable.
        rules (set): The production rules of the variable.
    """

    def __init__(self, name, rules):
        """
        The constructor of the Variable class.

        Args:
            name (str): The name of the variable.
            rules (set): The production rules of the variable.
        """
        self.name = name
        self.rules = rules
        
        self.validateVariableName()
        self.validateSize()
        self.validateIsLetter()

    def validateVariableName(self):
        """
        Validates that the name of the variable is in uppercase.

        Raises:
            InvalidNameError: If the name is not in uppercase.
        """
        if not self.name.isupper():
            raise InvalidNameError("The name of the variable " + "\"" + self.name + "\" must be in uppercase")

    def validateSize(self):
        """
        Validates that no production rule has more than two symbols. This to guarantee 
        that the grammar is in CNF (Chomsky Normal Form).

        Raises:
            InvalidSizeError: If a production rule has more than two symbols.
        """
        for val in self.rules:
            if len(val) > 2:
                raise InvalidSizeError("The production rule \"" + self.name + " --> "+ val + "\" has more than 2 symbols")

    def validateIsLetter(self):
        """
        Validates that no production rule has a symbol that is not a letter or lambda.

        Raises:
            InvalidRuleError: If a production rule has a symbol that is not a letter or lambda.
        """
        for val in self.rules:
            if not val.isalpha() and not val == '':
                raise IsNotLetterError("The production rule \"" + self.name + " --> "+ val + "\" has a symbol that is not a letter or lambda")

    def produceEmptyStrings(self):
        """
        Verify if the variable can produce empty strings (lambda).

        Returns:
            bool: Indicates if the variable can produce empty strings.
        """
        can = False
        for rule in self.rules:
            if not rule:
                can = True
        return can
                

    def __str__(self):
        """
        Creates a string representation for a Variable object.

        Returns:
            str: The string representation of the variable.
        """
        string = self.name + " --> "
        for rule in self.rules:
            if rule:
                string += rule + " | "
            else:
                string += "\u03BB" + " | "
        return string[:(len(string)-3)]

## Exceptions

class InvalidNameError(Exception):
    """Raised when the name of the variable is not in uppercase."""
    pass

class InvalidSizeError(Exception):
    """Raised when a production rule of a variable has more than two symbols."""
    pass

class IsNotLetterError(Exception):
    """Raised when a production rule of a variable is not a letter or lambda."""
    pass

## Tests
#var1 = Variable("S", {"b", "a", " "})
#print(var1)
#print(var1.produceEmptyStrings())
