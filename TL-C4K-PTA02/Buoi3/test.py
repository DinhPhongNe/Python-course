class MathO:
    result = 0
    def __init__(self, x):
        self.result = x
        
    def add(self, x, y):
        self.result += x + y
        
    def muiltiply(self, x, y):
        self.result += x * y
        
math_ops = MathO(20)
math_ops.add(3, 5)
math_ops.muiltiply(2, 4)

print(math_ops.result)