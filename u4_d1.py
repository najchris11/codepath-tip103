# def filter_sustainable_brands(brands, criterion):
#     retList = []
#     for brand in brands:
#         if criterion in brand["criteria"]:
#             retList.append(brand["name"])

#     return retList


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



# def find_best_fabric_pair(fabrics, budget):
#     sorted_fabrics = sorted(fabrics, key=lambda x: x[1])
#     l, r = 0, len(sorted_fabrics) - 1
#     res, fabs = 0, ()
    
#     while l < r:
#         leftnum, rightnum = sorted_fabrics[l][1], sorted_fabrics[r][1]
#         if leftnum + rightnum > budget:
#             r -= 1
#         elif leftnum + rightnum < budget:
#             l += 1
#             if leftnum + rightnum > res:
#                 fabs = (sorted_fabrics[l][0], sorted_fabrics[r][0])
#                 res = leftnum + rightnum
#         else:
#             return (sorted_fabrics[l][0], sorted_fabrics[r][0])
#     return fabs

# fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
# fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
# fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

# print(find_best_fabric_pair(fabrics, 45))
# print(find_best_fabric_pair(fabrics_2, 70))
# print(find_best_fabric_pair(fabrics_3, 60))

def filter_sustainable_brands(brands, criterion):
    retList = []
    for brand in brands:
        if criterion in brand["criteria"]:
            retList.append(brand["name"])
    return retList


brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))
