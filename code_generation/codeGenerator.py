from math import exp

from code_generation import nonTerminal
from code_generation.nonTerminal import NonTerminal
import re


class CodeGenerator:

    def __init__(self, parser):
        self.last_arr_pos = 0
        self.arr_dic = dict()
        self.parser = parser

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

    def generate_arithmetic_code(self, p, temp, label):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].begin = label
        p[0].code += p[1].code + "\n"
        p[0].code += p[3].code + "\n"
        p[0].code += "int " + p[0].place + " = "
        p[0].code += p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ";"
        p[0].type = "int"
        p[0].exp = p[1].get_exp() + " " + p[2] + " " + p[3].get_exp()

    def generate_negation_code(self, p, temp, label):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].begin = label
        p[0].code += p[2].code + "\n"
        p[0].code += "int " + p[0].place + " = "
        p[0].code += "0 " + p[1] + " " + p[2].get_value() + ";"
        p[0].type = "num"
        p[0].exp = "0 " + p[1] + " " + p[2].get_exp()

    def generate_boolean_relop_code(self, p, temp, true, false, label, assignment_true_label, assignment_false_label,
                                    next_label, if_label, start_3):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].true = true
        p[0].false = false
        p[0].begin = label
        p[0].next = next_label
        p[0].exp = p[1].get_value() + " " + p[2] + " " + p[3].get_value()
        nonTerminal.printed_labels.add(p[0].begin[0])
        p[0].code += p[0].begin[0] + " : printf(\"\");\n"
        p[0].code += p[1].code + "\n"
        if p[3].begin == '':
            p[3].begin = start_3
        if p[1].next != '':
            p[0].code += self.make_tunnel(p[1].next[0], p[3].begin[0])
        p[0].code += p[3].generate_labeled_code() + "\n"
        if p[3].next != '':
            p[0].code += self.make_tunnel(p[3].next[0], if_label[0])
        nonTerminal.printed_labels.add(if_label[0])
        p[0].code += if_label[0] + " : printf(\"\");\nint " + p[0].place + ";\n"
        p[0].code += re.sub(r'\n+', '\n',
                            'if (' + p[0].exp + ") goto " + p[0].true[0] + ";\ngoto " + p[0].false[0] + ";")
        p[0].code += self.make_tunnel(p[0].true[0], assignment_true_label[0])
        p[0].code += self.make_tunnel(p[0].false[0], assignment_false_label[0])
        nonTerminal.printed_labels.add(assignment_true_label[0])
        nonTerminal.printed_labels.add(assignment_false_label[0])
        p[0].code += assignment_true_label[0] + " : printf(\"\");\n" + p[0].place + " = 1;\n" + "goto " + p[0].next[
            0] + ";\n"
        p[0].code += assignment_false_label[0] + " : printf(\"\");\n" + p[0].place + " = 0;\n" + "goto " + p[0].next[
            0] + ";\n"
        p[0].quad = [[], []]

    def generate_if(self, p, next_label, exp_idx, stmt_idx, is_else_if, true_label, false_label):
        if not is_else_if:
            p[0].next = next_label[0], True
        if len(p) == 9:
            p[0].next = p[8].next

        if len(p[exp_idx].quad) == 0:
            p[0].exp = p[exp_idx].generate_boolean_code()
            true_label = p[exp_idx].true
            false_label = p[exp_idx].false
        elif len(p[exp_idx].quad) == 2:
            p[0].code += p[exp_idx].generate_labeled_code()
            nonTerminal.printed_labels.add(p[exp_idx].next[0])
            p[0].code += p[exp_idx].next[0] + " : printf(\"\");\nif(" + p[exp_idx].get_value() + " == 1) goto " + \
                         true_label[0] + ";\ngoto " + false_label[
                             0] + ";\n"
        else:
            p[0].code += p[exp_idx].generate_labeled_code()
            true_label = p[exp_idx].true
            false_label = p[exp_idx].false
        p[0].code += p[stmt_idx].exp
        stmt_exp_label = self.get_starting_label(p[stmt_idx].exp)
        if not is_else_if:
            p[0].code += p[6].exp
            p[0].code += p[6].code + "\n"
            next_label = p[6].begin
            p[0].code += self.make_tunnel(p[6].final[0], p[0].next[0])

            if len(p) == 9:
                p[0].code += self.make_tunnel(p[6].next[0], p[8].begin[0])
            else:
                p[0].code += self.make_tunnel(p[6].next[0], p[0].next[0])

        if not is_else_if:
            p[0].code += self.make_tunnel(false_label[0], p[6].begin[0])
        else:
            p[0].code += self.make_tunnel(false_label[0], next_label[0])
        p[0].code += self.make_tunnel(true_label[0], p[stmt_idx].begin[0])
        if p[stmt_idx].begin[0] == stmt_exp_label:
            p[0].code += p[stmt_idx].code
        else:
            p[0].code += p[stmt_idx].generate_labeled_code()
        if not is_else_if:
            p[0].code += "goto " + p[stmt_idx].next[0] + ";\n"
            p[0].code += self.make_tunnel(p[stmt_idx].next[0], p[0].next[0])
        else:
            p[0].code += "\ngoto " + p[0].final[0] + ";\n"
        if len(p) == 9:
            exp_label = self.get_starting_label(p[8].exp)
            if exp_label == p[8].begin[0]:
                p[0].code += p[8].exp + '\n'
                p[0].code += p[8].code + '\n'
            elif exp_label is None:
                p[0].code += p[8].generate_labeled_code() + '\n'
            else:
                nonTerminal.printed_labels.add(exp_label)
                p[0].code += self.make_tunnel(p[8].begin[0], exp_label)
                p[0].code += exp_label + " : printf(\"\");\n" + p[8].exp + '\n'
                p[0].code += p[8].code + '\n'
            p[0].code += "goto " + p[0].next[0] + ";\n"

    def generate_and(self, p, label_generator):
        # p[0] = NonTerminal()
        # if len(p[1].quad) == 0:
        #     p[1].generate_boolean_code()
        # if len(p[3].quad) == 0:
        #     p[3].generate_boolean_code()
        # p[0].code += p[1].generate_labeled_code()
        # p[0].code += p[3].generate_labeled_code()
        # p[0].true = t_label
        # p[0].false = f_label
        # p[0].code += self.make_tunnel(p[1].true[0], p[3].begin[0])
        # p[0].code += self.make_tunnel(p[3].true[0], p[0].true[0])
        # p[0].code += self.make_tunnel(p[1].false[0], p[0].false[0])
        # p[0].code += self.make_tunnel(p[3].false[0], p[0].false[0])
        # p[0].quad = [[]]
        p[0] = NonTerminal()
        p[0].begin = label_generator()
        nonTerminal.printed_labels.add(p[0].begin[0])
        p[0].code += p[0].begin[0] + " : printf(\"\");\n"
        p[0].code += p[1].code
        if len(p[1].quad) != 1:
            begin_0 = label_generator()
            if p[1].next != '':
                p[0].code += self.make_tunnel(p[1].next[0], begin_0[0])
            elif len(p[1].quad) == 0:
                p[1].begin = p[1].next = begin_0
            nonTerminal.printed_labels.add(begin_0[0])
            p[0].code += begin_0[0] + " : printf(\"\");\n"
            t0_label = label_generator()
            f0_label = label_generator()
            p[0].code += "if(" + p[1].get_value() + ") goto " + t0_label[0] + ";\ngoto " + f0_label[0] + ";\n"
        else:
            t0_label = p[1].true
            f0_label = p[1].false

        p[0].code += p[3].code
        if len(p[3].quad) != 1:
            begin_1 = label_generator()
            if p[3].next != '':
                p[0].code += self.make_tunnel(p[3].next[0], begin_1[0])
            elif len(p[3].quad) == 0:
                p[3].begin = p[3].next = begin_1
            nonTerminal.printed_labels.add(begin_1[0])
            p[0].code += begin_1[0] + " : printf(\"\");\n"
            t1_label = label_generator()
            f1_label = label_generator()
            p[0].code += "if(" + p[3].get_value() + ") goto " + t1_label[0] + ";\ngoto " + f1_label[0] + ";\n"
        else:
            t1_label = p[3].true
            f1_label = p[3].false
        p[0].true = label_generator()
        p[0].false = label_generator()
        p[0].code += self.make_tunnel(t0_label[0], p[3].begin[0])
        p[0].code += self.make_tunnel(t1_label[0], p[0].true[0])
        p[0].code += self.make_tunnel(f0_label[0], p[0].false[0])
        p[0].code += self.make_tunnel(f1_label[0], p[0].false[0])
        p[0].quad = [[]]

    def generate_or(self, p, label_generator):
        # p[0] = NonTerminal()
        # if len(p[3].quad) == 0:
        #     p[3].generate_boolean_code()
        # if len(p[1].quad) == 0:
        #     p[1].generate_boolean_code()
        # p[0].code += p[1].generate_labeled_code()
        # p[0].code += p[3].generate_labeled_code()
        # p[0].true = t_label
        # p[0].false = f_label
        # p[0].code += self.make_tunnel(p[1].true[0], p[0].true[0])
        # p[0].code += self.make_tunnel(p[3].true[0], p[0].true[0])
        # p[0].code += self.make_tunnel(p[1].false[0], p[3].begin[0])
        # p[0].code += self.make_tunnel(p[3].false[0], p[0].false[0])
        # p[0].quad = [[]]
        p[0] = NonTerminal()
        p[0].begin = label_generator()
        nonTerminal.printed_labels.add(p[0].begin[0])
        p[0].code += p[0].begin[0] + " : printf(\"\");\n"
        p[0].code += p[1].code
        if len(p[1].quad) != 1:
            begin_0 = label_generator()
            if p[1].next != '':
                p[0].code += self.make_tunnel(p[1].next[0], begin_0[0])
            elif len(p[1].quad) == 0:
                p[1].begin = p[1].next = begin_0
            nonTerminal.printed_labels.add(begin_0[0])
            p[0].code += begin_0[0] + " : printf(\"\");\n"
            t0_label = label_generator()
            f0_label = label_generator()
            p[0].code += "if(" + p[1].get_value() + ") goto " + t0_label[0] + ";\ngoto " + f0_label[0] + ";\n"
        else:
            t0_label = p[1].true
            f0_label = p[1].false

        p[0].code += p[3].code
        if len(p[3].quad) != 1:
            begin_1 = label_generator()
            if p[3].next != '':
                p[0].code += self.make_tunnel(p[3].next[0], begin_1[0])
            elif len(p[3].quad) == 0:
                p[3].begin = p[3].next = begin_1
            nonTerminal.printed_labels.add(begin_1[0])
            p[0].code += begin_1[0] + " : printf(\"\");\n"
            t1_label = label_generator()
            f1_label = label_generator()
            p[0].code += "if(" + p[3].get_value() + ") goto " + t1_label[0] + ";\ngoto " + f1_label[0] + ";\n"
        else:
            t1_label = p[3].true
            f1_label = p[3].false
        p[0].true = label_generator()
        p[0].false = label_generator()
        p[0].code += self.make_tunnel(t0_label[0], p[0].true[0])
        p[0].code += self.make_tunnel(t1_label[0], p[0].true[0])
        p[0].code += self.make_tunnel(f0_label[0], p[3].begin[0])
        p[0].code += self.make_tunnel(f1_label[0], p[0].false[0])
        p[0].quad = [[]]

    def generate_not(self, p, label_generator):
        # p[0] = NonTerminal()
        # if len(p[2].quad) == 0:
        #     p[2].generate_boolean_code()
        # p[0].code += p[2].generate_labeled_code()
        # p[0].true = t_label
        # p[0].false = f_label
        # p[0].code += self.make_tunnel(p[2].true[0], p[0].false[0])
        # p[0].code += self.make_tunnel(p[2].false[0], p[0].true[0])
        # p[0].quad = [[]]
        p[0] = NonTerminal()
        p[0].begin = label_generator()
        nonTerminal.printed_labels.add(p[0].begin[0])
        p[0].code += p[0].begin[0] + " : printf(\"\");\n"
        p[0].code += p[1].code
        if len(p[1].quad) != 1:
            begin_0 = label_generator()
            if p[1].next != '':
                p[0].code += self.make_tunnel(p[1].next[0], begin_0[0])
            elif len(p[1].quad) == 0:
                p[1].begin = p[1].next = begin_0
            nonTerminal.printed_labels.add(begin_0[0])
            p[0].code += begin_0[0] + " : printf(\"\");\n"
            t0_label = label_generator()
            f0_label = label_generator()
            p[0].code += "if(" + p[1].get_value() + ") goto " + t0_label[0] + ";\ngoto " + f0_label[0] + ";\n"
        else:
            t0_label = p[1].true
            f0_label = p[1].false

        p[0].true = label_generator()
        p[0].false = label_generator()
        p[0].code += self.make_tunnel(t0_label[0], p[0].false[0])
        p[0].code += self.make_tunnel(f0_label[0], p[3].true[0])
        p[0].quad = [[]]

    def generate_assign(self, p, iddec, label_generator, temp_generator):
        p[0] = NonTerminal()
        p[0].begin = label_generator()
        p[0].code = p[3].code
        p[0].code += p[1].code
        if not iddec:
            if p[3].get_value() == '':
                temp = temp_generator()
                p[0].code = "int " + temp + ";\n" + p[0].code + self.get_assign_from_bool(p, label_generator(),
                                                                                          label_generator(),
                                                                                          label_generator(),
                                                                                          temp)
            if p[3].next != '':
                p[0].code += self.make_tunnel(p[0].begin[0], p[3].next[0])
            p[0].code = p[0].begin[0] + " : printf(\"\");\n" + p[0].code
            nonTerminal.printed_labels.add(p[0].begin[0])
            p[0].code += "\n" + p[1].get_value() + " = " + p[3].get_value() + ';'
            p[0].exp = p[1].exp
        else:
            if p[3].get_value() == '':
                temp = temp_generator()
                p[0].code = "int " + temp + ";\n" + p[0].code + self.get_assign_from_bool(p, label_generator(),
                                                                                          label_generator(),
                                                                                          label_generator(),
                                                                                          temp)
            if p[3].next != '':
                p[0].code += self.make_tunnel(p[0].begin[0], p[3].next[0])
            p[0].code = p[0].begin[0] + " : printf(\"\");\n" + p[0].code
            nonTerminal.printed_labels.add(p[0].begin[0])
            p[0].exp = p[1].exp
            p[0].code += "\n" + p[1].exp + " = " + p[3].get_value() + ';'
        p[1].type = p[3].type
        p[1].beign = p[3].begin
        p[1].next = p[3].next
        if p[3].has_place():
            p[0].place = p[3].get_value()
        else:
            p[0].value = p[3].get_value()

    def get_assign_from_bool(self, p, true_l, false_l, next_l, temp, exp_idx=3):
        code = ''

        if len(p[3].quad) == 0:
            p[0].exp = p[exp_idx].generate_boolean_code()
        else:
            p[0].code += p[exp_idx].generate_labeled_code()

        code += self.make_tunnel(p[exp_idx].false[0], false_l[0])
        code += self.make_tunnel(p[exp_idx].true[0], true_l[0])
        nonTerminal.printed_labels.add(true_l[0])
        nonTerminal.printed_labels.add(false_l[0])
        nonTerminal.printed_labels.add(next_l[0])
        code += true_l[0] + " : printf(\"\");\n" + temp + " = 1;\ngoto " + next_l[0] + ";\n"
        code += false_l[0] + " : printf(\"\");\n" + temp + " = 0;\ngoto " + next_l[0] + ";\n"
        code += next_l[0] + " : printf(\"\");\n"
        p[exp_idx].place = temp
        return code

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

    def generate_lvalue_from_array(self, p, temp):
        p[0] = NonTerminal()
        if p[1] not in self.arr_dic:
            size = int(p[3].value)
            self.arr_dic[p[1]] = self.last_arr_pos
            p[0].code += 'array[' + str(self.last_arr_pos) + '] = ' + p[3].value + ';\n'
            self.last_arr_pos += size + 1
            p[0].exp = p[1]
        else:
            pos = self.arr_dic[p[1]]
            p[0].exp = p[1] + "[" + p[3].get_exp() + "]"
            p[0].code = p[3].code
            p[0].code += "int " + temp + " = " + p[3].get_value() + " + " + str(pos + 1) + ";\n"
            p[0].place = "array[" + temp + "]"

    def generate_statement_from_exp(self, p, next_label):

        p[0] = NonTerminal()
        p[0].next = next_label
        p[0].code = p[1].code

    def generate_case(self, p, start_label, next_label):
        p[0] = NonTerminal()
        p[0].begin = start_label
        p[0].code = p[4].code + "\ngoto " + next_label[0] + ";"
        p[0].cases = [(start_label[0], p[2].get_value(), next_label[0])]
        p[0].symbols.extend(p[4].symbols)

    def generate_cases_empty(self, p, start_label):
        p[0] = NonTerminal()
        p[0].begin = p[0].next = start_label

    def generate_statement_from_on(self, p, label_generator):
        p[0] = NonTerminal()
        p[0].begin = label_generator()
        p[0].next = label_generator()
        p[0].symbols.extend(p[6].symbols)
        current_label = p[0].begin
        next_label = label_generator()
        for i in range(len(p[6].cases)):
            case_record = p[6].cases[i]
            nonTerminal.printed_labels.add(current_label[0])
            p[0].code += current_label[0] + " : printf(\"\");\n" \
                                            "if(" + p[3].get_value() + " == " + case_record[1] + ") " \
                                                                                                 "goto " + case_record[
                             0] + ";\n" \
                                  "goto " + next_label[0] + ";\n"
            current_label = next_label
            next_label = label_generator()
        p[0].code += p[6].code
        p[0].code += "\n"
        for case_record in p[6].cases:
            p[0].code += self.make_tunnel(case_record[2], p[0].next[0]) + "\n"

    def generate_statement_from_for_in(self, p, next_label, header_label, dec_label, if_label, true_label, false_label,
                                       setup_label, temp, temp_size, temp_setup):
        p[0] = NonTerminal()
        p[0].begin = header_label
        p[0].next = next_label
        p[0].symbols.extend(p[7].symbols)
        arr_pos = self.arr_dic[p[5]]
        p[0].code += self.make_tunnel(header_label[0], dec_label[0])
        nonTerminal.printed_labels.add(dec_label[0])
        p[0].code += dec_label[0] + " : printf(\"\");\n"
        p[0].code += "int " + temp + " = 0;\nint " + temp_size + " = array[" + str(
            arr_pos) + "];\nint " + temp_setup + ";\n"
        nonTerminal.printed_labels.add(if_label[0])
        p[0].code += if_label[0] + ' : printf(\"\");\n'
        p[0].code += "if(" + temp + " < " + temp_size + ") goto " + true_label[0] + ";\ngoto " + false_label[0] + ";\n"

        p[0].code += self.make_tunnel(false_label[0], p[0].next[0])
        p[0].code += self.make_tunnel(true_label[0], setup_label[0])
        nonTerminal.printed_labels.add(setup_label[0])
        p[0].code += setup_label[0] + " : printf(\"\");\n"
        p[0].code += temp_setup + " = " + str(1 + arr_pos) + " + " + temp + ";"
        p[0].code += p[3] + " = array[" + temp_setup + "];"
        p[0].code += "goto " + p[7].begin[0] + ";\n"
        p[0].code += p[7].generate_labeled_code()
        p[0].code += temp + " = " + temp + " + 1;\n"
        p[0].code += "goto " + str(if_label[0]) + ";"

    def generate_statement_from_for(self, p, next_label, header_label, true_label, false_label):
        p[0] = NonTerminal()
        p[0].begin = header_label
        p[0].next = next_label
        p[0].symbols.extend(p[9].symbols)
        p[0].code += self.make_tunnel(header_label[0], p[3].begin[0])
        p[0].code += "\n" + p[3].generate_labeled_code() + "\n"
        if len(p[5].quad) == 0:
            p[0].exp = p[5].generate_boolean_code()
            true_label = p[5].true
            false_label = p[5].false
        elif len(p[5].quad) == 2:
            p[0].code += p[5].generate_labeled_code()
            nonTerminal.printed_labels.add(p[5].next[0])
            p[0].code += p[5].next[0] + " : printf(\"\");\nif(" + p[5].get_value() + " == 1) goto " + true_label[
                0] + ";\ngoto " + false_label[
                             0] + ";\n"
        else:
            p[0].code += p[5].generate_labeled_code()
            true_label = p[5].true
            false_label = p[5].false
        p[0].code += self.make_tunnel(false_label[0], p[0].next[0])
        p[0].code += self.make_tunnel(true_label[0], p[9].begin[0])
        p[0].code += p[9].generate_labeled_code()
        p[0].code += p[7].code + "\n"
        p[0].code += "\ngoto " + str(p[5].begin[0]) + ";"

    def generate_statement_from_while(self, p, next_label, true_label, false_label):
        p[0] = NonTerminal()
        p[0].begin = p[3].begin
        p[0].next = next_label
        p[0].symbols.extend(p[5].symbols)
        if len(p[3].quad) == 0:
            p[0].exp = p[3].generate_boolean_code()
            true_label = p[3].true
            false_label = p[3].false
        elif len(p[3].quad) == 2:
            p[0].code += p[3].generate_labeled_code()
            nonTerminal.printed_labels.add(p[3].next[0])
            p[0].code += p[3].next[0] + " : printf(\"\");\nif(" + p[3].get_value() + " == 1) goto " + true_label[
                0] + ";\ngoto " + false_label[
                             0] + ";\n"
        else:
            p[0].code += p[3].generate_labeled_code()
            true_label = p[3].true
            false_label = p[3].false
        p[0].code += self.make_tunnel(false_label[0], p[0].next[0])
        p[0].code += self.make_tunnel(true_label[0], p[5].begin[0])
        p[0].code += p[5].generate_labeled_code()
        p[0].code += "\ngoto " + str(p[3].begin[0]) + ";"

    def generate_empty_statement_list(self, p, new_label):
        p[0].begin = p[0].next = new_label

    def generate_statement_list(self, p):
        p[0].begin = p[1].begin
        p[0].next = p[2].next
        p[0].symbols.extend(p[1].symbols)
        p[0].symbols.extend(p[2].symbols)
        if p[2].begin == '':
            p[2].begin = p[1].next
        else:
            nonTerminal.printed_labels.add(p[1].next[0])
            p[0].code += "\n" + p[1].next[0] + " : printf(\"\");\ngoto " + p[2].begin[0] + ";"
        exp_label = self.get_starting_label(p[2].exp)
        if p[2].begin != '' and exp_label == p[2].begin[0]:
            p[0].code += p[1].code + "\n" + p[2].exp + "\n" + p[2].code
        else:
            p[0].code += p[1].code + "\n" + p[2].exp + "\n" + p[2].generate_labeled_code()

    def generate_empty_elseif_list(self, p, new_label, false_label, final_label):
        p[0].next = p[0].begin = new_label
        p[0].false = false_label
        p[0].final = final_label

    def generate_elseif_list(self, p, new_label, true_label, false_label):
        p[0].begin = p[1].begin
        p[0].final = p[1].final
        p[0].next = new_label
        p[0].false = p[1].false
        p[0].code += p[1].code
        p[0].symbols.extend(p[1].symbols)
        p[0].symbols.extend(p[6].symbols)
        p[0].code += self.make_tunnel(p[1].next[0], p[4].begin[0])
        self.generate_if(p, p[0].next, 4, 6, True)
        p[0].exp = p[1].exp + "\n" + p[0].exp

    def generate_from_block(self, p):
        p[0] = NonTerminal()
        p[0].code = p[2].code
        p[0].begin = p[2].begin
        p[0].next = p[2].next
        p[0].symbols.extend(p[2].symbols)

    def generate_paran_exp(self, p, temp, label):
        if p[2].get_value() != "":
            p[0] = NonTerminal()
            p[0].place = temp
            p[0].begin = label
            p[0].code += p[2].code + "\n"
            if p[2].next != '':
                p[0].code += self.make_tunnel(p[2].next[0], p[0].begin[0])
            nonTerminal.printed_labels.add(label[0])
            p[0].code += p[0].begin[0] + " : printf(\"\");\nint " + p[0].place + " = " + p[2].place + ';'
            p[0].type = p[2].type
            p[0].exp = p[2].get_exp()
            p[0].true = p[2].true
            p[0].false = p[2].false
            p[0].quad = p[2].quad
            p[0].next = p[2].next
        else:
            p[0] = p[2]

    def generate_lvalue_exp(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code
        p[0].exp = p[1].exp
        p[0].type = p[1].type
        p[0].place = p[1].place

    def generate_print(self, p, label):
        p[0] = NonTerminal()
        p[0].next = label
        p[0].code += 'printf("%d", ' + p[3] + ');'

    def generate_id_list(self, p):
        p[0] = NonTerminal()
        if len(p) == 2:
            p[0].code = p[1].code
            p[0].exp = p[1].exp
            p[0].symbols.append((p[1].exp, p.lexer.lexpos))

        else:
            p[0].code = p[3].code + '\n'
            p[0].code += p[1].code
            if p[3].exp == '':
                p[0].exp += p[1].exp
            else:
                p[0].exp += p[1].exp + ', ' + p[3].exp
            p[0].symbols.extend(p[1].symbols)
            p[0].symbols.append((p[3].exp, p.lexer.lexpos))

    def generate_vardec(self, p):
        p[0] = NonTerminal()
        p[0].exp = p[1].code + '\n'
        p[0].code = "int " + p[1].exp
        p[0].symbols.extend(p[1].symbols)

    def generate_program(self, p):
        p[0] = NonTerminal()
        p[0].code = self.template_header()
        block_idx = 4
        if len(p) == 6:
            p[0].symbols.extend(p[1].symbols)
            block_idx = 5
            code = self.fix_labels(p[1].exp + '\n' + p[block_idx].code)
            p[0].code += p[1].code + '\n'
            p[0].code += """int main() {\n""" + code + "return 0; \n}"
        else:
            code = self.fix_labels(p[block_idx].code)
            p[0].code += """int main() {\n""" + code + "return 0; \n}"
        p[0].symbols.append(p[block_idx].symbols)
        code = p[0].code
        code = re.sub(r'\n+', '\n', code)
        code = re.sub(r'\n+;\n+', "\n", code)
        print(code)
        print("\nSymbol Table:")
        print(p[0].symbols)

    def generate_dec_from_vardec(self, p):
        p[0] = NonTerminal()
        p[0].exp = p[1].exp + ";\n"
        p[0].code = p[1].code + ";\n"
        p[0].symbols.extend(p[1].symbols)

    def generate_declist(self, p):
        p[0] = NonTerminal()
        p[0].exp = p[1].exp
        p[0].code += p[1].code
        p[0].symbols.extend(p[1].symbols)
        if len(p) == 3:
            p[0].exp += p[2].exp
            p[0].code += p[2].code
            p[0].symbols.extend(p[2].symbols)

    def generate_cases(self, p):
        p[0] = NonTerminal()
        p[0].begin = p[1].begin
        p[0].next = p[2].next
        p[0].code = p[1].code + "\n" + p[2].generate_labeled_code()
        p[0].cases.extend(p[1].cases)
        p[0].cases.extend(p[2].cases)
        p[0].symbols.extend(p[1].symbols)
        p[0].symbols.extend(p[2].symbols)

    def make_tunnel(self, l1, l2):
        nonTerminal.printed_labels.add(l1)
        return "\n" + l1 + " : printf(\"\");\ngoto " + l2 + ";\n"

    def get_starting_label(self, code):
        if code is None:
            return None
        code = code.strip()
        area_reg = re.search(r"^L\d+ : printf", code)
        if area_reg is None:
            return None
        area = code[area_reg.regs[0][0]:area_reg.regs[0][1]]
        return area[:-9]

    def fix_labels(self, code):
        code = re.sub(r'\n+', '\n', code)
        code = re.sub(r'\n+;\n+', "\n", code)
        unused = []
        for i in range(self.parser.tempLabelCount):
            if "L" + str(i) not in nonTerminal.printed_labels:
                unused.append(i)
        if len(unused) > 0:
            replacement = unused[0]
            for un_label in unused:
                code = code.replace("goto L" + str(un_label) + ";", "goto L" + str(replacement) + ";")
            code += "L" + str(replacement) + " : printf(\"\");\n"

        tunnel = re.search(r'L\d+ : printf[(]["]["][)];\s+goto L\d+;', code)
        while tunnel is not None:
            area = code[tunnel.regs[0][0]:tunnel.regs[0][1]]
            tunnel_label_re = re.search(r"L\d+", area)
            tunnel_label = area[tunnel_label_re.regs[0][0]:tunnel_label_re.regs[0][1]]
            dest_label_re = re.search("goto L\d+", area)
            dest_label = area[dest_label_re.regs[0][0] + 5:dest_label_re.regs[0][1]]
            code = code[:tunnel.regs[0][0]] + code[tunnel.regs[0][1]:]
            code = code.replace("goto " + tunnel_label + ";", "goto " + dest_label + ";")
            # print(tunnel_label, "->", dest_label)
            tunnel = re.search(r'L\d+ : printf[(]["]["][)];\s+goto L\d+;', code)

        duplicate = re.search(r'L\d+ : printf[(]["]["][)];\s+L\d+ : printf[(]["]["][)];', code)
        while duplicate is not None:
            dup_area = code[duplicate.regs[0][0]:duplicate.regs[0][1]]
            first_dup_re = re.search(r"^L\d+", dup_area)
            second_dup_re = re.search('L\d+ : printf[(]["]["][)];$', dup_area)
            first_dup = dup_area[first_dup_re.regs[0][0]:first_dup_re.regs[0][1]]
            second_dup = dup_area[second_dup_re.regs[0][0]:second_dup_re.regs[0][1] - 14]
            code = code[:duplicate.regs[0][0]] + first_dup + " : printf(\"\");\n" + code[duplicate.regs[0][1]:]
            code = code.replace("goto " + second_dup + ";", "goto " + first_dup + ";")
            # print(second_dup, "->", first_dup)
            duplicate = re.search(r'L\d+ : printf[(]["]["][)];\s+L\d+ : printf[(]["]["][)];', code)
        code = code.replace(" printf(\"\");", ";")
        code = code.replace(r";", ";\n")
        return code
