class ToString:
    def __init__(self, x):
        self.s = str(x)
    def to_string(self):
        return self.s

int = float = bool = list = ToString

"""

"""

import builtins

# Test Case edits

class to_s(str):
    def to_string(self):
        return self.__str__()

class l_to_s(list):
    def to_string(self):
        return "["+",".join([str(i) for i in self])+"]"

builtins.int = to_s
builtins.float = to_s
builtins.bool = to_s
builtins.list = l_to_s
