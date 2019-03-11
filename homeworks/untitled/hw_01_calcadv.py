#!/usr/bin/env python
# coding: utf-8
import operator
def calc(expr):
   try:
        OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = [0]
        n=expr.find('(')
        nk=expr.find(')')
        while n != -1:
            if n != -1 and  nk!= -1:
                vih = expr[expr.find("(") + 1:expr.find(")")]
                for token in vih.split(" "):
                    if token in OPERATORS:
                        op2, op1 = stack.pop(), stack.pop()
                        stack.append(OPERATORS[token](op1, op2))
                    elif token:
                        stack.append(float(token))
                expr= expr.replace('(' + vih + ')', str(stack.pop()))
                stack.clear()
                n=expr.find('(')
                nk = expr.find(')')
            else:
                expr=[]
                stack.append('None')
                break
        for token in expr.split(" "):
            if token in OPERATORS:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(OPERATORS[token](op1,op2))
            elif token:
                if isinstance(token,(float,int)):
                    stack.append(float(token))
                else:
                    break
   except IndexError:
       stack.append('None')
   except ZeroDivisionError:
       stack.append('None')
   return stack.pop()

#!/usr/bin/env python
# coding: utf-8
import operator
def advanced_calculator(expr):
        OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = [0]
        n=expr.find('(')
        nk=expr.find(')')
    # while n != -1:
    #     if n != -1 and  nk!= -1:
    #         vih = expr[expr.find("(") + 1:expr.find(")")]
    #         for token in vih.split(" "):
    #             if token in OPERATORS:
    #                 op2, op1 = stack.pop(), stack.pop()
    #                 stack.append(OPERATORS[token](op1, op2))
    #             elif token:
    #                 if isinstance(token, (float, int)):
    #                     stack.append(float(token))
    #                 else:
    #                     break;
    #                     return None
    #         expr= expr.replace('(' + vih + ')', str(stack.pop()))
    #         stack.clear()
    #         n=expr.find('(')
    #         nk = expr.find(')')
        # else:
        #     expr=[]
        #     return None
        #     break
        expr=expr.split(" ")
        expr=expr.split(',')
        for token in expr.split(" "):
            if token in OPERATORS['-']:
                otr.append();
            if token in OPERATORS:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(OPERATORS[token](op1,op2))
            elif token:
                stack.append(float(token))
        if len(stack):
            return stack.pop()




