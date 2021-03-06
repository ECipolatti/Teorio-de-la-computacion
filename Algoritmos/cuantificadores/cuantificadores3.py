# -----
# Test A: implementaciones mas basicas.
def ExisteX_A(P, X):
    for x in X:
        if P(x):
            return True
    return False

def ParaTodoX_A(P, X):
    for x in X:
        if not P(x):
            return False
    return True

def ParaTodoX_ParaTodoY_A(P, X, Y):
    for x in X:
        for y in Y:
            if not P(x, y):
                return False
    return True

def ParaTodoX_ExisteY_A(P, X, Y):
    for x in X:
        existe_y = False
        for y in Y:
            if P(x, y):
                existe_y = True
                break
        if not existe_y:
            return False
    return True

def ExisteX_ParaTodoY_A(P, X, Y):
    for x in X:
        paratodo_y = True
        for y in Y:
            if not P(x, y):
                paratodo_y = False
                break
        if paratodo_y:
            return True
    return False

def ExisteX_ExisteY_A(P, X, Y):
    for x in X:
        for y in Y:
            if P(x, y):
                return True
    return False

# -----
