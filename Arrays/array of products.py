def arrayOfProducts(array):
	
	products= []
	for i in range(len(array)):
		arrayproduct = 1
		for j in range(len(array)):
			if i !=j :
				arrayproduct *= array[j]
		products.append(arrayproduct)
    return products