decimal = int(input("enter a number to convert")) # The decimal number to convert 
binary = ""   # The binary representation of the decimal number 
while decimal > 0: 
    remainder = decimal % 2 
    binary = str(remainder) + binary 
    decimal = decimal // 2 
 
print(binary)  # Prints "1010" 