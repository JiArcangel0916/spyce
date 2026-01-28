from .Error import InvalidSyntaxError

# string (production): list ng list ng string (production set)
CFG = {
    '<program>':[
        ['<global_var>', '<sub_func>', 'spyce', '(', ')', '->', 'void', '{', '<func_body>', '}']
    ],

    '<global_var>':[
        ['const', '<var_dtype>', ';', '<global_var>'], 
        ['<var_dtype>', ';', '<global_var>'],           
        []                                              
    ],

    '<var_dtype>':[
        ['int', '<int_vartype>'],
        ['float', '<float_vartype>'],
        ['char', '<char_vartype>'],
        ['string', '<str_vartype>'],
        ['bool', '<bool_vartype>']
    ],

    ############### Productions for INT (10-36) ###############
    '<int_vartype>':[
        ['id', '=', '<int_scalvar>', '<int_scaldec_tail>'],
        ['[', ']', '<int_arrtype>']
    ],

    '<int_scalvar>':[
        ['<arith>'],
        ['listen', '(', ')'],
        ['null']
    ],

    '<int_scaldec_tail>':[
        [',', 'id', '=', '<int_scalvar>', '<int_scaldec_tail>'],
        []
    ],

    '<int_arrtype>':[
        ['id', '=', '<int_1d_val>', '<int_1d_dec_tail>'],
        ['[', ']', 'id', '=', '<int_2d_val>', '<int_2d_dec_tail>']
    ],

    '<int_1d_val>':[
        ['id', '<inner_arr_indx>'],
        ['{', '<int_arrlit>', '}']
    ],

    '<inner_arr_indx>':[
        ['[', '<arith>', ']'],
        []
    ],

    '<int_arrlit>':[
        ['<arith>', '<int_val_tail>'],
        []
    ],

    '<int_val_tail>':[
        [',', '<arith>', '<int_val_tail>'],
        []
    ],

    '<int_1d_dec_tail>':[
        [',', 'id', '=', '<int_1d_val>', '<int_1d_dec_tail>'],
        []
    ],

    '<int_2d_val>':[
        ['id'],
        ['{', '<int_2d_elem>', '}']
    ],

    '<int_2d_elem>':[
        ['<int_1d_val>', '<int_2dval_tail>'],
        []
    ],

    '<int_2dval_tail>':[
        [',', '<int_1d_val>', '<int_2dval_tail>'],
        []
    ],

    '<int_2d_dec_tail>':[
        [',', 'id', '=', '<int_2d_val>', '<int_2d_dec_tail>'],
        []
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<float_vartype>':[
        ['id', '=', '<float_scalvar>', '<float_scaldec_tail>'],
        ['[', ']', '<float_arrtype>']
    ],

    '<float_scalvar>':[
        ['<arith>'],
        ['listen', '(', ')'],
        ['null']
    ],

    '<float_scaldec_tail>':[
        [',', 'id', '=', '<float_scalvar>', '<float_scaldec_tail>'],
        []
    ],

    '<float_arrtype>':[
        ['id', '=', '<float_1d_val>', '<float_1d_dec_tail>'],
        ['[', ']', 'id', '=', '<float_2d_val>', '<float_2d_dec_tail>']
    ],

    '<float_1d_val>':[
        ['id', '<inner_arr_indx>'],
        ['{', '<float_arrlit>', '}']
    ],

    '<float_arrlit>':[
        ['<arith>', '<float_val_tail>'],
        []
    ],

    '<float_val_tail>':[
        [',', '<arith>', '<float_val_tail>'],
        []
    ],

    '<float_1d_dec_tail>':[
        [',', 'id', '=', '<float_1d_val>', '<float_1d_dec_tail>'],
        []
    ],

    '<float_2d_val>':[
        ['id'],
        ['{', '<float_2d_elem>', '}']
    ],

    '<float_2d_elem>':[
        ['<float_1d_val>', '<float_2dval_tail>'],
        []
    ],

    '<float_2dval_tail>':[
        [',', '<float_1d_val>', '<float_2dval_tail>'],
        []
    ],

    '<float_2d_dec_tail>':[
        [',', 'id', '=', '<float_2d_val>', '<float_2d_dec_tail>'],
        []
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<char_vartype>':[
        ['id', '=', '<char_scalvar>', '<char_scaldec_tail>'],
        ['[', ']', '<char_arrtype>']
    ],

    '<char_scalvar>':[
        ['<char_val>'],
        ['listen', '(', ')'],
        ['null']
    ],

    '<char_scaldec_tail>':[
        [',', 'id', '=', '<char_scalvar>', '<char_scaldec_tail>'],
        []
    ],

    '<char_arrtype>':[
        ['id', '=', '<char_1d_val>', '<char_1d_dec_tail>'],
        ['[', ']', 'id', '=', '<char_2d_val>', '<char_2d_dec_tail>']
    ],

    '<char_1d_val>':[
        ['id', '<inner_arr_indx>'],
        ['{', '<char_arrlit>', '}']
    ],

    '<char_arrlit>':[
        ['<char_val>', '<char_val_tail>'],
        []
    ],

    '<char_val_tail>':[
        [',', '<char_val>', '<char_val_tail>'],
        []
    ],

    '<char_1d_dec_tail>':[
        [',', 'id', '=', '<char_1d_val>', '<char_1d_dec_tail>'],
        []
    ],

    '<char_2d_val>':[
        ['id'],
        ['{', '<char_2d_elem>', '}']
    ],

    '<char_2d_elem>':[
        ['<char_1d_val>', '<char_2dval_tail>'],
        []
    ],

    '<char_2dval_tail>':[
        [',', '<char_1d_val>', '<char_2dval_tail>'],
        []
    ],

    '<char_2d_dec_tail>':[
        [',', 'id', '=', '<char_2d_val>', '<char_2d_dec_tail>'],
        []
    ],

    '<char_val>':[
        ['char_lit'],
        ['<id_val>'],
        ['(', '<char_val_content>', ')']
    ],

    '<char_val_content>':[
        ['char_lit'],
        ['<id_val>']
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<str_vartype>':[
        ['id', '=', '<str_scalvar>', '<str_scaldec_tail>'],
        ['[', ']', '<str_arrtype>']
    ],

    '<str_scalvar>':[
        ['<arith>'],
        ['listen', '(', ')'],
        ['null']
    ],

    '<str_scaldec_tail>':[
        [',', 'id', '=', '<str_scalvar>', '<str_scaldec_tail>'],
        []
    ],

    '<str_arrtype>':[
        ['id', '=', '<str_1d_val>', '<str_1d_dec_tail>'],
        ['[', ']', 'id', '=', '<str_2d_val>', '<str_2d_dec_tail>']
    ],

    '<str_1d_val>':[
        ['id', '<inner_arr_indx>'],
        ['{', '<str_arrlit>', '}']
    ],

    '<str_arrlit>':[
        ['<arith>', '<str_val_tail>'],
        []
    ],

    '<str_val_tail>':[
        [',', '<arith>', '<str_val_tail>'],
        []
    ],

    '<str_1d_dec_tail>':[
        [',', 'id', '=', '<str_1d_val>', '<str_1d_dec_tail>'],
        []
    ],

    '<str_2d_val>':[
        ['id'],
        ['{', '<str_2d_elem>', '}']
    ],

    '<str_2d_elem>':[
        ['<str_1d_val>', '<str_2dval_tail>'],
        []
    ],

    '<str_2dval_tail>':[
        [',', '<str_1d_val>', '<str_2dval_tail>'],
        []
    ],

    '<str_2d_dec_tail>':[
        [',', 'id', '=', '<str_2d_val>', '<str_2d_dec_tail>'],
        []
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<bool_vartype>':[
        ['id', '=', '<bool_scalvar>', '<bool_scaldec_tail>'],
        ['[', ']', '<bool_arrtype>']
    ],

    '<bool_scalvar>':[
        ['<logical>'],
        ['listen', '(', ')'],
        ['null']
    ],

    '<bool_scaldec_tail>':[
        [',', 'id', '=', '<bool_scalvar>', '<bool_scaldec_tail>'],
        []
    ],

    '<bool_arrtype>':[
        ['id', '=', '<bool_1d_val>', '<bool_1d_dec_tail>'],
        ['[', ']', 'id', '=', '<bool_2d_val>', '<bool_2d_dec_tail>']
    ],

    '<bool_1d_val>':[
        ['id', '<inner_arr_indx>'],
        ['{', '<bool_arrlit>', '}']
    ],

    '<bool_arrlit>':[
        ['<bool_val>', '<bool_val_tail>'],
        []
    ],

    '<bool_val_tail>':[
        [',', '<bool_val>', '<bool_val_tail>'],
        []
    ],

    '<bool_1d_dec_tail>':[
        [',', 'id', '=', '<bool_1d_val>', '<bool_1d_dec_tail>'],
        []
    ],

    '<bool_2d_val>':[
        ['id'],
        ['{', '<bool_2d_elem>', '}']
    ],

    '<bool_2d_elem>':[
        ['<bool_1d_val>', '<bool_2dval_tail>'],
        []
    ],

    '<bool_2dval_tail>':[
        [',', '<bool_1d_val>', '<bool_2dval_tail>'],
        []
    ],

    '<bool_2d_dec_tail>':[
        [',', 'id', '=', '<bool_2d_val>', '<bool_2d_dec_tail>'],
        []
    ],

    '<bool_val>':[
        ['<logical>'],
    ],

    '<id_val>':[
        ['id', '<1d_indx>']
    ],

    '<1d_indx>':[
        ['[', '<arith>', ']', '<2d_indx>'],
        []
    ],

    '<2d_indx>':[
        ['[', '<arith>', ']'],
        []
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<sub_func>':[
        ['<sub_funcdec>', '<sub_func>'],
        []
    ],

    '<sub_funcdec>':[
        ['make', 'id', '(', '<parameters>', ')', '->', '<func_ret>', '<func_type>']
    ],

    '<parameters>':[
        ['<data_type>', '<1d_arr>', 'id', '<par_tail>'],
        []
    ],

    '<data_type>':[
        ['int'],
        ['float'],
        ['char'],
        ['string'],
        ['bool']
    ],

    '<1d_arr>':[
        ['[', ']', '<2d_arr>'],
        []
    ],

    '<2d_arr>':[
        ['[', ']'],
        []
    ],

    '<par_tail>':[
        [',', '<data_type>', '<1d_arr>', 'id', '<par_tail>'],
        []
    ],

    '<func_ret>':[
        ['<data_type>'],
        ['void'],
    ],

    '<func_type>':[
        ['{', '<func_body>', '}'],
        ['[', ']', '<arr_func>'],
    ],

    '<arr_func>':[
        ['{', '<func_body>', '}'],
        ['[', ']', '{', '<func_body>', '}'],
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<func_body>':[
        ['<stmnt>', '<func_body>'],
        []
    ],

    '<stmnt>':[
        ['<local_var>', ';'],
        ['id', '<id_stmnt>', ';'],
        ['<unary_op>', '<id_val>', ';'],
        ['<giveback>', ';'],
        ['<IO>', ';'],
        ['<conditional>'],
        ['<iterative>']
    ],

    '<id_stmnt>':[
        ['<1d_indx>', '<unary_or_assign>'],
        ['(', '<args>', ')']
    ],

    '<unary_or_assign>':[
        ['<unary_op>'],
        ['<assign_type>']
    ],

    '<expr>':[
        ['<arith>'],
        ['<logical>']
    ],

    '<local_var>':[
        ['const', '<var_dtype>'],
        ['<var_dtype>']
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<arith>':[
        ['<arith_operand>', '<chain_arith>']
    ],

    '<arith_operand>':[
        ['int_lit'],
        ['float_lit'],
        ['string_lit'],
        ['null'],
        ['<id_val>', '<unary_or_id>'],
        ['<unary_op>', '<id_val>'],
        ['(', '<arith>', ')']
    ],

    '<unary>':[
        ['<id_val>', '<unary_op>'],
        ['<unary_op>', '<id_val>']
    ],

    '<unary_op>':[
        ['++'],
        ['--']
    ],

    '<unary_or_id>':[
        ['<unary_op>'],
        []
    ],

    '<chain_arith>':[
        ['<binary_op>', '<arith_operand>', '<chain_arith>'],
        []
    ],

    '<binary_op>':[
        ['+'],
        ['-'],
        ['*'],
        ['/'],
        ['**'],
        ['%']
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<logical>':[
        ['<or_expr>']
    ],

    '<or_expr>':[
        ['<and_expr>', '<chain_or>']
    ],

    '<and_expr>':[
        ['<and_operand>', '<chain_and>'],
    ],

    '<and_operand>':[
        ['<logical_operand>'],
        ['NOT', '<not_expr>']
    ],

    '<logical_operand>':[
        ['<bool_lit>'],
        ['(','<relational>', ')'],
    ],

    '<not_expr>':[
        ['(', '<and_operand>', ')'],
        ['<logical_operand>'],
    ],

    '<chain_or>':[
        ['OR', '<and_expr>', '<chain_or>'],
        []
    ],

    '<chain_and>':[
        ['AND', '<and_operand>', '<chain_and>'],
        []
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 
    
    '<relational>':[
        ['<relation_operand>', '<relation_op>', '<relation_operand>']
    ],

    '<relation_operand>':[
        ['<literal>'],
        ['null'],
        ['(', '<expr>', ')'],
    ],

    '<literal>':[
        ['int_lit'],
        ['float_lit'],
        ['char_lit'],
        ['string_lit'],
        ['<bool_lit>'],
    ],

    '<bool_lit>':[
        ['true'],
        ['false'],
    ],

    '<relation_op>':[
        ['>'],
        ['<'],
        ['>='],
        ['<='],
        ['=='],
        ['!=']
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<assign_type>':[
        ['=', '<assign_operand>'],
        ['<cmpnd_op>', '<cmpnd_operand>']
    ],

    '<assign_operand>':[
        ['listen', '(', ')'],
        ['null'],
        ['id', '<func_or_indx>'],
        ['<expr>'],
    ],

    '<func_or_indx>':[
        ['(', '<args>', ')'],
        ['<1d_indx>']
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
        ['int_lit'],
        ['float_lit'],
        ['string_lit'],
        ['<id_val>']
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<giveback>':[
        ['giveback', '<ret_val>']
    ],

    '<ret_val>':[
        ['void'],
        ['<expr>'],
        ['char_lit'],
    ],

    '<IO>':[
        ['say', '(', '<args>', ')'],
        ['listen', '(', ')']
    ],

    '<args>':[
        ['<expr>', '<val_tail>'],
        []
    ],

    '<val_tail>':[
        [',', '<expr>', '<val_tail>'],
        []
    ],
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<conditional>':[
        ['when', '(', '<bool_val>', ')', '{', '<ctrl_block>', '}', '<else_tail>', '<otherwise>'],
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
        ['elsewhen', '(', '<bool_val>', ')', '{', '<ctrl_block>', '}', '<else_tail>'],
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
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 

    '<iterative>':[
        ['for', '(', '<ctrl_var>', '<for_bool>', '<for_unary>', ')', '{', '<ctrl_block>', '}'],
        ['while', '(', '<bool_val>', ')', '{', '<ctrl_block>', '}']
    ],

    '<ctrl_var>':[
        ['<local_var>', ';'],
        ['<id_val>', '=', '<assign_operand>', ';'],
        [';']
        
    ],

    '<for_bool>':[
        ['<bool_val>', ';'],
        [';']
    ],

    '<for_unary>':[
        ['<unary>'],
        []
    ]
    # ^^^^^^^^^^^^ VERIFIED ^^^^^^^^^^^^ 
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

    '<var_dtype>':{   # correct
        'int':      ['<var_dtype>', 0],      
        'float':    ['<var_dtype>', 1],       
        'char':     ['<var_dtype>', 2],       
        'string':   ['<var_dtype>', 3],       
        'bool':     ['<var_dtype>', 4],       
    },

    '<int_vartype>':{   # correct
        'id':   ['<int_vartype>', 0],      
        '[':    ['<int_vartype>', 1]       
    },

    '<int_scalvar>':{      # correct BUT WITH AMBIGUITY ON NULL
        'int_lit':      ['<int_scalvar>', 0],  
        'float_lit':    ['<int_scalvar>', 0],   
        'string_lit':   ['<int_scalvar>', 0],       
        'id':           ['<int_scalvar>', 0],      
        '++':           ['<int_scalvar>', 0],
        '--':           ['<int_scalvar>', 0],
        '(':            ['<int_scalvar>', 0],
        'listen':       ['<int_scalvar>', 1],  
        'null':         ['<int_scalvar>', 2]   
    },

    '<int_scaldec_tail>':{   # correct
        ',':['<int_scaldec_tail>', 0],  
        ';':['<int_scaldec_tail>', 1]    
    },

    '<int_arrtype>':{   # correct
        'id':   ['<int_arrtype>', 0],   
        '[':    ['<int_arrtype>', 1]      
    },

    '<int_1d_val>':{   # correct
        'id':   ['<int_1d_val>', 0],
        '{':    ['<int_1d_val>', 1]
    },

    '<inner_arr_indx>':{
        '[':['<inner_arr_indx>', 0],
        ',':['<inner_arr_indx>', 1],
        ';':['<inner_arr_indx>', 1],
        '}':['<inner_arr_indx>', 1]
    },

    '<int_arrlit>':{      # correct
        'int_lit':      ['<int_arrlit>', 0], 
        'float_lit':    ['<int_arrlit>', 0], 
        'string_lit':   ['<int_arrlit>', 0],
        'null':         ['<int_arrlit>', 0], 
        'id':           ['<int_arrlit>', 0],      
        '++':           ['<int_arrlit>', 0],
        '--':           ['<int_arrlit>', 0],
        '(':            ['<int_arrlit>', 0],
        '}':            ['<int_arrlit>', 1]
    },

    '<int_val_tail>':{   # correct
        ',':['<int_val_tail>', 0],
        '}':['<int_val_tail>', 1]
    },

    '<int_1d_dec_tail>':{   # correct
        ',':['<int_1d_dec_tail>', 0],
        ';':['<int_1d_dec_tail>', 1]
    },

    '<int_2d_val>':{   # correct
        'id':   ['<int_2d_val>', 0],
        '{':    ['<int_2d_val>', 1]
    },

    '<int_2d_elem>':{   # correct
        'id':   ['<int_2d_elem>', 0],
        '{':    ['<int_2d_elem>', 0],
        '}':    ['<int_2d_elem>', 1]
    },

    '<int_2dval_tail>':{   # correct
        ',':['<int_2dval_tail>', 0],
        '}':['<int_2dval_tail>', 1]
    },

    '<int_2d_dec_tail>':{   # correct
        ',':['<int_2d_dec_tail>', 0],
        ';':['<int_2d_dec_tail>', 1]
    },

    '<float_vartype>':{   # correct
        'id':   ['<float_vartype>', 0],     
        '[':    ['<float_vartype>', 1]       
    },

    '<float_scalvar>':{      # correct
        'int_lit':      ['<float_scalvar>', 0], 
        'float_lit':    ['<float_scalvar>', 0], 
        'string_lit':   ['<float_scalvar>', 0],
        'null':         ['<float_scalvar>', 0], 
        'id':           ['<float_scalvar>', 0],      
        '++':           ['<float_scalvar>', 0],
        '--':           ['<float_scalvar>', 0],
        '(':            ['<float_scalvar>', 0]
    },

    '<float_scaldec_tail>':{   # correct
        ',':['<float_scaldec_tail>', 0],  
        ';':['<float_scaldec_tail>', 1]    
    },

    '<float_arrtype>':{   # correct
        'id':   ['<float_arrtype>', 0],   
        '[':    ['<float_arrtype>', 1]      
    },

    '<float_1d_val>':{   # correct
        'id':   ['<float_1d_val>', 0],
        '{':    ['<float_1d_val>', 1]
    },

    '<float_arrlit>':{      # correct
        'int_lit':      ['<float_arrlit>', 0], 
        'float_lit':    ['<float_arrlit>', 0], 
        'string_lit':   ['<float_arrlit>', 0],
        'null':         ['<float_arrlit>', 0], 
        'id':           ['<float_arrlit>', 0],      
        '++':           ['<float_arrlit>', 0],
        '--':           ['<float_arrlit>', 0],
        '(':            ['<float_arrlit>', 0],
        '}':            ['<float_arrlit>', 1]
    },

    '<float_val_tail>':{   # correct
        ',':['<float_val_tail>', 0],
        '}':['<float_val_tail>', 1]
    },

    '<float_1d_dec_tail>':{   # correct
        ',':['<float_1d_dec_tail>', 0],
        ';':['<float_1d_dec_tail>', 1]
    },

    '<float_2d_val>':{   # correct
        'id':   ['<float_2d_val>', 0],
        '{':    ['<float_2d_val>', 1]
    },

    '<float_2d_elem>':{   # correct
        'id':   ['<float_2d_elem>', 0],
        '{':    ['<float_2d_elem>', 0],
        '}':    ['<float_2d_elem>', 1]
    },

    '<float_2dval_tail>':{   # correct
        ',':['<float_2dval_tail>', 0],
        '}':['<float_2dval_tail>', 1]
    },

    '<float_2d_dec_tail>':{   # correct
        ',':['<float_2d_dec_tail>', 0],
        ';':['<float_2d_dec_tail>', 1]
    },

    '<char_vartype>':{   # correct
        'id':   ['<char_vartype>', 0],     
        '[':    ['<char_vartype>', 1]       
    },

    '<char_scalvar>':{      # correct
        'char_lit': ['<char_scalvar>', 0],   
        'id':       ['<char_scalvar>', 0],
        '(':        ['<char_scalvar>', 0],      
        'listen':   ['<char_scalvar>', 1],  
        'null':     ['<char_scalvar>', 2]   
    },

    '<char_scaldec_tail>':{   # correct
        ',':['<char_scaldec_tail>', 0],  
        ';':['<char_scaldec_tail>', 1]    
    },

    '<char_arrtype>':{   # correct
        'id':   ['<char_arrtype>', 0],   
        '[':    ['<char_arrtype>', 1]      
    },

    '<char_1d_val>':{   # correct
        'id':   ['<char_1d_val>', 0],
        '{':    ['<char_1d_val>', 1]
    },

    '<char_arrlit>':{      # correct
        'char_lit': ['<char_arrlit>', 0], 
        'id':       ['<char_arrlit>', 0],       
        '(':        ['<char_arrlit>', 0],
        '}':        ['<char_arrlit>', 1]
    },

    '<char_val_tail>':{   # correct
        ',':['<char_val_tail>', 0],
        '}':['<char_val_tail>', 1]
    },

    '<char_1d_dec_tail>':{   # correct
        ',':['<char_1d_dec_tail>', 0],
        ';':['<char_1d_dec_tail>', 1]
    },

    '<char_2d_val>':{   # correct
        'id':   ['<char_2d_val>', 0],
        '{':    ['<char_2d_val>', 1]
    },

    '<char_2d_elem>':{   # correct
        'id':   ['<char_2d_elem>', 0],
        '{':    ['<char_2d_elem>', 0],
        '}':    ['<char_2d_elem>', 1]
    },

    '<char_2dval_tail>':{   # correct
        ',':['<char_2dval_tail>', 0],
        '}':['<char_2dval_tail>', 1]
    },

    '<char_2d_dec_tail>':{   # correct
        ',':['<char_2d_dec_tail>', 0],
        ';':['<char_2d_dec_tail>', 1]
    },

    '<char_val>':{   # correct
        'char_lit': ['<char_val>', 0],
        'id':       ['<char_val>', 1],
        '(':        ['<char_val>', 2]
    },

    '<char_val_content>':{   # correct
        'char_lit': ['<char_val_content>', 0],
        'id':       ['<char_val_content>', 1]
    },

    '<str_vartype>':{   # correct
        'id':   ['<str_vartype>', 0],     
        '[':    ['<str_vartype>', 1]       
    },

    '<str_scalvar>':{      ####### INCORRECT
        'string_lit':   ['<str_scalvar>', 0],       
        'id':           ['<str_scalvar>', 0],      
        '(':            ['<str_scalvar>', 0],
        'listen':       ['<str_scalvar>', 1],  
        'null':         ['<str_scalvar>', 2]   
    },

    '<str_scaldec_tail>':{   # correct
        ',':['<str_scaldec_tail>', 0],  
        ';':['<str_scaldec_tail>', 1]    
    },

    '<str_arrtype>':{   # correct
        'id':   ['<str_arrtype>', 0],   
        '[':    ['<str_arrtype>', 1]      
    },

    '<str_1d_val>':{   # correct
        'id':   ['<str_1d_val>', 0],
        '{':    ['<str_1d_val>', 1]
    },

    '<str_arrlit>':{      # correct 
        'int_lit':      ['<str_arrlit>', 0],  
        'float_lit':    ['<str_arrlit>', 0],   
        'string_lit':   ['<str_arrlit>', 0],       
        'id':           ['<str_arrlit>', 0],      
        '++':           ['<str_arrlit>', 0],
        '--':           ['<str_arrlit>', 0],
        '(':            ['<str_arrlit>', 0],
        'listen':       ['<str_arrlit>', 1],  
        'null':         ['<str_arrlit>', 2]
    },

    '<str_val_tail>':{   # correct
        ',':['<str_val_tail>', 0],
        '}':['<str_val_tail>', 1]
    },

    '<str_1d_dec_tail>':{   # correct
        ',':['<str_1d_dec_tail>', 0],
        ';':['<str_1d_dec_tail>', 1]
    },

    '<str_2d_val>':{   # correct
        'id':   ['<str_2d_val>', 0],
        '{':    ['<str_2d_val>', 1]
    },

    '<str_2d_elem>':{   # correct
        'id':   ['<str_2d_elem>', 0],
        '{':    ['<str_2d_elem>', 0],
        '}':    ['<str_2d_elem>', 1]
    },

    '<str_2dval_tail>':{   # correct
        ',':['<str_2dval_tail>', 0],
        '}':['<str_2dval_tail>', 1]
    },

    '<str_2d_dec_tail>':{   # correct
        ',':['<str_2d_dec_tail>', 0],
        ';':['<str_2d_dec_tail>', 1]
    },

    '<bool_vartype>':{   # correct
        'id':   ['<bool_vartype>', 0],     
        '[':    ['<bool_vartype>', 1]       
    },

    '<bool_scalvar>':{    # correct BUT DOES NOT SUPPORT ID
        'true':     ['<bool_scalvar>', 0],       
        'false':    ['<bool_scalvar>', 0],
        '(':        ['<bool_scalvar>', 0],
        'NOT':      ['<bool_scalvar>', 0],
        'listen':   ['<bool_scalvar>', 1],
        'null':     ['<bool_scalvar>', 2]
    },

    '<bool_scaldec_tail>':{   # correct
        ',':['<bool_scaldec_tail>', 0],  
        ';':['<bool_scaldec_tail>', 1]    
    },

    '<bool_arrtype>':{   # correct
        'id':   ['<bool_arrtype>', 0],   
        '[':    ['<bool_arrtype>', 1]      
    },

    '<bool_1d_val>':{   # correct
        'id':   ['<bool_1d_val>', 0],
        '{':    ['<bool_1d_val>', 1]
    },

    '<bool_arrlit>':{      # correct BUT DOES NOT SUPPORT ID
        'true':     ['<bool_arrlit>', 0],       
        'false':    ['<bool_arrlit>', 0],
        '(':        ['<bool_arrlit>', 0],
        'NOT':      ['<bool_arrlit>', 0],  
        'null':     ['<bool_arrlit>', 0],       
        '}':        ['<bool_arrlit>', 1]
    },

    '<bool_val_tail>':{   # correct
        ',':['<bool_val_tail>', 0],
        '}':['<bool_val_tail>', 1]
    },

    '<bool_1d_dec_tail>':{   # correct
        ',':['<bool_1d_dec_tail>', 0],
        ';':['<bool_1d_dec_tail>', 1]
    },

    '<bool_2d_val>':{   # correct
        'id':   ['<bool_2d_val>', 0],
        '{':    ['<bool_2d_val>', 1]
    },

    '<bool_2d_elem>':{   # correct
        'id':   ['<bool_2d_elem>', 0],
        '{':    ['<bool_2d_elem>', 0],
        '}':    ['<bool_2d_elem>', 1]
    },

    '<bool_2dval_tail>':{   # correct
        ',':['<bool_2dval_tail>', 0],
        '}':['<bool_2dval_tail>', 1]
    },

    '<bool_2d_dec_tail>':{   # correct
        ',':['<bool_2d_dec_tail>', 0],
        ';':['<bool_2d_dec_tail>', 1]
    },

    '<bool_val>':{      # correct BUT OES NOT SUPPORT ID
        'true':     ['<bool_val>', 0],       
        'false':    ['<bool_val>', 0],
        '(':        ['<bool_val>', 0],
        'NOT':      ['<bool_val>', 0] 
    },  

    '<id_val>':{   # correct
      'id':['<id_val>', 0]  
    },

    '<1d_indx>':{      # correct BUT DOES NOT HAVE RELATION AND LOGICAL OPERATOR
        '[':    ['<1d_indx>', 0],
        '++':   ['<1d_indx>', 1],
        '--':   ['<1d_indx>', 1],
        '=':    ['<1d_indx>', 1],
        '+=':   ['<1d_indx>', 1],
        '-=':   ['<1d_indx>', 1],
        '*=':   ['<1d_indx>', 1],
        '/=':   ['<1d_indx>', 1],
        '**=':  ['<1d_indx>', 1],
        '%=':   ['<1d_indx>', 1],
        ';':    ['<1d_indx>', 1],
        ')':    ['<1d_indx>', 1],
        ',':    ['<1d_indx>', 1],
        '+':    ['<1d_indx>', 1],
        '-':    ['<1d_indx>', 1],
        '*':    ['<1d_indx>', 1],
        '/':    ['<1d_indx>', 1],
        '**':   ['<1d_indx>', 1],
        '%':    ['<1d_indx>', 1],
        ']':    ['<1d_indx>', 1],
        '}':    ['<1d_indx>', 1]
    },

    '<2d_indx>':{      # correct BUT DOES NOT HAVE RELATION AND LOGICAL OPERATOR
        '[':    ['<2d_indx>', 0],
        '++':   ['<2d_indx>', 1],
        '--':   ['<2d_indx>', 1],
        '=':    ['<2d_indx>', 1],
        '+=':   ['<2d_indx>', 1],
        '-=':   ['<2d_indx>', 1],
        '*=':   ['<2d_indx>', 1],
        '/=':   ['<2d_indx>', 1],
        '**=':  ['<2d_indx>', 1],
        '%=':   ['<2d_indx>', 1],
        ';':    ['<2d_indx>', 1],
        ')':    ['<2d_indx>', 1],
        ',':    ['<2d_indx>', 1],
        '+':    ['<2d_indx>', 1],
        '-':    ['<2d_indx>', 1],
        '*':    ['<2d_indx>', 1],
        '/':    ['<2d_indx>', 1],
        '**':   ['<2d_indx>', 1],
        '%':    ['<2d_indx>', 1],
        ']':    ['<2d_indx>', 1],
        '}':    ['<2d_indx>', 1]
    },

    '<sub_func>':{   # correct
        'make': ['<sub_func>', 0],
        'spyce':['<sub_func>', 1]
    },

    '<sub_funcdec>':{   # correct
        'make':['<sub_funcdec>', 0]
    },

    '<parameters>':{   # correct
        'int':      ['<parameters>', 0],
        'float':    ['<parameters>', 0],
        'char':     ['<parameters>', 0],
        'string':   ['<parameters>', 0],
        'bool':     ['<parameters>', 0],
        ')':        ['<parameters>', 1]
    },

    '<data_type>':{   # correct
        'int':      ['<data_type>', 0],
        'float':    ['<data_type>', 1],
        'char':     ['<data_type>', 2],
        'string':   ['<data_type>', 3],
        'bool':     ['<data_type>', 4]
    },

    '<1d_arr>':{   # correct
        '[':    ['<1d_arr>', 0],
        'id':   ['<1d_arr>', 1]
    },

    '<2d_arr>':{   # correct
        '[':    ['<2d_arr>', 0],
        'id':   ['<2d_arr>', 1]
    },

    '<par_tail>':{   # correct
        ',':['<par_tail>', 0],
        ')':['<par_tail>', 1]
    },

    '<func_ret>':{   # correct
       'int':   ['<func_ret>', 0],
       'float': ['<func_ret>', 0], 
       'char':  ['<func_ret>', 0], 
       'string':['<func_ret>', 0], 
       'bool':  ['<func_ret>', 0], 
       'void':  ['<func_ret>', 1]
    },

    '<func_type>':{   # correct
        '{':['<func_type>', 0],
        '[':['<func_type>', 1]
    },

    '<arr_func>':{   # correct
        '{':['<arr_func>', 0],
        '[':['<arr_func>', 1]
    },

    '<func_body>':{   # correct
        'const':        ['<func_body>', 0],
        'int':          ['<func_body>', 0],
        'float':        ['<func_body>', 0],
        'char':         ['<func_body>', 0],
        'string':       ['<func_body>', 0],
        'bool':         ['<func_body>', 0],
        'id':           ['<func_body>', 0],     
        '++':           ['<func_body>', 0],
        '--':           ['<func_body>', 0],      
        'giveback':     ['<func_body>', 0],
        'say':          ['<func_body>', 0],
        'listen':       ['<func_body>', 0],     
        'when':         ['<func_body>', 0],
        'choose':       ['<func_body>', 0],
        'for':          ['<func_body>', 0],
        'while':        ['<func_body>', 0],
        '}':            ['<func_body>', 1]
    },

    '<stmnt>':{   # correct 
        'const':        ['<stmnt>', 0],
        'int':          ['<stmnt>', 0],
        'float':        ['<stmnt>', 0],
        'char':         ['<stmnt>', 0],
        'string':       ['<stmnt>', 0],
        'bool':         ['<stmnt>', 0],
        'id':           ['<stmnt>', 1],     
        '++':           ['<stmnt>', 2],
        '--':           ['<stmnt>', 2],      
        'giveback':     ['<stmnt>', 3],
        'say':          ['<stmnt>', 4],
        'listen':       ['<stmnt>', 4],     
        'when':         ['<stmnt>', 5],
        'choose':       ['<stmnt>', 5],
        'for':          ['<stmnt>', 6],
        'while':        ['<stmnt>', 6]
    },

    '<id_stmnt>':{   # correct
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

    '<unary_or_assign>':{   # correct
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

    '<local_var>':{   # correct
        'const':    ['<local_var>', 0],
        'int':      ['<local_var>', 1],
        'float':    ['<local_var>', 1],
        'char':     ['<local_var>', 1],
        'string':   ['<local_var>', 1],
        'bool':     ['<local_var>', 1]
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

    '<unary_op>':{   # correct
        '++':['<unary_op>', 0],
        '--':['<unary_op>', 1]
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

    '<val_tail>':{   # correct
        ',':['<val_tail>', 0],
        ')':['<val_tail>', 1]
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
        self.prev_token = None                      # Points to the token before the current token
    
    def advance(self):
        while True:
            self.token_idx += 1
            if self.token_idx < len(self.tokens):
                self.prev_token = self.curr_token
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
                    if self.prev_token is None:
                        error = InvalidSyntaxError(self.curr_token.pos_start, self.curr_token.pos_end, f'Unexpected token -> {self.curr_token.type} <- \nExpected tokens: {expected_tokens}')
                    else:  
                        error = InvalidSyntaxError(self.curr_token.pos_start, self.curr_token.pos_end, f'Unexpected token -> {self.curr_token.type} <- after "{self.prev_token.type}"\nExpected tokens: {expected_tokens}')
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
                    error = InvalidSyntaxError(self.curr_token.pos_start, self.curr_token.pos_end, f'Unexpected Token -> {self.curr_token.type} <- after "{self.prev_token.type}"\nExpected tokens: {expected_tokens}')
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