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
        result += f'at Line {self.pos_start.ln + 1}, Column {self.pos_end.col}\n\n'
        # result += self.visual_error()
        return result
    
    def visual_error(self):
        pass
        result = ''
        line = self.pos_start.fullText.split('\n')[self.pos_start.ln]
        spaces = ' ' * self.pos_start.col 
        arrows = '^' * ((self.pos_end.col + 5) - (self.pos_start.col - 3))

        result += f'{line}\n'
        result += spaces + arrows

        return result
        
########## LEXICAL ERROR ##########
# subclass of error that creates a lexical error type
class LexicalError(Error):
    def __init__(self, pos_start, pos_end, info):
        super().__init__(pos_start, pos_end, 'Lexical Error', info)

########## SYNTAX ERROR ##########
# subclass of error that creates a syntax error type
class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, info):
        super().__init__(pos_start, pos_end, 'Syntax Error', info)