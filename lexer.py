# Makes using letters easy instead of manually typing each
import string

########## DEFINITIONS ##########
# From regular definitions
DIGITS = '0123456789'
ALPHABET = string.ascii_letters
ALPHADIG = DIGITS + ALPHABET
WHITESPACE = '\n\t '
COMMENT = '~~'
ASCII = ALPHADIG + string.punctuation
ARITH = '+-/*%'
RELATIONAL = '=!<>'
OTHERSYMS = '({[]}),;:'

########## DELIMITERS ##########
delim = {
    'dt_dlm':               set(WHITESPACE + '[' + '{'),
    'bool_dlm':             set(WHITESPACE + ';' + '}'+ ')'),
    'void_dlm':             set(WHITESPACE + '{' + ';'),
    'lit_dlm':              set(WHITESPACE + ARITH + RELATIONAL +':' + ';' + '}' + ')'),
    'int_lit_dlm':          set(WHITESPACE + ARITH + RELATIONAL + ':' + ';' + '}' + ')' + '.'),
    'identifier_dlm':       set(WHITESPACE + '(' + ')' + '[' + ',' + ';' + '{' + '}'),
    'func_dlm':             set(WHITESPACE + ALPHADIG),
    'minus_dlm':            set(WHITESPACE + ALPHADIG + '(' + '_'),
    'arith_dlm':            set(WHITESPACE + ALPHADIG + '-' + '(' + '_'),
    'assignop_dlm':         set(WHITESPACE + ALPHADIG+ '('  + '\'' + '"' + '-' + '_'),
    'opparenth_dlm':        set(WHITESPACE + ALPHADIG + ';' + '(' + ')' + '{' + '}' + '\'' + '"'),
    'clparenth_dlm':        set(WHITESPACE + ALPHADIG + ARITH + RELATIONAL + ';' + '.' + '(' + ')' + '{' + '}' ),
    'opcurlb_dlm':          set(WHITESPACE + ALPHADIG + '}' + '\'' + '"'),
    'clcurlb_dlm':          set(WHITESPACE + ALPHABET + ';' + '{' + '\'' + '"' + '.'),
    'opsqrb_dlm':           set(WHITESPACE + DIGITS),
    'clsqrb_dlm':           set(WHITESPACE + ARITH + RELATIONAL + '=' + '['),
    'clquotes_dlm':         set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + '.'),
    'cldoublequotes_dlm':   set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + '.' + '+'),
    'comma_dlm':            set(WHITESPACE + ALPHADIG + '\'' + '"' + '(' + '{' + '+' + '-'),
    'unary_dlm':            set(WHITESPACE + ALPHABET + '_' + ';' + ')'),
    'comb0_dlm':            set(WHITESPACE + '('),
    'comb1_dlm':            set(WHITESPACE + '{'),
    'comb2_dlm':            set(WHITESPACE + ';'),
    'comb3_dlm':            set(ALPHADIG + '_')
}

########## RESERVED WORDS ##########
keywords = {
    'int', 'float', 'char', 'string', 'bool', 'say', 'listen', 'AND', 'OR', 'NOT',
    'when', 'elsewhen', 'otherwise', 'choose', 'case', 'default', 'for', 'while',
    'break', 'skip', 'continue', 'len', 'caps', 'small', 'indexOf', 'replace', 'trim',
    'replace', 'trim', 'reverse', 'substring', 'contains', 'append', 'pop', 'insert', 
    'remove', 'concat', 'unique', 'true', 'false', 'make', 'spyce', 'mix', 'const', 
    'void', 'giveback', 'this'
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
TT_DEFAULT = 'deafult'

# iteration
TT_FOR = 'for'
TT_WHILE = 'while'
TT_BREAK = 'break'
TT_SKIP = 'skip'
TT_CONTINUE = 'continue'

# common methods
TT_LEN = 'len'
TT_INDEXOF = 'indexOf'
TT_REVERSE = 'reverse'
TT_CONTAINS = 'contains'

# array methods
TT_APPEND = 'append'
TT_POP = 'pop'
TT_INSERT = 'insert'
TT_REMOVE = 'remove'
TT_CONCAT = 'concat'
TT_UNIQUE = 'unique'

# string methods
TT_CAPS = 'caps'
TT_SMALL = 'small'
TT_REPLACE = 'replace'
TT_TRIM = 'trim'
TT_SUBSTRING = 'substring'

# others
TT_TRUE = 'true'
TT_FALSE = 'false'
TT_MAKE = 'make'
TT_SPYCE = 'spyce'
TT_MIX = 'mix'
TT_CONST = 'const'
TT_VOID = 'void'
TT_GIVEBACK = 'giveback'
TT_THIS = 'this'

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
TT_COMMENT = '~~'
TT_COMMA = ','
TT_DOT = '.'

# LITERALS
TT_INTLIT = 'int literal'
TT_FLOATLIT = 'float literal'
TT_CHARLIT = 'char literal'
TT_STRINGLIT = 'string literal'
TT_COMMENTLIT = 'comment'

# IDENTIFIER
TT_IDENTIFIER = 'id'

TT_SPACE = ' '
TT_TAB = '\\t'
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

    # copies current position to caputre position
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fullText)

