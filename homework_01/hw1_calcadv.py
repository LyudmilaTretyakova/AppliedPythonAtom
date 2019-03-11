# import operator
# import re
# ops = { '+': operator.add,        '-': operator.sub,  '*': operator.mul,    '/': operator.truediv}
# def eval_expression(tokens, stack):
#     _rex=re.compile(r'^[-+]?[0-9]*[.,]?[0-9]+(?:[eE][-+]?[0-9]+)?$')
#     for token in tokens:
#         if _rex.match(token):
#             stack.append(float(token))
#         elif token in ops:
#             if len(stack) < 1:
#                 return None
#             elif len(stack)==1:
#                 return stack.pop()
#             else:
#                 a = stack.pop()
#                 b = stack.pop()
#             op = ops[token]
#             stack.append(op(b,a))
#         else:
#             return None
#     return stack.pop()
#
# def advanced_calculator (expr):
#     expression=expr
#     stack = []
#     if len(expression)==0:
#             return None
#     else:
#         return eval_expression(expression.split(' '), stack)