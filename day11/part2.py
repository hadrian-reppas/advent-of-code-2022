from shared import monkeys

for _ in range(10000):
    for monkey in monkeys:
        monkey.do_turn(monkeys, 1)

*_, count1, count2 = sorted(monkey.count for monkey in monkeys)
print(count1 * count2)