############# ERROR CLASS ##########
# pos_start = where the error began
# pos_end = where the error ended
# error_name = error name
# info = details about the error
class Error:
    def __init__(self, pos_start, pos_end, error_name, info):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.info = info

    # formatted string representation of the error
    def __repr__(self):
        result = f'{self.error_name}: {self.info} \n'
        result += f'Line {self.pos_start.ln + 1}, Column {self.pos_start.col + 1}\n'
        return result
    
########## LEXICALERROR ##########
# subclass of error that creates a lexical error type
class LexicalError(Error):
    def __init__(self, pos_start, pos_end, info):
        super().__init__(pos_start, pos_end, 'Lexical Error', info)

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
    
    # string representation of the tokens when print(Token) is done
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
        unique_id = 0   # counter for unique id in the source code

        while self.current_char != None:
            ############### WHITESPACE ###############
            if self.current_char in WHITESPACE:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    case '\n':
                        new_string += '\\n'
                        self.advance()
                        tokens.append(Token(TT_NEWLINE, new_string, pos_start, self.pos.copy()))
                        continue
                    case ' ':
                        new_string += 'space'
                        self.advance()
                        tokens.append(Token(TT_SPACE, new_string, pos_start, self.pos.copy()))
                        continue

            ############### KEYWORD OR IDENTIFIER ###############
            elif self.current_char in ALPHABET:
                new_string = ''                 # where the next characters will be appended
                identifier_count = 0            # count if an identifier is greater than the limit
                pos_start = self.pos.copy()     # copy the position of the text
                match self.current_char:
                    # AND
                    case 'A':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'N':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'D':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['comb0_dlm']:
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
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'O':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'T':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['comb0_dlm']:
                                        tokens.append(Token(TT_AND, new_string, pos_start, self.pos.copy()))
                                        continue
                                    elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                        pass
                                    elif self.current_char not in delim['comb0_dlm']:
                                        pos_end = self.pos.copy()
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                        continue
                    # OR
                    case 'O':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'R':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char != None:
                                if self.current_char in delim['comb0_dlm']:
                                    tokens.append(Token(TT_OR, new_string, pos_start, self.pos.copy()))
                                    continue
                                elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                    pass
                                elif self.current_char not in delim['comb0_dlm']:
                                    pos_end = self.pos.copy()
                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"')) 
                                    continue
                    # append
                    case 'a':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'p':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'p':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'n':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'd':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char == '(':
                                                    tokens.append(Token(TT_APPEND, new_string, pos_start, self.pos.copy()))
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
                    # b
                    case 'b':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # bool
                            case 'o':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'o':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['dt_dlm']:
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'a':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'k':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in delim['comb2_dlm']:
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
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # a
                            case 'a':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                match self.current_char:
                                    # caps
                                    case 'p':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 's':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char == '(':
                                                    tokens.append(Token(TT_CAPS, new_string, pos_start, self.pos.copy()))
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
                                    # case
                                    case 's':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in WHITESPACE:
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                match self.current_char:
                                    # char
                                    case 'a':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'r':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in delim['dt_dlm']:
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
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'o':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 's':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'e':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char in delim['comb0_dlm']:
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                # n
                                if self.current_char == 'n':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    match self.current_char:
                                        # concat
                                        case 'c':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'a':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 't':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char == '(':
                                                            tokens.append(Token(TT_CONCAT, new_string, pos_start, self.pos.copy()))
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
                                        # const
                                        case 's':
                                            if self.current_char == 't':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char in WHITESPACE:
                                                        tokens.append(Token(TT_CONST, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in WHITESPACE:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                        continue
                                        # contains
                                        case 't':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'a':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'i':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'n':
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char == 's':
                                                            new_string += self.current_char
                                                            identifier_count += 1
                                                            self.advance()
                                                            if self.current_char != None:
                                                                if self.current_char == '(':
                                                                    tokens.append(Token(TT_CONTAINS, new_string, pos_start, self.pos.copy()))
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
                    # default
                    case 'd':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'e':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'f':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'a':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'u':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'l':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 't':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char in delim['comb2_dlm']:
                                                        tokens.append(Token(TT_DEFAULT, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in delim['comb2_dlm']:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                        continue
                    # elsewhen
                    case 'e':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'l':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 's':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'w':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'h':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'e':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'n':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char in delim['comb0_dlm']:
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
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # false
                            case 'a':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'l':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 's':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in delim['bool_dlm']:
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'o':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'a':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 't':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in delim['dt_dlm']:
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'r':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char != None:
                                        if self.current_char in delim['comb0_dlm']:
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
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'i':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'v':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'b':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'a':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'c':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'k':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char in delim['comb0_dlm']:
                                                            tokens.append(Token(TT_GIVEBACK, new_string, pos_start, self.pos.copy()))
                                                            continue
                                                        elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                            pass
                                                        elif self.current_char not in delim['comb0_dlm']:
                                                            pos_end = self.pos.copy()
                                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                            continue
                    # i
                    case 'i':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        # n
                        if self.current_char == 'n':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            match self.current_char:
                                # indexOf
                                case 'd':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'x':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'O':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'f':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char == '(':
                                                            tokens.append(Token(TT_INDEXOF, new_string, pos_start, self.pos.copy()))
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
                                # insert
                                case 's':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'r':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 't':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char == '(':
                                                        tokens.append(Token(TT_INSERT, new_string, pos_start, self.pos.copy()))
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
                                # int
                                case 't':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char != None:
                                        if self.current_char in delim['dt_dlm']:
                                            tokens.append(Token(TT_INT, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in delim['dt_dlm']:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # l
                    case 'l':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # len
                            case 'e':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'n':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char != None:
                                        if self.current_char == '(':
                                            tokens.append(Token(TT_LEN, new_string, pos_start, self.pos.copy()))
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
                            # listen
                            case 'i':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 's':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 't':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'n':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char == '(':
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
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # make
                            case 'a':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'k':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in WHITESPACE:
                                                tokens.append(Token(TT_MAKE, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in WHITESPACE:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                            # mix
                            case 'i':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'x':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char != None:
                                        if self.current_char in WHITESPACE:
                                            tokens.append(Token(TT_MIX, new_string, pos_start, self.pos.copy()))
                                            continue
                                        elif self.current_char not in WHITESPACE and self.current_char in delim['comb3_dlm']:
                                            pass
                                        elif self.current_char not in WHITESPACE:
                                            pos_end = self.pos.copy()
                                            errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                            continue
                    # otherwise
                    case 'o':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 't':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'h':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'e':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'r':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'w':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'i':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 's':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'e':
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char != None:
                                                            if self.current_char in delim['comb1_dlm']:
                                                                tokens.append(Token(TT_OTHERWISE, new_string, pos_start, self.pos.copy()))
                                                                continue
                                                            elif self.current_char not in delim['comb1_dlm'] and self.current_char in delim['comb3_dlm']:
                                                                pass
                                                            elif self.current_char not in delim['comb1_dlm']:
                                                                pos_end = self.pos.copy()
                                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                                continue
                    # pop
                    case 'p':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'o':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'p':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char == '(':
                                        tokens.append(Token(TT_POP, new_string, pos_start, self.pos.copy()))
                                        continue
                                    elif self.current_char != '(' and self.current_char in delim['comb3_dlm']:
                                        pass
                                    elif self.current_char != '(':
                                        pos_end = self.pos.copy()
                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                        continue
                    # r
                    case 'r':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'e':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            match self.current_char:
                                # remove
                                case 'm':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'o':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'v':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'e':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char == '(':
                                                        tokens.append(Token(TT_REMOVE, new_string, pos_start, self.pos.copy()))
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
                                # replace
                                case 'p':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'a':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'c':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'e':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char == '(':
                                                            tokens.append(Token(TT_REPLACE, new_string, pos_start, self.pos.copy()))
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
                                # reverse
                                case 'v':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'e':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'r':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 's':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'e':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char != None:
                                                        if self.current_char == '(':
                                                            tokens.append(Token(TT_REVERSE, new_string, pos_start, self.pos.copy()))
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
                    # s
                    case 's':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # say
                            case 'a':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'y':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char != None:
                                        if self.current_char == '(':
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'i':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'p':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['comb2_dlm']:
                                                tokens.append(Token(TT_SKIP, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char not in delim['comb2_dlm'] and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char not in delim['comb2_dlm']:
                                                pos_end = self.pos.copy()
                                                errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                            # small
                            case 'm':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'a':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'l':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char == '(':
                                                    tokens.append(Token(TT_SMALL, new_string, pos_start, self.pos.copy()))
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
                            # spyce
                            case 'p':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'y':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'c':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char == '(':
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
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'r':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'i':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'n':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'g':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char in delim['dt_dlm']:
                                                        tokens.append(Token(TT_STRING, new_string, pos_start, self.pos.copy()))
                                                        continue
                                                    elif self.current_char not in delim['dt_dlm'] and self.current_char in delim['comb3_dlm']:
                                                        pass
                                                    elif self.current_char not in delim['dt_dlm']:
                                                        pos_end = self.pos.copy()
                                                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                        continue
                            # substring
                            case 'u':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'b':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 's':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 't':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char == 'r':
                                                new_string += self.current_char
                                                identifier_count += 1
                                                self.advance()
                                                if self.current_char == 'i':
                                                    new_string += self.current_char
                                                    identifier_count += 1
                                                    self.advance()
                                                    if self.current_char == 'n':
                                                        new_string += self.current_char
                                                        identifier_count += 1
                                                        self.advance()
                                                        if self.current_char == 'g':
                                                            new_string += self.current_char
                                                            identifier_count += 1
                                                            self.advance()
                                                            if self.current_char != None:
                                                                if self.current_char == '(':
                                                                    tokens.append(Token(TT_SUBSTRING, new_string, pos_start, self.pos.copy()))
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
                    # t
                    case 't':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        match self.current_char:
                            # this
                            case 'h':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'i':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 's':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char == '.':
                                                tokens.append(Token(TT_THIS, new_string, pos_start, self.pos.copy()))
                                                continue
                                            elif self.current_char != '.' and self.current_char in delim['comb3_dlm']:
                                                pass
                                            elif self.current_char != '.':
                                                pos_end = self.pos.copy()
                                                if self.current_char == '\n':
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\n" after keyword "{new_string}"'))
                                                elif self.current_char == '\t':
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "\\t" after keyword "{new_string}"'))
                                                else:
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                continue
                            # r
                            case 'r':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                match self.current_char:
                                    # trim
                                    case 'i':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'm':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char == '(':
                                                    tokens.append(Token(TT_TRIM, new_string, pos_start, self.pos.copy()))
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
                                    # true
                                    case 'u':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in delim['bool_dlm']:
                                                    tokens.append(Token(TT_TRUE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['bool_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['bool_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                    # unique
                    case 'u':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'n':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'i':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'q':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'u':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char == '(':
                                                    tokens.append(Token(TT_UNIQUE, new_string, pos_start, self.pos.copy()))
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
                    # void
                    case 'v':
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        if self.current_char == 'o':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            if self.current_char == 'i':
                                new_string += self.current_char
                                identifier_count += 1
                                self.advance()
                                if self.current_char == 'd':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char != None:
                                        if self.current_char in delim['void_dlm']:
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
                        new_string += self.current_char
                        identifier_count += 1
                        self.advance()
                        # h
                        if self.current_char == 'h':
                            new_string += self.current_char
                            identifier_count += 1
                            self.advance()
                            match self.current_char:
                                # when
                                case 'e':
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'n':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['comb0_dlm']:
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
                                    new_string += self.current_char
                                    identifier_count += 1
                                    self.advance()
                                    if self.current_char == 'l':
                                        new_string += self.current_char
                                        identifier_count += 1
                                        self.advance()
                                        if self.current_char == 'e':
                                            new_string += self.current_char
                                            identifier_count += 1
                                            self.advance()
                                            if self.current_char != None:
                                                if self.current_char in delim['comb0_dlm']:
                                                    tokens.append(Token(TT_WHILE, new_string, pos_start, self.pos.copy()))
                                                    continue
                                                elif self.current_char not in delim['comb0_dlm'] and self.current_char in delim['comb3_dlm']:
                                                    pass
                                                elif self.current_char not in delim['comb0_dlm']:
                                                    pos_end = self.pos.copy()
                                                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after keyword "{new_string}"'))
                                                    continue
                # Identifier
                while self.current_char != None and self.current_char in ALPHADIG + '_':
                    new_string += self.current_char
                    identifier_count += 1
                    self.advance()
                
                pos_end = self.pos.copy()
                if new_string in keywords:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Keyword "{new_string}" cannot be used as identifier'))
                    continue
                elif self.current_char != None and self.current_char not in delim['identifier_dlm']:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after identifier "{new_string}"'))
                    continue
                elif len(new_string) > 25:
                    errors.append(LexicalError(pos_start, pos_end, info=f'Identifier "{new_string}" exceeds maximum number of characters for identifiers: {identifier_count}/25'))
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
                    continue

            ############### LITERALS OR . FOR INT AND FLOAT LITERALS ###############
            elif self.current_char in DIGITS + '.':
                pos_start = self.pos.copy()
                digit_val = ''
                int_dig_count = 0
                dec_dig_count = 0
                dot_count = 0

                while self.current_char != None and self.current_char in DIGITS:
                    digit_val += self.current_char
                    int_dig_count += 1
                    self.advance()

                # if a . is found, increment count for dot counts and decimal digits
                if self.current_char == '.':
                    digit_val += self.current_char
                    dot_count += 1
                    self.advance()
                    while self.current_char != None and self.current_char in DIGITS:
                        digit_val += self.current_char
                        dec_dig_count += 1
                        self.advance()
                    # if a . is read again
                    if self.current_char == '.':
                        digit_val += self.current_char
                        dot_count += 1
                        self.advance()
                
                pos_end = self.pos.copy()
                
                match True:
                    # if there are more than 1 decimal points
                    case _ if dot_count > 1:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Multiple dots not allowed'))
                        continue
                    # if integer part > 19
                    case _ if int_dig_count > 19:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Integer part of {digit_val} exceeds maximum number of digits: {int_dig_count}/19'))
                        continue
                    # if decimal part > 19
                    case _ if dec_dig_count > 5:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Float part of {digit_val} exceeds maximum number of digits: {dec_dig_count}/5'))
                        continue
                    # if no integer part precedes decimal point (eg. .2321)
                    case _ if int_dig_count == 0 and dot_count == 1:
                        errors.append(LexicalError(pos_start, pos_end, info=f'{digit_val} must have digits before the decimal point'))
                        continue
                    # if no decimal part after the decimal pinot (eg. 123.)
                    case _ if dec_dig_count == 0 and dot_count == 1:
                        errors.append(LexicalError(pos_start, pos_end, info=f'{digit_val} must have digits after the decimal point'))
                        continue
                
                # if value is an integer 
                if dot_count == 0:
                    digit_val = digit_val.lstrip('0') or '0'   # strip leading 0 except 1
                    if self.current_char != None and self.current_char in delim['int_lit_dlm']:
                        tokens.append(Token(TT_INTLIT, digit_val, pos_start, pos_end))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after integer "{digit_val}"'))
                        continue
                # if value is a float 
                else:
                    num_parts = digit_val.split('.')                # split whole value to two parts <integer>.<float>
                    int_part = num_parts[0].lstrip('0') or '0'      # strip leading 0 except 1 for integer
                    float_part = num_parts[1].rstrip('0') or '0'    # strip trailing 0 except 1 for float
                    digit_val = f'{int_part}.{float_part}'
                    if self.current_char != None and self.current_char in delim['lit_dlm']:  
                        tokens.append(Token(TT_FLOATLIT, digit_val, pos_start, pos_end))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, pos_end, info=f'Invalid Delimiter "{self.current_char}" after float "{digit_val}"'))
                        continue

            ############### PERIOD ###############
            elif self.current_char == '.':
                new_string = ''
                pos_start = self.pos.copy()
                new_string += self.current_char
                self.advance()
                if self.current_char != None:
                    if self.current_char in delim['comb3_dlm']:
                        tokens.append(Token(TT_DOT, new_string, pos_start, self.pos.copy()))
                        continue
                    else:
                        errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                        continue
                
            ############### AN ARITHMETIC AND RELATIONAL SYMBOL ###############
            elif self.current_char in ARITH + RELATIONAL:
                new_string = ''
                pos_start = self.pos.copy()
                match self.current_char:
                    # +
                    case '+':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['assignop_dlm']:
                                tokens.append(Token(TT_PLUS, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char not in delim['assignop_dlm']:
                                match self.current_char:
                                    # ++
                                    case '+':
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['unary_dlm']:
                                                tokens.append(Token(TT_INC, new_string, pos_start, self.pos.copy()))
                                                continue
                                            else:
                                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                                continue
                                    # +=
                                    case '=':
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['minus_dlm']:
                                tokens.append(Token(TT_MINUS, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char not in delim['minus_dlm']:
                                match self.current_char:
                                    # --
                                    case '-':
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['unary_dlm']:
                                                tokens.append(Token(TT_DEC, new_string, pos_start, self.pos.copy()))
                                                continue
                                            else:
                                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                                continue
                                    # -=
                                    case '=':
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['assignop_dlm']:
                                                tokens.append(Token(TT_SUBASSIGN, new_string, pos_start, self.pos.copy()))
                                                continue
                                            else:
                                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                                continue
                                    # ->
                                    case '>':
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['func_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['arith_dlm']:
                                tokens.append(Token(TT_MULTIPLY, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char not in delim['arith_dlm']:
                                match self.current_char:
                                    # **
                                    case '*':
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['arith_dlm']:
                                                tokens.append(Token(TT_POW, new_string, pos_start, self.pos.copy()))
                                                continue
                                            # **=
                                            elif self.current_char == '=':
                                                new_string += self.current_char
                                                self.advance()
                                                if self.current_char != None:
                                                    if self.current_char in delim['assignop_dlm']:
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
                                        new_string += self.current_char
                                        self.advance()
                                        if self.current_char != None:
                                            if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['arith_dlm']:
                                tokens.append(Token(TT_DIVIDE, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char == '=':
                                new_string += self.current_char
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['arith_dlm']:
                                tokens.append(Token(TT_MOD, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char == '=':
                                new_string += self.current_char
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['assignop_dlm']:
                                tokens.append(Token(TT_ASSIGN, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char == '=':
                                new_string += self.current_char
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char == '=':
                            new_string += self.current_char
                            self.advance()
                            if self.current_char != None:
                                if self.current_char in delim['assignop_dlm']:
                                    tokens.append(Token(TT_NOTEQ, new_string, pos_start, self.pos.copy()))
                                    continue
                                else:
                                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                    continue
                    # >
                    case '>':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['assignop_dlm']:
                                tokens.append(Token(TT_GREAT, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char == '=':
                                new_string += self.current_char
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['assignop_dlm']:
                                tokens.append(Token(TT_LESS, new_string, pos_start, self.pos.copy()))
                                continue
                            elif self.current_char == '=':
                                new_string += self.current_char
                                self.advance()
                                if self.current_char != None:
                                    if self.current_char in delim['assignop_dlm']:
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
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['opparenth_dlm']:
                                tokens.append(Token(TT_LPAREN, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # )
                    case ')':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['clparenth_dlm']:
                                tokens.append(Token(TT_RPAREN, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # {
                    case '{':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['opcurlb_dlm']:
                                tokens.append(Token(TT_LCURL, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # }
                    case '}':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['clcurlb_dlm']:
                                tokens.append(Token(TT_RCURL, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # [
                    case '[':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['opsqrb_dlm']:
                                tokens.append(Token(TT_LSQR, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # ]
                    case ']':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['clsqrb_dlm']:
                                tokens.append(Token(TT_RSQR, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # :
                    case ':':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in WHITESPACE:
                                tokens.append(Token(TT_COLON, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # ,
                    case ',':
                        new_string += self.current_char
                        self.advance()
                        if self.current_char != None:
                            if self.current_char in delim['comma_dlm']:
                                tokens.append(Token(TT_COMMA, new_string, pos_start, self.pos.copy()))
                                continue
                            else:
                                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after symbol "{new_string}"'))
                                continue
                    # ;
                    case ';':
                        new_string += self.current_char
                        tokens.append(Token(TT_SEMICOLON, new_string, pos_start, self.pos.copy()))
                        self.advance()
                        continue

            ############### CHAR LITERAL ###############
            elif self.current_char == '\'':
                pos_start = self.pos.copy()
                self.advance()

                # if there is no character after '
                if self.current_char is None:
                    errors.append(LexicalError(pos_start, self.pos.copy(), info='Char values must at least have 1 character stored'))
                    continue

                char_val = self.current_char
                self.advance()

                # if the next character is not an ending single quote
                if self.current_char != '\'':
                    errors.append(LexicalError(pos_start, self.pos.copy(), info='Char values can only store one character'))
                    continue

                self.advance()
                pos_end = self.pos.copy()
                if self.current_char != None and self.current_char in delim['clquotes_dlm']:
                    tokens.append(Token(TT_CHARLIT, char_val, pos_start, pos_end))
                    continue
                else:
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after char lit \'{char_val}\''))
                    continue

            ############### STRING LITERAL ###############
            elif self.current_char == '"':
                pos_start = self.pos.copy()
                self.advance()
                string_val = ''
                
                while self.current_char != None and self.current_char != '"':
                    string_val += self.current_char
                    self.advance()
                
                self.advance()
                pos_end = self.pos.copy()

                if self.current_char != None and self.current_char in delim['cldoublequotes_dlm']:
                    tokens.append(Token(TT_STRINGLIT, string_val, pos_start, pos_end))
                    continue
                else:
                    errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid Delimiter "{self.current_char}" after string lit "{string_val}"'))
                    continue

            ############## IF CHARACTER IS UNRECOGNIZED BY THE COMPILER ##############
            else:
                pos_start = self.pos.copy()
                self.advance()
                errors.append(LexicalError(pos_start, self.pos.copy(), info=f'Invalid character "{self.current_char}"'))
                continue
        
        ############## ALWAYS APPEND EOF at the end of the lexeme table ##############
        tokens.append(Token('EOF', '', self.pos.copy(), self.pos.copy()))
        return tokens, errors

###############################################################
# FOR TESTING PURPOSES ONLY, MODIFY WHEN CONNECTED WITH BACKEND
###############################################################
# this will be the main function to be called by the server to send source code to backend
# this takes 'source' as the source code from the code editor and returns the generated tokens and errors
def lexical_analyze(source):
    lexer = Lexer(source)
    tokens, errors = lexer.tokenize()

    print(f'Text to run: {source}')
    if tokens:
        print('Tokens: ')
        for t in tokens:
            print(f'{t}')
    else:
        print('No tokens generated')
    
    if errors:
        print('Errors: ')
        for e in errors:
            print(f'{e}')
    else:
        print('No errors')
    
    return tokens, errors

###############################################################
# FOR TESTING PURPOSES ONLY, REMOVE WHEN CONNECTED WITH BACKEND
###############################################################
if __name__ == '__main__':
    # ADD TEST CASES HERE FOR TEMPORARY TESTING
    test_inputs = [
        '+. -. *. / % ** += -= ++ - **= *= /= %= < > <= >= == !=',
        'myFunct.ion12 myName4 myFunction3 myName Jian Albrecht Zildjian Albrecht Jian Zildjian'
        'make myFunction',  
        'AND OR NOT ',  
        'append(',          
        'invalid@', 
        '\'W\' "Hello, World!\\n" ', 
        '0000001.1 ',     
        'a, b; c '     
    ]
    for text in test_inputs:
        lexical_analyze(text)
        print("-" * 50)