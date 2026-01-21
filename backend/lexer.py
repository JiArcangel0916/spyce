# Makes using letters easy instead of manually typing each
import string
from .Error import LexicalError

########## DEFINITIONS ##########
# From regular definitions
DIGITS = '0123456789'
ALPHABET = string.ascii_letters
ALPHADIG = DIGITS + ALPHABET
WHITESPACE = '\n '
ASCII =  ''.join(chr(i) for i in range (32, 127)) + '\n '
ARITH = '+-/*%'
RELATIONAL = '==!=><>=<='
OTHERSYMS = '({[]}),;:'
ESCAPE_SEQ = 'nt\'"\\'

########## DELIMITERS ##########
delim = {
    'arith_dlm':            set(WHITESPACE + ALPHADIG + '-' + '('  + '~'),
    'assignop_dlm':         set(WHITESPACE + ALPHADIG + '('  + '\'' + '"' + '-'  + '~'),
    'bool_dlm':             set(WHITESPACE + ';' + ',' + '}'+ ')' + '+' + '=' + '!' + '~'),
    'clcurlb_dlm':          set(WHITESPACE + ALPHABET + ';' + '}' + ')' + ',' + '~'),
    'cldoublequotes_dlm':   set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + '+' + ':' + '~'),
    'clparenth_dlm':        set(WHITESPACE + ARITH + RELATIONAL + ';' + ',' + ')' + '{' + ']' + '~'),
    'clquotes_dlm':         set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + ':' + '~'),
    'clsqrb_dlm':           set(WHITESPACE + ARITH + RELATIONAL + ',' + ';' + '=' + '[' + ')' + '~'),
    'cmpassignop_dlm':      set(WHITESPACE + ALPHADIG + '\'' + '"' + '-'  + '~'),
    'comb0_dlm':            set(WHITESPACE + '(' + '~'),
    'comb1_dlm':            set(WHITESPACE + '{' + '~'),
    'comb2_dlm':            set(WHITESPACE + ';' + '~'),
    'comb3_dlm':            set(ALPHADIG  + '~'),
    'comb4_dlm':            set(WHITESPACE + ':' + '~'),
    'comma_dlm':            set(WHITESPACE + ALPHADIG  + '\'' + '"' + '(' + '{' + '+' + '-' + '~'),
    'colon_dlm':            set(WHITESPACE + ALPHADIG + '\'' + '"' + '-'  + '+' + '-' + '~'),
    'dt_dlm':               set(WHITESPACE + '[' + '{' + '~'),
    'func_dlm':             set(WHITESPACE + ALPHADIG + '~'),
    'identifier_dlm':       set(WHITESPACE + ARITH + RELATIONAL + '(' + ')' + '[' + ']' + ',' + ';' + '{' + '}' + '=' + '~'),
    'int_lit_dlm':          set(WHITESPACE + ARITH + RELATIONAL + ')' + ',' + ';' + '}' + ']' + ':' + '~'),
    'lit_dlm':              set(WHITESPACE + ARITH + RELATIONAL + ':' + ';' + '}' + ')' + ',' + '~'),
    'minus_dlm':            set(WHITESPACE + ALPHADIG + '('  + '~'),
    'none_dlm':             set(WHITESPACE + ';' + ',' + '}' + ')' + '=' + '!' + '+' + '~'),
    'opcurlb_dlm':          set(WHITESPACE + ALPHADIG + '{' + '}' + '\'' + '"' + '-'  + '+' + '~'),
    'opparenth_dlm':        set(WHITESPACE + ALPHADIG + '-'  + '(' + ')' + '\'' + '"' + '{' + '+' + '~'),
    'opsqrb_dlm':           set(WHITESPACE + ALPHADIG + ']' + '+' + '(' + '~'),
    'relational_dlm':       set(WHITESPACE + ALPHADIG  + '~'),
    'unary_dlm':            set(WHITESPACE + ALPHABET  + ';' + ')' + '~'),
    'void_dlm':             set(WHITESPACE + '{' + ';' + '~')
}

########## RESERVED WORDS ##########
keywords = {
    'AND', 'NOT', 'OR', 'bool', 'break', 'case', 'char', 'choose',
    'const', 'continue', 'default', 'elsewhen', 'false', 'float',
    'for', 'giveback', 'int', 'listen', 'make', 'null', 'otherwise', 
    'say', 'skip', 'spyce', 'string', 'true', 'void', 'when', 'while'
}

########## TOKENS ##########
# KEYWORDS
# data types
TT_INT = 'int'
TT_FLOAT = 'float'
TT_STRING = 'string'
TT_CHAR = 'char'
TT_BOOL = 'bool'

# input and output
TT_SAY = 'say'
TT_LISTEN = 'listen'

# logical operators
TT_AND = 'AND'
TT_OR = 'OR'
TT_NOT = 'NOT'

