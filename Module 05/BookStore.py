import ArrayStack
import BinaryTree
import ChainedHashTable
# import DLList
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
 
    def _build_parse_tree(self, exp: str) -> str:
        if not self.matched_expression(exp):
            raise ValueError("Expression contains unmatched parentheses")
        pattern = r'\(|\)|\[|\]|{|}|\+|\-|\*|/|,|\.|[a-zA-Z_][a-zA-Z0-9_]*|\d+|\s+'
        tokens = re.findall(pattern, exp)
        variables = [x for x in re.split(r'\W+', exp) if x.isalnum()]
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node()
        current = t.r
        for token in tokens:
            if token == '(':
                current.left = BinaryTree.BinaryTree.Node()
                current.left.parent = current
                current = current.left
            elif token in {'+', '-', '*', '/'}:
                current.set_val(token)
                current.set_key(token)
                current.right = BinaryTree.BinaryTree.Node()
                current.right.parent = current
                current = current.right
            elif token in variables:
                current.set_key(token)
                val = self.dict.find(token)
                if val is None:
                    raise ValueError(f"Missing value for variable '{token}'")
                current.set_val(val)
                current = current.parent
            elif token == ')':
                current = current.parent
            else:
                raise ValueError(f"{token} is an invalid token in the expression")
        return t
 
    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if root.left is not None and root.right is not None:
            operation = op[root.k]
            return operation(self._evaluate(root.left), self._evaluate(root.right))
        elif root.left is None and root.right is None:
            if root.k is None:
                raise ValueError("Missing an operand")
            value = self.dict.find(root.k)
            if value is not None:
                return value
            else:
                raise ValueError(f"Missing definition for variable {root.k}")
        else:
            raise ValueError("Missing an operand")
 
    def evaluate(self, exp):
        try:
            parseTree = self._build_parse_tree(exp)
        except ValueError:
            return "Error - Not all variable values are defined."
        else:
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
