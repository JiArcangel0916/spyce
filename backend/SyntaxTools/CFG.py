# string (production): list ng list ng string (production set)
CFG = {
    '<program>':[
        ['<global_var>', '<sub_func>', 'spyce', '(', ')', '->', 'void', '{', '<main_func_body>', 'giveback', '<void>', ';', '}']
    ],

    '<global_var>':[
        ['const', '<data_type>', '<var_type>', ';', '<global_var>'], 
        ['<data_type>', '<var_type>', ';', '<global_var>'],           
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
        ['id', '=', '<expr>', '<scaldec_tail>'],
        ['[', '<arr_size>', ']', '<arrtype>']
    ],

    '<arrtype>':[    
        ['id', '=', '<1d_val>', '<1d_dec_tail>'],
        ['[', '<arr_size>', ']', 'id', '=', '<2d_val>', '<2d_dec_tail>']
    ],

    '<scaldec_tail>':[    
        [',', 'id', '=', '<expr>', '<scaldec_tail>'],
        []
    ],

    '<arr_size>':[
        ['<num_lit>'],
        ['<bool_lit>']
    ],

    '<num_lit>':[
        ['int_lit'],
        ['float_lit']
    ],

    '<bool_lit>':[    
        ['true'],
        ['false'],
    ],

    '<1d_val>':[    
        ['id', '<inner_arr_indx>'],
        ['{', '<element_list>', '}']
    ],

    '<inner_arr_indx>':[    
        ['[', '<arith_expr>', ']'],
        ['(', '<args>', ')'],
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
        ['[', '<arr_size>', ']', '<2d_indx>'],
        []
    ],

    '<2d_indx>':[    
        ['[', '<arr_size>', ']'],
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
        ['<main_stmnt>', '<main_func_body>'],
        []
    ],

    '<void>':[    
        ['void'],
        []
    ],

    '<main_stmnt>':[    
        ['<local_var>', ';'],
        ['id', '<id_tail>', ';'],
        ['<unary_op>', '<id_val>', ';'],
        ['<IO>', ';'],
        ['<conditional>'],
        ['<iterative>']
    ],

    '<stmnt>':[    
        ['<main_stmnt>'],
        ['<giveback>', ';'],
    ],

    '<id_tail>':[    
        ['<id_accessor>'],
        ['<id_accessor_tail>']
    ],

    '<id_accessor>':[    
        ['[', '<arith_expr>', ']', '<more_indx>', '<id_accessor_tail>'],
        ['(', '<args>', ')']
    ],

    '<more_indx>':[    
        ['[', '<arith_expr>', ']'],
        []
    ],

    '<id_accessor_tail>':[    
        ['<unary_op>'],
        ['<assign_type>']
    ],

    '<assign_type>':[    
        ['=', '<expr>'],
        ['<cmpnd_op>', '<cmpnd_operand>']
    ],

    '<unary_op>':[    
        ['++'],
        ['--']
    ],

    '<local_var>':[    
        ['const', '<data_type>', '<var_type>'],
        ['<data_type>', '<var_type>']
    ],

    '<args>':[    
        ['<expr>', '<val_tail>'],
        ['{', '<arr_lit>', '}'],
        []
    ],

    '<arr_lit>':[
        ['<element_list>'],
        ['<1d_val>', '<2dval_tail>'],
        []
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
        ['<bool_lit>'],
        ['<id_val>']
    ],

    '<numstring_val>':[    
        ['<num_lit>'],
        ['string_lit'],
    ],

    '<id_val>':[    
        ['id', '<indx_access>']
    ],

    '<indx_access>':[
        ['[', '<arith_expr>', ']', '<indx_access_tail>'],
        []
    ],

    '<indx_access_tail>':[
        ['[', '<arith_expr>', ']'],
        []
    ],

    '<expr>':[    
        ['<logical_or_expr>']
    ],

    '<logical_or_expr>':[    
        ['<and_expr>', '<chain_or>']
    ],

    '<chain_or>':[    
        ['OR', '<and_expr>', '<chain_or>'],
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
        ['<relational_expr>', '<equal_expr_tail>']    
    ],

    '<equal_expr_tail>':[    
        ['==', '<relational_expr>'],
        ['!=', '<relational_expr>'],
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
        ['**', '<expo_arith_operand>', '<expo_arith_operand_tail>'],
        []
    ],

    '<operand>':[    
        ['<num_lit>'],
        ['<bool_lit>'],
        ['str', '(', '<expr>', ')'],
        ['(', '<expr>', ')'],
        ['listen', '(', ')'],
        ['string_lit'],
        ['char_lit'],
        ['<unary_op>', 'id', '<id_access_operand>'],
        ['id', '<id_operand_tail>']
    ],

    '<id_access_operand>':[    
        ['[','<arith_expr>', ']', '<more_indx>'],
        []
    ],

    '<id_operand_unary>':[    
        ['<unary_op>'],
        []
    ],

    '<id_operand_tail>':[    
        ['(', '<args>', ')'],
        ['[', '<arith_expr>', ']', '<more_indx>', '<id_operand_unary>'],
        ['<unary_op>'],
        []
    ],

    '<IO>':[    
        ['say', '(', '<expr>', ')'],
        ['listen', '(', ')']
    ],

    '<giveback>':[    
        ['giveback', '<ret_val>']
    ],

    '<ret_val>':[    
        ['<void>'],
        ['<expr>'],
    ],

    '<conditional>':[    
        ['when', '(', '<expr>', ')', '{', '<ctrl_block>', '}', '<else_tail>', '<otherwise>'],
        ['choose', '(', 'id', '<choose_indx>', ')', '{', '<case_tail>', 'default', ':', '<ctrl_block>', '}']
    ],

    '<choose_indx>':[
        ['[', '<arith_expr>', ']', '<choose_2d>'],
        []
    ],

    '<choose_2d>':[
        ['[', '<arith_expr>', ']'],
        []
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
        ['id', '<indx_access>', '<opt_expr>', ';'],
        [';'] 
    ],

    '<opt_expr>':[
        ['=', '<expr>'],
        []
    ],

    '<for_bool>':[    
        ['<expr>', ';'],
        [';']
    ],

    '<for_unary>':[    
        ['<unary>'],
        []
    ],

    '<unary>':[    
        ['<id_val>', '<unary_op>'],
        ['<unary_op>', '<id_val>']
    ]
}