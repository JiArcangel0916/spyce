########## TOKEN CLASS ##########
class Token:
    def __init__(self, type, value = None, pos_start = None, pos_end = None):
        self.type = type
        self.value = value

        # if there are characters, set pos_start and pos_end to a copy of the position
        # advance the pos_end to simulate the end of a single character token
        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        
        # update pos_end
        if pos_end:
            self.pos_end = pos_end
    
    # string representation of the tokens
    def __repr__(self):
        if self.value:
            return f'{self.value}: {self.type}'
        return f'{self.type}'