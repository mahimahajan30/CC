# QUESTION 1
# L = [10,20,30,40,50,60,70,80]
# L.append(200)
# L.append(300)
# print(L)
# L.pop(0)
# print(L)
# L.pop(1)
# print(L)
# L.sort()
# print(L)
# L.sort(reverse=True)
# print(L)


# QUESTION 2

# tup =(45,89.5,76,45.4,89,92,58,45)
# print("tuple--->",tup)
# highest_score =  max(tup)
# print("highest score is--->",highest_score)
# highest_score_indx=tup.index(highest_score)
# print(highest_score_indx)
# lowest_score= min(tup)
# print("lowest score is--->",lowest_score)
# count_lowest_score = tup.count(lowest_score)
# print("no of time it appears", count_lowest_score)
# reverse_tup = list(reversed(tup))
# print("reverse of tuple as list--->", reverse_tup)
# specific_score = 76
# if specific_score in tup:
#    first_occurence = tup.index(specific_score)
#    print("first occurenece is present at index",first_occurence)
# else:
#   print("the score is not present")



# QUESTION 3
# import random 
# def is_prime(num):
#    if num<2:
#        return False
#    for i in range(2,num):
#         if num % i == 0:
#             return False
#             return True
# random_numbers = [random.randint(100,900) for _ in range(100)]
# print("list of random number", random_numbers)
# odd_numbers = [num for num in random_numbers if num%2!=0]
# print("all odd numbers:",odd_numbers)
# even_numbers=[num for num in random_numbers if num%2==0]
# print("all even numbers:",even_numbers)
# prime_numbers = [num for num in random_numbers if is_prime(num)]
# print("all prime numbers:",prime_numbers)


# QUESTION 4
# A = {34,56,78,90}
# B = {78,45,90,23}
# print("union of a and b--->", A.union(B))
# print("intersection of a,b--->",A.intersection(B))
# print("symmetric difference--->", A.symmetric_difference(B))
# is_A_subset_B = A.issubset(B)
# is_B_superset_A = B.issuperset(A)
# print("is A subset of B--->", is_A_subset_B)
# print("is B superset of A--->", is_B_superset_A )

# x = int(input("enter the score to remove from set A:"))
# if x in A:
#     A.remove(x)
#     print("set A after removing the score--->", A)
# else:
#         print("the score is not present in set A")


# QUESTION 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"

}
print(sample_dict)
sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)