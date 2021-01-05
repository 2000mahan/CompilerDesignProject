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
        if self.begin != "" and not self.begin[1]:
            self.begin = (self.begin[0], True)
            return self.begin[0] + " :\n" + self.code
        return self.code

    def generate_boolean_code(self):
        if self.label != "" and not self.label[1]:
            self.code += self.label[1] + " :\n"
        self.true = (self.true[0], True)
        self.false = (self.false[0], True)
        self.code += 'if (' + self.exp + ") goto " + self.true[0] + ";\ngoto " + self.false[0]
        return self.code + ";"
