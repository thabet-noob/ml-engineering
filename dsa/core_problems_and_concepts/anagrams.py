# def char_count(s):
#     count ={}
#     for char in s:
#         if char not in count:
#             count[char]=0
#         count[char] += 1
#     return count

# # print(char_count("catr"))
# # print(char_count("cart"))

# def anagram(s1,s2):
#     if char_count(s1) == char_count(s2):
#         return True
#     else:
#         return False

# # print(anagram("catr", "cart"))
# print(char_count("catr") == char_count("cart"))


from collections import Counter


def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)


print(anagrams("catr", "cart"))
