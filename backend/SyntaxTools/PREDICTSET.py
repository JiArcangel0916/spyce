# string (production) : object (string:list(production, pangilang production))
PREDICT_SET = {
    '<program>':{    
        'const':    ['<program>', 0],       
        'int':      ['<program>', 0],
        'float':    ['<program>', 0],
        'char':     ['<program>', 0],
        'string':   ['<program>', 0],
        'bool':     ['<program>', 0],
        'make':     ['<program>', 0],
        'spyce':    ['<program>', 0]
    },

    '<global_var>':{    
        'const':    ['<global_var>', 0],    
        'int':      ['<global_var>', 1],    
        'float':    ['<global_var>', 1],
        'char':     ['<global_var>', 1],
        'string':   ['<global_var>', 1],
        'bool':     ['<global_var>', 1],
        'make':     ['<global_var>', 2],     
        'spyce':    ['<global_var>', 2]
    },

    '<data_type>':{    
        'int':      ['<data_type>', 0],
        'float':    ['<data_type>', 1],
        'char':     ['<data_type>', 2],
        'string':   ['<data_type>', 3],
        'bool':     ['<data_type>', 4]
    },

    '<var_type>':{    
        'id':      ['<var_type>', 0],      
        '[':    ['<var_type>', 1]             
    },

    '<arrtype>':{    
        'id':   ['<arrtype>', 0],
        '[':    ['<arrtype>', 1]
    },

    '<scaldec_tail>':{    
        ',':['<scaldec_tail>', 0],
        ';':['<scaldec_tail>', 1]
    },

    '<arr_size>':{
        'int_lit':  ['<arr_size>', 0],
        'float_lit':['<arr_size>', 0],
        'true':     ['<arr_size>', 1],
        'false':    ['<arr_size>', 1],
    },

    '<num_lit>':{
        'int_lit':    ['<num_lit>', 0],
        'float_lit':  ['<num_lit>', 1],
    },

    '<bool_lit>':{
        'true':    ['<bool_lit>', 0],
        'false':   ['<bool_lit>', 1],
    },

    '<1d_val>':{       
      'id':['<1d_val>', 0],
      '{': ['<1d_val>', 1]  
    },

    '<inner_arr_indx>':{    
        '[':['<inner_arr_indx>', 0],
        '(':['<inner_arr_indx>', 1],
        ',':['<inner_arr_indx>', 2],
        ';':['<inner_arr_indx>', 2],
        '}':['<inner_arr_indx>', 2]
    },

    '<element_list>':{    
        'NOT':          ['<element_list>', 0],
        'int_lit':      ['<element_list>', 0],
        'float_lit':    ['<element_list>', 0],
        'str':          ['<element_list>', 0],
        '(':            ['<element_list>', 0],
        '++':           ['<element_list>', 0],
        '--':           ['<element_list>', 0],
        'id':           ['<element_list>', 0],        
        'true':         ['<element_list>', 0],
        'false':        ['<element_list>', 0],
        'char_lit':     ['<element_list>', 0],
        'string_lit':   ['<element_list>', 0],
        'listen':       ['<element_list>', 0],
        '}':            ['<element_list>', 1]
    },

    '<val_tail>':{    
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

    '<2dval_tail>':{    
        ',':   ['<2dval_tail>', 0],
        '}':   ['<2dval_tail>', 1]
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
    },

    '<2d_indx>':{      
        '[':    ['<2d_indx>', 0],
        'id':   ['<2d_indx>', 1],
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
        'void': ['<void>', 0],
        ';':    ['<void>', 1] 
    },

    '<main_stmnt>':{       
        'const':        ['<main_stmnt>', 0],
        'int':          ['<main_stmnt>', 0],
        'float':        ['<main_stmnt>', 0],
        'char':         ['<main_stmnt>', 0],
        'string':       ['<main_stmnt>', 0],
        'bool':         ['<main_stmnt>', 0],
        'id':           ['<main_stmnt>', 1],     
        '++':           ['<main_stmnt>', 2],
        '--':           ['<main_stmnt>', 2],      
        'say':          ['<main_stmnt>', 3],
        'listen':       ['<main_stmnt>', 3],     
        'when':         ['<main_stmnt>', 4],
        'choose':       ['<main_stmnt>', 4],
        'for':          ['<main_stmnt>', 5],
        'while':        ['<main_stmnt>', 5]
    },

    '<stmnt>':{       
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

    '<id_tail>':{       
        '[':    ['<id_tail>', 0],
        '(':    ['<id_tail>', 0],
        '++':   ['<id_tail>', 1],
        '--':   ['<id_tail>', 1],
        '+=':   ['<id_tail>', 1],
        '-=':   ['<id_tail>', 1],
        '*=':   ['<id_tail>', 1],
        '/=':   ['<id_tail>', 1],
        '**=':  ['<id_tail>', 1],
        '%=':   ['<id_tail>', 1],
        '=':    ['<id_tail>', 1]
    },

    '<id_accessor>':{      
        '[':            ['<id_accessor>', 0],
        '(':            ['<id_accessor>', 1],
    },

    '<more_indx>':{     
        '[':        ['<more_indx>', 0],
        '++':       ['<more_indx>', 1],
        '--':       ['<more_indx>', 1],
        '+=':       ['<more_indx>', 1],
        '-=':       ['<more_indx>', 1],
        '*=':       ['<more_indx>', 1],
        '/=':       ['<more_indx>', 1],
        '**=':      ['<more_indx>', 1],
        '%=':       ['<more_indx>', 1],
        '=':        ['<more_indx>', 1],
        '**':       ['<more_indx>', 1],
        '*':        ['<more_indx>', 1],
        '/':        ['<more_indx>', 1],
        '%':        ['<more_indx>', 1],
        '+':        ['<more_indx>', 1],
        '-':        ['<more_indx>', 1],
        ']':        ['<more_indx>', 1],
        '>':        ['<more_indx>', 1],
        '<':        ['<more_indx>', 1],
        '>=':       ['<more_indx>', 1],
        '<=':       ['<more_indx>', 1],
        '==':       ['<more_indx>', 1],
        '!=':       ['<more_indx>', 1],
        'AND':      ['<more_indx>', 1],
        'OR':       ['<more_indx>', 1],
        ',':        ['<more_indx>', 1],
        ';':        ['<more_indx>', 1],
        '}':        ['<more_indx>', 1],
        ')':        ['<more_indx>', 1],
    },

    '<id_accessor_tail>':{     
        '++':   ['<id_accessor_tail>', 0],
        '--':   ['<id_accessor_tail>', 0],
        '=':    ['<id_accessor_tail>', 1],
        '+=':   ['<id_accessor_tail>', 1],
        '-=':   ['<id_accessor_tail>', 1],
        '*=':   ['<id_accessor_tail>', 1],
        '/=':   ['<id_accessor_tail>', 1],
        '**=':  ['<id_accessor_tail>', 1],
        '%=':   ['<id_accessor_tail>', 1]    
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

    '<unary_op>':{     
        '++':['<unary_op>', 0],
        '--':['<unary_op>', 1]
    },

    '<local_var>':{    
        'const':    ['<local_var>', 0],
        'int':      ['<local_var>', 1],
        'float':    ['<local_var>', 1],
        'char':     ['<local_var>', 1],
        'string':   ['<local_var>', 1],
        'bool':     ['<local_var>', 1]
    },

    '<args>':{    
        'NOT':          ['<args>', 0],
        'int_lit':      ['<args>', 0],
        'float_lit':    ['<args>', 0],
        'str':          ['<args>', 0],
        '(':            ['<args>', 0],
        '++':           ['<args>', 0],
        '--':           ['<args>', 0],
        'id':           ['<args>', 0],
        'true':         ['<args>', 0],
        'false':        ['<args>', 0],
        'char_lit':     ['<args>', 0],
        'string_lit':   ['<args>', 0],
        'listen':       ['<args>', 0],
        '{':            ['<args>', 1],
        ')':            ['<args>', 2]
    },

    '<arr_lit>': {
        'NOT':          ['<arr_lit>', 0],
        'int_lit':      ['<arr_lit>', 0],
        'float_lit':    ['<arr_lit>', 0],
        'str':          ['<arr_lit>', 0],
        '(':            ['<arr_lit>', 0],
        '++':           ['<arr_lit>', 0],
        '--':           ['<arr_lit>', 0],
        'id':           ['<arr_lit>', 0],
        'true':         ['<arr_lit>', 0],
        'false':        ['<arr_lit>', 0],
        'char_lit':     ['<arr_lit>', 0],
        'string_lit':   ['<arr_lit>', 0],
        'listen':       ['<arr_lit>', 0],
        '{':            ['<arr_lit>', 1],
        ')':            ['<arr_lit>', 2]
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
        'float_lit':    ['<cmpnd_operand>', 0],
        'string_lit':   ['<cmpnd_operand>', 0],
        'true':         ['<cmpnd_operand>', 1],
        'false':        ['<cmpnd_operand>', 1],
        'id':           ['<cmpnd_operand>', 2]
    },

    '<numstring_val>':{    
        'int_lit':     ['<numstring_val>', 0],
        'float_lit':   ['<numstring_val>', 0],
        'string_lit':  ['<numstring_val>', 1]
    },

    '<id_val>':{    
        'id':     ['<id_val>', 0]
    },

    '<indx_access>':{
        '[':    ['<indx_access>', 0],
        ';':    ['<indx_access>', 1],
        ')':    ['<indx_access>', 1],
        '=':    ['<indx_access>', 1],
        '++':   ['<indx_access>', 1],
        '--':   ['<indx_access>', 1]
    },

    '<indx_access_tail>':{
        '[':    ['<indx_access_tail>', 0],
        ';':    ['<indx_access_tail>', 1],
        ')':    ['<indx_access_tail>', 1],
        '=':    ['<indx_access_tail>', 1],
        '++':   ['<indx_access_tail>', 1],
        '--':   ['<indx_access_tail>', 1]
    },

    '<expr>':{    
        'NOT':          ['<expr>', 0],
        'int_lit':      ['<expr>', 0],
        'float_lit':    ['<expr>', 0],
        'true':         ['<expr>', 0],
        'false':        ['<expr>', 0],
        'string_lit':   ['<expr>', 0],
        'char_lit':     ['<expr>', 0],
        'str':          ['<expr>', 0],
        '(':            ['<expr>', 0],
        '++':           ['<expr>', 0],
        '--':           ['<expr>', 0],
        'id':           ['<expr>', 0],
        'listen':       ['<expr>', 0]
    },

    '<logical_or_expr>':{    
        'NOT':          ['<logical_or_expr>', 0],
        'int_lit':      ['<logical_or_expr>', 0],
        'float_lit':    ['<logical_or_expr>', 0],
        'true':         ['<logical_or_expr>', 0],
        'false':        ['<logical_or_expr>', 0],
        'string_lit':   ['<logical_or_expr>', 0],
        'char_lit':     ['<logical_or_expr>', 0],
        'str':          ['<logical_or_expr>', 0],
        '(':            ['<logical_or_expr>', 0],
        '++':           ['<logical_or_expr>', 0],
        '--':           ['<logical_or_expr>', 0],
        'id':           ['<logical_or_expr>', 0],
        'listen':       ['<logical_or_expr>', 0]
    },

    '<chain_or>':{    
        'OR':  ['<chain_or>', 0],
        ',':   ['<chain_or>', 1],
        ';':   ['<chain_or>', 1],
        '}':   ['<chain_or>', 1],
        ')':   ['<chain_or>', 1]
    },

    '<and_expr>':{    
        'NOT':          ['<and_expr>', 0],
        'int_lit':      ['<and_expr>', 0],
        'float_lit':    ['<and_expr>', 0],
        'true':         ['<and_expr>', 0],
        'false':        ['<and_expr>', 0],
        'string_lit':   ['<and_expr>', 0],
        'char_lit':     ['<and_expr>', 0],
        'str':          ['<and_expr>', 0],
        '(':            ['<and_expr>', 0],
        '++':           ['<and_expr>', 0],
        '--':           ['<and_expr>', 0],
        'id':           ['<and_expr>', 0],
        'listen':       ['<and_expr>', 0]
    },

    '<chain_and>':{    
        'AND': ['<chain_and>', 0],
        'OR':  ['<chain_and>', 1],
        ',':   ['<chain_and>', 1],
        ';':   ['<chain_and>', 1],
        '}':   ['<chain_and>', 1],
        ')':   ['<chain_and>', 1]
    },

    '<not_expr>':{    
        'NOT':          ['<not_expr>', 0],
        'int_lit':      ['<not_expr>', 1],
        'float_lit':    ['<not_expr>', 1],
        'true':         ['<not_expr>', 1],
        'false':        ['<not_expr>', 1],
        'string_lit':   ['<not_expr>', 1],
        'char_lit':     ['<not_expr>', 1],
        'str':          ['<not_expr>', 1],
        '(':            ['<not_expr>', 1],
        '++':           ['<not_expr>', 1],
        '--':           ['<not_expr>', 1],
        'id':           ['<not_expr>', 1],
        'listen':       ['<not_expr>', 1]
    },

    '<equal_expr>':{    
        'int_lit':      ['<equal_expr>', 0],
        'float_lit':    ['<equal_expr>', 0],
        'true':         ['<equal_expr>', 0],
        'false':        ['<equal_expr>', 0],
        'string_lit':   ['<equal_expr>', 0],
        'char_lit':     ['<equal_expr>', 0],
        'str':          ['<equal_expr>', 0],
        '(':            ['<equal_expr>', 0],
        '++':           ['<equal_expr>', 0],
        '--':           ['<equal_expr>', 0],
        'id':           ['<equal_expr>', 0],
        'listen':       ['<equal_expr>', 0]
    },

    '<equal_expr_tail>':{    
        '==':   ['<equal_expr_tail>', 0],
        '!=':   ['<equal_expr_tail>', 1],
        'AND':  ['<equal_expr_tail>', 2],
        'OR':   ['<equal_expr_tail>', 2],
        ',':    ['<equal_expr_tail>', 2],
        ';':    ['<equal_expr_tail>', 2],
        '}':    ['<equal_expr_tail>', 2],
        ')':    ['<equal_expr_tail>', 2]
    },

    '<relational_expr>':{    
        'int_lit':      ['<relational_expr>', 0],
        'float_lit':    ['<relational_expr>', 0],
        'true':         ['<relational_expr>', 0],
        'false':        ['<relational_expr>', 0],
        'string_lit':   ['<relational_expr>', 0],
        'char_lit':     ['<relational_expr>', 0],
        'str':          ['<relational_expr>', 0],
        '(':            ['<relational_expr>', 0],
        '++':           ['<relational_expr>', 0],
        '--':           ['<relational_expr>', 0],
        'id':           ['<relational_expr>', 0],
        'listen':       ['<relational_expr>', 0]
    },

    '<relational_expr_tail>':{    
        '>':    ['<relational_expr_tail>', 0],
        '<':    ['<relational_expr_tail>', 0],
        '>=':   ['<relational_expr_tail>', 0],
        '<=':   ['<relational_expr_tail>', 0],
        '==':   ['<relational_expr_tail>', 1],
        '!=':   ['<relational_expr_tail>', 1],
        'AND':  ['<relational_expr_tail>', 1],
        'OR':   ['<relational_expr_tail>', 1],
        ',':    ['<relational_expr_tail>', 1],
        ';':    ['<relational_expr_tail>', 1],
        '}':    ['<relational_expr_tail>', 1],
        ')':    ['<relational_expr_tail>', 1]
    },

    '<relation_op>':{    
        '>':    ['<relation_op>', 0],
        '<':    ['<relation_op>', 1],
        '>=':   ['<relation_op>', 2],
        '<=':   ['<relation_op>', 3]
    }, 

    '<arith_expr>':{    
        'int_lit':      ['<arith_expr>', 0],
        'float_lit':    ['<arith_expr>', 0],
        'true':         ['<arith_expr>', 0],
        'false':        ['<arith_expr>', 0],
        'string_lit':   ['<arith_expr>', 0],
        'char_lit':     ['<arith_expr>', 0],
        'str':          ['<arith_expr>', 0],
        '(':            ['<arith_expr>', 0],
        '++':           ['<arith_expr>', 0],
        '--':           ['<arith_expr>', 0],
        'id':           ['<arith_expr>', 0],
        'listen':       ['<arith_expr>', 0]          
    },

    '<arith_expr_tail>':{    
        '+':    ['<arith_expr_tail>', 0],
        '-':    ['<arith_expr_tail>', 1],
        ']':    ['<arith_expr_tail>', 2],
        '>':    ['<arith_expr_tail>', 2],
        '<':    ['<arith_expr_tail>', 2],
        '>=':   ['<arith_expr_tail>', 2],
        '<=':   ['<arith_expr_tail>', 2],
        '==':   ['<arith_expr_tail>', 2],
        '!=':   ['<arith_expr_tail>', 2],
        'AND':  ['<arith_expr_tail>', 2],
        'OR':   ['<arith_expr_tail>', 2],
        ',':    ['<arith_expr_tail>', 2],
        ';':    ['<arith_expr_tail>', 2],
        '}':    ['<arith_expr_tail>', 2],
        ')':    ['<arith_expr_tail>', 2]
    },

    '<arith_operand>':{    
        'int_lit':      ['<arith_operand>', 0],
        'float_lit':    ['<arith_operand>', 0],
        'true':         ['<arith_operand>', 0],
        'false':        ['<arith_operand>', 0],
        'string_lit':   ['<arith_operand>', 0],
        'char_lit':     ['<arith_operand>', 0],
        'str':          ['<arith_operand>', 0],
        '(':            ['<arith_operand>', 0],
        '++':           ['<arith_operand>', 0],
        '--':           ['<arith_operand>', 0],
        'id':           ['<arith_operand>', 0],
        'listen':       ['<arith_operand>', 0]           
    },      

    '<arith_operand_tail>':{    
        '*':    ['<arith_operand_tail>', 0],
        '/':    ['<arith_operand_tail>', 1],
        '%':    ['<arith_operand_tail>', 2],
        '+':    ['<arith_operand_tail>', 3],
        '-':    ['<arith_operand_tail>', 3],
        ']':    ['<arith_operand_tail>', 3],
        '>':    ['<arith_operand_tail>', 3],
        '<':    ['<arith_operand_tail>', 3],
        '>=':   ['<arith_operand_tail>', 3],
        '<=':   ['<arith_operand_tail>', 3],
        '==':   ['<arith_operand_tail>', 3],
        '!=':   ['<arith_operand_tail>', 3],
        'AND':  ['<arith_operand_tail>', 3],
        'OR':   ['<arith_operand_tail>', 3],
        ',':    ['<arith_operand_tail>', 3],
        ';':    ['<arith_operand_tail>', 3],
        '}':    ['<arith_operand_tail>', 3],
        ')':    ['<arith_operand_tail>', 3]
    },

    '<expo_arith_operand>':{    
        'int_lit':      ['<expo_arith_operand>', 0],
        'float_lit':    ['<expo_arith_operand>', 0],
        'true':         ['<expo_arith_operand>', 0],
        'false':        ['<expo_arith_operand>', 0],
        'string_lit':   ['<expo_arith_operand>', 0],
        'char_lit':     ['<expo_arith_operand>', 0],
        'str':          ['<expo_arith_operand>', 0],
        '(':            ['<expo_arith_operand>', 0],
        '++':           ['<expo_arith_operand>', 0],
        '--':           ['<expo_arith_operand>', 0],
        'id':           ['<expo_arith_operand>', 0],
        'listen':       ['<expo_arith_operand>', 0]
    },
    
    '<expo_arith_operand_tail>':{    
        '**':   ['<expo_arith_operand_tail>', 0],
        '*':    ['<expo_arith_operand_tail>', 1],
        '/':    ['<expo_arith_operand_tail>', 1],
        '%':    ['<expo_arith_operand_tail>', 1],
        '+':    ['<expo_arith_operand_tail>', 1],
        '-':    ['<expo_arith_operand_tail>', 1],
        ']':    ['<expo_arith_operand_tail>', 1],
        '>':    ['<expo_arith_operand_tail>', 1],
        '<':    ['<expo_arith_operand_tail>', 1],
        '>=':   ['<expo_arith_operand_tail>', 1],
        '<=':   ['<expo_arith_operand_tail>', 1],
        '==':   ['<expo_arith_operand_tail>', 1],
        '!=':   ['<expo_arith_operand_tail>', 1],
        'AND':  ['<expo_arith_operand_tail>', 1],
        'OR':   ['<expo_arith_operand_tail>', 1],
        ',':    ['<expo_arith_operand_tail>', 1],
        ';':    ['<expo_arith_operand_tail>', 1],
        '}':    ['<expo_arith_operand_tail>', 1],
        ')':    ['<expo_arith_operand_tail>', 1]
    },

    '<operand>':{    
        'int_lit':      ['<operand>', 0],
        'float_lit':    ['<operand>', 0],
        'true':         ['<operand>', 1],
        'false':        ['<operand>', 1],
        'str':          ['<operand>', 2],
        '(':            ['<operand>', 3],
        'listen':       ['<operand>', 4],
        'string_lit':   ['<operand>', 5],
        'char_lit':     ['<operand>', 6],
        '++':           ['<operand>', 7],
        '--':           ['<operand>', 7],
        'id':           ['<operand>', 8],
    },

    '<id_access_operand>':{    
        '[':    ['<id_access_operand>', 0],
        '**':   ['<id_access_operand>', 1],
        '*':    ['<id_access_operand>', 1],
        '/':    ['<id_access_operand>', 1],
        '%':    ['<id_access_operand>', 1],
        '+':    ['<id_access_operand>', 1],
        '-':    ['<id_access_operand>', 1],
        ']':    ['<id_access_operand>', 1],
        '>':    ['<id_access_operand>', 1],
        '<':    ['<id_access_operand>', 1],
        '>=':   ['<id_access_operand>', 1],
        '<=':   ['<id_access_operand>', 1],
        '==':   ['<id_access_operand>', 1],
        '!=':   ['<id_access_operand>', 1],
        'AND':  ['<id_access_operand>', 1],
        'OR':   ['<id_access_operand>', 1],
        ',':    ['<id_access_operand>', 1],
        ';':    ['<id_access_operand>', 1],
        '}':    ['<id_access_operand>', 1],
        ')':    ['<id_access_operand>', 1]
    },

    '<id_operand_unary>':{    
        '++':   ['<id_operand_unary>', 0],
        '--':   ['<id_operand_unary>', 0],
        '**':   ['<id_operand_unary>', 1],
        '*':    ['<id_operand_unary>', 1],
        '/':    ['<id_operand_unary>', 1],
        '%':    ['<id_operand_unary>', 1],
        '+':    ['<id_operand_unary>', 1],
        '-':    ['<id_operand_unary>', 1],
        ']':    ['<id_operand_unary>', 1],
        '>':    ['<id_operand_unary>', 1],
        '<':    ['<id_operand_unary>', 1],
        '>=':   ['<id_operand_unary>', 1],
        '<=':   ['<id_operand_unary>', 1],
        '==':   ['<id_operand_unary>', 1],
        '!=':   ['<id_operand_unary>', 1],
        'AND':  ['<id_operand_unary>', 1],
        'OR':   ['<id_operand_unary>', 1],
        ',':    ['<id_operand_unary>', 1],
        ';':    ['<id_operand_unary>', 1],
        '}':    ['<id_operand_unary>', 1],
        ')':    ['<id_operand_unary>', 1]
    },

    '<id_operand_tail>':{    
        '(':    ['<id_operand_tail>', 0],
        '[':    ['<id_operand_tail>', 1],
        '++':   ['<id_operand_tail>', 2],
        '--':   ['<id_operand_tail>', 2],
        '**':   ['<id_operand_tail>', 3],
        '*':    ['<id_operand_tail>', 3],
        '/':    ['<id_operand_tail>', 3],
        '%':    ['<id_operand_tail>', 3],
        '+':    ['<id_operand_tail>', 3],
        '-':    ['<id_operand_tail>', 3],
        ']':    ['<id_operand_tail>', 3],
        '>':    ['<id_operand_tail>', 3],
        '<':    ['<id_operand_tail>', 3],
        '>=':   ['<id_operand_tail>', 3],
        '<=':   ['<id_operand_tail>', 3],
        '==':   ['<id_operand_tail>', 3],
        '!=':   ['<id_operand_tail>', 3],
        'AND':  ['<id_operand_tail>', 3],
        'OR':   ['<id_operand_tail>', 3],
        ',':    ['<id_operand_tail>', 3],
        ';':    ['<id_operand_tail>', 3],
        '}':    ['<id_operand_tail>', 3],
        ')':    ['<id_operand_tail>', 3]
    },

    '<IO>':{    
        'say':      ['<IO>', 0],
        'listen':   ['<IO>', 1]
    },

    '<giveback>':{    
        'giveback':['<giveback>', 0]
    },

    '<ret_val>':{       
        'void':         ['<ret_val>', 0],
        ';':            ['<ret_val>', 0],
        'NOT':          ['<ret_val>', 1],
        'int_lit':      ['<ret_val>', 1],
        'float_lit':    ['<ret_val>', 1],
        'str':          ['<ret_val>', 1],
        '(':            ['<ret_val>', 1],
        '++':           ['<ret_val>', 1],
        '--':           ['<ret_val>', 1],
        'id':           ['<ret_val>', 1],
        'true':         ['<ret_val>', 1],
        'false':        ['<ret_val>', 1],
        'char_lit':     ['<ret_val>', 1],
        'string_lit':   ['<ret_val>', 1],
        'listen':       ['<ret_val>', 1]
    },

    '<conditional>':{    
        'when':     ['<conditional>', 0],
        'choose':   ['<conditional>', 1]
    },

    '<choose_indx>':{
        '[':    ['<choose_indx>', 0],
        ')':    ['<choose_indx>', 1]
    },

    '<choose_2d>':{
        '[':    ['<choose_2d>', 0],
        ')':    ['<choose_2d>', 1],
    },

    '<ctrl_block>':{       
        'const':        ['<ctrl_block>', 0],
        'int':          ['<ctrl_block>', 0],
        'float':        ['<ctrl_block>', 0],
        'char':         ['<ctrl_block>', 0],
        'string':       ['<ctrl_block>', 0],
        'bool':         ['<ctrl_block>', 0],
        'id':           ['<ctrl_block>', 0],
        '++':           ['<ctrl_block>', 0],
        '--':           ['<ctrl_block>', 0],
        'say':          ['<ctrl_block>', 0],
        'listen':       ['<ctrl_block>', 0],
        'when':         ['<ctrl_block>', 0],
        'choose':       ['<ctrl_block>', 0],
        'for':          ['<ctrl_block>', 0],
        'while':        ['<ctrl_block>', 0],
        'giveback':     ['<ctrl_block>', 0],
        'break':        ['<ctrl_block>', 0],
        'skip':         ['<ctrl_block>', 0],
        'continue':     ['<ctrl_block>', 0]
    },

    '<ctrl_block_tail>':{       
        'const':        ['<ctrl_block_tail>', 0],
        'int':          ['<ctrl_block_tail>', 0],
        'float':        ['<ctrl_block_tail>', 0],
        'char':         ['<ctrl_block_tail>', 0],
        'string':       ['<ctrl_block_tail>', 0],
        'bool':         ['<ctrl_block_tail>', 0],
        'id':           ['<ctrl_block_tail>', 0],
        '++':           ['<ctrl_block_tail>', 0],
        '--':           ['<ctrl_block_tail>', 0],
        'say':          ['<ctrl_block_tail>', 0],
        'listen':       ['<ctrl_block_tail>', 0],
        'when':         ['<ctrl_block_tail>', 0],
        'choose':       ['<ctrl_block_tail>', 0],
        'for':          ['<ctrl_block_tail>', 0],
        'while':        ['<ctrl_block_tail>', 0],
        'giveback':     ['<ctrl_block_tail>', 0],
        'break':        ['<ctrl_block_tail>', 0],
        'skip':         ['<ctrl_block_tail>', 0],
        'continue':     ['<ctrl_block_tail>', 0],
        '}':            ['<ctrl_block_tail>', 1],
        'case':         ['<ctrl_block_tail>', 1],
        'default':      ['<ctrl_block_tail>', 1],
    },

    '<ctrl_item>':{       
        'const':        ['<ctrl_item>', 0],
        'int':          ['<ctrl_item>', 0],
        'float':        ['<ctrl_item>', 0],
        'char':         ['<ctrl_item>', 0],
        'string':       ['<ctrl_item>', 0],
        'bool':         ['<ctrl_item>', 0],
        'id':           ['<ctrl_item>', 0],
        '++':           ['<ctrl_item>', 0],
        '--':           ['<ctrl_item>', 0],
        'say':          ['<ctrl_item>', 0],
        'listen':       ['<ctrl_item>', 0],
        'when':         ['<ctrl_item>', 0],
        'choose':       ['<ctrl_item>', 0],
        'for':          ['<ctrl_item>', 0],
        'while':        ['<ctrl_item>', 0],
        'giveback':     ['<ctrl_item>', 0],
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
        'const':        ['<else_tail>', 1],
        'int':          ['<else_tail>', 1],
        'float':        ['<else_tail>', 1],
        'char':         ['<else_tail>', 1],
        'string':       ['<else_tail>', 1],
        'bool':         ['<else_tail>', 1],
        'id':           ['<else_tail>', 1],
        '++':           ['<else_tail>', 1],
        '--':           ['<else_tail>', 1],
        'say':          ['<else_tail>', 1],
        'listen':       ['<else_tail>', 1],
        'when':         ['<else_tail>', 1],
        'choose':       ['<else_tail>', 1],
        'for':          ['<else_tail>', 1],
        'while':        ['<else_tail>', 1],
        'giveback':     ['<else_tail>', 1],
        '}':            ['<else_tail>', 1],
        'break':        ['<else_tail>', 1],
        'skip':         ['<else_tail>', 1],
        'continue':     ['<else_tail>', 1],
        'case':         ['<else_tail>', 1],
        'default':      ['<else_tail>', 1]
    },

    '<otherwise>':{       
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
        'say':          ['<otherwise>', 1],
        'listen':       ['<otherwise>', 1],
        'when':         ['<otherwise>', 1],
        'choose':       ['<otherwise>', 1],
        'for':          ['<otherwise>', 1],
        'while':        ['<otherwise>', 1],
        'giveback':     ['<otherwise>', 1],
        '}':            ['<otherwise>', 1],
        'break':        ['<otherwise>', 1],
        'skip':         ['<otherwise>', 1],
        'continue':     ['<otherwise>', 1],
        'case':         ['<otherwise>', 1],
        'default':      ['<otherwise>', 1]
    },

    '<case_tail>':{       
        'case':     ['<case_tail>', 0],
        'default':  ['<case_tail>', 1]
    },

    '<literal>':{    
        'int_lit':      ['<literal>', 0],
        'float_lit':    ['<literal>', 0],
        'string_lit':   ['<literal>', 0],
        'char_lit':     ['<literal>', 1],
        'true':         ['<literal>', 2],
        'false':        ['<literal>', 2]
    },

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
        'id':       ['<ctrl_var>', 1],
        ';':        ['<ctrl_var>', 2]
    },

    '<opt_expr>':{
        '=':    ['<opt_expr>', 0],
        ';':    ['<opt_expr>', 1],
    },

    '<for_bool>':{       
        'NOT':          ['<for_bool>', 0],
        'int_lit':      ['<for_bool>', 0],
        'float_lit':    ['<for_bool>', 0],
        'str':          ['<for_bool>', 0],
        '(':            ['<for_bool>', 0],
        '++':           ['<for_bool>', 0],
        '--':           ['<for_bool>', 0],
        'id':           ['<for_bool>', 0],
        'true':         ['<for_bool>', 0],
        'false':        ['<for_bool>', 0],
        'char_lit':     ['<for_bool>', 0],
        'string_lit':   ['<for_bool>', 0],
        'listen':       ['<for_bool>', 0],
        ';':            ['<for_bool>', 1]
    },

    '<for_unary>':{    
        'id':   ['<for_unary>', 0],
        '++':   ['<for_unary>', 0],
        '--':   ['<for_unary>', 0],
        ')':    ['<for_unary>', 1]
    },

    '<unary>':{    
        'id':['<unary>', 0],
        '++':['<unary>', 1],
        '--':['<unary>', 1]
    },
}