from .Error import InvalidSyntaxError

CFG = {
    '<program>':[
        ['<global_var>', '<sub_func>', 'spyce', '(', ')', '->', 'void', '{', '<func_body>', 'giveback', 'void', ';', '}']
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

    ############### Productions for INT (10-50) ###############
    '<int_vartype>':[
        ['id', '=', '<int_scalvar>', '<int_scaldec_tail>'],
        ['[', ']', '<int_arrtype>']
    ],

    '<int_scalvar>':[
        ['<int_val>'],
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
        ['[', '<indx_val>', ']'],
        []
    ],

    '<int_arrlit>':[
        ['<int_val>', '<int_val_tail>'],
        []
    ],

    '<int_val_tail>':[
        [',', '<int_val>', '<int_val_tail>'],
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

    '<int_val>':[
        ['int_lit'],
        ['(', 'int_lit', ')'],
        ['<int_arith>'],
        ['(', '<int_arith>', ')'],
        ['<id_val>'],
        ['(', '<id_val>', ')']
    ],

    '<id_val>':[
        ['id', '<1d_indx>']
    ],

    '<1d_indx>':[
        ['[', '<indx_val>', ']', '<2d_indx>'],
        []
    ],

    '<2d_indx>':[
        ['[', '<indx_val>', ']'],
        []
    ],

    '<indx_val>':[
        ['id'],
        ['int_lit'],
        ['<int_arith>']
    ],

    ############### Productions for FLOAT (51-81) ###############
    '<float_vartype>':[
        ['id', '=', '<float_scalvar>', '<float_scaldec_tail>'],
        ['[', ']', '<float_arrtype>']
    ],

    '<float_scalvar>':[
        ['<float_val>'],
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
        ['<float_val>', '<float_val_tail>'],
        []
    ],

    '<float_val_tail>':[
        [',', '<float_val>', '<float_val_tail>'],
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

    '<float_val>':[
        ['float_lit'],
        ['(', 'float_lit', ')'],
        ['<arith>'],
        ['(', '<arith>', ')'],
        ['<id_val>'],
        ['(', '<id_val>', ')']
    ],

    ############### Productions for CHAR (82-110) ###############
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
        ['(', 'char_lit', ')'],
        ['<id_val>'],
        ['(', '<id_val>', ')']
    ],

    ############### Productions for STRING (111-141) ###############
    '<str_vartype>':[
        ['id', '=', '<str_scalvar>', '<str_scaldec_tail>'],
        ['[', ']', '<str_arrtype>']
    ],

    '<str_scalvar>':[
        ['<str_val>'],
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
        ['<str_val>', '<str_val_tail>'],
        []
    ],

    '<str_val_tail>':[
        [',', '<str_val>', '<str_val_tail>'],
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

    '<str_val>':[
        ['string_lit'],
        ['(', 'string_lit', ')'],
        ['<str_concat>'],
        ['(', '<str_concat>', ')'],
        ['<id_val>'],
        ['(', '<id_val>', ')']
    ],

    ############### Productions for BOOL (142-176) ###############
    '<bool_vartype>':[
        ['id', '=', '<bool_scalvar>', '<bool_scaldec_tail>'],
        ['[', ']', '<bool_arrtype>']
    ],

    '<bool_scalvar>':[
        ['<bool_val>'],
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
        ['<bool_lit>'],
        ['(', '<bool_lit>', ')'],
        ['<relational>'],
        ['(', '<relational>', ')'],
        ['<logical>'],
        ['(', '<logical>', ')'],
        ['<id_val>'],
        ['(', '<id_val>', ')']
    ],

    '<bool_lit>':[
        ['true'],
        ['false']
    ],

    ############### Productions for FUNCTIONS (177 onwards) ###############
    '<sub_func>':[
        ['<sub_funcdec>', '<sub_func>'],
        []
    ],

    '<sub_funcdec>':[
        ['make', 'id', '(', '<parameters>', ')', '->', '<functype>']
    ],

    '<parameters>':[
        ['<datatype>', '<1d_arr>', 'id', '<par_tail>'],
        []
    ],

    '<datatype>':[
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
        [',', '<datatype>', '<1d_arr>', 'id', '<par_tail>'],
        []
    ],

    '<functype>':[
        ['int', '<int_subfunc>'],
        ['float', '<float_subfunc>'],
        ['char', '<char_subfunc>'],
        ['string', '<str_subfunc>'],
        ['bool', '<bool_subfunc>'],
        ['void', '{', '<func_body>', 'giveback', 'void', ';', '}']
    ],

    ############### Productions for INT SUBFUNC (199-202) ###############
    '<int_subfunc>':[
        ['{', '<func_body>', 'giveback', '<int_val>', ';', '}'],
        ['[', ']', '<int_functype>']
    ],

    '<int_functype>':[
        ['{', '<func_body>', 'giveback', '<int_1d_val>', ';', '}'],
        ['[', ']', '{', '<func_body>', 'giveback', '<int_2d_val>', ';', '}']
    ],

    ############### Productions for FLOAT SUBFUNC (203-206) ###############
    '<float_subfunc>':[
        ['{', '<func_body>', 'giveback', '<float_val>', ';', '}'],
        ['[', ']', '<float_functype>']
    ],

    '<float_functype>':[
        ['{', '<func_body>', 'giveback', '<float_1d_val>', ';', '}'],
        ['[', ']', '{', '<func_body>', 'giveback', '<float_2d_val>', ';', '}']
    ],

    ############### Productions for CHAR SUBFUNC (207-210) ###############
    '<char_subfunc>':[
        ['{', '<func_body>', 'giveback', '<char_val>', ';', '}'],
        ['[', ']', '<char_functype>']
    ],

    '<char_functype>':[
        ['{', '<func_body>', 'giveback', '<char_1d_val>', ';', '}'],
        ['[', ']', '{', '<func_body>', 'giveback', '<char_2d_val>', ';', '}']
    ],

    ############### Productions for STRING SUBFUNC (211-214) ###############
    '<str_subfunc>':[
        ['{', '<func_body>', 'giveback', '<str_val>', ';', '}'],
        ['[', ']', '<str_functype>']
    ],

    '<str_functype>':[
        ['{', '<func_body>', 'giveback', '<str_1d_val>', ';', '}'],
        ['[', ']', '{', '<func_body>', 'giveback', '<str_2d_val>', ';', '}']
    ],

    ############### Productions for BOOL SUBFUNC (215-218) ###############
    '<bool_subfunc>':[
        ['{', '<func_body>', 'giveback', '<bool_val>', ';', '}'],
        ['[', ']', '<bool_functype>']
    ],

    '<bool_functype>':[
        ['{', '<func_body>', 'giveback', '<bool_1d_val>', ';', '}'],
        ['[', ']', '{', '<func_body>', 'giveback', '<bool_2d_val>', ';', '}']
    ],

    ############### Productions for FUNC BODY (220 onwards) ###############
    '<func_body>':[
        ['<local_var>', '<func_body>'],
        ['<stmnt_list>', '<func_body>'],
        []
    ],

    '<local_var>':[
        ['const', '<var_dtype>', ';'],
        ['<var_dtype>', ';']
    ],

    '<stmnt_list>':[
        ['<stmnt>', '<stmnt_list>'],
        []
    ],

    '<stmnt>':[
        ['<expr>', ';'],
        ['<assignment>', ';'],
        ['<giveback>', ';'],
        ['<IO>', ';'],
        ['<func_call>', ';'],
        ['<conditional>'],
        ['<iterative>']
    ],

    '<expr>':[
        ['<arith>'],
        ['<str_concat>'],
        ['<relational>'],
        ['<logical>']
    ],

    ############### Productions for ARITHMETIC (237-259) ###############
    '<arith>':[
        ['<unary>'],
        ['<binary>']
    ],

    '<int_arith>':[
        ['<unary>'],
        ['<int_binary>']
    ],

    '<unary>':[
        ['<id_val>', '<unary_op>'],
        ['<unary_op>', '<id_val>']
    ],

    '<unary_op>':[
        ['++'],
        ['--']
    ],

    '<binary>':[
        ['<arith_operand>', '<chain_arith>']
    ],

    '<arith_operand>':[
        ['<int_val>'],
        ['<float_val>'],
        ['(', '<binary>', ')']
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

    '<int_binary>':[
        ['<int_val>', '<int_chain_arith>']
    ],

    '<int_chain_arith>':[
        ['<binary_op>', '<int_val>', '<int_chain_arith>'],
        []
    ],

    ############### Productions for STRING CONCAT (260-275) ###############
    '<str_concat>':[
        ['<str_operand>', '+', '<str_concat_operand>', '<chain_str_concat>']
    ],

    '<str_operand>':[
        ['string_lit'],
        ['(', 'string_lit', ')'],
        ['<id_val>'],
        ['(', '<id_val>', ')']
    ],

    '<str_concat_operand>':[
        ['(', '<expr>', ')'],
        ['<expr>'],
        ['<val>']
    ],

    '<val>':[
        ['null'],
        ['<int_val>'],
        ['<float_val>'],
        ['<char_val>'],
        ['<str_val>'],
        ['<bool_val>']
    ],

    '<chain_str_concat>':[
        ['+', '<str_concat_operand>'],
        []
    ],
    
    ############### Productions for RELATIONAL (276-314) ###############
    '<relational>':[
        ['<num_relation>'],
        ['<eq_relation>'],
        ['<str_relation>'],
        ['<ch_relation>']
    ],

    '<num_relation>':[
        ['<num_relation_operand>', '<relation_op>', '<num_relation_operand>']
    ],

    '<num_relation_operand>':[
        ['<int_val>'],
        ['<float_val>'],
        ['<arith>'],
        ['(', '<arith>', ')']
    ],

    '<eq_relation>':[
        ['<eq_operand>', '<eq_op>', '<eq_operand>']
    ],

    '<eq_operand>':[
        ['<float_val>'],
        ['<int_val>'],
        ['<arith>'],
        ['(', '<arith>', ')'],
        ['string_lit'],                 
        ['(', 'string_lit', ')'],
        ['(', '<str_concat>', ')'],
        ['<char_val>'],
        ['<bool_lit>'],
        ['(', '<bool_lit>', ')'],
        ['<relational>'],
        ['(', '<relational>', ')'],
        ['<logical>'],
        ['(', '<logical>', ')'],
        ['<id_val>'],
        ['null']
    ],

    '<str_relation>':[
        ['<str_relation_operand>', '<relation_op>', '<str_relation_operand>']
    ],

    '<str_relation_operand>':[
        ['string_lit'],
        ['(', 'string_lit', ')'],
        ['(', '<str_concat>', ')'],
        ['<id_val>']
    ],

    '<ch_relation>':[
        ['<char_val>', '<relation_op>', '<char_val>']
    ],

    '<relation_op>':[
        ['>'],
        ['<'],
        ['>='],
        ['<='],
        ['<eq_op>']
    ],

    '<eq_op>':[
        ['=='],
        ['!=']
    ],

    ############### Productions for LOGICAL (315-328) ###############
    '<logical>':[
        ['<or_expr>']
    ],

    '<or_expr>':[
        ['<and_expr>', '<chain_or>']
    ],

    '<and_expr>':[
        ['<and_operand>', '<chain_and>'],
        ['(', '<and_operand>', '<chain_and>', ')']
    ],

    '<and_operand>':[
        ['<logical_operand>'],
        ['NOT', '<not_expr>']
    ],

    '<not_expr>':[
        ['(', '<and_operand>', ')'],
        ['<logical_operand>'],
        ['(', '<logical_operand>', ')']
    ],

    '<logical_operand>':[
        ['<bool_val>']
    ],

    '<chain_or>':[
        ['OR', '<and_expr>', '<chain_or>'],
        []
    ],

    '<chain_and>':[
        ['AND', '<and_operand>'],
        []
    ],

    ############### Productions for ASSIGNMENT (329-352) ###############
    '<assignment>':[
        ['<id_val>', '<assign_type>']
    ],

    '<assign_type>':[
        ['=', '<assign_operand>'],
        ['<cmpnd_op>', '<cmpnd_operand>']
    ],

    '<assign_operand>':[
        ['listen', '(', ')'],
        ['null'],
        ['<id_val>'],
        ['<expr>'],
        ['<literal>'],
        ['<func_call>']
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

    '<literal>':[
        ['<bool_lit>'],
        ['int_lit'],
        ['float_lit'],
        ['char_lit'],
        ['string_lit']
    ],

    ############### Productions for ASSIGNMENT - FUNC CALL (353-362) ###############
    '<giveback>':[
        ['giveback', '<ret_val>']
    ],

    '<ret_val>':[
        ['void'],
        ['<val>']
    ],

    '<IO>':[
        ['say', '(', '<args>', ')'],
        ['listen', '(', ')']
    ],

    '<func_call>':[
        ['id', '(', '<args>', ')']
    ],

    '<args>':[
        ['<val>', '<val_tail>'],
        []
    ],

    '<val_tail>':[
        [',', '<val>', '<val_tail>'],
        []
    ],

    ############### Productions for CONDITIONAL (363 - 378) ###############
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

    ############### Productions for ITERATIVE (379 - 386) ###############
    '<iterative>':[
        ['for', '(', '<ctrl_var>', ';', '<for_bool>', ';', '<for_unary>', ')', '{', '<ctrl_block>', '}'],
        ['while', '(', '<bool_val>', ')', '{', '<ctrl_block>', '}']
    ],

    '<ctrl_var>':[
        ['<local_var>'],
        []
    ],

    '<for_bool>':[
        ['<bool_val>'],
        []
    ],

    '<for_unary>':[
        ['<unary>'],
        []
    ]
}

PREDICT_SET = {
    '<program>':{
        'const':    ['<program>', 0],       ###### 1
        'int':      ['<program>', 0],
        'float':    ['<program>', 0],
        'char':     ['<program>', 0],
        'string':   ['<program>', 0],
        'bool':     ['<program>', 0],
        'make':     ['<program>', 0],
        'spyce':    ['<program>', 0]
    },

    '<global_var>':{
        'const':    ['<global_var>', 0],    ###### 2
        'int':      ['<global_var>', 1],    ###### 3
        'float':    ['<global_var>', 1],
        'char':     ['<global_var>', 1],
        'string':   ['<global_var>', 1],
        'bool':     ['<global_var>', 1],
        'make':     ['<global_var>', 2],     ###### 4
        'spyce':    ['<global_var>', 2]
    },

    '<var_dtype>':{
        'int':      ['<var_dtype>', 0],       ###### 5
        'float':    ['<var_dtype>', 1],       ###### 6
        'char':     ['<var_dtype>', 2],       ###### 7
        'string':   ['<var_dtype>', 3],       ###### 8
        'bool':     ['<var_dtype>', 4],       ###### 9
    },

    ############### Productions for INT (10-50) ###############
    '<int_vartype>':{
        'id':   ['<int_vartype>', 0],      ###### 10
        '[':    ['<int_vartype>', 1]       ###### 11
    },

    '<int_scalvar>':{
        'int_lit':  ['<int_scalvar>', 0],  ###### 12
        '(':        ['<int_scalvar>', 0],       
        'id':       ['<int_scalvar>', 0],      
        '++':       ['<int_scalvar>', 0],
        '--':       ['<int_scalvar>', 0],
        'listen':   ['<int_scalvar>', 1],  ###### 13
        'null':     ['<int_scalvar>', 2]   ###### 14
    },

    '<int_scaldec_tail>':{
        ',':['<int_scaldec_tail>', 0],  ###### 15
        ';':['<int_scaldec_tail>', 1]    ###### 16
    },

    '<int_arrtype>':{
        'id':   ['<int_arrtype>', 0],   ###### 17
        '[':    ['<int_arrtype>', 1]      ###### 18
    },

    '<int_1d_val>':{
        'id':   ['<int_1d_val>', 0],
        '{':    ['<int_1d_val>', 1]
    },

    '<inner_arr_indx>':{
        '[':['<inner_arr_indx>', 0],
        ',':['<inner_arr_indx>', 1],
        ';':['<inner_arr_indx>', 1],
        '}':['<inner_arr_indx>', 1]
    },

    '<int_arrlit>':{
        'int_lit':  ['<int_arrlit>', 0],  
        '(':        ['<int_arrlit>', 0],       
        'id':       ['<int_arrlit>', 0],      
        '++':       ['<int_arrlit>', 0],
        '--':       ['<int_arrlit>', 0],
        '}':        ['<int_arrlit>', 1]
    },

    '<int_val_tail>':{
        ',':['<int_val_tail>', 0],
        '}':['<int_val_tail>', 1]
    },

    '<int_1d_dec_tail>':{
        ',':['<int_1d_dec_tail>', 0],
        ';':['<int_1d_dec_tail>', 1]
    },

    '<int_2d_val>':{
        'id':   ['<int_2d_val>', 0],
        '{':    ['<int_2d_val>', 1]
    },

    '<int_2d_elem>':{
        'id':   ['<int_2d_elem>', 0],
        '{':    ['<int_2d_elem>', 0],
        '}':    ['<int_2d_elem>', 1]
    },

    '<int_2dval_tail>':{
        ',':['<int_2dval_tail>', 0],
        '}':['<int_2dval_tail>', 1]
    },

    '<int_2d_dec_tail>':{
        ',':['<int_2d_dec_tail>', 0],
        ';':['<int_2d_dec_tail>', 1]
    },

    '<int_val>':{
        ####################### TO BE FIXED #######################
        'int_lit':['<int_val>', 0],
        '++':['<int_val>', 1],
        '--':['<int_val>', 1],
        'id':['<int_val>', 1],
        '(':['<int_val>', 2]
    },

    '<id_val>':{
      'id':['<id_val>', 0]  
    },

    '<1d_indx>':{
        '[':    ['<1d_indx>', 0],
        ',':    ['<1d_indx>', 1],
        ';':    ['<1d_indx>', 1],
        ']':    ['<1d_indx>', 1],
        '}':    ['<1d_indx>', 1],
        '+':    ['<1d_indx>', 1],
        '-':    ['<1d_indx>', 1],
        '*':    ['<1d_indx>', 1],
        '/':    ['<1d_indx>', 1],
        '**':   ['<1d_indx>', 1],
        '%':    ['<1d_indx>', 1],
        ')':    ['<1d_indx>', 1],
        '>':    ['<1d_indx>', 1],
        '<':    ['<1d_indx>', 1],
        '>=':   ['<1d_indx>', 1],
        '<=':   ['<1d_indx>', 1],
        '==':   ['<1d_indx>', 1],
        '!=':   ['<1d_indx>', 1],
        'AND':  ['<1d_indx>', 1],
        'OR':   ['<1d_indx>', 1],
        '++':   ['<1d_indx>', 1],
        '--':   ['<1d_indx>', 1],
        '=':    ['<1d_indx>', 1],
        '+=':   ['<1d_indx>', 1],
        '-=':   ['<1d_indx>', 1],
        '*=':   ['<1d_indx>', 1],
        '/=':   ['<1d_indx>', 1],
        '**=':  ['<1d_indx>', 1],
        '%=':   ['<1d_indx>', 1]
    },

    '<2d_indx>':{
        '[':    ['<2d_indx>', 0],
        ',':    ['<2d_indx>', 1],
        ';':    ['<2d_indx>', 1],
        ']':    ['<2d_indx>', 1],
        '}':    ['<2d_indx>', 1],
        '+':    ['<2d_indx>', 1],
        '-':    ['<2d_indx>', 1],
        '*':    ['<2d_indx>', 1],
        '/':    ['<2d_indx>', 1],
        '**':   ['<2d_indx>', 1],
        '%':    ['<2d_indx>', 1],
        ')':    ['<2d_indx>', 1],
        '>':    ['<2d_indx>', 1],
        '<':    ['<2d_indx>', 1],
        '>=':   ['<2d_indx>', 1],
        '<=':   ['<2d_indx>', 1],
        '==':   ['<2d_indx>', 1],
        '!=':   ['<2d_indx>', 1],
        'AND':  ['<2d_indx>', 1],
        'OR':   ['<2d_indx>', 1],
        '++':   ['<2d_indx>', 1],
        '--':   ['<2d_indx>', 1],
        '=':    ['<2d_indx>', 1],
        '+=':   ['<2d_indx>', 1],
        '-=':   ['<2d_indx>', 1],
        '*=':   ['<2d_indx>', 1],
        '/=':   ['<2d_indx>', 1],
        '**=':  ['<2d_indx>', 1],
        '%=':   ['<2d_indx>', 1]
    },

    '<indx_val>':{          ########## TO BE CHANGED #########
        'id':       ['<indx_val>', 0],
        'int_lit':  ['<indx_val>', 1],
        '(':        ['<indx_val>', 2],
        '++':       ['<indx_val>', 2],
        '--':       ['<indx_val>', 2],
    },

    ############### Productions for FLOAT (51-81) ###############
    '<float_vartype>':{
        'id':   ['<float_vartype>', 0],     
        '[':    ['<float_vartype>', 1]       
    },

    '<float_scalvar>':{
        'float_lit':    ['<float_scalvar>', 0],       
        'id':           ['<float_scalvar>', 0],      
        '++':           ['<float_scalvar>', 0],
        '--':           ['<float_scalvar>', 0],
        'int_lit':      ['<float_scalvar>', 0],
        '(':            ['<float_scalvar>', 0],
        'listen':       ['<float_scalvar>', 1],  
        'null':         ['<float_scalvar>', 2]   
    },

    '<float_scaldec_tail>':{
        ',':['<float_scaldec_tail>', 0],  
        ';':['<float_scaldec_tail>', 1]    
    },

    '<float_arrtype>':{
        'id':   ['<float_arrtype>', 0],   
        '[':    ['<float_arrtype>', 1]      
    },

    '<float_1d_val>':{
        'id':   ['<float_1d_val>', 0],
        '{':    ['<float_1d_val>', 1]
    },

    '<float_arrlit>':{
        'float_lit':    ['<float_arrlit>', 0], 
        'id':           ['<float_arrlit>', 0],
        '++':           ['<float_arrlit>', 0],
        '--':           ['<float_arrlit>', 0], 
        'int_lit':      ['<float_arrlit>', 0], 
        '(':            ['<float_arrlit>', 0],       
        '}':            ['<float_arrlit>', 1]
    },

    '<float_val_tail>':{
        ',':['<float_val_tail>', 0],
        '}':['<float_val_tail>', 1]
    },

    '<float_1d_dec_tail>':{
        ',':['<float_1d_dec_tail>', 0],
        ';':['<float_1d_dec_tail>', 1]
    },

    '<float_2d_val>':{
        'id':   ['<float_2d_val>', 0],
        '{':    ['<float_2d_val>', 1]
    },

    '<float_2d_elem>':{
        'id':   ['<float_2d_elem>', 0],
        '{':    ['<float_2d_elem>', 0],
        '}':    ['<float_2d_elem>', 1]
    },

    '<float_2dval_tail>':{
        ',':['<float_2dval_tail>', 0],
        '}':['<float_2dval_tail>', 1]
    },

    '<float_2d_dec_tail>':{
        ',':['<float_2d_dec_tail>', 0],
        ';':['<float_2d_dec_tail>', 1]
    },

    '<float_val>':{
        ####################### TO BE FIXED #######################
        'float_lit':['<float_val>', 0],
        'int_lit':['<float_val>', 1],
        '++':['<float_val>', 1],
        '--':['<float_val>', 1],
        'id':['<float_val>', 1],
        '(':['<float_val>', 2]
    },

    ############### Productions for CHAR (82-110) ###############
    '<char_vartype>':{
        'id':   ['<char_vartype>', 0],     
        '[':    ['<char_vartype>', 1]       
    },

    '<char_scalvar>':{
        'char_lit':     ['<char_scalvar>', 0],   
        '(':            ['<char_scalvar>', 0],
        'id':           ['<char_scalvar>', 0],      
        'listen':       ['<char_scalvar>', 1],  
        'null':         ['<char_scalvar>', 2]   
    },

    '<char_scaldec_tail>':{
        ',':['<char_scaldec_tail>', 0],  
        ';':['<char_scaldec_tail>', 1]    
    },

    '<char_arrtype>':{
        'id':   ['<char_arrtype>', 0],   
        '[':    ['<char_arrtype>', 1]      
    },

    '<char_1d_val>':{
        'id':   ['<char_1d_val>', 0],
        '{':    ['<char_1d_val>', 1]
    },

    '<char_arrlit>':{
        'char_lit':    ['<char_arrlit>', 0], 
        '(':            ['<char_arrlit>', 0],       
        'id':           ['<char_arrlit>', 0],
        '}':            ['<char_arrlit>', 1]
    },

    '<char_val_tail>':{
        ',':['<char_val_tail>', 0],
        '}':['<char_val_tail>', 1]
    },

    '<char_1d_dec_tail>':{
        ',':['<char_1d_dec_tail>', 0],
        ';':['<char_1d_dec_tail>', 1]
    },

    '<char_2d_val>':{
        'id':   ['<char_2d_val>', 0],
        '{':    ['<char_2d_val>', 1]
    },

    '<char_2d_elem>':{
        'id':   ['<char_2d_elem>', 0],
        '{':    ['<char_2d_elem>', 0],
        '}':    ['<char_2d_elem>', 1]
    },

    '<char_2dval_tail>':{
        ',':['<char_2dval_tail>', 0],
        '}':['<char_2dval_tail>', 1]
    },

    '<char_2d_dec_tail>':{
        ',':['<char_2d_dec_tail>', 0],
        ';':['<char_2d_dec_tail>', 1]
    },

    '<char_val>':{
        'char_lit':['<char_val>', 0],
        'id':['<char_val>', 1],
        '(':['<char_val>', 2]
    },

    ############### Productions for STRING (111-141) ###############
    '<str_vartype>':{
        'id':   ['<str_vartype>', 0],     
        '[':    ['<str_vartype>', 1]       
    },

    '<str_scalvar>':{
        'string_lit':   ['<str_scalvar>', 0],       
        'id':           ['<str_scalvar>', 0],      
        '(':            ['<str_scalvar>', 0],
        'listen':       ['<str_scalvar>', 1],  
        'null':         ['<str_scalvar>', 2]   
    },

    '<str_scaldec_tail>':{
        ',':['<str_scaldec_tail>', 0],  
        ';':['<str_scaldec_tail>', 1]    
    },

    '<str_arrtype>':{
        'id':   ['<str_arrtype>', 0],   
        '[':    ['<str_arrtype>', 1]      
    },

    '<str_1d_val>':{
        'id':   ['<str_1d_val>', 0],
        '{':    ['<str_1d_val>', 1]
    },

    '<str_arrlit>':{
        'string_lit':   ['<str_arrlit>', 0], 
        'id':           ['<str_arrlit>', 0],
        '(':            ['<str_arrlit>', 0],       
        '}':            ['<str_arrlit>', 1]
    },

    '<str_val_tail>':{
        ',':['<str_val_tail>', 0],
        '}':['<str_val_tail>', 1]
    },

    '<str_1d_dec_tail>':{
        ',':['<str_1d_dec_tail>', 0],
        ';':['<str_1d_dec_tail>', 1]
    },

    '<str_2d_val>':{
        'id':   ['<str_2d_val>', 0],
        '{':    ['<str_2d_val>', 1]
    },

    '<str_2d_elem>':{
        'id':   ['<str_2d_elem>', 0],
        '{':    ['<str_2d_elem>', 0],
        '}':    ['<str_2d_elem>', 1]
    },

    '<str_2dval_tail>':{
        ',':['<str_2dval_tail>', 0],
        '}':['<str_2dval_tail>', 1]
    },

    '<str_2d_dec_tail>':{
        ',':['<str_2d_dec_tail>', 0],
        ';':['<str_2d_dec_tail>', 1]
    },

    '<str_val>':{
        ####################### TO BE FIXED #######################
        'string_lit':   ['<str_val>', 0],       
        'id':           ['<str_val>', 1],      
        '(':            ['<str_val>', 0],
    },

    ############### Productions for BOOL (142-176) ###############
    '<bool_vartype>':{
        'id':   ['<bool_vartype>', 0],     
        '[':    ['<bool_vartype>', 1]       
    },

    '<bool_scalvar>':{ ##### POSSIBLE PROBLEM
        'float_lit':    ['<bool_scalvar>', 0],       
        '++':           ['<bool_scalvar>', 0],
        '--':           ['<bool_scalvar>', 0],
        'int_lit':      ['<bool_scalvar>', 0],
        'true':         ['<bool_scalvar>', 0],
        'false':        ['<bool_scalvar>', 0],
        '(':            ['<bool_scalvar>', 0],
        'id':           ['<bool_scalvar>', 0], 
        'null':         ['<bool_scalvar>', 0],      
        'string_lit':   ['<bool_scalvar>', 0],      
        'char_lit':     ['<bool_scalvar>', 0],      
        'NOT':          ['<bool_scalvar>', 0],      
        'listen':       ['<bool_scalvar>', 1],  
        'null':         ['<bool_scalvar>', 2]   
    },

    '<bool_scaldec_tail>':{
        ',':['<bool_scaldec_tail>', 0],  
        ';':['<bool_scaldec_tail>', 1]    
    },

    '<bool_arrtype>':{
        'id':   ['<bool_arrtype>', 0],   
        '[':    ['<bool_arrtype>', 1]      
    },

    '<bool_1d_val>':{
        'id':   ['<bool_1d_val>', 0],
        '{':    ['<bool_1d_val>', 1]
    },

    '<bool_arrlit>':{
        'float_lit':    ['<bool_arrlit>', 0],       
        '++':           ['<bool_arrlit>', 0],
        '--':           ['<bool_arrlit>', 0],
        'int_lit':      ['<bool_arrlit>', 0],
        'true':         ['<bool_arrlit>', 0],
        'false':        ['<bool_arrlit>', 0],
        '(':            ['<bool_arrlit>', 0],
        'id':           ['<bool_arrlit>', 0], 
        'null':         ['<bool_arrlit>', 0],      
        'string_lit':   ['<bool_arrlit>', 0],      
        'char_lit':     ['<bool_arrlit>', 0],      
        'NOT':          ['<bool_arrlit>', 0],       
        '}':            ['<bool_arrlit>', 1]
    },

    '<bool_val_tail>':{
        ',':['<bool_val_tail>', 0],
        '}':['<bool_val_tail>', 1]
    },

    '<bool_1d_dec_tail>':{
        ',':['<bool_1d_dec_tail>', 0],
        ';':['<bool_1d_dec_tail>', 1]
    },

    '<bool_2d_val>':{
        'id':   ['<bool_2d_val>', 0],
        '{':    ['<bool_2d_val>', 1]
    },

    '<bool_2d_elem>':{
        'id':   ['<bool_2d_elem>', 0],
        '{':    ['<bool_2d_elem>', 0],
        '}':    ['<bool_2d_elem>', 1]
    },

    '<bool_2dval_tail>':{
        ',':['<bool_2dval_tail>', 0],
        '}':['<bool_2dval_tail>', 1]
    },

    '<bool_2d_dec_tail>':{
        ',':['<bool_2d_dec_tail>', 0],
        ';':['<bool_2d_dec_tail>', 1]
    },

    '<bool_val>':{
        ####################### TO BE FIXED #######################
        'true':['<bool_val>', 0],
        'false':['<bool_val>', 0],
        '(':['<bool_val>', 1],
        'float_lit':['<bool_val>', 2],
        '++':['<bool_val>', 2],
        '--':['<bool_val>', 2],
        'int_lit':['<bool_val>', 2],
        'id':['<bool_val>', 2],
        'null':['<bool_val>', 2],
        'string_lit':['<bool_val>', 2],
        'char_lit':['<bool_val>', 2],
    },

    '<bool_lit>':{
        'true': ['<bool_lit>', 0],
        'false':['<bool_lit>', 1],
    },

    ############### Productions for FUNCTIONS (177 onwards) ###############
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

    '<datatype>':{
        'int':      ['<datatype>', 0],
        'float':    ['<datatype>', 1],
        'char':     ['<datatype>', 2],
        'string':   ['<datatype>', 3],
        'bool':     ['<datatype>', 4],
    },

    '<1d_arr>':{
        '[':    ['<1d_arr>', 0],
        'id':   ['<1d_arr>', 1]
    },

    '<2d_arr>':{
        '[':    ['<2d_arr>', 0],
        'id':   ['<2d_arr>', 1]
    },

    '<par_tail>':{
        ',':['<par_tail>', 0],
        ')':['<par_tail>', 1]
    },

    '<functype>':{
       'int':   ['<functype>', 0],
       'float': ['<functype>', 1], 
       'char':  ['<functype>', 2], 
       'string':['<functype>', 3], 
       'bool':  ['<functype>', 4], 
       'void':  ['<functype>', 5], 
    },

    ############### Productions for INT SUBFUNC (199-202) ###############
    '<int_subfunc>':{
        '{':['<int_subfunc>', 0],
        '[':['<int_subfunc>', 1]
    },

    '<int_functype>':{
        '{':['<int_functype>', 0],
        '[':['<int_functype>', 1]
    },

    ############### Productions for FLOAT SUBFUNC (203-206) ###############
    '<float_subfunc>':{
        '{':['<float_subfunc>', 0],
        '[':['<float_subfunc>', 1]
    },

    '<float_functype>':{
        '{':['<float_functype>', 0],
        '[':['<float_functype>', 1]
    },

    ############### Productions for CHAR SUBFUNC (207-210) ###############
    '<char_subfunc>':{
        '{':['<char_subfunc>', 0],
        '[':['<char_subfunc>', 1]
    },

    '<char_functype>':{
        '{':['<char_functype>', 0],
        '[':['<char_functype>', 1]
    },

    ############### Productions for STRING SUBFUNC (211-214) ###############
    '<str_subfunc>':{
        '{':['<str_subfunc>', 0],
        '[':['<str_subfunc>', 1]
    },

    '<str_functype>':{
        '{':['<str_functype>', 0],
        '[':['<str_functype>', 1]
    },

    ############### Productions for BOOL SUBFUNC (215-218) ###############
    '<bool_subfunc>':{
        '{':['<bool_subfunc>', 0],
        '[':['<bool_subfunc>', 1]
    },

    '<bool_functype>':{
        '{':['<bool_functype>', 0],
        '[':['<bool_functype>', 1]
    },

    ############### Productions for FUNC BODY (220 onwards) ###############
    '<func_body>':{
        'const':        ['<func_body>', 0],
        'int':          ['<func_body>', 0],
        'float':        ['<func_body>', 0],
        'char':         ['<func_body>', 0],
        'string':       ['<func_body>', 0],
        'bool':         ['<func_body>', 0],
        'float_lit':    ['<func_body>', 1],
        '++':           ['<func_body>', 1],
        '--':           ['<func_body>', 1],
        'int_lit':      ['<func_body>', 1],
        'true':         ['<func_body>', 1],
        'false':        ['<func_body>', 1],
        '(':            ['<func_body>', 1],
        'id':           ['<func_body>', 1],
        'null':         ['<func_body>', 1],
        'string_lit':   ['<func_body>', 1],
        'char_lit':     ['<func_body>', 1],
        'NOT':          ['<func_body>', 1],
        'giveback':     ['<func_body>', 1],
        'say':          ['<func_body>', 1],
        'listen':       ['<func_body>', 1],
        'when':         ['<func_body>', 1],
        'choose':       ['<func_body>', 1],
        'for':          ['<func_body>', 1],
        'while':        ['<func_body>', 1],
        'giveback':     ['<func_body>', 2]
    },

    '<local_var>':{
        'const':    ['<local_var>', 0],
        'int':      ['<local_var>', 1],
        'float':    ['<local_var>', 1],
        'char':     ['<local_var>', 1],
        'string':   ['<local_var>', 1],
        'bool':     ['<local_var>', 1],
    },

    '<stmnt_list>':{
        'float_lit':    ['<stmnt_list>', 0],
        '++':           ['<stmnt_list>', 0],
        '--':           ['<stmnt_list>', 0],
        'int_lit':      ['<stmnt_list>', 0],
        'true':         ['<stmnt_list>', 0],
        'false':        ['<stmnt_list>', 0],
        '(':            ['<stmnt_list>', 0],
        'id':           ['<stmnt_list>', 0],
        'null':         ['<stmnt_list>', 0],
        'string_lit':   ['<stmnt_list>', 0],
        'char_lit':     ['<stmnt_list>', 0],
        'NOT':          ['<stmnt_list>', 0],
        'giveback':     ['<stmnt_list>', 0],
        'say':          ['<stmnt_list>', 0],
        'listen':       ['<stmnt_list>', 0],
        'when':         ['<stmnt_list>', 0],
        'choose':       ['<stmnt_list>', 0],
        'for':          ['<stmnt_list>', 0],
        'while':        ['<stmnt_list>', 0],
        'const':        ['<stmnt_list>', 1],
        'int':          ['<stmnt_list>', 1],
        'float':        ['<stmnt_list>', 1],
        'char':         ['<stmnt_list>', 1],
        'string':       ['<stmnt_list>', 1],
        'bool':         ['<stmnt_list>', 1],
    },

    '<stmnt>':{
        'float_lit':    ['<stmnt>', 0],
        '++':           ['<stmnt>', 0],
        '--':           ['<stmnt>', 0],
        'int_lit':      ['<stmnt>', 0],
        'true ':        ['<stmnt>', 0],
        'false':        ['<stmnt>', 0],
        '(':            ['<stmnt>', 0],
        'null':         ['<stmnt>', 0],
        'string_lit':   ['<stmnt>', 0],
        'char_lit':     ['<stmnt>', 0],
        'NOT':          ['<stmnt>', 0],
        'id':           ['<stmnt>', 1],
        'giveback':     ['<stmnt>', 2],
        'say':          ['<stmnt>', 3],
        'listen':       ['<stmnt>', 3],
        'id':           ['<stmnt>', 4],
        'when':         ['<stmnt>', 5],
        'choose':       ['<stmnt>', 5],
        'for':          ['<stmnt>', 6],
        'while':        ['<stmnt>', 6],
    },

    '<expr>':{
        'id':['<expr>', 0],
        '++':['<expr>', 0],
        '--':['<expr>', 0],
        'int_lit':['<expr>', 0],
        '(':['<expr>', 0],
        'float_lit':['<expr>', 0],
        'string_lit':['<expr>', 1],
        'true':['<expr>', 2],
        'false':['<expr>', 2],
        'null':['<expr>', 2],
        'char_lit':['<expr>', 2],
        'NOT':['<expr>', 2],
    },

    ############### Productions for ARITHMETIC (237-259) ###############
    '<arith>':{
        'id':['<arith>', 0],
        '++':['<arith>', 0],
        '--':['<arith>', 0],
        'int_lit':['<arith>', 1],
        '(':['<arith>', 1],
        'id':['<arith>', 1],
        'float_lit':['<arith>', 1],
    },

    '<int_arith>':{
        'id':['<int_arith>', 0],
        '++':['<int_arith>', 0],
        '--':['<int_arith>', 0],
        'int_lit':['<int_arith>', 1],
        '(':['<int_arith>', 1],
        'id':['<int_arith>', 1],
    },

    '<unary>':{
        'id':['<unary>', 0],
        '++':['<unary>', 1],
        '--':['<unary>', 1]
    },

    '<unary_op>':{
        '++':['<unary_op>', 0],
        '--':['<unary_op>', 1]
    },

    '<binary>':{
        'int_lit':['<binary>', 0],
        '(':['<binary>', 0],
        'id':['<binary>', 0],
        '++':['<binary>', 0],
        '--':['<binary>', 0],
        'float_lit':['<binary>', 0],
    },

    '<arith_operand>':{
       'int_lit':['<arith_operand>', 0], 
       'id':['<arith_operand>', 1], 
       '++':['<arith_operand>', 1], 
       '--':['<arith_operand>', 1], 
       'float_lit':['<arith_operand>', 1], 
       '(':['<arith_operand>', 2]
    },

    '<chain_arith>':{
        '+':    ['<chain_arith>', 0],
        '-':    ['<chain_arith>', 0],
        '*':    ['<chain_arith>', 0],
        '/':    ['<chain_arith>', 0],
        '**':   ['<chain_arith>', 0],
        '%':    ['<chain_arith>', 0],
        ';':    ['<chain_arith>', 1],
        ')':    ['<chain_arith>', 1],
        ',':    ['<chain_arith>', 1],
        '}':    ['<chain_arith>', 1],
        '>':    ['<chain_arith>', 1],
        '<':    ['<chain_arith>', 1],
        '>=':   ['<chain_arith>', 1],
        '<=':   ['<chain_arith>', 1],
        '==':   ['<chain_arith>', 1],
        '!=':   ['<chain_arith>', 1],
        'AND':  ['<chain_arith>', 1],
        'OR':   ['<chain_arith>', 1],
    },

    '<binary_op>':{
        '+':    ['<binary_op>', 0],
        '-':    ['<binary_op>', 1],
        '*':    ['<binary_op>', 2],
        '/':    ['<binary_op>', 3],
        '**':   ['<binary_op>', 4],
        '%':    ['<binary_op>', 5]
    },

    '<int_binary>':{
       'int_lit':['<int_binary>', 0], 
       '(':['<int_binary>', 0], 
       'id':['<int_binary>', 0], 
       '++':['<int_binary>', 0], 
       '--':['<int_binary>', 0], 
    },

    '<int_chain_arith>':{
        '+':    ['<int_chain_arith>', 0],
        '-':    ['<int_chain_arith>', 0],
        '*':    ['<int_chain_arith>', 0],
        '/':    ['<int_chain_arith>', 0],
        '**':   ['<int_chain_arith>', 0],
        '%':    ['<int_chain_arith>', 0],
        ',':    ['<int_chain_arith>', 1],
        ';':    ['<int_chain_arith>', 1],
        ']':    ['<int_chain_arith>', 1],
        '}':    ['<int_chain_arith>', 1],
        ')':    ['<int_chain_arith>', 1],
        '>':    ['<int_chain_arith>', 1],
        '<':    ['<int_chain_arith>', 1],
        '>=':   ['<int_chain_arith>', 1],
        '<=':   ['<int_chain_arith>', 1],
        '==':   ['<int_chain_arith>', 1],
        '!=':   ['<int_chain_arith>', 1],
        'AND':  ['<int_chain_arith>', 1],
        'OR':   ['<int_chain_arith>', 1],
    },

    ############### Productions for STRING CONCAT (260-275) ###############
    '<str_concat>':{
        'string_lit':['<str_concat>', 0],
        '(':['<str_concat>', 0],
        'id':['<str_concat>', 0],
    },

    '<str_operand>':{
        'string_lit':['<str_operand>', 0],
        '(':['<str_operand>', 1],
        'id':['<str_operand>', 2],
    },

    '<str_concat_operand>':{
        'float_lit':['<str_concat_operand>', 0],
        '++':['<str_concat_operand>', 0],
        '--':['<str_concat_operand>', 0],
        'int_lit':['<str_concat_operand>', 0],
        'true':['<str_concat_operand>', 0],
        'false':['<str_concat_operand>', 0],
        '(':['<str_concat_operand>', 0],
        'id':['<str_concat_operand>', 0],
        'null':['<str_concat_operand>', 0],
        'string_lit':['<str_concat_operand>', 0],
        'char_lit':['<str_concat_operand>', 0],
        'NOT':['<str_concat_operand>', 0],
        'true':['<str_concat_operand>', 1],
        'false':['<str_concat_operand>', 1],
    },

    '<val>':{
        'null':['<val>', 0],
        'int_lit':['<val>', 1],
        '(':['<val>', 1],
        'id':['<val>', 1],
        '++':['<val>', 1],
        '--':['<val>', 1],
        'float_lit':['<val>', 2],
        'char_lit':['<val>', 3],
        'string_lit':['<val>', 4],
        'NOT':['<val>', 5]
    },

    '<chain_str_concat>':{
        '+':['<chain_str_concat>', 0],
        ',':['<chain_str_concat>', 1],
        ';':['<chain_str_concat>', 1],
        '}':['<chain_str_concat>', 1],
        ')':['<chain_str_concat>', 1],
    },
    
    ############### Productions for RELATIONAL (276-314) ###############
    '<relational>':{
        'int_lit':['<relational>', 0],
        '++':['<relational>', 0],
        '--':['<relational>', 0],
        'float_lit':['<relational>', 0],
        'true':['<relational>', 1],
        'false':['<relational>', 1],
        'id':['<relational>', 1],
        'null':['<relational>', 1],
        'NOT':['<relational>', 1],
        'string_lit':['<relational>', 2],
        'char_lit':['<relational>', 3],
    },

    '<num_relation>':{
        'int_lit':['<num_relation>', 0],
        '(':['<num_relation>', 0],
        'id':['<num_relation>', 0],
        '++':['<num_relation>', 0],
        '--':['<num_relation>', 0],
        'float_lit':['<num_relation>', 0],
    },

    '<num_relation_operand>':{
        'int_lit':['<num_relation_operand>', 0],
        'float_lit':['<num_relation_operand>', 1],
        '(':['<num_relation_operand>', 2],
        '++':['<num_relation_operand>', 2],
        '--':['<num_relation_operand>', 2],
        'id':['<num_relation_operand>', 2],
    },

    '<eq_relation>':{
        'float_lit':['<eq_relation>', 0],
        '++':['<eq_relation>', 0],
        '--':['<eq_relation>', 0],
        'int_lit':['<eq_relation>', 0],
        'true':['<eq_relation>', 0],
        'false':['<eq_relation>', 0],
        '(':['<eq_relation>', 0],
        'id':['<eq_relation>', 0],
        'null':['<eq_relation>', 0],
        'string_lit':['<eq_relation>', 0],
        'char_lit':['<eq_relation>', 0],
        'NOT':['<eq_relation>', 0],
    },

    '<eq_operand>':[
        
    ],

    '<str_relation>':{
        'string_lit':['<str_relation>', 0],
        '(':['<str_relation>', 0],
        'id':['<str_relation>', 0],
    },

    '<str_relation_operand>':{
        'string_lit':['<str_relation_operand>', 0],
        '(':['<str_relation_operand>', 2],
        'id':['<str_relation_operand>', 3],
    },

    '<ch_relation>':{
        'char_lit':['<str_relation>', 0],
        '(':['<str_relation>', 0],
        'id':['<str_relation>', 0],
    },

    '<relation_op>':{
        '>':    ['<relation_op>', 0],
        '<':    ['<relation_op>', 1],
        '>=':   ['<relation_op>', 2],
        '<=':   ['<relation_op>', 3],
        '==':   ['<relation_op>', 4],
        '!=':   ['<relation_op>', 4],
    },

    '<eq_op>':{
        '==':['<eq_op>', 0],
        '!=':['<eq_op>', 1],
    },

    ############### Productions for LOGICAL (315-328) ###############
    '<logical>':{
        'float_lit':['<logical>', 0],
        '++':['<logical>', 0], 
        '--':['<logical>', 0], 
        'int_lit':['<logical>', 0], 
        'true':['<logical>', 0], 
        'false':['<logical>', 0], 
        '(':['<logical>', 0], 
        'id':['<logical>', 0], 
        'null':['<logical>', 0], 
        'string_lit':['<logical>', 0], 
        'char_lit':['<logical>', 0], 
        'NOT':['<logical>', 0], 
    },

    '<or_expr>':{
        'float_lit':['<or_expr>', 0],
        '++':['<or_expr>', 0], 
        '--':['<or_expr>', 0], 
        'int_lit':['<or_expr>', 0], 
        'true':['<or_expr>', 0], 
        'false':['<or_expr>', 0], 
        '(':['<or_expr>', 0], 
        'id':['<or_expr>', 0], 
        'null':['<or_expr>', 0], 
        'string_lit':['<or_expr>', 0], 
        'char_lit':['<or_expr>', 0], 
        'NOT':['<or_expr>', 0], 
    },

    '<and_expr>':{
        'float_lit':['<and_expr>', 0],
        '++':['<and_expr>', 0], 
        '--':['<and_expr>', 0], 
        'int_lit':['<and_expr>', 0], 
        'true':['<and_expr>', 0], 
        'false':['<and_expr>', 0], 
        '(':['<and_expr>', 0], 
        'id':['<and_expr>', 0], 
        'null':['<and_expr>', 0], 
        'string_lit':['<and_expr>', 0], 
        'char_lit':['<and_expr>', 0], 
        'NOT':['<and_expr>', 0], 
    },

    '<and_operand>':{
        'float_lit':['<and_operand>', 0],
        '++':['<and_operand>', 0], 
        '--':['<and_operand>', 0], 
        'int_lit':['<and_operand>', 0], 
        'true':['<and_operand>', 0], 
        'false':['<and_operand>', 0], 
        '(':['<and_operand>', 0], 
        'id':['<and_operand>', 0], 
        'null':['<and_operand>', 0], 
        'string_lit':['<and_operand>', 0], 
        'char_lit':['<and_operand>', 0], 
        'NOT':['<and_operand>', 0], 
    },

    '<not_expr>':{
        'float_lit':['<not_expr>', 0],
        '++':['<not_expr>', 0], 
        '--':['<not_expr>', 0], 
        'int_lit':['<not_expr>', 0], 
        'true':['<not_expr>', 0], 
        'false':['<not_expr>', 0], 
        '(':['<not_expr>', 0], 
        'id':['<not_expr>', 0], 
        'null':['<not_expr>', 0], 
        'string_lit':['<not_expr>', 0], 
        'char_lit':['<not_expr>', 0], 
        'NOT':['<not_expr>', 0], 
    },

    '<logical_operand>':{
        'float_lit':['<logical_operand>', 0],
        '++':['<logical_operand>', 0], 
        '--':['<logical_operand>', 0], 
        'int_lit':['<logical_operand>', 0], 
        'true':['<logical_operand>', 0], 
        'false':['<logical_operand>', 0], 
        '(':['<logical_operand>', 0], 
        'id':['<logical_operand>', 0], 
        'null':['<logical_operand>', 0], 
        'string_lit':['<logical_operand>', 0], 
        'char_lit':['<logical_operand>', 0], 
        'NOT':['<logical_operand>', 0], 
    },

    '<chain_or>':{
        'OR':['<chain_or>', 0],
        ',':['<chain_or>', 1],
        ';':['<chain_or>', 1],
        ')':['<chain_or>', 1],
        '}':['<chain_or>', 1],
        '+':['<chain_or>', 1],
        '==':['<chain_or>', 1],
        '!=':['<chain_or>', 1],
    },

    '<chain_and>':{
        'AND':['<chain_and>', 0],
        'OR':['<chain_and>', 1],
        ',':['<chain_and>', 1],
        ';':['<chain_and>', 1],
        ')':['<chain_and>', 1],
        '}':['<chain_and>', 1],
        '+':['<chain_and>', 1],
        '==':['<chain_and>', 1],
        '!=':['<chain_and>', 1],
    },

    ############### Productions for ASSIGNMENT (329-352) ###############
    '<assignment>':{
        'id':['<assignment>', 0]
    },

    '<assign_type>':{
        '=':    ['<assign_type>', 0],
        '+=':   ['<assign_type>', 1],
        '-=':   ['<assign_type>', 1],
        '*=':   ['<assign_type>', 1],
        '/=':   ['<assign_type>', 1],
        '**=':  ['<assign_type>', 1],
        '%=':   ['<assign_type>', 1],
    },

    '<assign_operand>':{
        'listen':       ['<assign_operand>', 0],
        'null':         ['<assign_operand>', 1],
        'id':           ['<assign_operand>', 2],
        'float_lit':    ['<assign_operand>', 3],
        '++':           ['<assign_operand>', 3],
        '--':           ['<assign_operand>', 3],
        'int_lit':      ['<assign_operand>', 3],
        'true':         ['<assign_operand>', 3],
        'false':        ['<assign_operand>', 3],
        '(':            ['<assign_operand>', 3],
        'string_lit':   ['<assign_operand>', 3],
        'char_lit':     ['<assign_operand>', 3],
        'NOT':          ['<assign_operand>', 3],
    },

    '<cmpnd_op>':{
        '+=':   ['<cmpnd_op>', 0],
        '-=':   ['<cmpnd_op>', 1],
        '*=':   ['<cmpnd_op>', 2],
        '/=':   ['<cmpnd_op>', 3],
        '**=':  ['<cmpnd_op>', 4],
        '%=':   ['<cmpnd_op>', 5],
    },

    '<cmpnd_operand>':{
        'int_lit':      ['<cmpnd_operand>', 0],
        'float_lit':    ['<cmpnd_operand>', 1],
        'string_lit':   ['<cmpnd_operand>', 2],
        'id':           ['<cmpnd_operand>', 3]
    },

    '<literal>':{
        'true':         ['<literal>', 0],
        'false':        ['<literal>', 0],
        'int_lit':      ['<literal>', 1],
        'float_lit':    ['<literal>', 2],
        'char_lit':     ['<literal>', 3],
        'string_lit':   ['<literal>', 4]
    },

    ############### Productions for ASSIGNMENT - FUNC CALL (353-362) ###############
    '<giveback>':{
        'giveback':['<giveback>', 0]
    },

    '<ret_val>':{
        'void':         ['<ret_val>', 0],
        'null':         ['<ret_val>', 1],
        'int_lit':      ['<ret_val>', 1],
        '(':            ['<ret_val>', 1],
        'id':           ['<ret_val>', 1],
        '++':           ['<ret_val>', 1],
        '--':           ['<ret_val>', 1],
        'float_lit':    ['<ret_val>', 1],
        'char_lit':     ['<ret_val>', 1],
        'string_lit':   ['<ret_val>', 1],
        'true':         ['<ret_val>', 1],
        'false':        ['<ret_val>', 1],
        'NOT':          ['<ret_val>', 1]
    },

    '<IO>':{
        'say':      ['<IO>', 0],
        'listen':   ['<IO>', 1]
    },

    '<func_call>':{
        'id':['<func_call>', 0]
    },

    '<args>':{  ########################### SHOULD ADD HAVING ARRAY LITERALS
        'null':         ['<args>', 0],
        'int_lit':      ['<args>', 0],
        '(':            ['<args>', 0],
        'id':           ['<args>', 0],
        '++':           ['<args>', 0],
        '--':           ['<args>', 0],
        'float_lit':    ['<args>', 0],
        'char_lit':     ['<args>', 0],
        'string_lit':   ['<args>', 0],
        'true':         ['<args>', 0],
        'false':        ['<args>', 0],
        'NOT':          ['<args>', 0],
        ')':            ['<args>', 1]
    },

    '<val_tail>':{
        ',':['<val_tail>', 0],
        ')':['<val_tail>', 1]
    },

    ############### Productions for CONDITIONAL (363 - 378) ###############
    '<conditional>':{
        'when':     ['<conditional>', 0],
        'choose':   ['<conditional>', 1]
    },

    '<ctrl_block>':{
        'float_lit':    ['<ctrl_block>', 0],
        '++':           ['<ctrl_block>', 0],
        '--':           ['<ctrl_block>', 0],
        'int_lit':      ['<ctrl_block>', 0],
        'true':         ['<ctrl_block>', 0],
        'false':        ['<ctrl_block>', 0],
        '(':            ['<ctrl_block>', 0],
        'id':           ['<ctrl_block>', 0],
        'null':         ['<ctrl_block>', 0],
        'string_lit':   ['<ctrl_block>', 0],
        'char_lit':     ['<ctrl_block>', 0],
        'NOT':          ['<ctrl_block>', 0],
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

    '<ctrl_block_tail>':{
        'float_lit':    ['<ctrl_block_tail>', 0],
        '++':           ['<ctrl_block_tail>', 0],
        '--':           ['<ctrl_block_tail>', 0],
        'int_lit':      ['<ctrl_block_tail>', 0],
        'true':         ['<ctrl_block_tail>', 0],
        'false':        ['<ctrl_block_tail>', 0],
        '(':            ['<ctrl_block_tail>', 0],
        'id':           ['<ctrl_block_tail>', 0],
        'null':         ['<ctrl_block_tail>', 0],
        'string_lit':   ['<ctrl_block_tail>', 0],
        'char_lit':     ['<ctrl_block_tail>', 0],
        'NOT':          ['<ctrl_block_tail>', 0],
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

    '<ctrl_item>':{
        'float_lit':    ['<ctrl_item>', 0],
        '++':           ['<ctrl_item>', 0],
        '--':           ['<ctrl_item>', 0],
        'int_lit':      ['<ctrl_item>', 0],
        'true':         ['<ctrl_item>', 0],
        'false':        ['<ctrl_item>', 0],
        '(':            ['<ctrl_item>', 0],
        'id':           ['<ctrl_item>', 0],
        'null':         ['<ctrl_item>', 0],
        'string_lit':   ['<ctrl_item>', 0],
        'char_lit':     ['<ctrl_item>', 0],
        'NOT':          ['<ctrl_item>', 0],
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

    '<ctrl_stmnt>':{
        'break':    ['<ctrl_stmnt>', 0],
        'skip':     ['<ctrl_stmnt>', 1],
        'continue': ['<ctrl_stmnt>', 2]
    },
    
    '<else_tail>':{ 
        'elsewhen':     ['<else_tail>', 0],
        'otherwise':    ['<else_tail>', 1],
        'float_lit':    ['<else_tail>', 1],
        '++':           ['<else_tail>', 1],
        '--':           ['<else_tail>', 1],
        'int_lit':      ['<else_tail>', 1],
        'true':         ['<else_tail>', 1],
        'false':        ['<else_tail>', 1],
        '(':            ['<else_tail>', 1],
        'id':           ['<else_tail>', 1],
        'null':         ['<else_tail>', 1],
        'string_lit':   ['<else_tail>', 1],
        'char_lit':     ['<else_tail>', 1],
        'NOT':          ['<else_tail>', 1],
        'giveback':     ['<else_tail>', 1],
        'say':          ['<else_tail>', 1],
        'listen':       ['<else_tail>', 1],
        'when':         ['<else_tail>', 1],
        'choose':       ['<else_tail>', 1],
        'for':          ['<else_tail>', 1],
        'while':        ['<else_tail>', 1],
        'const':        ['<else_tail>', 1],
        'int':          ['<else_tail>', 1],
        'float':        ['<else_tail>', 1],
        'char':         ['<else_tail>', 1],
        'string':       ['<else_tail>', 1],
        'bool':         ['<else_tail>', 1],
        'break':        ['<else_tail>', 1],
        'skip':         ['<else_tail>', 1],
        'continue':     ['<else_tail>', 1],
        '}':            ['<else_tail>', 1],
        'case':         ['<else_tail>', 1],
        'default':      ['<else_tail>', 1]
    },

    '<otherwise>':{
        'otherwise':    ['<otherwise>', 0],
        'float_lit':    ['<otherwise>', 1],
        '++':           ['<otherwise>', 1],
        '--':           ['<otherwise>', 1],
        'int_lit':      ['<otherwise>', 1],
        'true':         ['<otherwise>', 1],
        'false':        ['<otherwise>', 1],
        '(':            ['<otherwise>', 1],
        'id':           ['<otherwise>', 1],
        'null':         ['<otherwise>', 1],
        'string_lit':   ['<otherwise>', 1],
        'char_lit':     ['<otherwise>', 1],
        'NOT':          ['<otherwise>', 1],
        'giveback':     ['<otherwise>', 1],
        'say':          ['<otherwise>', 1],
        'listen':       ['<otherwise>', 1],
        'when':         ['<otherwise>', 1],
        'choose':       ['<otherwise>', 1],
        'for':          ['<otherwise>', 1],
        'while':        ['<otherwise>', 1],
        'const':        ['<otherwise>', 1],
        'int':          ['<otherwise>', 1],
        'float':        ['<otherwise>', 1],
        'char':         ['<otherwise>', 1],
        'string':       ['<otherwise>', 1],
        'bool':         ['<otherwise>', 1],
        'break':        ['<otherwise>', 1],
        'skip':         ['<otherwise>', 1],
        'continue':     ['<otherwise>', 1],
        '}':            ['<otherwise>', 1],
        'case':         ['<otherwise>', 1],
        'default':      ['<otherwise>', 1]
    },

    '<case_tail>':{
        'case':     ['<case_tail>', 0],
        'default':  ['<case_tail>', 1]
    },

    ############### Productions for ITERATIVE (379 - 386) ###############
    '<iterative>':{
        'for':      ['<iterative>', 0],
        'while':    ['<iterative>', 1]
    },

    '<ctrl_var>':{
        'const':    ['<ctrl_var>', 0],
        'int':      ['<ctrl_var>', 0],
        'float':    ['<ctrl_var>', 0],
        'char':     ['<ctrl_var>', 0],
        'string':   ['<ctrl_var>', 0],
        'bool':     ['<ctrl_var>', 0],
        ';':        ['<ctrl_var>', 1]
    },

    '<for_bool>':{
        'float_lit':    ['<for_bool>', 0],
        '++':           ['<for_bool>', 0],
        '--':           ['<for_bool>', 0],
        'int_lit':      ['<for_bool>', 0],
        'true':         ['<for_bool>', 0],
        'false':        ['<for_bool>', 0],
        '(':            ['<for_bool>', 0],
        'id':           ['<for_bool>', 0],
        'null':         ['<for_bool>', 0],
        'string_lit':   ['<for_bool>', 0],
        'char_lit':     ['<for_bool>', 0],
        'NOT':          ['<for_bool>', 0],
        ';':            ['<for_bool>', 1]
    },

    '<for_unary>':{
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
            print(stack)            ##### used to track which path the syntax goes
            top = stack[-1]
            if self.curr_token is None or self.curr_token.type == 'EOF':             # If there are no more tokens or reached the EOF
                self.curr_token = type('Token', (object,), {                         # Create a token indicating the EOF
                    'type': 'EOF',
                    'pos_start': self.tokens[-1].pos_end if self.tokens else None,
                    'pos_end': self.tokens[-1].pos_end if self.tokens else None
                })()

            if is_nonterminal(top): 
                print(top)
                if top in PREDICT_SET and self.curr_token.type in PREDICT_SET[top]:
                    prod_key = PREDICT_SET[top][self.curr_token.type]
                    prod = CFG[prod_key[0]][prod_key[1]]
                    stack.pop()
                    prev_popped_nonterminal = top
                    stack.extend(reversed(prod))
                else:
                    expected_tokens = list(PREDICT_SET[top].keys())
                    error = InvalidSyntaxError(self.curr_token.pos_start, self.curr_token.pos_end, f'Unexpected token -> {self.curr_token.type} <- after "{self.prev_token.type}"\nExpected tokens: {expected_tokens}')
                    break
            else:               # If terminal, check if the top of the stack is the same as the non terminal
                stack.pop()
                if top == self.curr_token.type:
                    self.advance()
                    prev_popped_nonterminal = None
                else:                                                               
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
# Initializes an empty set
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
    return "✅ Success from Syntax Analyzer", None