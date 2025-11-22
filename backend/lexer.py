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
    'arith_dlm':            set(WHITESPACE + ALPHADIG + '-' + '(' + '_' + '~'),
    'assignop_dlm':         set(WHITESPACE + ALPHADIG + '('  + '\'' + '"' + '-' + '_' + '~'),
    'bool_dlm':             set(WHITESPACE + ';' + ',' + '}'+ ')' + '+' + '~'),
    'clcurlb_dlm':          set(WHITESPACE + ALPHABET + ';' + '}' + ')' + ',' + '~'),
    'cldoublequotes_dlm':   set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + '+' + ':' + '~'),
    'clparenth_dlm':        set(WHITESPACE + ARITH + RELATIONAL + ';' + ',' + ')' + '{' + ']' + '~'),
    'clquotes_dlm':         set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + ':' + '~'),
    'clsqrb_dlm':           set(WHITESPACE + ARITH + RELATIONAL + ',' + ';' + '=' + '[' + ')' + '~'),
    'cmpassignop_dlm':      set(WHITESPACE + ALPHADIG + '\'' + '"' + '-' + '_' + '~'),
    'comb0_dlm':            set(WHITESPACE + '(' + '~'),
    'comb1_dlm':            set(WHITESPACE + '{' + '~'),
    'comb2_dlm':            set(WHITESPACE + ';' + '~'),
    'comb3_dlm':            set(ALPHADIG + '_' + '~'),
    'comb4_dlm':            set(WHITESPACE + ':' + '~'),
    'comma_dlm':            set(WHITESPACE + ALPHADIG + '_' + '\'' + '"' + '(' + '{' + '+' + '-' + '~'),
    'colon_dlm':            set(WHITESPACE + ALPHADIG + '\'' + '"' + '-' + '_' + '+' + '-' + '~'),
    'dt_dlm':               set(WHITESPACE + '[' + '{' + '~'),
    'func_dlm':             set(WHITESPACE + ALPHADIG + '~'),
    'identifier_dlm':       set(WHITESPACE + ARITH + RELATIONAL + '(' + ')' + '[' + ']' + ',' + ';' + '{' + '}' + '=' + '.' + '~'),
    'int_lit_dlm':          set(WHITESPACE + ARITH + RELATIONAL + ')' + ',' + ';' + '}' + ']' + ':' + '~'),
    'lit_dlm':              set(WHITESPACE + ARITH + RELATIONAL + ':' + ';' + '}' + ')' + ',' + '~'),
    'minus_dlm':            set(WHITESPACE + ALPHADIG + '(' + '_' + '~'),
    'none_dlm':             set(WHITESPACE + ';' + ',' + '}' + ')' + '=' + '!' + '+' + '~'),
    'opcurlb_dlm':          set(WHITESPACE + ALPHADIG + '{' + '}' + '\'' + '"' + '-' + '_' + '+' + '~'),
    'opparenth_dlm':        set(WHITESPACE + ALPHADIG + '-' + '_' + '(' + ')' + '\'' + '"' + '{' + '+' + '~'),
    'opsqrb_dlm':           set(WHITESPACE + ALPHADIG + ']' + '+' + '(' + '~'),
    'relational_dlm':       set(WHITESPACE + ALPHADIG + '_' + '~'),
    'unary_dlm':            set(WHITESPACE + ALPHABET + '_' + ';' + ')' + '~'),
    'void_dlm':             set(WHITESPACE + '{' + ';' + '~')
}

