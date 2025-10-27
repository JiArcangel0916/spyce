# Makes using letters easy instead of manually typing each
import string


##############
# DEFINITIONS  -> From regular definitions
##############
DIGITS = '0123456789'
ALPHABET = string.ascii_letters
ALPHADIG = DIGITS + ALPHABET
WHITESPACE = '\n\t '
COMMENT = '~~'
ASCII = ALPHADIG + string.punctuation
ARITH = '+-/*%'
RELATIONAL = '=!<>'

############
# DELIMITERS
############
delim = {
    'dt_dlm':               set(WHITESPACE + '[' + '{'),
    'bool_dlm':             set(WHITESPACE + ';' + '}'+ ')'),
    'void_dlm':             set(WHITESPACE + '{' + ';'),
    'lit_dlm':              set(WHITESPACE + ARITH + RELATIONAL +':' + ';' + '}' + ')'),
    'int_lit_dlm':          set(WHITESPACE + ARITH + RELATIONAL + ':' + ';' + '}' + ')' + '.'),
    'indentifier_dlm':      set(WHITESPACE + '(' + ')' + '[' + ',' + ';' + '{' + '}'),
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
    'clquotes':             set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + '.'),
    'cldoublequotes_dlm':   set(WHITESPACE + RELATIONAL + ';' + ',' + '}' + ')' + '.' + '+'),
    'comb0_dlm':            set(WHITESPACE + '('),
    'comb1_dlm':            set(WHITESPACE + '{'),
    'comb2_dlm':            set(WHITESPACE + ';'),
    'comb3_dlm':            set(ALPHADIG + '_')
}

################
# RESERVED WORDS 
################
keywords = {
    'int', 'float', 'char', 'string', 'bool', 'say', 'listen', 'AND', 'OR', 'NOT',
    'when', 'elsewhen', 'otherwise', 'choose', 'case', 'default', 'for', 'while',
    'break', 'skip', 'continue', 'len', 'caps', 'small', 'indexOf', 'replace', 'trim',
    'replace', 'trim', 'repeat', 'isEmpty', 'reverse', 'substring', 'contains', 'append',
    'pop', 'insert', 'clear', 'remove', 'concat', 'unique', 'true', 'false', 'make', 'spyce',
    'mix', 'const', 'void', 'giveback', 'this'
}

########
# TOKENS 
########

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
TT_CLEAR = 'clear'
TT_REMOVE = 'remove'
TT_CONCAT = 'concat'

# string methods
TT_CAPS = 'caps'
TT_SMALL = 'small'
TT_REPLACE = 'replace'
TT_TRIM = 'trim'
TT_REPEAT = 'repeat'
TT_ISEMPTY = 'isEmpty'
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
TT_SEMIC = ';'
TT_COLON = ':'
TT_COMMENT = '~~'
TT_COMMA = ','

# LITERALS
TT_INTLIT = 'int literal'
TT_FLOATLIT = 'float literal'
TT_CHARLIT = 'char literal'
TT_STRINGLIT = 'string literal'
TT_COMMENTLIT = 'comment'

# IDENTIFIER
TT_IDENTIFER = 'id'