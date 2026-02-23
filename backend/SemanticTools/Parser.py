########## PARSER ##########
# The Parser is responsible for using the AST Nodes to form the structure of the code
# Behaves like the syntax analyzer but it builds the Tree from the AST Nodes where the Traverser will traverse through
# It uses the symbol table 

from backend.LexerTools.Token import Token
from Error import ParseError
from SymbolTable import SymbolTable
from ASTNodes import (
    ASTNode, NumNode, StrLitNode, BoolLitNode, IdNode, BiArithNode, ExpoNode, RelNode, LogicNode, UnaryOperatorNode,
    UnaryNode, DataTypeNode, ConstNode, VoidNode, VarDecNode, AssignNode, MixLitNode, MixDecNode, MixIndxNode, MixIndxAssignNode,
    SpyceNode, ParamNode, MakeDecNode, FuncBodyNode, ArgsNode, FuncCallNode, SayNode, ListenNode, GivebackNode, WhenNode,
    ElsewhenNode, OtherwiseNode, ChooseNode, CaseNode, DefaultNode, ForLoopNode, ForHeaderNode, WhileNode, BreakNode,
    ContNode, StrNode, IntNode, FloatNode, BoolNode, TypeNode, LenNode, LowerNode, UpperNode, TruncNode
    )

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = 0
        self.current_token = tokens[self.current_token]
        self.semantic_errors = []
        self.symbol_table = SymbolTable()

    def advance(self):
        while True:
            self.token_idx += 1
            if self.token_idx < len(self.tokens):
                self.current_token = self.tokens[self.token_idx]
                if self.current_token.type not in ['\n', ' ', '\\n', 'space']:
                    break
            else:
                self.current_token = None
                break
        return self.current_token
    
    def reset(self):
        self.token_idx = -1
        self.advance()

    def look_ahead(self):
        current_idx = self.token_idx
        while True:
            current_idx += 1
            if current_idx < len(self.tokens):
                next_token = self.tokens[current_idx]
                if next_token.type not in ['\n', ' ', '\\n', 'space']:
                    return next_token
            else: return None
    
    ########## MAIN AST BUILDER FUNCTIONS ##########
    # Functions that builds the tree from tokens from the lexer
    # This is where the meaning of a statement is evaluated
    # Represents the logical structure of the program instead of syntax (e.g. requiring ; at the end of every statement)
    # For examples like int a = 5, b = 2, c = 3; it removes all the commas and symbols that are not needed for semantic check

    # Function that starts the building of the Tree
    def build_ast(self):
        errors = []
        self.reset()
        root = ASTNode('Program')

        while self.current_token is not None and self.current_token != 'EOF':
            if self.current_token is not None and self.current_token.type in ['const', 'int', 'float', 'string', 'bool', 'make', 'spyce']:
                dec, err = self.parseDeclaration()
                if dec:
                    if isinstance(dec, list):
                        for d in dec: root.add_child(d)
                    else:
                        root.add_child(dec)
                if err:
                    if isinstance(err, list):
                        for e in err: errors.extend(e)
                    else: 
                        errors.append(e)
            else: 
                self.advance()
        return root, errors
        
    # Function that puts the tokens read to its corresponding node from the ASTNodes
    # Parses all the possible operands to expressions and arguments to function calls
    def parseFactor(self):
        tkn = self.current_token

        # Numerical Value
        if tkn.type in ('int_lit', 'float_lit'):
            self.advance()
            if tkn.type in ('++', '--'):
                op = self.current_token
                pos_end = self.current_token.pos_end
                self.advance()
                return UnaryNode(op, NumNode(tkn.value, tkn.pos_start, tkn.pos_end), postfix=True, pos_start=tkn.pos_start, pos_end=pos_end), None
            return NumNode(tkn.value, tkn.pos_start, tkn.pos_end), None
        
        # String literal
        elif tkn.type == 'string_lit':
            self.advance()
            return StrLitNode(tkn.value, tkn.pos_start, tkn.pos_end), None
        
        # true
        elif tkn.type == 'true':
            self.advance()
            return BoolLitNode(tkn.value, tkn.pos_start, tkn.pos_end), None

        # false
        elif tkn.type == 'false':
            self.advance()
            return BoolLitNode(tkn.value, tkn.pos_start, tkn.pos_end), None
        
        # str
        elif tkn.type == 'str':
            self.advance()
            if self.current_token.type != '(':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            arg, err = self.parseExpr()
            if err: return None, err
            
            self.advance()
            if self.current_token != ')':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ) <-')
        
            return StrNode(arg, tkn.pos_start, self.current_token.pos_end), None
        
        # nested expression
        elif tkn.type == '(':
            pos_start = tkn.pos_start
            self.advance()
            expr, err = self.parseExpr()
            
            if err: return None, err

            if self.current_token.type == ')':
                self.advance()
                return expr, None
            else:
                return None, ParseError(tkn.pos_start, tkn.pos_end, f'Expected -> ) <-'), None

        # listen
        elif tkn.type == 'listen':
            self.advance()
            if self.current_token.type != '(':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            if self.current_token != ')':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ) <-')

            return ListenNode(tkn.type, tkn.pos_start, self.current_token.pos_end), None
        
        # Unary operation (prefix)
        elif tkn.type() in ('++', '--'):
            op = tkn
            self.advance()
            factor, err = self.parseFactor()
            if err: return None, err

            return UnaryNode(op, factor, pre=True, pos_start=op.pos_start, pos_end=op.pos_end), None
        
        # Should be added in operands #
        # NOT
        elif tkn.type() == 'NOT':
            op = tkn
            self.advance()
            factor, err = self.parseFactor()
            if err: return None, err

            return UnaryNode(op, factor, pre=True, pos_start=op.pos_start, pos_end=op.pos_end), None
        
        # Mix index access
        elif tkn.type() == 'id' and self.look_ahead().type == '[':
            pos_start = tkn.pos_start
            indx1, indx2 = None, None
            name = tkn.value
            self.advance()
            self.advance()

            indx1, err = self.parseExpr()
            if err: return None, err

            if self.current_token.type != ']':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ] <-')
            self.advance()

            if self.current_token.type == '[':
                self.advance()

                indx2, err = self.parseExpr()
                if err: return None, err

                if self.current_token.type != ']':
                    return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ] <-')
                self.advance()

            return MixIndxNode(name, indx1, indx2, pos_start, self.current_token.pos_end), None
        
        # Function call
        elif tkn.type == 'id' and self.look_ahead().type == '(':
            pos_start = tkn.pos_start
            name = tkn.value
            args = []
            self.advance()
            self.advance()
            
            while self.current_token.type != ')':
                arg, err = self.parseExpr()

                if err: return None, err
                args.append(arg)

                if self.current_token.type == ',':
                    while self.current_token.type == ',':
                        self.advance()
                        
                        arg, err = self.parseExpr()
                        if err: return None, err
                        args.append(arg)
            
            if self.current_token.type == ')':
                self.advance()
                return FuncCallNode(name, args, pos_start, pos_end), None
            else:
                self.advance()
                return None, ParseError(pos_start, pos_end, 'Expected: -> ) <-')
        
        # Compound assignment
        elif tkn.type == 'id' and self.look_ahead().type in ['+=', '-=', '*=', '/=', '%=', '**=']:
            pos_start = tkn.pos_start
            name = tkn.val
            op = None
            self.advance()
            if self.current_token.type == '+=': op = '+'
            elif self.current_token.type == '-=': op = '-'
            elif self.current_token.type == '*=': op = '*'
            elif self.current_token.type == '/=': op = '/'
            elif self.current_token.type == '%=': op = '%'
            self.advance()
            
            val, err = self.parseExpr()
            if err: return None, err

            left = IdNode(name, pos_start, self.current_token.pos_end)
            right = val
            arith_node = BiArithNode(left, Token(op, pos_start=left.pos_start, pos_end=right.pos_end), right)

            return AssignNode(name, arith_node, pos_start, self.current_token.pos_end), None
        
        # Unary oepration (postfix)
        elif tkn.type == 'id':
            pos_start = tkn.pos_start
            name = tkn.val
            self.advance()
            if self.current_token.type in ('++', '--'):
                op = self.current_token
                self.advance()
                return UnaryNode(op, IdNode(name, pos_start, tkn.pos_end), postfix=True, pos_start=pos_start, pos_end=tkn.pos_end), None
            
            # Id only
            return IdNode(name, pos_start, tkn.pos_end), None
        
        elif tkn.type == 'integer':
            self.advance()

            if self.current_token.type != '(':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            arg, err = self.parseExpr()
            if err: return None, err
            
            if self.current_token != ')':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ) <-')
        
            return IntNode(arg, tkn.pos_start, self.current_token.pos_end), None
        
        elif tkn.type == 'floating':
            self.advance()
            if self.current_token.type != '(':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            arg, err = self.parseExpr()
            if err: return None, err
            
            if self.current_token != ')':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ) <-')
        
            return FloatNode(arg, tkn.pos_start, self.current_token.pos_end), None
        
        elif tkn.type == 'bool':
            self.advance()
            if self.current_token.type != '(':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()
            
            arg, err = self.parseExpr()
            if err: return None, err
            
            if self.current_token != ')':
                return None, ParseError(tkn.pos_start, tkn.pos_end, 'Expected: -> ) <-')
        
            return BoolNode(arg, tkn.pos_start, self.current_token.pos_end), None
        
        elif tkn.type == 'len':
            pos_start = tkn.pos_start
            self.advance()

            if self.current_token.type != '(':
                return ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            len_val, err = self.parseExpr()
            if err: return None, err

            allowed_args = (IdNode, StrLitNode, MixLitNode, MixIndxNode)
            if not isinstance(len_val, allowed_args):
                return None, ParseError(len_val.pos_start, len_val.pos_end, f'Invalid argument -> {type(len_val.__repr__)} <- for len(). Only variables, string literals, mix literals, or mix indices')
            
            if self.current_token.type != ')':
                return ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ) <-')
            self.advance()

            return LenNode(len_val, tkn.pos_start, self.current_token.pos_end)
        
        elif tkn.type == 'lower':
            self.advance()
            if self.current_token.type != '(':
                return ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            lower_val, err = self.parseExpr()
            if err: return None, err

            if not isinstance(lower_val, (StrLitNode, IdNode, MixIndxNode)):
                return None, ParseError(lower_val.pos_start, lower_val.pos_end, f'Invalid argument for lower(). Only variables and string literals are allowed')

        elif tkn.type == 'upper':
            self.advance()
            if self.current_token.type != '(':
                return ParseError(tkn.pos_start, tkn.pos_end, 'Expected -> ( <-')
            self.advance()

            upper_val, err = self.parseExpr()
            if err: return None, err

            if not isinstance(upper_val, (StrLitNode, IdNode, MixIndxNode)):
                return None, ParseError(upper_val.pos_start, upper_val.pos_end, f'Invalid argument for upper(). Only variables and string literals are allowed')
            
        else:
            return None, ParseError(tkn.pos_start, tkn.pos_end, f'Unexpected -> {tkn.type} <-. Expected one of [int, float, string, identifier, "(", "++", "--", "-", "NOT"]')
    
    def parseExpr(self): return self.parseLog()    

    def parseLog(self): return self.parseBinArith(self.parseEq, ['AND', 'OR'], LogicNode)

    def parseEq(self): return self.parseBinArith(self.parseRel, ['==', '!='], RelNode)

    def parseRel(self): return self.parseBinArith(self.parseArith, ['<', '>', '<=', '>='], RelNode)

    def parseArith(self): return self.parseBinArith(self.parseTerm, ['+', '-'], BiArithNode)

    def parseTerm(self): return self.parseBinArith(self.parseExpo, ['*', '/', '%'], BiArithNode)

    def parseExpo(self): return self.parseBinArith(self.parseFactor, ['**'], ExpoNode)

    def parseBinArith(self, func, op, node): 
        pos_start = self.current_token.pos_start
        left, err = func()
        if err: return None, err

        while self.current_token.type in op:
            op = self.current_token
            self.advance()
            right, err = func()
            if err: return None, err

            left = node(left, op, right, pos_start, self.current_token.pos_end)
        
        return left, None

    def parseId(self):
        if self.current_token.type != 'id':
            return None, ParseError(self.current_token.pos_start, self.current_token.pos_end, f'Unexpected -> {self.current_token.type} <-. Expected: id')
        
        name = self.current_token.value
        pos_start = self.current_token.pos_start
        id_assign = ['=', '+=', '-=', '*=', '/=', '%=', '**=']
        id_unary = ['++', '--']

        expected_id = id_assign + id_unary + ['(', '[', ',', ';']

        self.advance()

        if self.current_token.type not in expected_id:
            return None, ParseError(self.current_token.pos_start, self.current_token.pos_end, f'Unexpected -> {self.current_token.type} <-. Expected: {expected_id}')

        elif self.current_token.type in id_assign:
            op = self.current_token.type
            self.advance()
            

    def parseDec(self): pass    