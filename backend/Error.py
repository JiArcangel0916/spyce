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
        result += f'Line {self.pos_start.ln + 1}, Column {self.pos_end.col + 1}\n'
        return result

########## LEXICALERROR ##########
# subclass of error that creates a lexical error type
class LexicalError(Error):
    def __init__(self, pos_start, pos_end, info):
        super().__init__(pos_start, pos_end, 'Lexical Error', info)