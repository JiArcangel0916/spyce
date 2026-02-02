from .Error import InvalidSyntaxError

# string (production): list ng list ng string (production set)
CFG = {
    '<program>':[       
        ['<global_var>', '<sub_func>', 'spyce', '(', ')', '->', 'void', '{', '<main_func_body>', 'giveback', '<void>', ';', '}']
    ],

    '<global_var>':[       
        ['const', '<data_type>', '<var_type>', ';', '<global_var>'], 
        ['<data_type>', 'var_type', ';', '<global_var>'],           
        []                                              
    ],

    '<data_type>':[
        ['int'],
        ['float'],
        ['char'],
        ['string'],
        ['bool']
    ],

    '<var_type>':[
        ['id', '=', '<scalvar>', '<scaldec_tail>'],
        ['[', 'int_lit', ']', '<arrtype>']
    ],

    '<arrtype>':[
        ['id', '=', '<1d_val>', '<1d_dec_tail>'],
        ['[', 'int_lit', ']', 'id', '<2d_val>', '<2d_dec_tail>']
    ],

    '<scalvar>':[
        ['listen', '(', ')'],
        ['<expr>']
    ],

    '<scaldec_tail>':[
        [',', 'id', '=', '<scalvar>', '<scaldec_tail>'],
        []
    ],

    '<1d_val>':[
        ['id', '<inner_arr_indx>'],
        ['{', 'element_list', '}']
    ],

    '<inner_arr_indx>':[
        ['[', '<arith_expr>', ']'],
        []
    ],

    '<element_list>':[
        ['<expr>', '<val_tail>'],
        []
    ],
    
    '<val_tail>':[
        [',', '<expr>', '<val_tail>'],
        []
    ],

    '<1d_dec_tail>':[
        [',', 'id', '=', '<1d_val>', '<1d_dec_tail>'],
        []
    ],

    '<2d_val>':[
        ['id'],
        ['{', '<2d_elem>', '}']
    ],

    '<2d_elem>':[
        ['<1d_val>', '<2dval_tail>'],
        []
    ],

    '<2dval_tail>':[
        [',', '<1d_val>', '<2dval_tail>'],
        []
    ],

    '<2d_dec_tail>':[
        [',', 'id', '=', '<2d_val>', '<2d_dec_tail>'],
        []
    ],

    '<sub_func>':[
        ['<sub_funcdec>', '<sub_func>'],
        []
    ],

    '<sub_funcdec>':[
        ['make', 'id', '(', '<parameters>', ')', '->', '<func_ret>']
    ],

    '<parameters>':[
        ['<data_type>', '<1d_indx>', 'id', '<par_tail>'],
        []
    ],

    '<1d_indx>':[
        ['[', 'int_lit', ']', '<2d_indx>'],
        []
    ],

    '<2d_indx>':[
        ['[', 'int_lit', ']'],
        []
    ],

    '<par_tail>':[
        [',', '<data_type>', '<1d_indx>', 'id', '<par_tail>'],
        []
    ],

    '<func_ret>':[
        ['<data_type>', '<func_type>'],
        ['void', '{', '<func_body>', '}'],
    ],

    '<func_type>':[
        ['{', '<func_body>', '}'],
        ['[', ']', '<arr_func>'],
    ],

    '<arr_func>':[
        ['{', '<func_body>', '}'],
        ['[', ']', '{', '<func_body>', '}'],
    ],

    '<func_body>':[
        ['<stmnt>', '<func_body>'],
        []
    ],

    '<main_func_body>':[
        ['<main_stmnt>', '<func_body>'],
        []
    ],

    '<void>':[
        ['void'],
        []
    ],

    '<main_stmnt>':[
        ['<local_var>', ';'],
        ['id', '<id_stmnt>', ';'],
        ['<unary_op>', '<id_val>', ';'],
        ['<IO>', ';'],
        ['<conditional>'],
        ['<iterative>']
    ],

    '<stmnt>':[
        ['<main_stmnt>'],
        ['<giveback>', ';'],
    ],

    '<id_stmnt>':[
        ['<index_access>', '<unary_or_assign>'],
        ['(', '<args>', ')']
    ],

    '<unary_or_assign>':[
        ['<unary_op>'],
        ['<assign_type>']
    ],

    '<unary_op>':[
        ['++'],
        ['--']
    ],

    '<local_var>':[
        ['const', '<data_type>', '<var_type>'],
        ['<data_type>', '<var_type>']
    ],

    '<index_access>':[
        ['[', '<arith_expr>', ']', '<2d_access>'],
        []
    ],
    
    '<2d_access>':[
        ['[', '<arith_expr>', ']'],
        []
    ],

    '<args>':[
        ['<expr>', '<val_tail>'],
        []
    ],

    '<assign_type>':[
        ['=', '<expr>'],
        ['<cmpnd_op>', '<cmpnd_operand>']
    ],

    '<cmpnd_op>':[
        ['+='],
        ['-='],
        ['*='],
        ['/='],
        ['**='],
        ['%=']
    ],

    '<cmpnd_operand>':[
        ['<numstring_val>'],
        ['<id_val>'],
    ],

    '<numstring_val>':[
        ['int_lit'],
        ['float_lit'],
        ['string_lit'],
    ],

    '<id_val>':[
        ['id', '<indx_access>']
    ],

    '<expr>':[
        ['<logical_or_expr>']
    ],

    '<logical_or_expr>':[
        ['<and_expr>', '<chain_or>']
    ],

    '<chain_or>':[
        ['OR', '<and_expr> <chain_or>'],
        []
    ],

    '<and_expr>':[
        ['<not_expr>', '<chain_and>']
    ],

    '<chain_and>':[
        ['AND', '<not_expr>', '<chain_and>'],
        []
    ],

    '<not_expr>':[
        ['NOT', '<equal_expr>'],
        ['<equal_expr>']
    ],

    '<equal_expr>':[
        ['<equal_operand>', '<equal_expr_tail>']
    ],

    '<equal_operand>':[
        ['<relational_expr>'],
        ['<bool_lit>'],
        ['char_lit'],
        ['string_lit']
    ],

    '<bool_lit>':[
        ['true'],
        ['false'],
    ],

    '<equal_expr_tail>':[
        ['==', '<equal_operand>'],
        ['!=', '<equal_operand>'],
        []
    ],

    '<relational_expr>':[
        ['<arith_expr>', '<relational_expr_tail>']
    ],

    '<relational_expr_tail>':[
        ['<relation_op>', '<arith_expr>'],
        []
    ],

    '<relation_op>':[
        ['>'],
        ['<'],
        ['>='],
        ['<=']
    ],

    '<arith_expr>':[
        ['<arith_operand>', '<arith_expr_tail>']  
    ],

    '<arith_expr_tail>':[
        ['+', '<arith_operand>', '<arith_expr_tail>'],
        ['-', '<arith_operand>', '<arith_expr_tail>'],
        []
    ],

    '<arith_operand>':[
        ['<expo_arith_operand>', '<arith_operand_tail>']
    ],

    '<arith_operand_tail>':[
        ['*', '<expo_arith_operand>', '<arith_operand_tail>'],
        ['/', '<expo_arith_operand>', '<arith_operand_tail>'],
        ['%', '<expo_arith_operand>', '<arith_operand_tail>'],
        []
    ],

    '<expo_arith_operand>':[
        ['<operand>', '<expo_arith_operand_tail>']
    ],

    '<expo_arith_operand_tail>':[
        ['**', '<expo_arith_operand_tail>'],
        []
    ],

    '<operand>':[
        ['<num_lit>'],
        ['id', '<id_operand>'],
        ['str', '(', '<expr>', ')'],
        ['(', '<expr>', ')']
    ],

    '<id_operand>':[
        ['<indx_access>', '<unary_or_null>'],
        ['(', '<args>', ')']
    ],

    '<unary_or_null>':[
        ['<unary_op>'],
        []
    ],

    '<unary>':[
        ['<id_val>', '<unary_op>'],
        ['<unary_op>', '<id_val>']
    ],

    '<num_lit>':[
        ['int_lit'],
        ['float_lit']
    ],

    '<IO>':[
        ['say', '(', '<expr>', ')'],
        ['listen', '(', ')']
    ],

    '<giveback>':[
        ['giveback', '<ret_val>']
    ],

    '<ret_val>':[
        ['void'],
        ['<expr>'],
    ],

    '<conditional>':[
        ['when', '(', '<expr>', ')', '{', '<ctrl_block>', '}', '<else_tail>', '<otherwise>'],
        ['choose', '(', '<id_val>', ')', '{', '<case_tail>', 'default', ':', '<ctrl_block>', '}']
    ],

    '<ctrl_block>':[
        ['<ctrl_item>', '<ctrl_block_tail>']
    ],

    '<ctrl_block_tail>':[
        ['<ctrl_item>', '<ctrl_block_tail>'],
        []
    ],

    '<ctrl_item>':[
        ['<stmnt>'],
        ['<ctrl_stmnt>', ';']
    ],

    '<ctrl_stmnt>':[
        ['break'],
        ['skip'],
        ['continue']
    ],
    
    '<else_tail>':[
        ['elsewhen', '(', '<expr>', ')', '{', '<ctrl_block>', '}', '<else_tail>'],
        []
    ],

    '<otherwise>':[
        ['otherwise', '{', '<ctrl_block>', '}'],
        []
    ],

    '<case_tail>':[
        ['case', '<literal>', ':', '<ctrl_block>', '<case_tail>'],
        []
    ],

    '<literal>':[
        ['<numstring_val>'],
        ['char_lit'],
        ['<bool_lit>']
    ],

    '<iterative>':[
        ['for', '(', '<ctrl_var>', '<for_bool>', '<for_unary>', ')', '{', '<ctrl_block>', '}'],
        ['while', '(', '<expr>', ')', '{', '<ctrl_block>', '}']
    ],

    '<ctrl_var>':[
        ['<local_var>', ';'],
        ['<id_val>', '=', '<assign_operand>', ';'],
        [';']
        
    ],

    '<assign_operand>':[
        ['<scalvar>'],
        ['id', '<func_or_indx>']
    ],

    '<func_or_indx>':[
        ['(', '<args>', ')'],
        ['<1d_indx>']
    ],

    '<for_bool>':[
        ['<expr>', ';'],
        [';']
    ],

    '<for_unary>':[
        ['<unary>'],
        []
    ]
}

