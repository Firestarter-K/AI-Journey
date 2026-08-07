
print("Hello World!")

arrCloths = ["Shirt", "Pants", "Jacket", "Socks"]
for cloth in arrCloths:
    print(cloth)

arrClothColors = [x + " Color" for x in arrCloths]

for i in range(len(arrCloths)):
    print(f"{arrCloths[i]} - {arrClothColors[i]}")