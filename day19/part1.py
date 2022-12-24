from shared import max_geodes, blueprints

total = sum(max_geodes(bp, 24) * bp.index for bp in blueprints)
print(total)