# string (production) : object (string:list(production, pangilang production))
PREDICT_SET = {
    '<program>':{   # correct
        'const':    ['<program>', 0],       
        'int':      ['<program>', 0],
        'float':    ['<program>', 0],
        'char':     ['<program>', 0],
        'string':   ['<program>', 0],
        'bool':     ['<program>', 0],
        'make':     ['<program>', 0],
        'spyce':    ['<program>', 0]
    },

    '<global_var>':{   # correct
        'const':    ['<global_var>', 0],    
        'int':      ['<global_var>', 1],    
        'float':    ['<global_var>', 1],
        'char':     ['<global_var>', 1],
        'string':   ['<global_var>', 1],
        'bool':     ['<global_var>', 1],
        'make':     ['<global_var>', 2],     
        'spyce':    ['<global_var>', 2]
    },

    '<data_type>':{   # correct
        'int':      ['<data_type>', 0],
        'float':    ['<data_type>', 1],
        'char':     ['<data_type>', 2],
        'string':   ['<data_type>', 3],
        'bool':     ['<data_type>', 4]
    },

    '<var_type>':{   # correct
        'id':      ['<var_type>', 0],      
        '[':    ['<var_type>', 1]             
    },

    '<arrtype>':{
        'id':   ['<arrtype>', 0],
        '[':    ['<arrtype>', 1]
    },

    '<scalvar>':{
        'listen':       ['<scalvar>', 0],
        'NOT':          ['<scalvar>', 1],
        'int_lit':      ['<scalvar>', 1],
        'float_lit':    ['<scalvar>', 1],
        'id':           ['<scalvar>', 1],
        'str':          ['<scalvar>', 1],
        '(':            ['<scalvar>', 1],
        '++':           ['<scalvar>', 1],
        '--':           ['<scalvar>', 1],
        'true':         ['<scalvar>', 1],
        'false':        ['<scalvar>', 1],
        'char_lit':     ['<scalvar>', 1],
        'string_lit':   ['<scalvar>', 1]
    },

    '<scaldec_tail>':{
        ',':['<scaldec_tail>', 0],
        ';':['<scaldec_tail>', 1]
    },

    '<1d_val>':{   
      'id':['<1d_val>', 0],
      '{': ['<1d_val>', 1]  
    },

    '<inner_arr_indx>':{
        '[':['<inner_arr_indx>', 0],
        ',':['<inner_arr_indx>', 1],
        ';':['<inner_arr_indx>', 1],
        '}':['<inner_arr_indx>', 1]
    },

    '<element_list>':{
        'NOT':          ['<element_list>', 0],
        'int_lit':      ['<element_list>', 0],
        'float_lit':    ['<element_list>', 0],
        'id':           ['<element_list>', 0],
        'str':          ['<element_list>', 0],
        '(':            ['<element_list>', 0],
        '++':           ['<element_list>', 0],
        '--':           ['<element_list>', 0],
        'true':         ['<element_list>', 0],
        'false':        ['<element_list>', 0],
        'char_lit':     ['<element_list>', 0],
        'string_lit':   ['<element_list>', 0],
        '}':            ['<element_list>', 1]
    },

    '<val_tail>':{   # correct
        ',':['<val_tail>', 0],
        '}':['<val_tail>', 1],
        ')':['<val_tail>', 1]
    },

    '<1d_dec_tail>':{
        ',':['<1d_dec_tail>', 0],
        ';':['<1d_dec_tail>', 1]
    },

    '<2d_val>':{
        'id':   ['<2d_val>', 0],
        '{':    ['<2d_val>', 1]
    },

    '<2d_elem>':{
        'id':   ['<2d_elem>', 0],
        '{':    ['<2d_elem>', 0],
        '}':    ['<2d_elem>', 1]
    },

    '<2d_val_tail>':{
        ',':   ['<2d_val_tail>', 0],
        '}':   ['<2d_val_tail>', 1]
    },

    '<2d_dec_tail>':{
        ',':   ['<2d_dec_tail>', 0],
        ';':   ['<2d_dec_tail>', 1]
    },

    '<sub_func>':{   
        'make': ['<sub_func>', 0],
        'spyce':['<sub_func>', 1]
    },

    '<sub_funcdec>':{   
        'make':['<sub_funcdec>', 0]
    },

    '<parameters>':{   
        'int':      ['<parameters>', 0],
        'float':    ['<parameters>', 0],
        'char':     ['<parameters>', 0],
        'string':   ['<parameters>', 0],
        'bool':     ['<parameters>', 0],
        ')':        ['<parameters>', 1]
    },

    '<1d_indx>':{   
        '[':    ['<1d_indx>', 0],
        'id':   ['<1d_indx>', 1],
        ';':    ['<1d_indx>', 1]
    },

    '<2d_indx>':{  
        '[':    ['<2d_indx>', 0],
        'id':   ['<2d_indx>', 1],
        ';':    ['<2d_indx>', 1]
    },

    '<par_tail>':{  
        ',':['<par_tail>', 0],
        ')':['<par_tail>', 1]
    },

    '<func_ret>':{   
       'int':   ['<func_ret>', 0],
       'float': ['<func_ret>', 0], 
       'char':  ['<func_ret>', 0], 
       'string':['<func_ret>', 0], 
       'bool':  ['<func_ret>', 0], 
       'void':  ['<func_ret>', 1]
    },

    '<func_type>':{   
        '{':['<func_type>', 0],
        '[':['<func_type>', 1]
    },

    '<arr_func>':{  
        '{':['<arr_func>', 0],
        '[':['<arr_func>', 1]
    },

    '<func_body>':{   
        'const':        ['<func_body>', 0],
        'int':          ['<func_body>', 0],
        'float':        ['<func_body>', 0],
        'char':         ['<func_body>', 0],
        'string':       ['<func_body>', 0],
        'bool':         ['<func_body>', 0],
        'id':           ['<func_body>', 0],     
        '++':           ['<func_body>', 0],
        '--':           ['<func_body>', 0],      
        'say':          ['<func_body>', 0],
        'listen':       ['<func_body>', 0],     
        'when':         ['<func_body>', 0],
        'choose':       ['<func_body>', 0],
        'for':          ['<func_body>', 0],
        'while':        ['<func_body>', 0],
        'giveback':     ['<func_body>', 0],
        '}':            ['<func_body>', 1]
    },

    '<main_func_body>':{   
        'const':        ['<main_func_body>', 0],
        'int':          ['<main_func_body>', 0],
        'float':        ['<main_func_body>', 0],
        'char':         ['<main_func_body>', 0],
        'string':       ['<main_func_body>', 0],
        'bool':         ['<main_func_body>', 0],
        'id':           ['<main_func_body>', 0],     
        '++':           ['<main_func_body>', 0],
        '--':           ['<main_func_body>', 0],      
        'say':          ['<main_func_body>', 0],
        'listen':       ['<main_func_body>', 0],     
        'when':         ['<main_func_body>', 0],
        'choose':       ['<main_func_body>', 0],
        'for':          ['<main_func_body>', 0],
        'while':        ['<main_func_body>', 0],
        'giveback':     ['<main_func_body>', 1]
    },

    '<void>':{
        'void':['<void>', 0],
        ';':['<void>', 1] 
    },

    '<main_stmnt>':{   
        'const':        ['<stmnt>', 0],
        'int':          ['<stmnt>', 0],
        'float':        ['<stmnt>', 0],
        'char':         ['<stmnt>', 0],
        'string':       ['<stmnt>', 0],
        'bool':         ['<stmnt>', 0],
        'id':           ['<stmnt>', 1],     
        '++':           ['<stmnt>', 2],
        '--':           ['<stmnt>', 2],      
        'say':          ['<stmnt>', 3],
        'listen':       ['<stmnt>', 3],     
        'when':         ['<stmnt>', 4],
        'choose':       ['<stmnt>', 4],
        'for':          ['<stmnt>', 5],
        'while':        ['<stmnt>', 5]
    },

    '<main_stmnt>':{   
        'const':        ['<stmnt>', 0],
        'int':          ['<stmnt>', 0],
        'float':        ['<stmnt>', 0],
        'char':         ['<stmnt>', 0],
        'string':       ['<stmnt>', 0],
        'bool':         ['<stmnt>', 0],
        'id':           ['<stmnt>', 0],     
        '++':           ['<stmnt>', 0],
        '--':           ['<stmnt>', 0],      
        'say':          ['<stmnt>', 0],
        'listen':       ['<stmnt>', 0],     
        'when':         ['<stmnt>', 0],
        'choose':       ['<stmnt>', 0],
        'for':          ['<stmnt>', 0],
        'while':        ['<stmnt>', 0],
        'giveback':     ['<stmnt>', 1]
    },

    '<id_stmnt>':{   
        '[':    ['<id_stmnt>', 0],
        '++':   ['<id_stmnt>', 0],
        '--':   ['<id_stmnt>', 0],
        '=':    ['<id_stmnt>', 0],
        '+=':   ['<id_stmnt>', 0],
        '-=':   ['<id_stmnt>', 0],
        '*=':   ['<id_stmnt>', 0],
        '/=':   ['<id_stmnt>', 0],
        '**=':  ['<id_stmnt>', 0],
        '%=':   ['<id_stmnt>', 0],
        '(':    ['<id_stmnt>', 1],
    },

    '<unary_or_assign>':{
        '++':   ['<unary_or_assign>', 0],
        '--':   ['<unary_or_assign>', 0],
        '=':    ['<unary_or_assign>', 1],
        '+=':   ['<unary_or_assign>', 1],
        '-=':   ['<unary_or_assign>', 1],
        '*=':   ['<unary_or_assign>', 1],
        '/=':   ['<unary_or_assign>', 1],
        '**=':  ['<unary_or_assign>', 1],
        '%=':   ['<unary_or_assign>', 1],
    },

    '<unary_op>':{   # correct
        '++':['<unary_op>', 0],
        '--':['<unary_op>', 1]
    },

    '<local_var>':{   # correct
        'const':    ['<local_var>', 0],
        'int':      ['<local_var>', 1],
        'float':    ['<local_var>', 1],
        'char':     ['<local_var>', 1],
        'string':   ['<local_var>', 1],
        'bool':     ['<local_var>', 1]
    },

    ############ STOPPED HERE

    '<expr>':{      # correct BUT HAS AMBIGUITY WITH (
        'int_lit':      ['<expr>', 0],
        'float_lit':    ['<expr>', 0],
        'string_lit':   ['<expr>', 0],
        'null':         ['<expr>', 0],
        'id':           ['<expr>', 0],
        '++':           ['<expr>', 0],
        '--':           ['<expr>', 0],
        'true':         ['<expr>', 1],
        'false':        ['<expr>', 1],
        '(':            ['<expr>', 1],
        'NOT':          ['<expr>', 1]
    },

    

    '<arith>':{   # correct
        'int_lit':      ['<arith>', 0],
        'float_lit':    ['<arith>', 0],
        'string_lit':   ['<arith>', 0],
        'null':         ['<arith>', 0],
        'id':           ['<arith>', 0],
        '++':           ['<arith>', 0],
        '--':           ['<arith>', 0],
        '(':            ['<arith>', 0]
    },

    '<arith_operand>':{   # correct
        'int_lit':      ['<arith_operand>', 0],
        'float_lit':    ['<arith_operand>', 1],
        'string_lit':   ['<arith_operand>', 2],
        'null':         ['<arith_operand>', 3],
        'id':           ['<arith_operand>', 4],
        '++':           ['<arith_operand>', 5],
        '--':           ['<arith_operand>', 5],
        '(':            ['<arith_operand>', 6]
    },

    '<unary>':{   # correct
        'id':['<unary>', 0],
        '++':['<unary>', 1],
        '--':['<unary>', 1]
    },

    

    '<unary_or_id>':{      # correct
        '++':   ['<unary_or_id>', 0],
        '--':   ['<unary_or_id>', 0],
        '+':    ['<unary_or_id>', 1],
        '-':    ['<unary_or_id>', 1],
        '*':    ['<unary_or_id>', 1],
        '/':    ['<unary_or_id>', 1],
        '**':   ['<unary_or_id>', 1],
        '%':    ['<unary_or_id>', 1],
        ']':    ['<unary_or_id>', 1],
        ',':    ['<unary_or_id>', 1],
        ')':    ['<unary_or_id>', 1],
        '}':    ['<unary_or_id>', 1],
        ';':    ['<unary_or_id>', 1]
    },

    '<chain_arith>':{      # correct
        '+':    ['<chain_arith>', 0],
        '-':    ['<chain_arith>', 0],
        '*':    ['<chain_arith>', 0],
        '/':    ['<chain_arith>', 0],
        '**':   ['<chain_arith>', 0],
        '%':    ['<chain_arith>', 0],
        ']':    ['<chain_arith>', 1],
        ',':    ['<chain_arith>', 1],
        ')':    ['<chain_arith>', 1],
        '}':    ['<chain_arith>', 1],
        ';':    ['<chain_arith>', 1]
    },

    '<binary_op>':{   # correct
        '+':    ['<binary_op>', 0],
        '-':    ['<binary_op>', 1],
        '*':    ['<binary_op>', 2],
        '/':    ['<binary_op>', 3],
        '**':   ['<binary_op>', 4],
        '%':    ['<binary_op>', 5]
    },

    '<logical>':{      # correct
        'true':     ['<logical>', 0],
        'false':    ['<logical>', 0],  
        '(':        ['<logical>', 0],  
        'NOT':      ['<logical>', 0]
    },

    '<or_expr>':{      # correct
        'true':     ['<or_expr>', 0],
        'false':    ['<or_expr>', 0],  
        '(':        ['<or_expr>', 0],  
        'NOT':      ['<or_expr>', 0]  
    },

    '<and_expr>':{      # correct
        'true':     ['<and_expr>', 0],
        'false':    ['<and_expr>', 0],  
        '(':        ['<and_expr>', 0],  
        'NOT':      ['<and_expr>', 0]
    },

    '<and_operand>':{      # correct
        'true':         ['<and_operand>', 0], 
        'false':        ['<and_operand>', 0],
        '(':            ['<and_operand>', 0],
        'NOT':          ['<and_operand>', 1]
    },

    '<logical_operand>':{   # correct
        'true':         ['<logical_operand>', 0], 
        'false':        ['<logical_operand>', 0], 
        '(':            ['<logical_operand>', 1]
    },

    '<not_expr>':{   # correct BUT WITH AMBIGUITY WITH (<RELATIONAL>) AND (<LOGICAL>)
        '(':            ['<not_expr>', 0], 
        'true':         ['<not_expr>', 1], 
        'false':        ['<not_expr>', 1]
    },

    '<chain_or>':{      # correct
        'OR':   ['<chain_or>', 0],
        ',':    ['<chain_or>', 1],
        '}':    ['<chain_or>', 1],
        ')':    ['<chain_or>', 1],
        ';':    ['<chain_or>', 1]
    },

    '<chain_and>':{      # correct
        'AND':  ['<chain_and>', 0],
        'OR':   ['<chain_and>', 1],
        ',':    ['<chain_and>', 1],
        '}':    ['<chain_and>', 1],
        ')':    ['<chain_and>', 1],
        ';':    ['<chain_and>', 1]
    },
    
    '<relational>':{   # correct BUT SHOULD HAVE ID
        'int_lit':      ['<relational>', 0],
        'float_lit':    ['<relational>', 0],
        'char_lit':     ['<relational>', 0],
        'string_lit':   ['<relational>', 0],
        'true':         ['<relational>', 0],
        'false':        ['<relational>', 0],
        'null':         ['<relational>', 0],
        '(':            ['<relational>', 0]
    },

    '<relation_operand>':{   # correct BUT SHOULD HAVE ID
        'int_lit':      ['<relation_operand>', 0],
        'float_lit':    ['<relation_operand>', 0],
        'char_lit':     ['<relation_operand>', 0],
        'string_lit':   ['<relation_operand>', 0],
        'true':         ['<relation_operand>', 0],
        'false':        ['<relation_operand>', 0],
        'null':         ['<relation_operand>', 1],
        '(':            ['<relation_operand>', 2]
    },

    '<literal>':{   # correct
        'int_lit':      ['<literal>', 0],
        'float_lit':    ['<literal>', 1],
        'char_lit':     ['<literal>', 2],
        'string_lit':   ['<literal>', 3],
        'true':         ['<literal>', 4],
        'false':        ['<literal>', 4]
    },

    '<bool_lit>':{   # correct
        'true':   ['<bool_lit>', 0],
        'false':  ['<bool_lit>', 1]
    },

    '<relation_op>':{   # correct
        '>':    ['<relation_op>', 0],
        '<':    ['<relation_op>', 1],
        '>=':   ['<relation_op>', 2],
        '<=':   ['<relation_op>', 3],
        '==':   ['<relation_op>', 4],
        '!=':   ['<relation_op>', 5]
    },    

    '<assign_type>':{   # correct
        '=':    ['<assign_type>', 0],
        '+=':   ['<assign_type>', 1],
        '-=':   ['<assign_type>', 1],
        '*=':   ['<assign_type>', 1],
        '/=':   ['<assign_type>', 1],
        '**=':  ['<assign_type>', 1],
        '%=':   ['<assign_type>', 1],
    },

    '<assign_operand>':{      # correct BUT WITH AMBIGUITY WITH NULL AND ID
        'listen':       ['<assign_operand>', 0],
        'null':         ['<assign_operand>', 1],
        'id':           ['<assign_operand>', 2],
        'int_lit':      ['<assign_operand>', 3],
        'float_lit':    ['<assign_operand>', 3],
        'string_lit':   ['<assign_operand>', 3],
        '++':           ['<assign_operand>', 3],
        '--':           ['<assign_operand>', 3],
        '(':            ['<assign_operand>', 3],
        'NOT':          ['<assign_operand>', 3],
        'true':         ['<assign_operand>', 3],
        'false':        ['<assign_operand>', 3]
    },

    '<func_or_indx>':{   # correct
        '(': ['<func_or_indx>', 0],
        '[': ['<func_or_indx>', 1],
        ';': ['<func_or_indx>', 1]
    },

    '<cmpnd_op>':{   # correct
        '+=':   ['<cmpnd_op>', 0],
        '-=':   ['<cmpnd_op>', 1],
        '*=':   ['<cmpnd_op>', 2],
        '/=':   ['<cmpnd_op>', 3],
        '**=':  ['<cmpnd_op>', 4],
        '%=':   ['<cmpnd_op>', 5],
    },

    '<cmpnd_operand>':{   # correct
        'int_lit':      ['<cmpnd_operand>', 0],
        'float_lit':    ['<cmpnd_operand>', 1],
        'string_lit':   ['<cmpnd_operand>', 2],
        'id':           ['<cmpnd_operand>', 3]
    },

    '<giveback>':{   # correct
        'giveback':['<giveback>', 0]
    },

    '<ret_val>':{      # correct
        'void':         ['<ret_val>', 0],
        'int_lit':      ['<ret_val>', 1],
        'float_lit':    ['<ret_val>', 1],
        'string_lit':   ['<ret_val>', 1],
        'null':         ['<ret_val>', 1],
        'id':           ['<ret_val>', 1],
        '++':           ['<ret_val>', 1],
        '--':           ['<ret_val>', 1],
        '(':            ['<ret_val>', 1],
        'NOT':          ['<ret_val>', 1],
        'true':         ['<ret_val>', 1],
        'false':        ['<ret_val>', 1],
        'char_lit':     ['<ret_val>', 2]
    },

    '<IO>':{   # correct
        'say':      ['<IO>', 0],
        'listen':   ['<IO>', 1]
    },

    '<args>':{      # correct BUT SHOULD HAVE ARRAY LITERALS AND CHAR
        'int_lit':      ['<args>', 0],
        'float_lit':    ['<args>', 0],
        'string_lit':   ['<args>', 0],
        'null':         ['<args>', 0],
        'id':           ['<args>', 0],
        '++':           ['<args>', 0],
        '--':           ['<args>', 0],
        '(':            ['<args>', 0],
        'NOT':          ['<args>', 0],
        'true':         ['<args>', 0],
        'false':        ['<args>', 0],
        ')':            ['<args>', 1]
    },

    '<conditional>':{   # correct
        'when':     ['<conditional>', 0],
        'choose':   ['<conditional>', 1]
    },

    '<ctrl_block>':{      # correct
        'const':        ['<ctrl_block>', 0],
        'int':          ['<ctrl_block>', 0],
        'float':        ['<ctrl_block>', 0],
        'char':         ['<ctrl_block>', 0],
        'string':       ['<ctrl_block>', 0],
        'bool':         ['<ctrl_block>', 0],
        'id':           ['<ctrl_block>', 0],
        '++':           ['<ctrl_block>', 0],
        '--':           ['<ctrl_block>', 0],
        'giveback':     ['<ctrl_block>', 0],
        'say':          ['<ctrl_block>', 0],
        'listen':       ['<ctrl_block>', 0],
        'when':         ['<ctrl_block>', 0],
        'choose':       ['<ctrl_block>', 0],
        'for':          ['<ctrl_block>', 0],
        'while':        ['<ctrl_block>', 0],
        'break':        ['<ctrl_block>', 0],
        'skip':         ['<ctrl_block>', 0],
        'continue':     ['<ctrl_block>', 0]
    },

    '<ctrl_block_tail>':{      # correct
        'const':        ['<ctrl_block_tail>', 0],
        'int':          ['<ctrl_block_tail>', 0],
        'float':        ['<ctrl_block_tail>', 0],
        'char':         ['<ctrl_block_tail>', 0],
        'string':       ['<ctrl_block_tail>', 0],
        'bool':         ['<ctrl_block_tail>', 0],
        'id':           ['<ctrl_block_tail>', 0],
        '++':           ['<ctrl_block_tail>', 0],
        '--':           ['<ctrl_block_tail>', 0],
        'giveback':     ['<ctrl_block_tail>', 0],
        'say':          ['<ctrl_block_tail>', 0],
        'listen':       ['<ctrl_block_tail>', 0],
        'when':         ['<ctrl_block_tail>', 0],
        'choose':       ['<ctrl_block_tail>', 0],
        'for':          ['<ctrl_block_tail>', 0],
        'while':        ['<ctrl_block_tail>', 0],
        'break':        ['<ctrl_block_tail>', 0],
        'skip':         ['<ctrl_block_tail>', 0],
        'continue':     ['<ctrl_block_tail>', 0],
        '}':            ['<ctrl_block_tail>', 1],
        'case':         ['<ctrl_block_tail>', 1],
        'default':      ['<ctrl_block_tail>', 1]
    },

    '<ctrl_item>':{      # correct
        'const':        ['<ctrl_item>', 0],
        'int':          ['<ctrl_item>', 0],
        'float':        ['<ctrl_item>', 0],
        'char':         ['<ctrl_item>', 0],
        'string':       ['<ctrl_item>', 0],
        'bool':         ['<ctrl_item>', 0],
        'id':           ['<ctrl_item>', 0],
        '++':           ['<ctrl_item>', 0],
        '--':           ['<ctrl_item>', 0],
        'giveback':     ['<ctrl_item>', 0],
        'say':          ['<ctrl_item>', 0],
        'listen':       ['<ctrl_item>', 0],
        'when':         ['<ctrl_item>', 0],
        'choose':       ['<ctrl_item>', 0],
        'for':          ['<ctrl_item>', 0],
        'while':        ['<ctrl_item>', 0],
        'break':        ['<ctrl_item>', 1],
        'skip':         ['<ctrl_item>', 1],
        'continue':     ['<ctrl_item>', 1]
    },

    '<ctrl_stmnt>':{   # correct
        'break':    ['<ctrl_stmnt>', 0],
        'skip':     ['<ctrl_stmnt>', 1],
        'continue': ['<ctrl_stmnt>', 2]
    },
    
    '<else_tail>':{      # correct
        'elsewhen':     ['<else_tail>', 0],
        'otherwise':    ['<else_tail>', 1],
        'const':        ['<else_tail>', 1],
        'int':          ['<else_tail>', 1],
        'float':        ['<else_tail>', 1],
        'char':         ['<else_tail>', 1],
        'string':       ['<else_tail>', 1],
        'bool':         ['<else_tail>', 1],
        'id':           ['<else_tail>', 1],
        '++':           ['<else_tail>', 1],
        '--':           ['<else_tail>', 1],
        'giveback':     ['<else_tail>', 1],
        'say':          ['<else_tail>', 1],
        'listen':       ['<else_tail>', 1],
        'when':         ['<else_tail>', 1],
        'choose':       ['<else_tail>', 1],
        'for':          ['<else_tail>', 1],
        'while':        ['<else_tail>', 1],
        'break':        ['<else_tail>', 1],
        'skip':         ['<else_tail>', 1],
        'continue':     ['<else_tail>', 1],
        '}':            ['<else_tail>', 1],
        'case':         ['<else_tail>', 1],
        'default':      ['<else_tail>', 1]

    },

    '<otherwise>':{      # correct
        'otherwise':    ['<otherwise>', 0],
        'const':        ['<otherwise>', 1],
        'int':          ['<otherwise>', 1],
        'float':        ['<otherwise>', 1],
        'char':         ['<otherwise>', 1],
        'string':       ['<otherwise>', 1],
        'bool':         ['<otherwise>', 1],
        'id':           ['<otherwise>', 1],
        '++':           ['<otherwise>', 1],
        '--':           ['<otherwise>', 1],
        'giveback':     ['<otherwise>', 1],
        'say':          ['<otherwise>', 1],
        'listen':       ['<otherwise>', 1],
        'when':         ['<otherwise>', 1],
        'choose':       ['<otherwise>', 1],
        'for':          ['<otherwise>', 1],
        'while':        ['<otherwise>', 1],
        'break':        ['<otherwise>', 1],
        'skip':         ['<otherwise>', 1],
        'continue':     ['<otherwise>', 1],
        '}':            ['<otherwise>', 1],
        'case':         ['<otherwise>', 1],
        'default':      ['<otherwise>', 1]
    },

    '<case_tail>':{      # correct
        'case':     ['<case_tail>', 0],
        'default':  ['<case_tail>', 1]
    },

    '<iterative>':{   # correct
        'for':      ['<iterative>', 0],
        'while':    ['<iterative>', 1]
    },

    '<ctrl_var>':{   # correct
        'const':    ['<ctrl_var>', 0],
        'int':      ['<ctrl_var>', 0],
        'float':    ['<ctrl_var>', 0],
        'char':     ['<ctrl_var>', 0],
        'string':   ['<ctrl_var>', 0],
        'bool':     ['<ctrl_var>', 0],
        'id':       ['<ctrl_var>', 1],
        ';':        ['<ctrl_var>', 2]
    },

    '<for_bool>':{      # correct
        'true':         ['<for_bool>', 0],
        'false':        ['<for_bool>', 0],
        '(':            ['<for_bool>', 0],
        'NOT':          ['<for_bool>', 0],
        ';':            ['<for_bool>', 1]
    },

    '<for_unary>':{   # correct
        'id':   ['<for_unary>', 0],
        '++':   ['<for_unary>', 0],
        '--':   ['<for_unary>', 0],
        ')':    ['<for_unary>', 1]
    }
}

