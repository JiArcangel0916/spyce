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
        # result += string_with_arrows(self.pos_start.fullText, self.pos_start, self.pos_end, self.info)
        return result

########## LEXICALERROR ##########
# subclass of error that creates a lexical error type
class LexicalError(Error):
    def __init__(self, pos_start, pos_end, info):
        super().__init__(pos_start, pos_end, 'Lexical Error', info)


def string_with_arrows(text, pos_start, pos_end, info):
    result = ''
    # Calculate indices
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)
    # Generate each line
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Calculate line columns
        line = text[idx_start:idx_end]
        if 'Invalid Delimiter' in info:
            col_start = pos_end.col
            col_end = pos_end.col + 1
        elif 'Invalid character' in info:
            col_start = pos_end.col
            col_end = pos_end.col + 1
        elif 'not closed' in info:
            col_start = pos_end.col - 3
            col_end = pos_end.col
        else:
            col_start = pos_start.col
            col_end = pos_end.col
        # Append to result: line, newline, arrows, and another newline for separation
        result += line + '\n' 
        result += ' ' * col_start + '^' * max(0, col_end - col_start) + '\n'  # Added '\n' after arrows; max(0, ...) prevents negative lengths
        # Re-calculate indices
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0 : idx_end = len(text)
    return result.replace('\t', ' ')
    # result = ''

    # # Calculate indices
    # idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    # idx_end = text.find('\n', idx_start + 1)
    # if idx_end < 0: idx_end = len(text)

    # # Generate each line
    # line_count = pos_end.ln - pos_start.ln + 1
    # for i in range(line_count):
    #     # Calculate line columns
    #     line = text[idx_start:idx_end]
    #     col_start = (pos_start.col+1) if i == 0 else 0
    #     col_end = (pos_end.col+1) if i == line_count - 1 else len(line) - 1

    #     # Append to result
    #     result += line + '\n'
    #     # result += ' ' * col_start + '^' * (col_end + 1 - col_start)
    #     result += ' ' * col_start + '^' * max(0, col_end - col_start)

    #     # Re-calculate indices
    #     idx_start = idx_end
    #     idx_end = text.find('\n', idx_start + 1)
    #     if idx_end < 0 : idx_end = len(text)

    # return result.replace('\t', ' ')