from collections import defaultdict
# def filter_sustainable_brands(brands, criterion):
#     retList = []
#     for brand in brands:
#         if criterion in brand["criteria"]:
#             retList.append(brand["name"])
#     return retList

# # Time O(mXx)
# # Space O(n)

# brands = [
#     {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
#     {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
#     {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
#     {"name": "TrendyStyle", "criteria": ["trendy designs"]}
# ]

# brands_2 = [
#     {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
#     {"name": "FastStyle", "criteria": ["mass production"]},
#     {"name": "NatureWear", "criteria": ["eco-friendly"]},
#     {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
#     {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
#     {"name": "FastCloth", "criteria": ["cheap production"]}
# ]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# def count_material_usage(brands):
#     retDict = defaultdict(int)
#     for brand in brands:
#         for material in brand["materials"]:
#             retDict[material] += 1
#     return dict(retDict)

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))


# def organize_fabrics(fabrics):
#     fabrics.sort(key = lambda x : x[1], reverse = True)
#     return [fabric[0] for fabric in fabrics] #list comprehension

# fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
# fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
# fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

# print(organize_fabrics(fabrics))
# print(organize_fabrics(fabrics_2))
# print(organize_fabrics(fabrics_3))

# def process_supplies(supplies):
    

# supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
# supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
# supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

# print(process_supplies(supplies))
# print(process_supplies(supplies_2))
# print(process_supplies(supplies_3))



# def calculate_fabric_waste(items, fabric_rolls):
#     totalItemsFab = 0
#     for item in items:
#         totalItemsFab += item[1]
#     totalRollsFab = sum(fabric_rolls)
#     return totalRollsFab - totalItemsFab

# items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
# fabric_rolls = [5, 5, 5]

# items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
# fabric_rolls2 = [4, 4, 4]

# items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
# fabric_rolls3 = [7, 5, 5]

# print(calculate_fabric_waste(items, fabric_rolls))
# print(calculate_fabric_waste(items_2, fabric_rolls2))
# print(calculate_fabric_waste(items_3, fabric_rolls3))


def organize_fabric_rolls(fabric_rolls):
    fabric_rolls.sort()
    retList = []
    listOfDiff = [fabric_rolls[i+1] - fabric_rolls[i] for i in range(0, len(fabric_rolls)-1)]
    # for i in range(0, len(fabric_rolls)-1):
    #     listOfDiff.append(fabric_rolls[i+1]- fabric_rolls[i])
    if len(fabric_rolls%2 == 0):
        return [(fabric_rolls[i], fabric_rolls[i+1]) for i in range(0, len(fabric_rolls)-1, 2)]
    else:
        maxIndex = fabric_rolls.index(max(fabric_rolls))
        


    return retList

fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))

