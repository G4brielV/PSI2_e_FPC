"""Escher"""
def escher(quant, nums):
    objetivo = int(nums[0]) + int(nums [-1])
    for i in range(1, len(nums)):
        if int(nums[i]) + int(nums[-1-i]) != objetivo:
            return "N"
    return "S"

a = "2,1,7,13,12".split(",")
b = len(str(a))

print(escher(b,a))