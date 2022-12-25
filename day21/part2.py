from shared import monkeys, calculate


def visit(name):
    if name == "humn":
        return True
    elif isinstance(monkeys[name], int):
        return False
    lhs, _, rhs = monkeys[name]
    result = visit(lhs) or visit(rhs)
    if result:
        depends_on_humn.add(name)
    return result


def find(name, target):
    if name == "humn":
        return target
    lhs, op, rhs = monkeys[name]
    if lhs in depends_on_humn:
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


depends_on_humn = set()
visit("root")

lhs, _, rhs = monkeys["root"]
if lhs in depends_on_humn:
    humn = find(lhs, calculate(rhs))
else:
    humn = find(rhs, calculate(lhs))

print(humn)
