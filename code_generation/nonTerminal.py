import re

printed_labels = set()

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
        self.final = ''
        self.cases = []
        self.symbols = []

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
        if self.begin != "" and (re.match(r'^\n*' + self.begin[0] + " :", self.code) is None):
            self.begin = (self.begin[0], True)
            code = re.sub(r'\n+', '\n', self.code)
            code = re.sub(r'^\n+', '', code)
            printed_labels.add(self.begin[0])
            return self.begin[0] + " : printf(\"\");\n" + code

        return self.code

    def generate_boolean_code(self):
        if self.begin != "":
            self.begin = (self.begin[0], True)
            printed_labels.add(self.begin[0])
            self.code = self.begin[0] + " : printf(\"\");\n" + self.code
        code = self.code
        if self.true != '' and self.false != '' and self.exp != '':
            code = re.sub(r'\n+', '\n', 'if (' + self.exp + ") goto " + self.true[0] + ";\ngoto " + self.false[0] + ";")
        code = re.sub(r'^\n+', '', code)
        self.code += code
        return self.code + ";"
