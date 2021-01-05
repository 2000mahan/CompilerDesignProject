from code_generation.nonTerminal import NonTerminal
import re

class CodeGenerator:

    def __init__(self):
        pass

    def template_header(self):
        return """#include <stdio.h>
#include <setjmp.h>

int array[(int)1e6];

union jmp_buffer_union
{
	jmp_buf env_in_buf;
	struct {
		int env[64];	
	}env_in_int;
}env;

int val, i;

#define forward_jmp(position)								\
	val = 0;												\
	val=setjmp(env.env_in_buf); 							\
	if(!val)			 									\
		for(i = 0;i < 64;i++)								\
			array[position + i] = env.env_in_int.env[i]

#define back_jmp(position) 									\
	for(i = 0;i < 64;i++)									\
		env.env_in_int.env[i] = array[position + i];		\
	longjmp(env.env_in_buf, 1)
	
	
"""

    def generate_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code += p[1].code + "\n"
        p[0].code += p[3].code + "\n"
        p[0].code += "int " + p[0].place + " = "
        p[0].code += p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ";"
        p[0].type = "int"
        p[0].exp = p[1].get_exp() + " " + p[2] + " " + p[3].get_exp()

    def generate_negation_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code += p[2].code + "\n"
        p[0].code += "int " + p[0].place + " = "
        p[0].code += "0 " + p[1] + " " + p[2].get_value() + ";"
        p[0].type = "num"
        p[0].exp = "0 " + p[1] + " " + p[2].get_exp()

    def generate_boolean_relop_code(self, p, temp, true, false, label):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].true = true
        p[0].false = false
        p[0].begin = label
        p[0].exp = p[1].get_value() + " " + p[2] + " " + p[3].get_value()
        p[0].type = "bool"

    def generate_if(self, p, next_label, exp_idx, stmt_idx, is_else_if):
        p[0].next = next_label[0], True

        if len(p[exp_idx].quad) == 0:
            print(p[exp_idx].generate_boolean_code())
        true_list = list(self.generate_t_list(p[exp_idx]))
        false_list = list(self.generate_f_list(p[exp_idx]))
        if not is_else_if:
            p[0].code += p[6].code + "\n"
            next_label = p[6].begin
        if len(p) == 9:
            p[0].code += p[8].code + '\n'
        for (true_label, _) in true_list:
            p[0].code += true_label + " : printf(\"\");\n" + \
                         "goto " + p[stmt_idx].begin[0] + ";\n"
        for (false_label, _) in false_list:
            p[0].code += false_label + " : printf(\"\");\n" + \
                         "goto " + next_label[0] + ";\n"
        if len(p) == 9:
            p[0].code += p[6].next[0] + " : printf(\"\");\n"
            p[0].code += "goto " + p[0].next[0] + ';\n'

        p[0].code += p[stmt_idx].generate_labeled_code()
        p[stmt_idx].begin = (p[stmt_idx].begin[0], True)

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

    def generate_assign(self, p, iddec):
        p[0] = NonTerminal()
        p[0].code = p[3].code
        if not iddec:
            p[0].code += "\n" + p[1].get_value() + " = " + p[3].get_value() + ';'
            p[0].exp = p[1].exp
        else:
            p[0].exp = p[1].exp + " = " + p[3].get_value()
        p[1].type = p[3].type
        p[1].beign = p[3].begin
        p[1].next = p[3].next
        if p[3].has_place():
            p[0].place = p[3].get_value()
        else:
            p[0].value = p[3].get_value()

    def generate_iddec_lvalue(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code
        p[0].exp = p[1].exp
        p[0].type = p[1].type
        p[0].place = p[1].place

    def generate_lvalue_from_id(self, p):
        p[0] = NonTerminal()
        p[0].exp = p[1]
        p[0].place = p[1]

    def generatelvalue_from_array(self, p, temp):
        p[0] = NonTerminal()
        p[0].exp = p[1] + "[" + p[3].get_exp() + "]"
        p[0].code = p[3].code + '\nint ' + temp + " = " + p[1] + "[" + p[3].get_value() + "]"
        p[0].place = temp

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

    def generate_empty_elseif_list(self, p, new_label):
        p[0].next = p[0].begin = new_label

    def generate_elseif_list(self, p, new_label):
        p[0].begin = p[4].begin
        p[0].next = new_label
        p[0].next = (p[1].next[0], True)
        self.generate_if(p, p[0].next, 4, 6, True)
        # p[2].begin = p[1].next
        # p[0].code = p[1].code + "\n" + p[2].generate_labeled_code()

    def generate_from_block(self, p):
        p[0] = NonTerminal()
        p[0].code = p[2].code
        p[0].begin = p[2].begin
        p[0].next = p[2].next

    def generate_paran_exp(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        if p[2].type != "bool":
            p[0].code = p[2].code + "\n"
            p[0].code += "int " + p[0].place + " = " + p[2].place + ';'
        p[0].type = p[2].type
        p[0].exp = p[2].get_exp()
        p[0].true = p[2].true
        p[0].false = p[2].false

    def generate_lvalue_exp(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code
        p[0].exp = p[1].exp
        p[0].type = p[1].type
        p[0].place = p[1].place

    def generate_print(self, p, label):
        p[0] = NonTerminal()
        p[0].next = label
        p[0].code += 'printf(%d, ' + p[3] + ');'

    def generate_id_list(self, p):
        p[0] = NonTerminal()
        if len(p) == 2:
            p[0].code = p[1].code
            p[0].exp = p[1].exp
        else:
            p[0].code = p[3].code + '\n'
            p[0].code += p[1].code
            p[0].exp += p[1].exp + ', ' + p[3].exp

    def generate_vardec(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code + '\n'
        p[0].code += p[3].type + " " + p[1].exp

    def generate_program(self, p):
        p[0] = NonTerminal()
        p[0].code = self.template_header()
        block_idx = 4
        if len(p) == 6:
            block_idx = 5
            p[0].code += p[1].code + '\n'
        p[0].code += """int main() {\n""" + p[block_idx].code + "\n }"
        code = p[0].code
        code = re.sub(r'\n+', '\n', code)
        print(code)

    def generate_dec_from_vardec(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code + ";\n"

    def generate_declist(self, p):
        p[0] = NonTerminal()
        p[0].code += p[1].code
        if len(p) == 3:
            p[0].code += p[2].code
