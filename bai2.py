A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
common_s = set(A) ^ set(B)
common_count = len(set(A) ^ set(B))
print(A == B)
print(set(A) ^ set(B))
for i in common_s:
    print(i)
print(common_count)

