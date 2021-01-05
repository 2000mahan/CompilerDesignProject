import re

class NonTerminal:

    def __init__(self):
        self.place = ""
        self.true = ""
        self.false = ""
        self.begin = ""
        self.type = ""
        self.exp = ""
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
            code = re.sub(r'\n+', '\n', self.code)
            code = re.sub(r'^\n+', '', code)
            return self.begin[0] + " : printf(\"\");\n" + code

        return self.code

    def generate_boolean_code(self):
        if self.begin != "" and not self.begin[1]:
            self.begin = (self.begin[0], True)
            self.code += self.begin[0] + " : printf(\"\");\n"
        self.true = (self.true[0], True)
        self.false = (self.false[0], True)
        code = re.sub(r'\n+', '\n', 'if (' + self.exp + ") goto " + self.true[0] + ";\ngoto " + self.false[0])
        code = re.sub(r'^\n+', '', code)
        self.code += code
        return self.code + ";"
