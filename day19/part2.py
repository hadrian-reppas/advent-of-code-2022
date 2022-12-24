from shared import max_geodes, blueprints

product = (
    max_geodes(blueprints[0], 32)
    * max_geodes(blueprints[1], 32)
    * max_geodes(blueprints[2], 32)
)
print(product)