# conditionals
TT_WHEN = 'when'
TT_ELSEWHEN = 'elsewhen'
TT_OTHERWISE = 'otherwise'
TT_CHOOSE = 'choose'
TT_CASE = 'case'
TT_DEFAULT = 'default'

# iteration
TT_FOR = 'for'
TT_WHILE = 'while'
TT_BREAK = 'break'
TT_SKIP = 'skip'
TT_CONTINUE = 'continue'

# others
TT_TRUE = 'true'
TT_FALSE = 'false'
TT_MAKE = 'make'
TT_SPYCE = 'spyce'
TT_CONST = 'const'
TT_VOID = 'void'
TT_GIVEBACK = 'giveback'
TT_NULL = 'null'

# RESERVED SYMBOLS
# arithmetic operators
TT_PLUS = '+'
TT_MINUS = '-'
TT_DIVIDE = '/'
TT_MULTIPLY = '*'
TT_POW = '**'
TT_MOD = '%'

# assignment operators
TT_ASSIGN = '='
TT_ADDASSIGN = '+='
TT_SUBASSIGN = '-='
TT_MULASSIGN = '*='
TT_DIVASSIGN = '/='
TT_MODASSIGN = '%='
TT_POWASSIGN = '**='

# relational operators
TT_EQUAL = '=='
TT_NOTEQ = '!='
TT_GREAT = '>'
TT_LESS = '<' 
TT_GREATEQ = '>='
TT_LESSEQ = '<='

# unary operator
TT_INC = '++'
TT_DEC = '--'

# others
TT_RETURN = '->'
TT_LCURL = '{'
TT_RCURL = '}'
TT_LPAREN = '('
TT_RPAREN = ')'
TT_LSQR = '['
TT_RSQR = ']'
TT_SEMICOLON = ';'
TT_COLON = ':'
TT_COMMA = ','

# LITERALS
TT_INTLIT = 'int_lit'
TT_FLOATLIT = 'float_lit'
TT_CHARLIT = 'char_lit'
TT_STRINGLIT = 'string_lit'
TT_COMMENTLIT = 'comment'

# IDENTIFIER
TT_IDENTIFIER = 'id'

TT_SPACE = 'space'
TT_NEWLINE = '\\n'

########## POSITION CLASS ##########
# used to track the location of the lexer in the source code
# idx = current index in the source code
# ln = line number in the code editor
# col = current column number in the line
# fullText = full source code
class Position:
    def __init__(self, idx, ln, col, fullText):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fullText = fullText
    
    # moves the lexer to the next character in the line
    def advance(self, current_char=None):
        self.idx += 1
        self.col += 1

        # if the next character is in the new line, reset col and inc ln and returns the position
        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    # copies current position to capture position
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fullText)
    
########## TOKEN CLASS ##########
class Token:
    def __init__(self, type, value = None, pos_start = None, pos_end = None):
        self.type = type
        self.value = value

        # if there are characters, set pos_start and pos_end to a copy of the position
        # advance the pos_end to simulate the end of a single character token
        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        
        # update pos_end
        if pos_end:
            self.pos_end = pos_end
    
    # string representation of the tokens
    def __repr__(self):
        if self.value:
            return f'{self.value}: {self.type}'
        return f'{self.type}'

