class NonTerminal:

    def __init__(self):
        self.place = ""
        self.true = ""
        self.false = ""
        self.begin = ""
        self.type = ""
        self.exp = ""
        self.label = ""
        self.code = """"""
        self.quad = []
        self.parameters = []
        self.value = ""
        self.next = ""

    def get_value(self):
        if self.value == "":
            return self.place
        return self.value

    def has_place(self):
        if self.place == "":
            return False
        return True

    def get_exp(self):
        if self.value == "":
            return self.exp
        return self.value

    def generate_labeled_code(self):
        if self.begin != "":
            return self.begin + " :\n" + self.code
        return self.code

    def generate_boolean_code(self):
        if self.label != "":
            self.code += self.label + " :\n"
        self.code += 'if (' + self.exp + ") goto " + self.true + ";\ngoto " + self.false
        return self.code + ";"
