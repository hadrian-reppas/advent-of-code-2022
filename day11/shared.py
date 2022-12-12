from dataclasses import dataclass
from math import lcm


@dataclass
class Monkey:
    items: list[int]
    operation: None
    divisor: int
    true_monkey: int
    false_monkey: int
    count: int = 0

    def do_turn(self, monkeys, worry):
        for item in self.items:
            item = self.operation(item) // worry
            item %= mod
            if item % self.divisor == 0:
                monkeys[self.true_monkey].items.append(item)
            else:
                monkeys[self.false_monkey].items.append(item)
            self.count += 1
        self.items.clear()


monkeys = []
for monkey in open("input.txt").read().split("\n\n"):
    _, items, op, divisor, true_monkey, false_monkey = monkey.split("\n")
    monkeys.append(
        Monkey(
            list(eval(items[18:] + ",")),
            eval("lambda old: " + op[18:]),
            int(divisor[21:]),
            int(true_monkey[29:]),
            int(false_monkey[30:]),
        )
    )

mod = lcm(*(monkey.divisor for monkey in monkeys))
