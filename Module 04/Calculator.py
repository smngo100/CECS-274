import numpy as np
import ArrayStack
import ChainedHashTable
#import BinaryTree
import ChainedHashTable
#import DLList
import operator
import re

class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable()

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for i in s:
            if i == "(":
                stack.push("(")
            elif i == ")":
                try:
                    stack.pop()
                except IndexError:
                    return False
        size = stack.size()
        if size == 0:
            return True
        else:
            return False

    def build_parse_tree(self, exp: str) -> str:
        # todo
        pass

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        pass

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def print_expression(self, expr):
        variables = [x for x in re.split(r'\W+', expr) if x.isalnum()]
        everything_else = re.split(r'\w+', expr)
        result = ""
        for i in range(len(variables)):
            result += everything_else[i]
            value = self.dict.find(variables[i])
            if value is not None:
                result += str(value)
            else:
                result += variables[i]
        if len(everything_else) > len(variables):
            result += everything_else[-1]
        print(result)
