def decimal_to_bin(num):

    if num//2 == 1:
        return "1" + f"{num%2}"

    return  decimal_to_bin(num//2) + f"{num%2}"



print(f"18 --> {decimal_to_bin(18)}")
print(f"53 --> {decimal_to_bin(53)}")

