class Operation:

    def __innit__(self):
        pass

    def add(self, a, b):
        if not isinstance(a, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        if not isinstance(b, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        return a+b
    
    def minus(self, a, b):
        if not isinstance(a, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        if not isinstance(b, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        return a-b
    
    def mul(self, a, b):
        if not isinstance(a, (int, float)):
            raise ValueError("Value must eihter be an integer or a float")
        
        if not isinstance(b, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        return a*b
    
    def div(self, a, b):
        if not isinstance(a, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        if not isinstance(b, (int, float)):
            raise ValueError("Value must either be an integer or a float")
        
        if b==0:
            raise ValueError("Zero division error")
        return a/b
    