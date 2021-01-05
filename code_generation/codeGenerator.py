from code_generation.nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        pass

    def generate_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code += p[1].code + "\n"
        p[0].code += p[3].code + "\n"
        p[0].code += p[0].place + " = "
        p[0].code += p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ";"
        p[0].type = "num"
        p[0].exp = p[1].get_exp() + " " + p[2] + " " + p[3].get_exp()

    def generate_negation_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code += p[2].code + "\n"
        p[0].code += p[0].place + " = "
        p[0].code += "0 " + p[1] + " " + p[2].get_value() + ";"
        p[0].type = "num"
        p[0].exp = "0 " + p[1] + " " + p[2].get_exp()

    def generate_boolean_relop_code(self, p, temp, true, false):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].true = true
        p[0].false = false
        p[0].exp = p[1].get_value() + " " + p[2] + " " + p[3].get_value()
        p[0].type = "bool"

    def generate_if(self, p, next_label):
        p[0] = NonTerminal()
        p[0].next = next_label

        if len(p[3].quad) == 0:
            print(p[3].generate_boolean_code())

        true_list = list(self.generate_t_list(p[3]))
        false_list = list(self.generate_f_list(p[3]))
        for true_label in true_list:
            p[0].code += true_label + ":\n" + \
                "goto " + p[5].begin + ";\n"
        for false_label in false_list:
            p[0].code += false_label + ":\n" + \
                "goto " + next_label + ";\n"
        p[0].code += p[5].generate_labeled_code()
        print(p[0].code)

    def generate_t_list(self, p):
        result = set()
        if len(p.quad) == 0:
            result.add(p.true)
        elif p.quad[1] == "and":
            result = result.union(self.generate_t_list(p.quad[2]))
        elif p.quad[1] == "not":
            result = result.union(self.generate_f_list(p.quad[0]))
        else:
            result = result.union(self.generate_t_list(p.quad[0]))
            result = result.union(self.generate_t_list(p.quad[2]))

        return result

    def generate_f_list(self, p):
        result = set()
        if len(p.quad) == 0:
            result.add(p.false)
        elif p.quad[1] == "or":
            result = result.union(self.generate_f_list(p.quad[2]))
        elif p.quad[1] == "not":
            result = result.union(self.generate_t_list(p.quad[0]))
        else:
            result = result.union(self.generate_f_list(p.quad[0]))
            result = result.union(self.generate_f_list(p.quad[2]))

        return result

    def generate_assign(self, p):
        p[0] = NonTerminal()
        p[0].exp = p[1].get_exp() + " = " + p[3].get_exp()
        p[0].code = p[3].code + "\n" + p[1].get_value() + " = " + p[3].get_value()
        p[1].type = p[3].type
        if p[3].has_place():
            p[0].place = p[3].get_value()
        else:
            p[0].value = p[3].get_value()

    def generate_lvalue_from_id(self, p):
        p[0] = NonTerminal()
        p[0].exp = p[1]
        p[0].value = p[1]
        p[0].code = p[1]

    def generate_statement_from_exp(self, p, next_label):

        p[0] = NonTerminal()
        p[0].next = next_label
        p[0].code = p[1].code

    def generate_empty_statement_list(self, p, new_label):
        p[0].begin = p[0].next = new_label

    def generate_statement_list(self, p):
        p[0].begin = p[1].begin
        p[0].next = p[2].next
        p[2].begin = p[1].next
        p[0].code = p[1].code + "\n" + p[2].generate_labeled_code()

    def generate_from_block(self, p):
        p[0] = NonTerminal()
        p[0].code = p[2].code
        p[0].begin = p[2].begin
        p[0].next = p[2].next

    def generate_paran_exp(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[2].code
        p[0].type = p[2].type
        p[0].exp = p[2].get_exp()
        p[0].true = p[2].true
        p[0].false = p[2].false
        print(p[0].code)
