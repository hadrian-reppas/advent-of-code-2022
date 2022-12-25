monkeys = {}
for line in open("input.txt").read().split("\n"):
    monkey, expr = line.split(": ")
    if " " in expr:
        monkeys[monkey] = expr.split()
    else:
        monkeys[monkey] = int(expr)


def calculate(name):
    expr = monkeys[name]
    if isinstance(expr, int):
        return expr
    lhs, op, rhs = expr
    code = f"calculate(lhs) {op} calculate(rhs)"
    return round(eval(code))
