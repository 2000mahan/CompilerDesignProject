from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        pass

    def generate_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[0].place + " = "
        p[0].code += p[1].get_value() + " " + p[2] + " " + p[3].get_value()
        print(p[0].code)