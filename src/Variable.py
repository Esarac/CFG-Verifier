class Variable:

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
        self.validateVariableName()
        self.validateSize()
        self.validateIsLetter()

    def validateVariableName(self):
        if not self.name.isupper():
            raise Exception("\"" + self.name + "\" must be in uppercase")

    def validateSize(self):
        for val in self.rules:
            if len(val) > 2:
                raise Exception("The production rule \"" + val + "\" length is greater than 2")

    def validateIsLetter(self):
        for val in self.rules:
            if not val.isalpha() and not val == ' ':
                raise Exception("The production rule \"" + val + "\" is not a letter or lambda")

    #documentation

    def __str__(self):
        string = self.name + " --> "
        for path in self.rules:
            string += path + " | "
        return string[:(len(string)-3)]