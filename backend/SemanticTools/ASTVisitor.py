########## ASTVisitor #########
# Base class for for the ASTTraverser stating how to "visit" each node
# Each visit has its own way of traversing a node
# vist() - uses getattr() of python to find the correct function that visits a specific node
# generic_visit() - visits the root node or the topmost in the tree. This prevents the compiler from cashing if no function has made for a node
# visit_children() - while a node has a children, it visits its children until to the leaf node
# If there are specific rules for a certain feature in the compiler (e.g. toint() only accepts other data type other than string with letters in it), their visit function woulld be longer
# Otherwise, it would just be visit_children(node) 

from ..Error import SemanticError
from .SymbolTable import SymbolTable
from .ASTNodes import (
    ASTNode, NumNode, StrLitNode, BoolLitNode, IdNode, BiArithNode, ExpoNode, RelNode, LogicNode, UnaryOperatorNode,
    UnaryNode, DataTypeNode, ConstNode, VoidNode, VarDecNode, AssignNode, MixLitNode, MixDecNode, MixIndxNode, MixIndxAssignNode,
    SpyceNode, ParamNode, MakeDecNode, FuncBodyNode, ArgsNode, FuncCallNode, SayNode, ListenNode, GivebackNode, WhenNode,
    ElsewhenNode, OtherwiseNode, ChooseNode, CaseNode, DefaultNode, ForLoopNode, ForHeaderNode, WhileNode, BreakNode,
    ContNode, ToStrNode, ToIntNode, ToFloatNode, ToBoolNode, TypeNode, LenNode, LowerNode, UpperNode, TruncNode
    )

""" NOTES FOR FUTURE SESSIONS
- Giveback should allow returning mix literals  (From Parser)
- No implementation of cases having indices     (From Parser)
- Returning integer recognizes it as float
"""

class ASTVisitor:
    def visit(self, node, parent=None):
        visitor = getattr(self, f'visit_{type(node).__name__}', self.generic_visit)
        return visitor(node, parent)
    
    def generic_visit(self, node, parent):
        if parent is None: 
            print(f'Visiting root node: {type(node).__name__}')
        self.visit_children(node)


    def visit_children(self, node):
        for child in node.children:
            self.visit(child, node)

########## ASTTraverser ##########
# Main component of the semantic analyzer
# It defines the meaning of the nodes by type checking
# Pushing and popping variables to the symbol table and checks if a variable exists
# It determines the result of an expression and checks of operands are possible to the expression

