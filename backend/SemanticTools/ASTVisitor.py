########## ASTVisitor #########
# Base class for for the ASTTraverser stating how to "visit" each node
# Each visit has its own way of traversing a node
# vist() - uses getattr() of python to find the correct function that visits a specific node
# generic_visit() - visits the root node or the topmost in the tree. This prevents the compiler from cashing if no function has made for a node
# visit_children() - while a node has a children, it visits its children until to the leaf node

from SymbolTable import SymbolTable

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

########## ASTTraverser ##########
# Main component of the semantic analyzer
# It defines the meaning of the nodes by type checking
# Puhsing and popping variables to the symbol table and checks if a variable exists
# It determines the result of an expression

class ASTTraverser(ASTVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.errors = []
        self.unresolved = []