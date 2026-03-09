########## CodeRunnner #########
# The code runner inherits from the ASTVisitor since both interpreter and semantic do the same thing
# The difference between interpreter and semantic:
#   Semantic - checks if the code written is semantically correct
#   Interpreter - runs the code it visits
# Both uses the ASTVistior to traverse through the built Abstract Tree Syntax

import threading, copy
from SemanticTools.ASTVisitor import ASTVisitor
from SemanticTools.ASTVisitor import ASTTraverser as trav
from .Error import SemanticError
from SemanticTools.ASTNodes import (
    NumNode, StrLitNode, BoolLitNode, IdNode, BiArithNode, ExpoNode, RelNode, LogicNode, UnaryOperatorNode,
    UnaryNode, DataTypeNode, ConstNode, VoidNode, VarDecNode, AssignNode, MixLitNode, MixDecNode, MixIndxNode, MixIndxAssignNode,
    SpyceNode, ParamNode, MakeDecNode, FuncBodyNode, ArgsNode, FuncCallNode, SayNode, ListenNode, GivebackNode, WhenNode,
    ElsewhenNode, OtherwiseNode, ChooseNode, CaseNode, DefaultNode, ForLoopNode, ForHeaderNode, WhileNode, BreakNode,
    ContNode, ToStrNode, ToIntNode, ToFloatNode, ToBoolNode, TypeNode, LenNode, LowerNode, UpperNode, TruncNode
)

class CodeRunner(ASTVisitor):
    def __init__(self, STable, socketio=None):
        self.STable = STable
        self.output = []
        self.error = None
        self.socketio = socketio
        self.input_events = {}
        self.input_values = {}
        self.current_node = None  
        self.current_parent = None  
        self.processed_listen_nodes = set()

    ##################
    # HELPER FUNCTIONS
    ##################
    def eval_node(self, node):
        if   isinstance(node, NumNode): return node.val, None
        elif isinstance(node, StrLitNode): return node.val, None
        elif isinstance(node, BoolLitNode): return node.val, None
        elif isinstance(node, IdNode): 
            symbol = self.STable.get(node.name)
            if symbol is None:
                return None, SemanticError(node.pos_start, node.pos_end, f"Variable '{node.name}' is already declared")

            if isinstance(symbol, VarDecNode):
                val, err = self.eval_node(symbol.val)
                if err: return None, err
            
            elif isinstance(symbol, MixDecNode):
                val = symbol.val
                if isinstance(val, MixLitNode):
                    val = val.vals

            return val, None

        elif isinstance(node, BiArithNode): 
            main_parent = node.parent
            while main_parent and hasattr(main_parent, 'parent'):
                pass

        elif    isinstance(node, UnaryNode): 
            if node.op.op == 'NOT' and node.prefix is True:
                self.eval_node(node.operand)
            return node.val, None
        elif    isinstance(node, StrLitNode): return node.val, None
        elif    isinstance(node, StrLitNode): return node.val, None
        elif    isinstance(node, StrLitNode): return node.val, None



    #################
    # VISIT FUNCTIONS
    #################
    def visit_NumNode(self, node, parent):
        print(f'Visiting NumNode: {node.val}')
        return node.val

    def visit_StrLitNode(self, node, parent):
        print(f'Visiting StrLitNode: {node.val}')
        return node.val

    def visit_BoolLitNode(self, node, parent):
        print(f'Visiting BoolLitNode: {node.val}')
        self.visit_children(node)

    def visit_IdNode(self, node, parent):
        print(f'Visiting IdNode: {node.name}')
        symbol = self.STable.get(node.name)
        if symbol is None:
            self.error = (SemanticError(node.pos_start, node.pos_end, f"Variable '{node.name}' is not defined"))
            return None
        if isinstance(symbol, VarDecNode):
            return symbol.val
        return None
    
    def visit_BiArithNode(self, node, parent):
        print(f'Visiting BiArithNode: {node.val}')
        self.visit_children(node)

    def visit_ExpoNode(self, node, parent):
        print(f'Visiting ExpoNode')

    def visit_RelNode(self, node, parent):
        print(f'Visiting RelNode: {node.op}')

    def visit_LogicNode(self, node, parent):
        print(f'Visiting RelNode: {node.op}')

    def visit_UnaryNode(self, node, parent):
        print(f'Visiting UnaryNode: {node.op.op}')
        if node.op.op in ['++', '--']:
            if not isinstance(node.operand, IdNode):
                self.error(SemanticError(node.pos_start, node.pos_end, f"{node.op.op} cannot be used to non-variables"))
                return None
            
            var_name = node.operand.name
            symbol = self.STable.get(var_name)
            
            if symbol is None:
                self.error = (SemanticError(node.pos_start, node.pos_end, f"Variable '{node.name}' is not defined"))
                return None
            
            current_val, err = self.eval_node(node.operand)
            if err:
                self.error = err
                return None

            new_val = current_val + 1 if node.op.op == '++' else current_val - 1
            val_node = NumNode(new_val, None, None)
            new_sym = VarDecNode(symbol.const, symbol.datatype, symbol.name, val_node, symbol.pos_start, symbol.pos_end)
            self.STable.set(var_name, new_sym)

            return new_val, None
        return self.eval_node(node)
    
    def visit_DataTypeNode(self, node, parent):
        print(f'Visiting DataTypeNode: {node.datatype}')
        self.visit_children(node)

    def visit_VarDecNode(self, node, parent):
        print(f'Visiting VarDecnode: {node.datatype} {node.name}')

        main_parent = parent
        while main_parent and not isinstance(main_parent, (SpyceNode, MakeDecNode)):
            main_parent = main_parent.parent

        if main_parent is None: pass
        else:
            dec_node = self.STable.get_local(node.name)
            if not dec_node and parent is not None:
                self.STable.set_local(node.name, node)
                dec_node = self.STable.get(node.name)