class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens                        # Tokens read by lexer
        self.token_idx = 0                          # Used to tell which index to read from the list of tokens
        self.curr_token = tokens[self.token_idx]    # Points to the current token based on the index
    
    def advance(self):
        while True:
            self.token_idx += 1
            if self.token_idx < len(self.tokens):
                self.curr_token = self.tokens[self.token_idx]
                if self.curr_token.type not in ['\n', ' ', '\\n', 'space']:      # Skip whitespaces
                    break
            else:
                self.curr_token = None
                break
        return self.curr_token, self.prev_token
    
    ################################
    # Main syntax analzyer algorithm
    ################################
    def syntax_analyze(self):
        stack = ['<program>']
        error = None
        prev_popped_nonterminal = None

        while stack:
            print(stack)            ##### used to track which path the syntax goes (Can be removed)
            top = stack[-1]
            if self.curr_token is None or self.curr_token.type == 'EOF':             # If there are no more tokens or reached the EOF
                self.curr_token = type('Token', (object,), {                         # Point to token indicating the EOF
                    'type': 'EOF',
                    'pos_start': self.tokens[-1].pos_end if self.tokens else None,
                    'pos_end': self.tokens[-1].pos_end if self.tokens else None
                })()

            if is_nonterminal(top):                                                 # If top of stack is non-terminal
                if top in PREDICT_SET and self.curr_token.type in PREDICT_SET[top]: # Check if non-terminal is in the predict set and the current token is in the predict set of the non-terminal
                    prod_key = PREDICT_SET[top][self.curr_token.type]               # Gets the list in the predict set where the top and current token is found
                    prod = CFG[prod_key[0]][prod_key[1]]                            # Gets the reference of the predict set from the CFG (which production and product set)
                    stack.pop()
                    prev_popped_nonterminal = top
                    stack.extend(reversed(prod))
                else:
                    expected_tokens = list(PREDICT_SET[top].keys())                 # If non-terminal is not in the predict set, error
                    error = InvalidSyntaxError(self.curr_token.pos_start, self.curr_token.pos_end, f'Unexpected token -> {self.curr_token.type} <- \nExpected tokens: {expected_tokens}')
                    break
            else:                                                                   # If terminal, check if the top of the stack is the same as the terminal
                stack.pop()
                if top == self.curr_token.type:
                    self.advance()
                    prev_popped_nonterminal = None
                else:                                                               # Getting expected tokens to put in the error message                          
                    if prev_popped_nonterminal and is_nonterminal(prev_popped_nonterminal):
                        expected_tokens = list(get_first_set(prev_popped_nonterminal))
                        if top not in expected_tokens:
                            expected_tokens.append(top)
                    else:
                        expected_tokens = [top]
                    if self.curr_token.type in expected_tokens:
                        expected_tokens.remove(self.curr_token.type)
                    error = InvalidSyntaxError(self.curr_token.pos_start, self.curr_token.pos_end, f'Unexpected Token -> {self.curr_token.type} <-\nExpected tokens: {expected_tokens}')
                    break
        if error:
            return error
        return []

# Function to return a boolean whether a text is a non-terminal by checking if it starts and ends with < and > respectively
def is_nonterminal(text):
    return text.startswith('<') and text.endswith('>')

# Function to get the first set of a non-terminal
# Loops through the CFG of the given non-terminal
# If there are productions, get the first symbol
    # If the first symbol is also a non-terminal, get its first set and put it into the set
    # If the first symbol is a terminal, directly add it to the list
def get_first_set(non_terminal):
    first_set = set()
    for prod in CFG[non_terminal]:
        if prod:
            first_symbol = prod[0]
            if is_nonterminal(first_symbol):
                first_set.update(get_first_set(first_symbol))
            else:
                first_set.add(first_symbol)
    return first_set

def syntax_analyze(tokens):
    syntax = SyntaxAnalyzer(tokens)
    error = syntax.syntax_analyze()

    if error:
        print(error)
        return "❌ Failure from Syntax Analyzer", error
    print("####### Successful Syntax #######")
    return "✅ Success from Syntax Analyzer", None