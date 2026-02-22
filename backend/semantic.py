from .SemanticTools import SymbolTable, ASTNodes, ASTVisitor

def semantic_analyze(tokens):
    symbol_table = SymbolTable()
