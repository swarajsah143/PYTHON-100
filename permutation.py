# from itertools import product

# # List of digits from 0 to 9
# digits = '0123456789'
# c=0
# # Generate combinations of three-digit numbers with repeating digits
# combinations_list = product(digits,repeat=3)

# # Convert each combination to a string and print
# for combo in combinations_list:
#     number = ''.join(combo)
#     c=c+1
#     print(number)
# print("\n\n",c)



# def generate_permutations(sequence):
#     if len(sequence) == 0:
#         return [""]
#     if len(sequence) == 1:
#         return [sequence]

#     permutations = []
#     for i in range(len(sequence)):
#         first_element = sequence[i]
#         remaining_elements = sequence[:i] + sequence[i + 1:]
#         for sub_permutation in generate_permutations(remaining_elements):
#             permutations.append(first_element + sub_permutation)
#     return permutations

# # Define a sequence of elements
# sequence = "ABCD"

# # Generate permutations and print them
# permutations = generate_permutations(sequence)
# for perm in permutations:
#     print(perm)

lst=[1,2,3,4]
print(lst[4:4])