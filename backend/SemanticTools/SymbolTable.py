class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def push(self):
        self.scopes.append({})

    def pop(self):
        self.scopes.pop()

    def get(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
    
    def get_local(self, name):
        if name in self.scopes[-1]:
            return self.scopes[-1][name]
        print(f'{name} not in local scope')
        return None
    
    def get_type(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                if hasattr(scope[name], 'datatype'): return scope[name].datatype
                return scope[name]
            print(f'{name} not found')
            return None
        
    def set(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
            
        if not self.scopes:
            self.scopes.append({})
        self.scopes[-1][name] = value

    def set_local(self, name, value):
        self.scopes[-1][name] = value