########## MAIN LEXER CLASS ##########
class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = Position(0, 0, 0, source)

        if len(source) > 0:
            self.current_char = self.source[0]
        else:
            self.current_char = None

    # moves the position of the lexer to the next character
    def advance(self):
        self.pos.advance(self.current_char)

        # if lexer location is still within the source code, set current_char to the index
        if self.pos.idx < len(self.source):
            self.current_char = self.source[self.pos.idx]
        # otherwise, set the current_char to None, indicating EOF (end of file)
        else:
            self.current_char = None

    ########## MAIN TOKENIZER ALGORITHM ##########
    def tokenize(self):
        tokens = []     # where tokens generated will be stored
        errors = []     # where errors found will be stored
        states = []     # state tracking
        unique_id = 0   # counter for unique id in the source code

        while self.current_char is not None:
            ############### KEYWORD OR IDENTIFIER ###############
            if self.current_char in ALPHABET + '_':
                identifier_state = 277
                new_string = ''                 # where the next characters will be appended
                identifier_count = 0            # count if an identifier is greater than the limit
                pos_start = self.pos.copy()     # copy the position of the text
                match self.current_char:
                    # AND
                    case 'A':
                        states.append(1)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'N':
                            states.append(2)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'D':
                                states.append(3)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char is not None:
                                    if self.current_char in delim['comb0_dlm']:
                                        states.append(4)
                                        tokens.append(Token(TT_AND, new_string, pos_start, self.pos.copy()))
                                        continue
                                    elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                        pass
                                    elif self.current_char not in delim['comb0_dlm']:
                                        pos_end = self.pos.copy()
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                    # NOT
                    case 'N':
                        states.append(5)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'O':
                            states.append(6)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'T':
                                states.append(7)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char is not None:
                                    if self.current_char in delim['comb0_dlm']:
                                        states.append(8)
                                        tokens.append(Token(TT_NOT, new_string, pos_start, self.pos.copy()))
                                        continue
                                    elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                        pass
                                    elif self.current_char not in delim['comb0_dlm']:
                                        pos_end = self.pos.copy()
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                    # OR
                    case 'O':
                        states.append(9)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'R':
                            states.append(10)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char is not None:
                                if self.current_char in delim['comb0_dlm']:
                                    states.append(11)
                                    tokens.append(Token(TT_OR, new_string, pos_start, self.pos.copy()))
                                    continue
                                elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                    pass
                                elif self.current_char not in delim['comb0_dlm']:
                                    pos_end = self.pos.copy()
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                    continue
                    # b
                    case 'b':
                        states.append(12)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # bool
                            case 'o':
                                states.append(13)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'o':
                                    states.append(14)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        states.append(15)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in delim['dt_dlm']:
                                                states.append(16)
                                                tokens.append(Token(TT_BOOL, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['dt_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                continue
                            # break
                            case 'r':
                                states.append(17)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(18)    
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'a':
                                        states.append(19)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'k':
                                            states.append(20)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['comb2_dlm']:
                                                    states.append(21)
                                                    tokens.append(Token(TT_BREAK, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['comb2_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                    # c
                    case 'c':
                        states.append(22)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # case
                            case 'a':
                                states.append(23)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 's':
                                    states.append(24)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        states.append(25)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in WHITESPACE:
                                                states.append(26)
                                                tokens.append(Token(TT_CASE, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in WHITESPACE:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after  "{new_string}"'))
                                                continue
                            # h
                            case 'h':
                                states.append(27)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                match self.current_char:
                                    # char
                                    case 'a':
                                        states.append(28)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'r':
                                            states.append(29)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['dt_dlm']:
                                                    states.append(30)
                                                    tokens.append(Token(TT_CHAR, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['dt_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                                    # choose
                                    case 'o':
                                        states.append(31)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'o':
                                            states.append(32)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 's':
                                                states.append(33)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'e':
                                                    states.append(34)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char is not None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            states.append(35)
                                                            tokens.append(Token(TT_CHOOSE, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                            continue
                            # o
                            case 'o':
                                states.append(36)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                # n
                                if self.current_char == 'n':
                                    states.append(37)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    match self.current_char:
                                        # const
                                        case 's':
                                            states.append(38)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 't':
                                                states.append(39)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char is not None:
                                                    if self.current_char in WHITESPACE:
                                                        states.append(40)
                                                        tokens.append(Token(TT_CONST, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in WHITESPACE:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                        continue
                                        # continue
                                        case 't':
                                            states.append(41)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'i':
                                                states.append(42)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'n':
                                                    states.append(43)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'u':
                                                        states.append(44)
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char == 'e':
                                                            states.append(45)
                                                            new_string += self.current_char
                                                            identifier_count += 1
                                                            self.advance()
                                                            if self.current_char is not None:
                                                                if self.current_char in delim['comb2_dlm']:
                                                                    states.append(46)
                                                                    tokens.append(Token(TT_CONTINUE, new_string, pos_start, self.pos.copy()))
                                                                    continue
                                                                elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                                    pass
                                                                elif self.current_char not in delim['comb2_dlm']:
                                                                    pos_end = self.pos.copy()
                                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                                    continue              
                    # default
                    case 'd':
                        states.append(47)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'e':
                            states.append(48)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'f':
                                states.append(49)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'a':
                                    states.append(50)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'u':
                                        states.append(51)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'l':
                                            states.append(52)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 't':
                                                states.append(53)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char is not None:
                                                    if self.current_char in delim['comb4_dlm']:
                                                        states.append(54)
                                                        tokens.append(Token(TT_DEFAULT, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in delim['comb4_dlm'] and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in delim['comb4_dlm']:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                        continue
                    # elsewhen
                    case 'e':
                        states.append(55)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'l':
                            states.append(56)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 's':
                                states.append(57)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(58)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'w':
                                        states.append(59)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'h':
                                            states.append(60)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'e':
                                                states.append(61)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'n':
                                                    states.append(62)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char is not None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            states.append(63)
                                                            tokens.append(Token(TT_ELSEWHEN, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                            continue
                    # f
                    case 'f':
                        states.append(64)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # false
                            case 'a':
                                states.append(65)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'l':
                                    states.append(66)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 's':
                                        states.append(67)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            states.append(68)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['bool_dlm']:
                                                    states.append(69)
                                                    tokens.append(Token(TT_FALSE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['bool_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['bool_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                            # float
                            case 'l':
                                states.append(70)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'o':
                                    states.append(71)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'a':
                                        states.append(72)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 't':
                                            states.append(73)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['dt_dlm']:
                                                    states.append(74)
                                                    tokens.append(Token(TT_FLOAT, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['dt_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                            # for
                            case 'o':
                                states.append(75)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'r':
                                    states.append(76)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['comb0_dlm']:
                                            states.append(77)
                                            tokens.append(Token(TT_FOR, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['comb0_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                    # giveback
                    case 'g':
                        states.append(78)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'i':
                            states.append(79)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'v':
                                states.append(80)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(81)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'b':
                                        states.append(82)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'a':
                                            states.append(83)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'c':
                                                states.append(84)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'k':
                                                    states.append(85)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char is not None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            states.append(86)
                                                            tokens.append(Token(TT_GIVEBACK, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                            continue
                    # int
                    case 'i':
                        states.append(87)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'n':
                            states.append(88)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 't':
                                states.append(89)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char is not None:
                                    if self.current_char in delim['dt_dlm']:
                                        states.append(90)
                                        tokens.append(Token(TT_INT, new_string, pos_start, self.pos.copy()))
                                        continue
                                    elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                        pass
                                    elif self.current_char not in delim['dt_dlm']:
                                        pos_end = self.pos.copy()
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                    # listen
                    case 'l':
                        states.append(91)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'i':
                            states.append(92)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 's':
                                states.append(93)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 't':
                                    states.append(94)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        states.append(95)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'n':
                                            states.append(96)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char == '(':
                                                    states.append(97)
                                                    tokens.append(Token(TT_LISTEN, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char != '(':
                                                    pos_end = self.pos.copy()
                                                    if self.current_char == '\n':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after "{new_string}"'))
                                                    elif self.current_char == ' ':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "space" after "{new_string}"'))
                                                    else:
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                    # make
                    case 'm':
                        states.append(98)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'a':
                            states.append(99)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'k':
                                states.append(100)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(101)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in WHITESPACE:
                                            states.append(102)
                                            tokens.append(Token(TT_MAKE, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in WHITESPACE:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                    # none
                    case 'n':
                        states.append(103)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'u':
                            states.append(104)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'l':
                                states.append(105)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'l':
                                    states.append(106)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['none_dlm']:
                                            states.append(107)
                                            tokens.append(Token(TT_NULL, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['none_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['none_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                    # otherwise
                    case 'o':
                        states.append(108)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 't':
                            states.append(109)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'h':
                                states.append(110)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(111)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'r':
                                        states.append(112)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'w':
                                            states.append(113)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'i':
                                                states.append(114)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 's':
                                                    states.append(115)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'e':
                                                        states.append(116)
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char is not None:
                                                            if self.current_char in delim['comb1_dlm']:
                                                                states.append(117)
                                                                tokens.append(Token(TT_OTHERWISE, new_string, pos_start, self.pos.copy()))
                                                                continue
                                                            elif self.current_char not in delim['comb1_dlm'] and self.current_char in delim['comb3_dlm']:
                                                                pass
                                                            elif self.current_char not in delim['comb1_dlm']:
                                                                pos_end = self.pos.copy()
                                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                            continue
                    # s
                    case 's':
                        states.append(118)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # say
                            case 'a':
                                states.append(119)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'y':
                                    states.append(120)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char == '(':
                                            states.append(121)
                                            tokens.append(Token(TT_SAY, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char != '(':
                                            pos_end = self.pos.copy()
                                            if self.current_char == '\n':
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after "{new_string}"'))
                                            elif self.current_char == ' ':
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "space" after "{new_string}"'))
                                            else:
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                            # skip
                            case 'k':
                                states.append(122)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'i':
                                    states.append(123)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'p':
                                        states.append(124)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in delim['comb2_dlm']:
                                                states.append(125)
                                                tokens.append(Token(TT_SKIP, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['comb2_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                continue
                            # spyce
                            case 'p':
                                states.append(126)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'y':
                                    states.append(127)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'c':
                                        states.append(128)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            states.append(129)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char == '(':
                                                    states.append(130)
                                                    tokens.append(Token(TT_SPYCE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char != '(':
                                                    pos_end = self.pos.copy()
                                                    if self.current_char == '\n':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after "{new_string}"'))
                                                    elif self.current_char == '\t':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "space" after "{new_string}"'))
                                                    else:
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                            # string
                            case 't':
                                states.append(131)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'r':
                                    states.append(132)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'i':
                                        states.append(133)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'n':
                                            states.append(134)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'g':
                                                states.append(135)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char is not None:
                                                    if self.current_char in delim['dt_dlm']:
                                                        states.append(136)
                                                        tokens.append(Token(TT_STRING, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in delim['dt_dlm']:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                        continue
                    # true
                    case 't':
                        states.append(137)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'r':
                            states.append(138)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'u':
                                states.append(139)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(140)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['bool_dlm']:
                                            states.append(141)
                                            tokens.append(Token(TT_TRUE, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['bool_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['bool_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                    # void
                    case 'v':
                        states.append(142)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'o':
                            states.append(143)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'i':
                                states.append(144)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'd':
                                    states.append(145)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['void_dlm']:
                                            states.append(146)
                                            tokens.append(Token(TT_VOID, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['void_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['void_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                    # w
                    case 'w':
                        states.append(147)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        # h
                        if self.current_char == 'h':
                            states.append(148)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            match self.current_char:
                                # when
                                case 'e':
                                    states.append(149)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'n':
                                        states.append(150)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in delim['comb0_dlm']:
                                                states.append(151)
                                                tokens.append(Token(TT_WHEN, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['comb0_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                continue
                                # while
                                case 'i':
                                    states.append(152)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        states.append(153)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            states.append(154)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['comb0_dlm']:
                                                    states.append(155)
                                                    tokens.append(Token(TT_WHILE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['comb0_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                                    continue
                # Identifier  ### TEMPORARY FIX ###
                while identifier_count == 0 and self.current_char == '_':
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character -> {self.current_char} <-'))
                    self.advance()
                    while self.current_char == ' ':
                        self.advance()
        
                while self.current_char is not None and self.current_char in ALPHADIG + '_' and identifier_count < 25:
                    states.append(identifier_state)
                    new_string += self.current_char
                    identifier_count += 1
                    identifier_state += 1
                    self.advance()
                
                pos_end = self.pos.copy()
                if self.current_char is not None and new_string in keywords:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Keyword "{new_string}" cannot be used as identifier'))
                    continue
                elif self.current_char is not None and self.current_char in ALPHADIG + '_' and identifier_count == 25:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}". Exceeding maximum identifier length of 25 characters.'))
                    continue
                elif self.current_char is None or self.current_char not in delim['identifier_dlm']:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                    continue
                else:
                    found = False
                    for t in tokens:
                        # If the same identifier is read, input the same token
                        if t.value == new_string:
                            found = True
                            tokens.append(Token(t.type, new_string, pos_start, pos_end))
                            break
                    # If a new identifier is read, concatenate a counter for the token
                    if not found:
                        unique_id += 1
                        tokens.append(Token(f'{TT_IDENTIFIER}', new_string, pos_start, pos_end))
                
            ############### AN ARITHMETIC AND RELATIONAL SYMBOL ###############
            elif self.current_char in ARITH + RELATIONAL:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    # +
                    case '+':
                        states.append(156)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(157)
                            tokens.append(Token(TT_PLUS, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char not in delim['assignop_dlm']:
                            match self.current_char:
                                # ++
                                case '+':
                                    states.append(158)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['unary_dlm']:
                                        states.append(159)
                                        tokens.append(Token(TT_INC, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                                # +=
                                case '=':
                                    states.append(160)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                        states.append(161)
                                        tokens.append(Token(TT_ADDASSIGN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                                case _:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                    continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue     
                    # - 
                    case '-':
                        states.append(162)
                        num_lit_state = 220
                        decimal_state = 258
                        new_string += self.current_char
                        self.advance()
                        # If negative int
                        if self.current_char in DIGITS:
                            states.clear()
                            states.append(num_lit_state)
                            int_count = 0
                            decimal_count = 0
                            number_lit = ''
                            number_lit += self.current_char
                            int_count += 1
                            self.advance()
                            while self.current_char is not None and self.current_char in DIGITS and self.current_char != '.' and int_count < 19:
                                int_count += 1
                                num_lit_state += 1
                                states.append(num_lit_state)
                                number_lit += self.current_char
                                self.advance()
                            pos_end = self.pos.copy()

                            # If a . is found; float value
                            if self.current_char == '.':
                                states.append(decimal_state)
                                number_lit += self.current_char
                                self.advance()
                                if self.current_char is None or self.current_char not in DIGITS:
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "." after value "{new_string[:-1]}"'))
                                    continue

                                while self.current_char is not None and self.current_char in DIGITS and decimal_count < 5:
                                    decimal_count += 1
                                    decimal_state += 1 
                                    states.append(decimal_state)
                                    number_lit += self.current_char
                                    self.advance()
                                pos_end = self.pos.copy()

                                if self.current_char is not None and self.current_char in delim['lit_dlm']:
                                    states.append(decimal_state)
                                    num_parts = number_lit.split('.')               # split whole value to two parts <integer>.<float>
                                    int_part = num_parts[0].lstrip('0') or '0'      # strip leading 0 except 1 for integer
                                    float_part = num_parts[1].rstrip('0') or '0'    # strip trailing 0 except 1 for float
                                    digit_val = f'{int_part}.{float_part}'
                                    new_string += digit_val
                                    if new_string == '-0.0':
                                        new_string = '0.0'
                                        tokens.append(Token(TT_FLOATLIT, new_string, pos_start, pos_end))
                                        continue
                                    else:
                                        tokens.append(Token(TT_FLOATLIT, new_string, pos_start, pos_end))
                                        continue
                                elif self.current_char is not None and self.current_char in DIGITS:
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}". Exceeding maximum number of decimal values of 5 digits'))
                                    continue
                                else:
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                    continue
                            # If only integers
                            elif self.current_char is not None and self.current_char in delim['int_lit_dlm']:
                                states.append(num_lit_state)
                                digit_val = number_lit.lstrip('0') or '0'           # strip leading 0 except 1
                                new_string += digit_val
                                if new_string == '-0':
                                    new_string = '0'
                                    tokens.append(Token(TT_INTLIT, new_string, pos_start, pos_end))
                                    continue
                                else:
                                    tokens.append(Token(TT_INTLIT, new_string, pos_start, pos_end))
                                    continue
                            elif self.current_char is not None and self.current_char in DIGITS:
                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}". Exceeding maximum number of 19 digits for integers'))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue
                        elif self.current_char is not None and self.current_char in delim['minus_dlm']:
                            states.append(248)
                            tokens.append(Token(TT_MINUS, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char not in delim['minus_dlm']:
                            match self.current_char:
                                # --
                                case '-':
                                    states.append(164)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['unary_dlm']:
                                            states.append(165)
                                            tokens.append(Token(TT_DEC, new_string, pos_start, self.pos.copy()))
                                            continue
                                        else:
                                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                                    # -=
                                case '=':
                                    states.append(166)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                        states.append(167)
                                        tokens.append(Token(TT_SUBASSIGN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                                # ->
                                case '>':
                                    states.append(168)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['func_dlm']:
                                        states.append(169)
                                        tokens.append(Token(TT_RETURN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                                case _:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                    continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # *
                    case '*':
                        states.append(170)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['arith_dlm']:
                            states.append(171)
                            tokens.append(Token(TT_MULTIPLY, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char not in delim['arith_dlm']:
                            match self.current_char:
                                # **
                                case '*':
                                    states.append(172)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['arith_dlm']:
                                        states.append(173)
                                        tokens.append(Token(TT_POW, new_string, pos_start, self.pos.copy()))
                                        continue
                                    # **=
                                    elif self.current_char == '=':
                                        states.append(174)
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                            states.append(175)
                                            tokens.append(Token(TT_POWASSIGN, new_string, pos_start, self.pos.copy()))
                                            continue
                                        else:
                                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                            continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                                # *=
                                case '=':
                                    states.append(176)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                        states.append(177)
                                        tokens.append(Token(TT_MULASSIGN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                        continue
                                case _:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                    continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue 
                    # /
                    case '/':
                        states.append(178)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['arith_dlm']:
                            states.append(179)
                            tokens.append(Token(TT_DIVIDE, new_string, pos_start, self.pos.copy()))
                            continue
                        # /=
                        elif self.current_char == '=':
                            states.append(180)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                states.append(181)
                                tokens.append(Token(TT_DIVASSIGN, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue 
                    # %
                    case '%':
                        states.append(182)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['arith_dlm']:
                            states.append(183)
                            tokens.append(Token(TT_MOD, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char == '=':
                            states.append(184)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                states.append(185)
                                tokens.append(Token(TT_MODASSIGN, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue  
                    # =
                    case '=':
                        states.append(186)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(187)
                            tokens.append(Token(TT_ASSIGN, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char == '=':
                            states.append(188)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(189)
                                tokens.append(Token(TT_EQUAL, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # !
                    case '!':
                        states.append(190)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char == '=':
                            states.append(191)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(192)
                                tokens.append(Token(TT_NOTEQ, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Character -> {new_string} <-'))
                            continue
                    # >
                    case '>':
                        states.append(193)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(194)
                            tokens.append(Token(TT_GREAT, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char == '=':
                            states.append(195)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(196)
                                tokens.append(Token(TT_GREATEQ, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # <
                    case '<':
                        states.append(197)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(198)
                            tokens.append(Token(TT_LESS, new_string, pos_start, self.pos.copy()))
                            continue
                        # <=
                        elif self.current_char == '=':
                            states.append(199)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(200)
                                tokens.append(Token(TT_LESSEQ, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
            
            ############### OTHER SYMBOLS (()[]{},:;) ###############
            elif self.current_char in OTHERSYMS:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    # (
                    case '(':
                        states.append(201)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['opparenth_dlm']:
                            states.append(202)
                            tokens.append(Token(TT_LPAREN, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # )
                    case ')':
                        states.append(203)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['clparenth_dlm']:
                            states.append(204)
                            tokens.append(Token(TT_RPAREN, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # {
                    case '{':
                        states.append(205)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['opcurlb_dlm']:
                            states.append(206)
                            tokens.append(Token(TT_LCURL, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # }
                    case '}':
                        states.append(207)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is None or self.current_char in delim['clcurlb_dlm']:
                            states.append(208)
                            tokens.append(Token(TT_RCURL, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # [
                    case '[':
                        states.append(209)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['opsqrb_dlm']:
                            states.append(210)
                            tokens.append(Token(TT_LSQR, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # ]
                    case ']':
                        states.append(211)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['clsqrb_dlm']:
                            states.append(212)
                            tokens.append(Token(TT_RSQR, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # :
                    case ':':
                        states.append(213)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in WHITESPACE:
                            states.append(214)
                            tokens.append(Token(TT_COLON, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # ,
                    case ',':
                        states.append(215)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['comma_dlm']:
                            states.append(216)
                            tokens.append(Token(TT_COMMA, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                            continue
                    # ;
                    case ';':
                        states.append(217)
                        new_string += self.current_char
                        tokens.append(Token(TT_SEMICOLON, new_string, pos_start, self.pos.copy()))
                        self.advance()
                        continue

            ############### INT AND FLOAT LITERALS ###############
            # If literal starts with a number
            elif self.current_char in DIGITS:
                decimal_state = 259
                num_lit_state = 221
                states.append(num_lit_state)
                new_string = ''
                int_count = 0
                decimal_count = 0
                pos_start = self.pos.copy()
                new_string += self.current_char

                # If the current character is a non-zero, set a flag
                has_non_zero = self.current_char != '0'
                if has_non_zero:            
                    int_count += 1
                self.advance()

                # Collect all digits
                while self.current_char is not None and self.current_char in DIGITS and self.current_char != '.' and int_count < 19:            
                    new_string += self.current_char
                    # If this digit or the starting digit is a non-zero, start counting
                    if self.current_char != '0' or has_non_zero:
                        has_non_zero = True
                        int_count += 1
                        num_lit_state += 1
                        states.append(num_lit_state)
                    self.advance()
                pos_end = self.pos.copy()

                # If a . is found; float value
                if self.current_char == '.':
                    states.append(decimal_state)
                    new_string += self.current_char
                    self.advance()
                    if self.current_char is None or self.current_char not in DIGITS:            
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "." after value "{new_string[:-1]}"'))
                        continue

                    while self.current_char is not None and self.current_char in DIGITS and (decimal_count < 5 or self.current_char == '0'):
                        decimal_count += 1
                        decimal_state += 1
                        states.append(decimal_state)
                        new_string += self.current_char
                        self.advance()
                    pos_end = self.pos.copy()

                    if self.current_char is not None and self.current_char in delim['lit_dlm']:
                        states.append(decimal_state)
                        num_parts = new_string.split('.')               # split whole value to two parts <integer>.<float>
                        int_part = num_parts[0].lstrip('0') or '0'      # strip leading 0 except 1 for integer
                        float_part = num_parts[1].rstrip('0') or '0'    # strip trailing 0 except 1 for float

                        # Check if decimal digits do not exceed 5
                        if len(float_part) > 5:
                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid number of significant decimal digits in "{new_string}". Maximum is 5.'))
                            continue
                        digit_val = f'{int_part}.{float_part}'
                        tokens.append(Token(TT_FLOATLIT, digit_val, pos_start, pos_end))
                        continue
                    elif self.current_char is not None and self.current_char in DIGITS:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}". Exceeding maximum number of significant decimal digits of 5'))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                        continue

                # If only integers
                elif self.current_char is not None and self.current_char in delim['int_lit_dlm']:
                    states.append(num_lit_state)
                    digit_val = new_string.lstrip('0') or '0'           # strip leading 0 except 1 
                    tokens.append(Token(TT_INTLIT, digit_val, pos_start, pos_end))
                    continue
                elif self.current_char is not None and self.current_char in DIGITS:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}". Exceeding maximum number of significant digits for integers'))
                    continue
                else:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter -> {self.current_char} <- after "{new_string}"'))
                    continue

            ############### CHAR LITERAL ##############
            elif self.current_char == '\'':
                states.append(270)
                pos_start = self.pos.copy()
                char_val = ''
                char_val += self.current_char           
                char_count = 0
                withNonAscii = False
                self.advance()

                # empty char literal
                if self.current_char == '\'':
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Char values must at least have 1 character stored'))
                    self.advance()
                    continue

                # valid char literal
                else:
                    states.append(271)
                    while self.current_char is not None and self.current_char != '\'':
                        char_count += 1
                        char_val += self.current_char
                        self.advance()
                    if self.current_char == '\'':
                        states.append(272)
                        char_val += self.current_char
                        self.advance()
                        pos_end = self.pos.copy()

                        # check each if literal contains non ASCII
                        for i in char_val.replace(' ', ''):
                            if i not in ASCII + WHITESPACE:
                                withNonAscii = True 
                                break
                        if withNonAscii:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Char values must only be ASCII values: {char_val}'))
                            continue    

                        # if more than one character is inside
                        if char_count > 1:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Char values can only store 1 character. Char value: {char_val}'))
                            continue
                        else:
                            if self.current_char is not None and self.current_char in delim['clquotes_dlm']:
                                states.append(273)
                                tokens.append(Token(TT_CHARLIT, char_val, pos_start, pos_end))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after {char_val}'))
                                continue

                    # if char is not closed
                    else:
                        pos_end = self.pos.copy()
                        errors.append(LexicalError(pos_start, pos_end, info=f'Char not closed: {char_val}'))
                        continue

            ############### STRING LITERAL ###############
            elif self.current_char == '"':
                states.append(274)
                pos_start = self.pos.copy()
                string_val = ''
                escape_seq = ''
                string_val += self.current_char
                withNonAscii = False
                self.advance()

                while self.current_char is not None and self.current_char != '"':
                    if self.current_char == '\\':
                        escape_seq += self.current_char
                        self.advance()
                        if self.current_char is None or self.current_char not in ESCAPE_SEQ:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character -> {self.current_char} <- after \\. "\\{self.current_char}" is an unknown escape sequence'))
                            continue
                        else:
                            escape_seq += self.current_char
                            string_val += escape_seq
                            escape_seq = '' 
                            self.advance()
                            continue
                    
                    if self.current_char == '\n':
                        string_val += ' '
                        self.advance()
                        continue
                    
                    string_val += self.current_char
                    self.advance()

                if self.current_char == '"':
                    states.append(275)
                    string_val += self.current_char
                    self.advance()
                    pos_end = self.pos.copy()
                    
                    # check if all characters are in ASCII
                    for i in string_val.replace(' ', ''):
                        if i not in ASCII:
                            withNonAscii = True
                            break
                    if withNonAscii:
                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'String values must only be ASCII values: {string_val}'))
                        continue
                    # if valid string
                    if self.current_char is not None and self.current_char in delim['cldoublequotes_dlm']:
                        states.append(276)
                        tokens.append(Token(TT_STRINGLIT, string_val, pos_start, pos_end))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter -> {self.current_char} <- after {string_val}'))
                        continue

                # if string is not closed
                else:
                    errors.append(LexicalError(pos_start, pos_start, info=f'String not closed: {string_val}'))
                    continue

            ############### COMMENT ###############
            elif self.current_char == '~':
                states.append(327)
                comment_val = ''
                pos_start = self.pos.copy()
                comment_val += self.current_char
                self.advance()

                # next character must also be ~, otherwise an error occurs
                if self.current_char == '~':
                    states.append(328)
                    comment_val += self.current_char
                    self.advance()

                    # read until EOF or ~
                    while self.current_char is not None:
                        if self.current_char == '~':
                            comment_val += self.current_char
                            self.advance()

                            # another ~ to end the comment
                            if self.current_char == '~':
                                states.append(329)
                                comment_val += self.current_char
                                self.advance()
                                states.append(330)
                                tokens.append(Token(TT_COMMENTLIT, comment_val, pos_start, self.pos.copy()))
                                break

                        # add everything as a comment   
                        else:
                            comment_val += self.current_char
                            self.advance()
                            
                    # if comment is unclosed
                    else:
                        errors.append(LexicalError(pos_start, pos_start, info=f'Comment not closed: {comment_val}'))
                        continue
                else:
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character "{comment_val}"'))
                    continue
            
            ############### WHITESPACE ###############
            elif self.current_char in WHITESPACE:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    case ' ':
                        while self.current_char == ' ':
                            states.append(218)
                            self.advance()
                        new_string += 'space'
                        tokens.append(Token(TT_SPACE, new_string, pos_start, self.pos.copy()))
                        continue
                    case '\n':
                        new_string += '\\n'
                        states.append(219)
                        self.advance()
                        tokens.append(Token(TT_NEWLINE, new_string, pos_start, self.pos.copy()))
                        continue

            ############## IF CHARACTER IS UNRECOGNIZED BY THE COMPILER ##############
            else:
                pos_start = self.pos.copy()
                invalid_char = self.current_char
                self.advance()
                pos_end = self.pos.copy()
                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid character -> {invalid_char} <-'))
                continue
        
        ############## ALWAYS APPEND EOF at the end of the lexeme table ##############
        tokens.append(Token('EOF', '', self.pos.copy(), self.pos.copy()))
        return tokens, errors

# this will be the main function to be called by the server to send source code to backend
# this takes 'source' as the source code from the code editor and returns the generated tokens and errors
def lexical_analyze(source):
    lexer = Lexer(source)
    tokens, errors = lexer.tokenize()

    return tokens, errors