def linearSearchProduct(productList,targetProduct):
 indices = []

 for index, product in enumerate(productList):
  if product == targetProduct:
   indices.append(index)

 return indices
  

#Example Usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes", "boot", "shoes","shoes"]
target = "shoes"
result = linearSearchProduct(products,target)
print(result)