########## RESERVED WORDS ##########
keywords = {
    'AND', 'NOT', 'OR', 'bool', 'break', 'case', 'char', 'choose',
    'const', 'continue', 'default', 'elsewhen', 'false', 'float',
    'for', 'giveback', 'int', 'listen', 'make', 'none', 'otherwise', 
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
TT_NONE = 'none'

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

TT_SPACE = ' '
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
                identifier_state = 380
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
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
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
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
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
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                    continue
                    # b
                    case 'b':
                        states.append(19)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # bool
                            case 'o':
                                states.append(20)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'o':
                                    states.append(21)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        states.append(22)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in delim['dt_dlm']:
                                                states.append(23)
                                                tokens.append(Token(TT_BOOL, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['dt_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                            # break
                            case 'r':
                                states.append(24)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(25)    
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'a':
                                        states.append(26)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'k':
                                            states.append(27)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['comb2_dlm']:
                                                    states.append(28)
                                                    tokens.append(Token(TT_BREAK, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['comb2_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                    # c
                    case 'c':
                        states.append(29)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # case
                            case 'a':
                                states.append(30)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 's':
                                    states.append(34)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        states.append(35)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in WHITESPACE:
                                                states.append(36)
                                                tokens.append(Token(TT_CASE, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in WHITESPACE:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                            # h
                            case 'h':
                                states.append(37)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                match self.current_char:
                                    # char
                                    case 'a':
                                        states.append(38)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'r':
                                            states.append(39)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['dt_dlm']:
                                                    states.append(40)
                                                    tokens.append(Token(TT_CHAR, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['dt_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                                    # choose
                                    case 'o':
                                        states.append(41)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'o':
                                            states.append(42)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 's':
                                                states.append(43)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'e':
                                                    states.append(44)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char is not None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            states.append(45)
                                                            tokens.append(Token(TT_CHOOSE, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                            continue
                            # o
                            case 'o':
                                states.append(46)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                # n
                                if self.current_char == 'n':
                                    states.append(47)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    match self.current_char:
                                        # const
                                        case 's':
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
                                                    if self.current_char in WHITESPACE:
                                                        states.append(54)
                                                        tokens.append(Token(TT_CONST, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in WHITESPACE:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                        continue
                                        # continue
                                        case 't':
                                            states.append(55)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'i':
                                                states.append(61)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'n':
                                                    states.append(62)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'u':
                                                        states.append(63)
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char == 'e':
                                                            states.append(64)
                                                            new_string += self.current_char
                                                            identifier_count += 1
                                                            self.advance()
                                                            if self.current_char is not None:
                                                                if self.current_char in delim['comb2_dlm']:
                                                                    states.append(65)
                                                                    tokens.append(Token(TT_CONTINUE, new_string, pos_start, self.pos.copy()))
                                                                    continue
                                                                elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                                    pass
                                                                elif self.current_char not in delim['comb2_dlm']:
                                                                    pos_end = self.pos.copy()
                                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                                    continue              
                    # default
                    case 'd':
                        states.append(66)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'e':
                            states.append(67)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'f':
                                states.append(68)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'a':
                                    states.append(69)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'u':
                                        states.append(70)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'l':
                                            states.append(71)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 't':
                                                states.append(72)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char is not None:
                                                    if self.current_char in delim['comb4_dlm']:
                                                        states.append(73)
                                                        tokens.append(Token(TT_DEFAULT, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in delim['comb4_dlm'] and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in delim['comb4_dlm']:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                        continue
                    # elsewhen
                    case 'e':
                        states.append(74)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'l':
                            states.append(75)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 's':
                                states.append(76)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(77)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'w':
                                        states.append(78)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'h':
                                            states.append(79)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'e':
                                                states.append(80)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'n':
                                                    states.append(81)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char is not None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            states.append(82)
                                                            tokens.append(Token(TT_ELSEWHEN, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                            continue
                    # f
                    case 'f':
                        states.append(83)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # false
                            case 'a':
                                states.append(84)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'l':
                                    states.append(85)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 's':
                                        states.append(86)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            states.append(87)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['bool_dlm']:
                                                    states.append(88)
                                                    tokens.append(Token(TT_FALSE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['bool_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['bool_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                            # float
                            case 'l':
                                states.append(89)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'o':
                                    states.append(90)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'a':
                                        states.append(91)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 't':
                                            states.append(92)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['dt_dlm']:
                                                    states.append(93)
                                                    tokens.append(Token(TT_FLOAT, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['dt_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                            # for
                            case 'o':
                                states.append(94)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'r':
                                    states.append(95)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['comb0_dlm']:
                                            states.append(96)
                                            tokens.append(Token(TT_FOR, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['comb0_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # giveback
                    case 'g':
                        states.append(97)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'i':
                            states.append(98)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'v':
                                states.append(99)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(100)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'b':
                                        states.append(101)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'a':
                                            states.append(102)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'c':
                                                states.append(103)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'k':
                                                    states.append(104)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char is not None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            states.append(105)
                                                            tokens.append(Token(TT_GIVEBACK, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                            continue
                    # int
                    case 'i':
                        states.append(106)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'n':
                            states.append(107)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 't':
                                states.append(119)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char is not None:
                                    if self.current_char in delim['dt_dlm']:
                                        states.append(120)
                                        tokens.append(Token(TT_INT, new_string, pos_start, self.pos.copy()))
                                        continue
                                    elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                        pass
                                    elif self.current_char not in delim['dt_dlm']:
                                        pos_end = self.pos.copy()
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                        continue
                    # listen
                    case 'l':
                        states.append(121)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'i':
                            states.append(125)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 's':
                                states.append(126)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 't':
                                    states.append(127)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        states.append(128)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'n':
                                            states.append(129)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char == '(':
                                                    states.append(130)
                                                    tokens.append(Token(TT_LISTEN, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char != '(':
                                                    pos_end = self.pos.copy()
                                                    if self.current_char == '\n':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after keyword "{new_string}"'))
                                                    elif self.current_char == '\t':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\t" after keyword "{new_string}"'))
                                                    else:
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                    # m
                    case 'm':
                        states.append(131)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'a':
                            states.append(132)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'k':
                                states.append(133)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(134)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in WHITESPACE:
                                            states.append(135)
                                            tokens.append(Token(TT_MAKE, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in WHITESPACE:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # none
                    case 'n':
                        states.append(139)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'o':
                            states.append(140)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'n':
                                states.append(141)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(142)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['none_dlm']:
                                            states.append(143)
                                            tokens.append(Token(TT_NONE, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['none_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['none_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # otherwise
                    case 'o':
                        states.append(144)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 't':
                            states.append(145)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'h':
                                states.append(146)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(147)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'r':
                                        states.append(148)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'w':
                                            states.append(149)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'i':
                                                states.append(150)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 's':
                                                    states.append(151)
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'e':
                                                        states.append(152)
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char is not None:
                                                            if self.current_char in delim['comb1_dlm']:
                                                                states.append(153)
                                                                tokens.append(Token(TT_OTHERWISE, new_string, pos_start, self.pos.copy()))
                                                                continue
                                                            elif self.current_char not in delim['comb1_dlm'] and self.current_char in delim['comb3_dlm']:
                                                                pass
                                                            elif self.current_char not in delim['comb1_dlm']:
                                                                pos_end = self.pos.copy()
                                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                            continue
                    # s
                    case 's':
                        states.append(177)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # say
                            case 'a':
                                states.append(178)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'y':
                                    states.append(179)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char == '(':
                                            states.append(180)
                                            tokens.append(Token(TT_SAY, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char != '(':
                                            pos_end = self.pos.copy()
                                            if self.current_char == '\n':
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after keyword "{new_string}"'))
                                            elif self.current_char == '\t':
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\t" after keyword "{new_string}"'))
                                            else:
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                            # skip
                            case 'k':
                                states.append(181)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'i':
                                    states.append(182)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'p':
                                        states.append(183)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in delim['comb2_dlm']:
                                                states.append(184)
                                                tokens.append(Token(TT_SKIP, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['comb2_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                            # spyce
                            case 'p':
                                states.append(190)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'y':
                                    states.append(191)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'c':
                                        states.append(192)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            states.append(193)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char == '(':
                                                    states.append(194)
                                                    tokens.append(Token(TT_SPYCE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char != '(':
                                                    pos_end = self.pos.copy()
                                                    if self.current_char == '\n':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after keyword "{new_string}"'))
                                                    elif self.current_char == '\t':
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\t" after keyword "{new_string}"'))
                                                    else:
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                            # string
                            case 't':
                                states.append(195)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'r':
                                    states.append(196)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'i':
                                        states.append(197)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'n':
                                            states.append(198)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'g':
                                                states.append(199)
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char is not None:
                                                    if self.current_char in delim['dt_dlm']:
                                                        states.append(200)
                                                        tokens.append(Token(TT_STRING, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in delim['dt_dlm']:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                        continue
                    # true
                    case 't':
                        states.append(210)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'r':
                            states.append(211)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'u':
                                states.append(215)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    states.append(216)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['bool_dlm']:
                                            states.append(217)
                                            tokens.append(Token(TT_TRUE, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['bool_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['bool_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # void
                    case 'v':
                        states.append(225)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'o':
                            states.append(226)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'i':
                                states.append(227)
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'd':
                                    states.append(228)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['void_dlm']:
                                            states.append(229)
                                            tokens.append(Token(TT_VOID, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['void_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['void_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # w
                    case 'w':
                        states.append(230)
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        # h
                        if self.current_char == 'h':
                            states.append(231)
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            match self.current_char:
                                # when
                                case 'e':
                                    states.append(232)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'n':
                                        states.append(233)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char is not None:
                                            if self.current_char in delim['comb0_dlm']:
                                                states.append(234)
                                                tokens.append(Token(TT_WHEN, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['comb0_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                                # while
                                case 'i':
                                    states.append(235)
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        states.append(236)
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            states.append(237)
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char is not None:
                                                if self.current_char in delim['comb0_dlm']:
                                                    states.append(238)
                                                    tokens.append(Token(TT_WHILE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['comb0_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                # Identifier
                states.clear()
                while self.current_char is not None and self.current_char in ALPHADIG + '_' and identifier_count < 25:
                    states.append(identifier_state)
                    new_string += self.current_char
                    identifier_count += 1
                    identifier_state += 1
                    self.advance()
                
                pos_end = self.pos.copy()
                if new_string in keywords:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Keyword "{new_string}" cannot be used as identifier'))
                    continue
                elif identifier_count > 25:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after identifier "{new_string}"'))
                    continue
                elif self.current_char is None or self.current_char not in delim['identifier_dlm']:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after identifier "{new_string}"'))
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
                        tokens.append(Token(f'{TT_IDENTIFIER}{unique_id}', new_string, pos_start, pos_end))
                
            ############### AN ARITHMETIC AND RELATIONAL SYMBOL ###############
            elif self.current_char in ARITH + RELATIONAL:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    # +
                    case '+':
                        states.append(241)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(242)
                            tokens.append(Token(TT_PLUS, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char not in delim['assignop_dlm']:
                            match self.current_char:
                                # ++
                                case '+':
                                    states.append(243)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['unary_dlm']:
                                        states.append(244)
                                        tokens.append(Token(TT_INC, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                        continue
                                # +=
                                case '=':
                                    states.append(245)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                        states.append(246)
                                        tokens.append(Token(TT_ADDASSIGN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                        continue
                                case _:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                    continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue     
                    # - 
                    case '-':
                        states.append(247)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char == '.':
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is None or self.current_char not in DIGITS:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Decimal point must have digits before and after it "{new_string}"'))
                                continue
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Float values must at least have one integer digit before the decimal point'))
                            continue
                
                        # If literal starts with a number
                        elif self.current_char in DIGITS:
                            int_count = 0
                            decimal_count = 0
                            new_string += self.current_char
                            int_count += 1
                            self.advance()
                            while self.current_char is not None and self.current_char in DIGITS and self.current_char != '.' and int_count < 19:
                                int_count += 1
                                new_string += self.current_char
                                self.advance()
                            pos_end = self.pos.copy()

                            # If a . is found; float value
                            if self.current_char == '.':
                                new_string += self.current_char
                                self.advance()
                                if self.current_char is None or self.current_char not in DIGITS:
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "." after value "{new_string}"'))
                                    continue

                                while self.current_char is not None and self.current_char in DIGITS and decimal_count < 5:
                                    decimal_count += 1
                                    new_string += self.current_char
                                    self.advance()
                                pos_end = self.pos.copy()
        
                                if self.current_char is not None and self.current_char in delim['lit_dlm']:
                                    num_parts = new_string.split('.')               # split whole value to two parts <integer>.<float>
                                    int_part = num_parts[0].lstrip('0') or '0'      # strip leading 0 except 1 for integer
                                    float_part = num_parts[1].rstrip('0') or '0'    # strip trailing 0 except 1 for float
                                    digit_val = f'{int_part}.{float_part}'
                                    tokens.append(Token(TT_FLOATLIT, digit_val, pos_start, pos_end))
                                    continue
                                else:
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after value "{new_string}"'))
                                    continue
                                
                            # If only integers
                            elif self.current_char is not None and self.current_char in delim['int_lit_dlm']:
                                digit_val = new_string.lstrip('0') or '0'           # strip leading 0 except 1
                                tokens.append(Token(TT_INTLIT, digit_val, pos_start, pos_end))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after value "{new_string}"'))
                                continue
                        elif self.current_char is not None and self.current_char in delim['minus_dlm']:
                            states.append(248)
                            tokens.append(Token(TT_MINUS, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char not in delim['minus_dlm']:
                            match self.current_char:
                                # --
                                case '-':
                                    states.append(249)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None:
                                        if self.current_char in delim['unary_dlm']:
                                            states.append(250)
                                            tokens.append(Token(TT_DEC, new_string, pos_start, self.pos.copy()))
                                            continue
                                        else:
                                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                            continue
                                    # -=
                                case '=':
                                    states.append(251)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                        states.append(252)
                                        tokens.append(Token(TT_SUBASSIGN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                        continue
                                # ->
                                case '>':
                                    states.append(253)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['func_dlm']:
                                        states.append(254)
                                        tokens.append(Token(TT_RETURN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                        continue
                                case _:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                    continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # *
                    case '*':
                        states.append(255)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['arith_dlm']:
                            states.append(256)
                            tokens.append(Token(TT_MULTIPLY, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char not in delim['arith_dlm']:
                            match self.current_char:
                                # **
                                case '*':
                                    states.append(257)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['arith_dlm']:
                                        states.append(258)
                                        tokens.append(Token(TT_POW, new_string, pos_start, self.pos.copy()))
                                        continue
                                    # **=
                                    elif self.current_char == '=':
                                        states.append(259)
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                            states.append(260)
                                            tokens.append(Token(TT_POWASSIGN, new_string, pos_start, self.pos.copy()))
                                            continue
                                        else:
                                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                            continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                        continue
                                # *=
                                case '=':
                                    states.append(261)
                                    new_string += self.current_char
                                    self.advance()
                                    if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                        states.append(262)
                                        tokens.append(Token(TT_POWASSIGN, new_string, pos_start, self.pos.copy()))
                                        continue
                                    else:
                                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                        continue
                                case _:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                    continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue 
                    # /
                    case '/':
                        states.append(263)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['arith_dlm']:
                            states.append(264)
                            tokens.append(Token(TT_DIVIDE, new_string, pos_start, self.pos.copy()))
                            continue
                        # /=
                        elif self.current_char == '=':
                            states.append(265)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                states.append(266)
                                tokens.append(Token(TT_DIVASSIGN, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue 
                    # %
                    case '%':
                        states.append(267)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['arith_dlm']:
                            states.append(268)
                            tokens.append(Token(TT_MOD, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char == '=':
                            states.append(269)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['cmpassignop_dlm']:
                                states.append(270)
                                tokens.append(Token(TT_MODASSIGN, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue  
                    # =
                    case '=':
                        states.append(271)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(272)
                            tokens.append(Token(TT_ASSIGN, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char == '=':
                            states.append(273)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(274)
                                tokens.append(Token(TT_EQUAL, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # !
                    case '!':
                        states.append(275)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char == '=':
                            states.append(276)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(277)
                                tokens.append(Token(TT_NOTEQ, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Character "{new_string}"'))
                            continue
                    # >
                    case '>':
                        states.append(278)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(279)
                            tokens.append(Token(TT_GREAT, new_string, pos_start, self.pos.copy()))
                            continue
                        elif self.current_char == '=':
                            states.append(280)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(281)
                                tokens.append(Token(TT_GREATEQ, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # <
                    case '<':
                        states.append(282)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                            states.append(283)
                            tokens.append(Token(TT_LESS, new_string, pos_start, self.pos.copy()))
                            continue
                        # <=
                        elif self.current_char == '=':
                            states.append(284)
                            new_string += self.current_char
                            self.advance()
                            if self.current_char is not None and self.current_char in delim['assignop_dlm']:
                                states.append(285)
                                tokens.append(Token(TT_LESSEQ, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue  
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
            
            ############### OTHER SYMBOLS (()[]{},:;) ###############
            elif self.current_char in OTHERSYMS:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    # (
                    case '(':
                        states.append(286)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['opparenth_dlm']:
                            states.append(287)
                            tokens.append(Token(TT_LPAREN, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # )
                    case ')':
                        states.append(288)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['clparenth_dlm']:
                            states.append(289)
                            tokens.append(Token(TT_RPAREN, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # {
                    case '{':
                        states.append(290)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['opcurlb_dlm']:
                            states.append(291)
                            tokens.append(Token(TT_LCURL, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # }
                    case '}':
                        states.append(292)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is None or self.current_char in delim['clcurlb_dlm']:
                            states.append(293)
                            tokens.append(Token(TT_RCURL, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # [
                    case '[':
                        states.append(294)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char is not None and self.current_char in delim['opsqrb_dlm']:
                            states.append(295)
                            tokens.append(Token(TT_LSQR, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # ]
                    case ']':
                        states.append(296)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['clsqrb_dlm']:
                            states.append(297)
                            tokens.append(Token(TT_RSQR, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # :
                    case ':':
                        states.append(298)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in WHITESPACE:
                            states.append(299)
                            tokens.append(Token(TT_COLON, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # ,
                    case ',':
                        states.append(300)
                        new_string += self.current_char
                        self.advance()
                        if self.current_char in delim['comma_dlm']:
                            states.append(301)
                            tokens.append(Token(TT_COMMA, new_string, pos_start, self.pos.copy()))
                            continue
                        else:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                            continue
                    # ;
                    case ';':
                        states.append(302)
                        new_string += self.current_char
                        tokens.append(Token(TT_SEMICOLON, new_string, pos_start, self.pos.copy()))
                        self.advance()
                        continue

            ############### INT AND FLOAT LITERALS ###############
            # If a decimal point is used to start a float value
            elif self.current_char == '.':
                new_string = ''
                pos_start = self.pos.copy()
                new_string += self.current_char
                self.advance()
                if self.current_char is None or self.current_char not in DIGITS:
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Decimal point must have digits before and after it "{new_string}"'))
                    continue
                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Float values must at least have one integer digit before the decimal point'))
                continue
                
            # If literal starts with a number
            elif self.current_char in DIGITS:
                new_string = ''
                int_count = 0
                decimal_count = 0
                pos_start = self.pos.copy()
                new_string += self.current_char
                int_count += 1
                self.advance()
                while self.current_char is not None and self.current_char in DIGITS and self.current_char != '.' and int_count < 19:
                    int_count += 1
                    new_string += self.current_char
                    self.advance()
                pos_end = self.pos.copy()

                # If a . is found; float value
                if self.current_char == '.':
                    new_string += self.current_char
                    self.advance()
                    if self.current_char is None or self.current_char not in DIGITS:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "." after value "{new_string}"'))
                        continue

                    while self.current_char is not None and self.current_char in DIGITS and decimal_count < 5:
                        decimal_count += 1
                        new_string += self.current_char
                        self.advance()
                    pos_end = self.pos.copy()
        
                    if self.current_char is not None and self.current_char in delim['lit_dlm']:
                        num_parts = new_string.split('.')               # split whole value to two parts <integer>.<float>
                        int_part = num_parts[0].lstrip('0') or '0'      # strip leading 0 except 1 for integer
                        float_part = num_parts[1].rstrip('0') or '0'    # strip trailing 0 except 1 for float
                        digit_val = f'{int_part}.{float_part}'
                        tokens.append(Token(TT_FLOATLIT, digit_val, pos_start, pos_end))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after value "{new_string}"'))
                        continue

                # If only integers
                elif self.current_char is not None and self.current_char in delim['int_lit_dlm']:
                    digit_val = new_string.lstrip('0') or '0'           # strip leading 0 except 1
                    tokens.append(Token(TT_INTLIT, digit_val, pos_start, pos_end))
                    continue
                else:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after value "{new_string}"'))
                    continue

            ############### CHAR LITERAL ##############
            elif self.current_char == '\'':
                states.append(373)
                pos_start = self.pos.copy()
                char_val = ''
                char_val += self.current_char           
                char_count = 0
                withNonAscii = False
                self.advance()

                # empty char literal
                if self.current_char == '\'':
                    errors.append(LexicalError(pos_start, self.pos.copy(), info='Char values must at least have 1 character stored'))
                    continue

                # valid char literal
                else:
                    states.append(374)
                    while self.current_char is not None and self.current_char != '\'':
                        char_count += 1
                        char_val += self.current_char
                        self.advance()
                    if self.current_char == '\'':
                        states.append(375)
                        char_val += self.current_char
                        self.advance()
                        pos_end = self.pos.copy()

                        # check each if literal contains non ASCII
                        for i in char_val.replace(' ', ''):
                            if i not in ASCII + WHITESPACE:
                                withNonAscii = True 
                                break
                        if withNonAscii:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info='Char values must only be ASCII values'))
                            continue    

                        # if more than one character is inside
                        if char_count > 1:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info='Char values can only store 1 character'))
                            continue
                        else:
                            if self.current_char is not None and self.current_char in delim['clquotes_dlm']:
                                startChar = False
                                tokens.append(Token(TT_CHARLIT, char_val, pos_start, pos_end))
                                states.append(376)
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after char lit {char_val}'))
                                continue

                    # if char is not closed
                    else:
                        pos_end = self.pos.copy()
                        errors.append(LexicalError(pos_start, pos_end, info='Char value not closed'))
                        continue

            ############### STRING LITERAL ###############
            elif self.current_char == '"':
                states.append(377)
                pos_start = self.pos.copy()
                string_val = ''
                string_val += self.current_char
                withNonAscii = False
                self.advance()
                
                # read succeeding characters as strings until EOF or " is found
                while self.current_char is not None and self.current_char != '"':
                    if self.current_char == '\\':
                        string_val += self.current_char
                        self.advance()
                        if self.current_char is None or self.current_char not in ESCAPE_SEQ:
                            errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character "{self.current_char}" after \\'))
                            continue
                    string_val += self.current_char
                    self.advance()

                if self.current_char == '"':
                    states.append(378)
                    string_val += self.current_char
                    self.advance()
                    pos_end = self.pos.copy()
                    
                    # check if all characters are in ASCII
                    for i in string_val.replace(' ', ''):
                        if i not in ASCII:
                            withNonAscii = True
                            break
                    if withNonAscii:
                        errors.append(LexicalError(pos_start, self.pos.copy(), info='String values must only be ASCII values'))
                        continue

                    # if valid string
                    if self.current_char is not None and self.current_char in delim['cldoublequotes_dlm']:
                        states.append(379)
                        tokens.append(Token(TT_STRINGLIT, string_val, pos_start, pos_end))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after string lit {string_val}'))
                        continue

                # if string is not closed
                else:
                    pos_end = self.pos.copy()
                    errors.append(LexicalError(pos_start, pos_end, info='String value not closed'))
                    continue

            ############### COMMENT ###############
            elif self.current_char == '~':
                states.append(430)
                comment_val = ''
                pos_start = self.pos.copy()
                comment_val += self.current_char
                self.advance()

                # next character must also be ~, otherwise an error occurs
                if self.current_char == '~':
                    states.append(431)
                    comment_val += self.current_char
                    self.advance()

                    # read until EOF or ~
                    while self.current_char is not None:
                        if self.current_char == '~':
                            comment_val += self.current_char
                            self.advance()

                            # another ~ to end the comment
                            if self.current_char == '~':
                                states.append(432)
                                comment_val += self.current_char
                                self.advance()
                                states.append(433)
                                tokens.append(Token(TT_COMMENTLIT, comment_val, pos_start, self.pos.copy()))
                                break

                        # add everything as a comment   
                        else:
                            comment_val += self.current_char
                            self.advance()
                            
                    # if comment is unclosed
                    else:
                        errors.append(LexicalError(pos_start, self.pos.copy(), info='Comment not closed'))
                        continue
                else:
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character "{comment_val}"'))
                    continue
            
            ############### WHITESPACE ###############
            elif self.current_char in WHITESPACE:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    case '\n':
                        new_string += '\\n'
                        self.advance()
                        tokens.append(Token(TT_NEWLINE, new_string, pos_start, self.pos.copy()))
                        continue
                    case ' ':
                        while self.current_char == ' ':
                            self.advance()
                        new_string += 'space'
                        tokens.append(Token(TT_SPACE, new_string, pos_start, self.pos.copy()))
                        continue

            ############## IF CHARACTER IS UNRECOGNIZED BY THE COMPILER ##############
            else:
                pos_start = self.pos.copy()
                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character "{self.current_char}"'))
                self.advance()
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