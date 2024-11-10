import ArrayStack
import ChainedHashTable
import BinaryTree
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
        if not self.matched_expression(exp):
            raise ValueError
        pattern = r'\(|\)|\[|\]|{|}|\+|\-|\*|/|,|\.|[a-zA-Z_][a-zA-Z0-9_]*|\d+|\s+'
        tokens = re.findall(pattern, exp)
        t = BinaryTree.BinaryTree()
        current = t.r
        for token in tokens:
            if token == '(':
                current.left = BinaryTree.Node(token)
                current = current.left
            elif token in {'+', '-', '/', '*'}:
                current.set_value(token)
                current.set_key(token)
            elif token.isalnum:
                current.set_key(token)
                current.set_value(dict.find(token))
                current = current.parent
            elif token == ')':
                current = current.parent
        return t

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if root.left is not None and root.right is not None:
            op = root.k
            return op(self._evaluate(root.left), self.evaluate(root.right))
        elif root.left is None and root.right is None:
            if root.k is None:
                raise ValueError("Missing an operand")
            elif root.k in self.variables:
                return self.variables[root.k]
            else:
                raise ValueError(f"Missing definition for variable {root.k}")
        else:
            raise ValueError("Missing an operand")

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
