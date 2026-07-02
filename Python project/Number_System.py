#1. Decimal → Binary
n = int(input("Enter Decimal: "))
print(bin(n)[2:])

#2. Decimal → Octal
n = int(input("Enter Decimal: "))
print(oct(n)[2:])

#3. Decimal → Hexadecimal
n = int(input("Enter Decimal: "))
print(hex(n)[2:].upper())

#4. Binary → Decimal
b = input("Enter Binary: ")
print(int(b, 2))

#5. Octal → Decimal
o = input("Enter Octal: ")
print(int(o, 8))

#6. Hexadecimal → Decimal
h = input("Enter Hexadecimal: ")
print(int(h, 16))

#7. One Program (Most Efficient)
n = int(input("Enter Decimal: "))

print("Binary:", bin(n)[2:])
print("Octal:", oct(n)[2:])
print("Hexadecimal:", hex(n)[2:].upper())
