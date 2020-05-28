from time import time
start = time()

NUMBERS = set("123456789")
product_list = []

for i in range(1,99):
    for j in range(100,9999):
        # Multipy the two numbers and combine all product, i and
        # j into one string.
        product = i * j
        combined = str(product) + str(i) + str(j)

        # We need only 9 digits, exit if no of digits are greater than 9
        if len(combined) > 9 :
            break

        # Check for the availability of the 9 digits from 1-9
        if set(combined) == NUMBERS:
            product_list.append(product)

 # Obtaining unique products
unique_product_list = set(product_list)

print(sum(unique_product_list))
print( "Time:", time() - start, "Sec.")
