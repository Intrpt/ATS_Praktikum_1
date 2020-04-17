class Vector:
    """docstring for Vector"""
    def __init__(self, p):
        #super(Vector, self).__init__()
        self.p = p

    def __eq__(self, other):
        return (self.p.x == other.p.x) && (self.p.y == other.p.y)
