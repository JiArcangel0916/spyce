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

    # copies current position to capture position
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fullText)