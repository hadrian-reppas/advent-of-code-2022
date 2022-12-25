from shared import monkeys, calculate


def depends_on_humn(name):
    if name == "humn":
        return True
    elif isinstance(monkeys[name], int):
        return False
    lhs, _, rhs = monkeys[name]
    return depends_on_humn(lhs) or depends_on_humn(rhs)

def find(name, target):
    if name == "humn":
        return target
    lhs, op, rhs = monkeys[name]
    if depends_on_humn(lhs):
        other = calculate(rhs)
        if op == "+":
            return find(lhs, target - other)
        elif op == "-":
            return find(lhs, target + other)
        elif op == "*":
            return find(lhs, target // other)
        elif op == "/":
            return find(lhs, target * other)
    else:
        other = calculate(lhs)
        if op == "+":
            return find(rhs, target - other)
        elif op == "-":
            return find(rhs, other - target)
        elif op == "*":
            return find(rhs, target // other)
        elif op == "/":
            return find(rhs, other // target)


lhs, _, rhs = monkeys["root"]
if depends_on_humn(lhs):
    humn = find(lhs, calculate(rhs))
else:
    humn = find(rhs, calculate(lhs))

print(humn)
