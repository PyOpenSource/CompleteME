import sympy


def fouriers_law(params):
    qpp, k, t1, t2, l = sympy.symbols("qpp k T1 T2 L")
    f_law = qpp - k * (t1-t2)/l

    param_set = set([qpp, k, t1, t2, l])
    solve_for = param_set - set(params.keys())
    expr = sympy.solve(f_law, solve_for)[0]
    expr = expr.subs(params)

    return expr



# Tests (Move to a test file)
qpp, k, t1, t2, l = sympy.symbols("qpp k T1 T2 L")
params = {k: 1.7, t1: 1400, t2: 1150, l: 0.15}
output = fouriers_law(params)
#print(output)
