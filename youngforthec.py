def to_binary(number,bit):
    binary = bin(number)
    binary = binary[2:]
    while len(binary)<bit:
        binary = "0"+binary
    return binary

def reverse_binary(binary,bit_size):
    reverse = ""
    for bit in binary:
        if(bit == "1"):
            reverse += "0"
        else:
            reverse += "1"
    reverse = int(reverse , 2) +1
    return to_binary(reverse,bit_size)

number = int(input("enter number"))
bit = int(input("enter amount of bits"))
print(reverse_binary(to_binary(number,bit),bit))
