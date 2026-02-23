class ASTVisitor:
    def visit(self, node, parent=None):
        visitor = getattr(self, f'visit_{type(node).__name__}', self.generic_visit)
        return visitor(node, parent)
    
    def generic_visit(self, node, parent):
        if parent is None: 
            print(f'Visiting root node: {type(node).__name__}')

    def visit_children(self, node):
        for child in node.children:
            self.visit(child, node)

class ASTTraverser(ASTVisitor):
    pass