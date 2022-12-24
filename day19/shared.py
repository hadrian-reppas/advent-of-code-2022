from dataclasses import dataclass


@dataclass
class Resources:
    ore: int
    clay: int
    obsidian: int
    geode: int

    def __le__(self, other):
        return (
            self.ore <= other.ore
            and self.clay <= other.clay
            and self.obsidian <= other.obsidian
            and self.geode <= other.geode
        )

    def __add__(self, other):
        return Resources(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geode + other.geode,
        )

    def __sub__(self, other):
        return Resources(
            self.ore - other.ore,
            self.clay - other.clay,
            self.obsidian - other.obsidian,
            self.geode - other.geode,
        )

    def key(resources):
        resources, robots = resources
        return (
            resources.geode + robots.geode,
            resources.obsidian + robots.obsidian,
            resources.clay + robots.clay,
            resources.ore + robots.ore,
            robots.geode,
            robots.obsidian,
            robots.clay,
            robots.ore,
        )


@dataclass
class Blueprint:
    index: int
    ore: Resources
    clay: Resources
    obsidian: Resources
    geode: Resources


blueprints = []
for line in open("input.txt").read().split("\n"):
    (
        _, index,
        _, _, _, _, a, _,
        _, _, _, _, b, _,
        _, _, _, _, c, _, _, d, _,
        _, _, _, _, e, _, _, f, _,
    ) = line.split()
    blueprints.append(
        Blueprint(
            int(index[:-1]),
            Resources(int(a), 0, 0, 0),
            Resources(int(b), 0, 0, 0),
            Resources(int(c), int(d), 0, 0),
            Resources(int(e), 0, int(f), 0),
        )
    )


def max_geodes(blueprint, time):
    queue = [(Resources(0, 0, 0, 0), Resources(1, 0, 0, 0))]
    for t in range(time):
        new = []
        for resources, robots in queue:
            if blueprint.ore <= resources:
                new.append((
                    resources - blueprint.ore + robots,
                    robots + Resources(1, 0, 0, 0)
                ))
            if blueprint.clay <= resources:
                new.append((
                    resources - blueprint.clay + robots,
                    robots + Resources(0, 1, 0, 0),
                ))
            if blueprint.obsidian <= resources:
                new.append((
                    resources - blueprint.obsidian + robots,
                    robots + Resources(0, 0, 1, 0),
                ))
            if blueprint.geode <= resources:
                new.append((
                    resources - blueprint.geode + robots,
                    robots + Resources(0, 0, 0, 1),
                ))
            new.append((resources + robots, robots))
        queue = sorted(new, reverse=True, key=Resources.key)[:100]
    return max(resources.geode for resources, _ in queue)
