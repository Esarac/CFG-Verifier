class Variable:

    def __init__(self, name, paths):
        self.name = name
        self.paths = paths
        if self.validateVariableName() == False:
            raise Exception()


    def validateVariableName(self):
        return self.name.isupper()

    def __str__(self):
        string = self.name + " --> "
        for path in self.paths:
            string += path + " | "
        return string[:(len(string)-3)]
