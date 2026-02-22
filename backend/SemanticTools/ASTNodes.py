class ASTNode():
    def __init__(self, data, pos_start=None, pos_end=None):
        self.data = data
        self.children = []
        self.parent = None
        self.pos_start = pos_start
        self.pos_end = pos_end

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + 'ᴸ--' if self.parent else spaces
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()

    def tree_str(self):
        spaces = ' ' * self.getlevel() * 3
        prefix = spaces + 'ᴸ--' if self.parent else spaces
        result = prefix + self(self.data) + '\n'
        if self.children:
            for child in self.children:
                result += child.tree_str()
            return result
        
class NumNode():
    pass