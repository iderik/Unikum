def get_x(vec):
    return vec[0]

def get_y(vec):
    return vec[1]

def add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def sub(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1])

def mul(vec, a):
    return (vec[0]*a, vec[1]*a)

def div(vec, a):
    return (vec[0]/a, vec[1]/a)

def neg(vec):
    return (-vec[0], -vec[1])