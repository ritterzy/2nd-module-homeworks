class paralelogram:
    def __init__(self,a_side,b_side):
        self.a=a_side
        self.b=b_side
class square(paralelogram):
    def __init__(self):
        square= self.a * self.a
        print(square)

class rectangular(paralelogram):
    def __init__(self):
        square = self.a * self.b
        print(square)
class rhombus(paralelogram):
    def __init__(self):
        square = self.a * self.a
        print(square)
parallelogram=paralelogram(5,8)
Rhombus=rhombus(4)
print(rhombus.Rhombus())