class ASTTraverser(ASTVisitor):
    def __init__(self, STable):
        self.STable = STable
        self.errors = []
        self.unresolved = []

    ##################
    # HELPER FUNCTIONS
    ##################
    # Returns the data type of a node
    def infer_type(self, node):
        if      isinstance(node, NumNode):                              return 'int' if isinstance(node.val, int) else 'float'
        elif    isinstance(node, StrLitNode):                           return 'string'
        elif    isinstance(node, (BoolLitNode, RelNode, LogicNode)):    return 'bool'
        elif    isinstance(node, UnaryNode):                            return self.infer_type(node.operand)
        elif    isinstance(node, ExpoNode):                             return 'float' if node.left == 'float' or node.right == 'float' else 'int'
        elif    isinstance(node, IdNode):                               return self.STable.get_type(node.name) if self.STable.get_name(node.name) else 'unknown'
        elif    isinstance(node, BiArithNode):
            if node.op in ['<', '>', '<=', '>=', '==', '!=', 'AND', 'OR', 'NOT']:   return 'bool'
        elif    isinstance(node, MixIndxNode):                          return self.STable.get_type(node.name)
        elif    isinstance(node, MixDecNode):                           return 'mix'
        elif    isinstance(node, FuncCallNode):
            func_node = self.STable.get_type(node.name)                         
            if isinstance(func_node, MakeDecNode):                      return func_node.ret
        elif    isinstance(node, ToIntNode):                            return 'int'
        elif    isinstance(node, ToFloatNode):                          return 'float'
        elif    isinstance(node, ToStrNode):                            return 'string'
        elif    isinstance(node, ToBoolNode):                           return 'bool'
        elif    isinstance(node, LenNode):                              return 'int'
        elif    isinstance(node, TypeNode):                             return 'type'
        elif    isinstance(node, UpperNode):                            return 'string'
        elif    isinstance(node, LowerNode):                            return 'string'
        elif    isinstance(node, TruncNode):                            return 'float'
        elif    isinstance(node, ListenNode):                           return 'string'

    # Evaluates expressions
    def eval_node(self, node):
        try:
            if isinstance(node, NumNode): 
                return node.value
            elif isinstance(node, BiArithNode): 
                left_val = self.eval_node(node.left)
                right_val = self.eval_node(node.right)
                try:
                    return eval(f'{left_val} {node.op} {right_val}')
                except:
                    return None
            elif isinstance(node, UnaryNode):
                if node.prefix and node.op.op == '-':
                    return -self.eval_node(node.operand)
                return None
            return None
        except:
            return None

    def resolve(self):
        pass
    
    ##################
    # VISIT FUNCTIONS
    ##################
    def visit_NumNode(self, node, parent):
        print(f'Visiting NumNode: {node.val}')
        self.visit_children(node)

    def visit_StrLitNode(self, node, parent):
        print(f'Visiting StrLitNode: {node.val}')
        self.visit_children(node)

    def visit_BoolLitNode(self, node, parent):
        print(f'Visiting BoolLitNode: {node.val}')
        self.visit_children(node)

    def visit_IdNode(self, node, parent):
        print(f'Visiting IdNode: {node.name}')
        if not self.STable.get(node.name) and not isinstance(parent, (FuncCallNode, MixIndxNode)):
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Variable "{node.name}" is not defined'))
        else:
            filtered_instance = (AssignNode, VarDecNode, FuncCallNode, MixIndxNode, MixIndxAssignNode, LenNode, GivebackNode, BiArithNode, ToIntNode, ToFloatNode, ToStrNode, ToBoolNode, TruncNode, UpperNode, LowerNode)
            id = self.STable.get(node.name)
            main_parent = parent
            while main_parent.parent and not isinstance(main_parent, filtered_instance):
                main_parent = main_parent.parent

                if isinstance(main_parent, filtered_instance):
                    if isinstance(id, MakeDecNode) and not isinstance(main_parent, FuncCallNode):
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Cannot call '{node.name}' without arguments"))
                    elif isinstance(id, MixDecNode) and not isinstance(main_parent, (MixIndxNode, MixIndxAssignNode, LenNode, ToIntNode, ToFloatNode, ToStrNode, ToBoolNode, TruncNode, UpperNode, LowerNode)):
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Cannot call '{node.name}' without specified index"))

    def visit_BiArithNode(self, node, parent):
        print(f'Visiting BiArithNode: {node.val}')
        self.visit_children(node)

        left_type = self.infer_type(node.left)
        right_type = self.infer_type(node.right)
        parent = parent
        op_type = self.infer_type(node)
        answer = None

        if left_type != right_type:
            if left_type == 'string' and right_type in ['int', 'float', 'bool']:
                self.errors.append(SemanticError(parent.pos_start, parent.pos_end, f'String cannot be added to other types'))
            elif left_type in ['int', 'float', 'bool'] and right_type == 'string':
                self.errors.append(SemanticError(parent.pos_start, parent.pos_end, f'String cannot be added to other types'))

        elif isinstance(node, BiArithNode):
            num_operand = ['int', 'float', 'true', 'false']
            if left_type in num_operand and right_type in num_operand:
                try:
                    answer = eval(f'{node.left.val} {node.op} {node.right.val}')
                except:
                    print('ERROR AT VISIT_BIARITHNODE')
                
                if answer == 0:
                    if isinstance(parent, BiArithNode) and parent.op == '/' and parent.right == node:
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))
            
            # If the operation is returned by a function
            if isinstance(parent, GivebackNode):
                func = parent.parent
                while not isinstance(func, MakeDecNode):
                    if func.parent:
                        func = func.parent
                    else:
                        break
                
                if isinstance(func, MakeDecNode) and func.ret != op_type: 
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Type Mismatch: Function {func.name} returns {func.ret}, but got {op_type}'))
            
            if node.op == '/':
                # If the right operand is a literal
                if isinstance(node.right, NumNode) and node.right.val == 0:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))

                # If the right operand is an id 
                elif isinstance(node.right, IdNode):
                    if self.STable.get(node.right.name):
                        id = self.STable.get(node.right.name)
                        if isinstance(id, VarDecNode) and isinstance(id.val, NumNode) and id.val.val == 0:
                            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))

                # If the right operand is a mix index    
                elif isinstance(node.right, MixIndxNode):
                    value = None

                    # Look up the mix in the symbol table
                    if self.STable.get(node.right.name):
                        id = self.STable.get(node.right.name)

                        if isinstance(id, MixDecNode):
                            size1 = id.size1
                            size2 = id.size2
                            indx1, indx2 = None

                            # If two brackets are used but the mix is only one dimension
                            if node.right.indx2 and not id.size2:
                                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Index Out of bounds: "{node.right.name}" is a one-dimension mix'))

                            # If one bracket is used but the mix is two dimenions
                            elif not node.right.indx2 and id.size2:
                                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Cannot use whole mix as an operand'))

                            # Evalute the first index access
                            try:    indx1 = self.eval_node(node.right.index1)
                            except: indx1 = None

                            # Evalute the second index access if provided
                            if node.right.indx2:
                                try:    indx2 = self.eval_node(node.righ.indx2)
                                except: indx2 = None
                            else: indx2 = None

                        if indx1 is not None and size1 is not None and (indx1 < 0 or indx1 >= self.size1):
                            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Index out of bounds'))
                        if indx2 is not None and size2 is not None and (indx2 < 0 or indx2 >= self.size1):
                            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Index out of bounds'))
                        if indx1 is not None and (indx2 is None or indx2 is not None):
                            if indx2 is None:
                                try:
                                    value = id.val.vals[indx1]
                                except IndexError:
                                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Index out of bounds'))
                            else:
                                value = id.val[indx1].vals[indx2]

                            if isinstance(value, NumNode) and value.val == 0:
                                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))
                            elif isinstance(value, IdNode) and isinstance(value.parent, BiArithNode):
                                id_symbol = self.STable.get(value.name)
                                if id_symbol:
                                    if isinstance(id_symbol, VarDecNode) and isinstance(id_symbol.val, NumNode) and id_symbol.val.val == 0:
                                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))
                            elif isinstance(value, BiArithNode):
                                value = self.eval_node(value)
                                if value == 0:
                                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))

                elif isinstance(node.right, FuncCallNode):
                    func_id = self.STable.get(node.right.name)
                    if func_id:
                        if isinstance(func_id, MakeDecNode):
                            if isinstance(func.id.ret, NumNode):
                                if func_id.ret == 0:
                                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Division by zero'))    

    def visit_ExpoNode(self, node, parent):
        print(f'Visiting ExpoNode')
        self.visit_children(node)

    def visit_RelNode(self, node, parent):
        print(f'Visiting RelNode: {node.op}')
        self.visit_children(node)

    def visit_LogicNode(self, node, parent):
        print(f'Visiting RelNode: {node.op}')
        self.visit_children(node)

    def visit_UnaryNode(self, node, parent):
        print(f'Visiting UnaryNode: {node.op.op}')
        self.visit_children(node)
        main_parent = parent

        while main_parent.parent and not isinstance(main_parent, GivebackNode):
            main_parent = main_parent.parent
        
        if node.op.op in ['++', '--']:
            if not isinstance(node.operand, IdNode):
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'{node.op.op} cannot be used to non-variables'))
            else:
                unary_id = self.STable.get(node.operand.name)
                if not unary_id:
                    pass
                elif unary_id and not isinstance(unary_id, VarDecNode) and not isinstance(main_parent, GivebackNode):
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'{node.op.op} cannot be used to non-variables'))
                elif unary_id.const:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Cannot modify constant variable {unary_id.name}'))

    def visit_DataTypeNode(self, node, parent):
        print(f'Visiting DataTypeNode: {node.datatype}')
        self.visit_children(node)

    def visit_VarDecNode(self, node, parent):
        print(f'Visiting VarDecnode: {node.datatype} {node.name}')

        if not self.STable.get_local(node.name):
            self.STable.set_local(node.name, node)
        else:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Variable '{node.name}' is already declared"))

        self.visit_children(node)

    def visit_AssignNode(self, node, parent): 
        print(f'Visiting AssignNode: {node.name}')
        self.visit_children(node)
        if self.STable.get(node.name):
            id = self.STable.get(node.name)
            if id.const:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Cannot modify constant variable {id.name}'))
            elif isinstance(id, MixDecNode):
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Cannot assign whole mix to {id.name}'))
            elif isinstance(id, MakeDecNode):
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Cannot whole function to {id.name}'))
            else:
                val_type = self.infer_type(node.val)
                var_type = self.STable.get_type(node.name)

                if var_type != val_type:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Unexpected -> {val_type} <-. Expected: {var_type}'))

    def visit_MixLitNode(self, node, parent):
        print(f'Visiting MixLitNode: {node.vals}')
        self.visit_children(node)
    
    def visit_MixDecNode(self, node, parent):
        print(f'Visiting MixDecNode: {node.name}')
        if self.STable.get(node.name):
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Variable '{node.name}' already declared"))
        else:
            self.STable.set(node.name, node)

        if not node.size1 and not node.size2 and not node.value.val:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix size must be greater than 0'))
        
        if node.size1:
            if self.infer_type(node.size1) not in ('int_lit', 'float_lit', 'true', 'false'):
                self.errors.append(SemanticError(node.size1.pos_start, node.size1.pos_end, f'A {self.infer_type(node.size1)} cannot be used for mix size declaration'))
            else:
                size1_val = self.eval_node(node.size1)

        if node.size2:
            if self.infer_type(node.size2) not in ('int_lit', 'float_lit', 'true', 'false'):
                self.errors.append(SemanticError(node.size2.pos_start, node.size2.pos_end, f'A {self.infer_type(node.size2)} cannot be used for mix size declaration'))
            else:
                size2_val = self.eval_node(node.size2)

        # Single-dimension mix
        if node.size1 and not node.size2:
            size1_val = self.eval_node(node.size1)
            if size1_val is not None:
                if not isinstance(node.val, MixLitNode):
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, "Invalid value to initialize mix"))
                elif size1_val <= 0:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix size must be greater than 0'))
                elif len(node.val.vals) > size1_val:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix overload, number of mix literals cannot be greater than the size decalared'))
                else:
                    while len(node.val.vals) < size1_val:
                        node.val.vals.append(NumNode(0))

        # 2-dimensional mix
        if node.size1 and node.size2:
            size1_val = self.eval_node(node.size1)
            size2_val = self.eval_node(node.size2)
            if size1_val is not None and size2_val is not None:
                if size1_val <= 0:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix size1 must be greater than 0'))
                elif size2_val <= 0:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix size2 must be greater than 0'))
                elif len(node.val) > size1_val:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix overload, number of mix literals cannot be greater than the size decalared'))
                for inner_node in node.val:
                    if not isinstance(inner_node, MixLitNode):
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, "Invalid value to initialize 2-dimensional mix"))
                    if len(inner_node.val) > size2_val:
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Mix overload, number of mix literals cannot be greater than the size decalared'))
                    else:
                        while len(inner_node.val) < size2_val:
                            inner_node.val.append(NumNode(0, None, None))
        self.visit_children(node)

    def visit_MixIndxNode(self, node, parent):
        print(f'Visiting MixIndxNode: {node.name}')
        symbol = self.STable.get(node.name)

        if symbol is None:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Mix {node.name} is not declared"))
        else:
            if isinstance(symbol, MixDecNode):
                pass
            elif isinstance(symbol, VarDecNode):
                if symbol.datatype != 'string':
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"{node.name} cannot does not support indexing"))
                elif symbol.datatype == 'string':
                    pass
            else:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f"{node.name} is not a string or mix"))
        
        if node.indx1:
            if isinstance(node.indx1, FuncCallNode) and not self.STable.get(node.indx1.name):
                self.unresolved.append((node.indx1, node)) # save to unresolved first if not read yet
            else:
                indx1_type = self.infer_type(node.indx1)
                if indx1_type not in ['int', 'float', 'bool', 'string']:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Invalid type used for mix index"))
                else:
                    pass

        if node.indx2:
            if isinstance(node.indx2, FuncCallNode) and not self.STable.get(node.indx2.name):
                self.unresolved.append((node.indx2, node)) # save to unresolved first if not read yet
            else:
                indx2_type = self.infer_type(node.indx2)
                if indx2_type not in ['int', 'float', 'bool', 'string']:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Invalid type used for mix index"))
                else:
                    pass
        
        if isinstance(symbol, MixDecNode):
            if node.index2 and not symbol.size2:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f"{node.name} is a 1-dimension mix only, unexpected 2nd pair of bracket"))
            
            size1_val = symbol.size1
            size2_val = symbol.size2
            indx1_val = self.eval_node(node.index1) if node.index1 else None
            indx2_val = self.eval_node(node.index2) if node.index2 else None
            
            if indx1_val and indx1_val < 0:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be a negative value"))
            elif indx1_val > size1_val:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be greater than the mix size"))
            
            if indx2_val and indx2_val < 0:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be a negative value"))
            elif indx2_val and size2_val:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be greater than the mix size"))
        self.visit_children(node)

    def visit_MixIndxAssignNode(self, node, parent): 
        print(f'Visiting MixIndxAssignNode')
        self.visit_children(node)
        symbol = self.STable.get(node.name)

        if not symbol:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'{node.name} is not declared'))
        else:
            if hasattr(symbol, 'const') and symbol.restrict:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Constant mix element cannot be modified'))
                pass

            if node.index1:
                if isinstance(symbol, FuncCallNode) and not self.STable.get(node.index1.name):
                    self.unresolved.append((node.index1, node))
                else:
                    indx1_type = self.infer_type(node.index1)
                    if indx1_type not in ['int', 'float', 'bool', 'string']:
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Invalid type used for mix index"))
                    else:
                        pass

            if node.index2:
                if isinstance(symbol, FuncCallNode) and not self.STable.get(node.index2.name):
                    self.unresolved.append((node.index2, node))
                else:
                    indx2_type = self.infer_type(node.index2)
                    if indx2_type not in ['int', 'float', 'bool', 'string']:
                        self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Invalid type used for mix index"))
                    else:
                        pass

            if isinstance(symbol, MixDecNode):
                if node.index2 and not symbol.size2:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"{node.name} is a 1-dimension mix only, unexpected 2nd pair of bracket"))

                size1_val = symbol.size1
                size2_val = symbol.size2
                indx1_val = self.eval_node(node.index1) if node.index1 else None
                indx2_val = self.eval_node(node.index2) if node.index2 else None
            
                if indx1_val and indx1_val < 0:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be a negative value"))
                elif indx1_val > size1_val:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be greater than the mix size"))
            
                if indx2_val and indx2_val < 0:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be a negative value"))
                elif indx2_val and size2_val:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Index cannot be greater than the mix size"))
            self.visit_children(node)

    def visit_SpyceNode(self, node, parent):
        print(f'Visiting SpyceNode')
        if self.STable.get('spyce'):
            self.errors.append(SemanticError(node.pos_start, node.pos_end, "Only one spyce function must be present"))
            return

        self.STable.set('spyce', node)
        self.STable.push()
        for child in list(node.children):
            if isinstance(child, MakeDecNode):
                if self.STable.get(child.name):
                    self.errors.append(SemanticError(child.pos_start, child.pos_end, f"Function '{child.name}' already declared in this scope"))
                else:
                    self.STable.set(child.name, child)
        self.visit_children(node)
        self.STable.pop()

    def visit_ParamNode(self, node, parent):
        print(f'Visiting ParamNode: {node.name}')
        if self.STable.get_local(node.name):
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Parameter '{node.name}' already declared"))
        else:
            self.symbol_table.set(node.name, node.datatype)
        self.visit_children(node)

    def visit_MakeDecNode(self, node, parent):
        print(f'Visiting MakeDecNode: {node.name}')
        if self.STable.get(node.name) and not isinstance(parent.parent, (MakeDecNode, SpyceNode)):
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Function '{node.name}' already declared"))
        else:
            self.STable.set(node.name, node)
        self.STable.push()
        self.visit_children(node)

        def check_ret(node):
            if isinstance(node, GivebackNode): return True
            if hasattr(node, 'children'): 
                for ch in node.children:
                    if check_ret(ch): return True
            return False
        
        if node.ret and node.ret != 'void':
            ret_flag = False

            cchild = node.body.children[:]
            for ch in cchild:
                if check_ret(ch):
                    ret_flag = True
                    break
        self.STable.pop()

    def visit_FuncBodyNode(self, node, parent):
        print(f'Visiting FuncBodyNode')
        self.STable.push()
        self.visit_children(node)

        for child in list(node.children):
            if isinstance(child, MakeDecNode):
                if self.STable.get(child.name):
                    self.errors.append(SemanticError(child.pos_start, child.pos_end, f"Function '{child.name}' already declared in this scope"))
                else:
                    self.STable.set(child.name, child)
        self.STable.pop()

    def visit_FuncCallNode(self, node, parent): 
        print(f'Visiting FuncCallNode')
        self.visit_children(node)
        symbol = self.STable.get(node.name)

        if symbol is None:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Function undefined'))
        else:
            if isinstance(symbol, MakeDecNode):
                if len(symbol.params) != len(node.args):
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Expected {len(symbol.params)} arguments for {node.name}, but got {len(node.args)}'))
            else:
                self.errors.append(SemanticError(node.pos_start, node.pos_end, f'{node.name} is not a function'))

    def visit_SayNode(self, node, parent):
        print(f'Visiting SayNode')
        self.visit_children(node)

    def visit_ListenNode(self, node, parent):
        print(f'Visiting ListenNode')
        self.visit_children(node)

    def visit_GivebackNode(self, node, parent): 
        print(f'Visiting GivebackNode')
        self.visit_children(node)
        main_parent = parent

        while main_parent and not isinstance(main_parent, (MakeDecNode, SpyceNode)):
            if main_parent: main_parent = main_parent.parent

        if isinstance(main_parent, MakeDecNode) and main_parent.ret != None:
            if isinstance(node.val, FuncCallNode):
                func_node = self.STable.get(node.value.name)
                func_ret = 'void' if func_node.ret is None else func_node.ret
                if main_parent.ret != func_ret:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Type Mismatch: Expected {main_parent.ret} but returns {func_ret}'))
            elif isinstance(node.val, MixIndxNode):
                pass
            elif isinstance(node.val, IdNode):
                pass
            elif isinstance(node.val, BiArithNode):
                pass
            else:
                func_ret = 'void' if self.infer_type(node.val) == 'None' else self.infer_type(node.val)
                if main_parent.ret != func_ret:
                    print(main_parent.ret)
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Type Mismatch: Expected {main_parent.ret} but returns {func_ret}')) 

        elif isinstance(main_parent, SpyceNode):
            if not isinstance(node.val, VoidNode):
                self.error.append(SemanticError(SemanticError(node.pos_start, node.pos_end, f'Unexpected: -> {node.val} <-Spyce function must only return void or none')))
            elif node.val is None:
                pass

        else:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Function must have return type'))

    def visit_WhenNode(self, node, parent): 
        print(f'Visiting WhenNode')
        self.visit_children(node)

    def visit_ElsewhenNode(self, node, parent): 
        print(f'Visiting ElsewhenNode')
        self.visit_children(node)

    def visit_OtherwiseNode(self, node, parent): 
        print(f'Visiting OtherwiseNode')
        self.visit_children(node)

    def visit_ChooseNode(self, node, parent):
        print(f'Visiting ChooseNode')
        self.visit_children(node)

    def visit_CaseNode(self, node, parent):
        print(f'Visiting CaseNode')
        self.visit_children(node)

        if isinstance(node.condition, IdNode):
            if self.STable.get(node.condition.name):
                cond_type = self.STable.get_type(node.condition.name)
                if cond_type in ['mix', 'void']:
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Cases cannot be of type {cond_type}'))
                else:
                    pass

    def visit_DefaultNode(self, node, parent):
        print(f'Visiting DefaultNode')
        self.visit_children(node)

    def visit_ForLoopNode(self, node, parent):
        print(f'Visiting ForLoopNode')
        self.STable.push()
        self.visit_children(node)
        self.STable.pop()

    def visit_ForHeaderNode(self, node, parent):
        print(f'Visiting ForHeaderNode')
        self.visit_children(node)

    def visit_WhileNode(self, node, parent):
        print(f'Visiting WhileNode')
        self.visit_children(node)

    def visit_BreakNode(self, node, parent): 
        print(f'Visiting BreakNode')
        self.visit_children(node)

    def visit_ContNode(self, node, parent): 
        print(f'Visiting ContNode')
        self.visit_children(node)

    def visit_ToIntNode(self, node, parent):
        print(f'Visiting ToIntNode')
        self.visit_children(node)
        arg = node.arg
        operand_type = self.infer_type(arg)

        # If argument is a mix
        if isinstance(arg, IdNode):
            symbol = self.STable.get(arg.name)
            if isinstance(symbol, MixDecNode):
                self.errors.append(SemanticError(node.pos_start, node.pos_end, "Cannot convert whole mix to integer"))
                return

        # If argument is a string not made up of numbers
        if operand_type == 'string':
            if isinstance(arg, StrLitNode):
                clean_val = arg.val.strip('"').strip("'")
                if not clean_val.lstrip('-').isdigit():
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Cannot convert non-numeric string '{clean_val}' to int"))
            else:
                pass

        # Valid arguments
        elif operand_type in ['int', 'float', 'bool']:
            pass

        else:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Cannot convert type '{operand_type}' to int"))

    def visit_ToFloatNode(self, node, parent):
        print(f'Visiting ToIntNode')
        self.visit_children(node)
        arg = node.arg
        operand_type = self.infer_type(arg)

        # If argument is a mix
        if isinstance(arg, IdNode):
            symbol = self.STable.get(arg.name)
            if isinstance(symbol, MixDecNode):
                self.errors.append(SemanticError(node.pos_start, node.pos_end, "Cannot convert whole mix to float"))
                return

        # If argument is a string not made up of numbers
        if operand_type == 'string':
            if isinstance(arg, StrLitNode):
                clean_val = arg.val.strip('"').strip("'")
                if not clean_val.lstrip('-').isdigit():
                    self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Cannot convert non-numeric string '{clean_val}' to float"))
            else:
                pass

        # Valid arguments
        elif operand_type in ['int', 'float', 'bool']:
            pass

        else:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f"Cannot convert type '{operand_type}' to float"))

    def visit_ToStrNode(self, node, parent):
        print(f'Visiting ToSTrNode')
        self.visit_children(node)

    def visit_ToBoolNode(self, node, parent):
        print(f'Visiting ToBoolNode')
        self.visit_children(node)

    def visit_LenNode(self, node, parent):
        print(f'Visiting LenNode')
        self.visit_children(node)
        arg = node.arg
        operand_type = self.infer_type(arg)

        if operand_type != 'string' and operand_type != 'mix':
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Invalid argument {arg.val} for len(). Only strings and mix are allowed'))
        else:
            pass

    def visit_TypeNode(self, node, parent):
        print(f'Visiting TypeNode')
        self.visit_children(node)

    def visit_UpperNode(self, node, parent):
        print(f'Visiting UpperNode')
        self.visit_children(node)
        arg = node.arg
        operand_type = self.infer_type(arg)

        if operand_type != 'string':
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Only string values accepted for function upper() function'))
        else:
            pass

    def visit_LowerNode(self, node, parent):
        print(f'Visiting LowerNode')
        self.visit_children(node)
        arg = node.arg
        operand_type = self.infer_type(arg)

        if operand_type != 'string':
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Only string values accepted for function lower() function'))
        else:
            pass

    def visit_TruncNode(self, node, parent): 
        print(f'Visiting TruncNode')
        self.visit_children(node)
        arg1 = node.val
        arg2 = node.dig

        if self.infer_type(arg1) not in ['int', 'float']:
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Only integer and float values allowed for first argument in trunc(number, int_lit)'))
        elif self.infer_type(arg2) != 'int':
            self.errors.append(SemanticError(node.pos_start, node.pos_end, f'Only integer values allowed for second argument in trunc(number, int_lit)'))
