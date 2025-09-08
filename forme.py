
# user_dict = {"name":None,
#         "age":None,
#         "diseases":[],
#         "preferences":[],
#         "current_weight":None,
#         "desired_weight":None,
#         "height":None,}

# user_dict['preferences'].append('apple')

# print(user_dict["preferences"])

# formula = (10*75) + (6.25*180) - (5*17) - 161
# formula *= 1.9

# print(formula)

# numbers = [2,7,11,15]
# target = 9
# a = 0
# b = -1
# ans=[]
# while numbers[a]+numbers[b]!=target:
#     if numbers[a]+numbers[b]>target:
#         b -= 1
#     elif numbers[a]+numbers[b]<target:
#         a += 1
# ans.append(a+1)
# ans.append(len(numbers)+b+1)
# print(ans)

# n = int(input())
# m = int(input())
# costs = []
# ton = []
# gr = {}
# nodes = [ton[i][1] for i in range(len(ton))]
# for i in range(n):
#     i = int(input())
#     costs.append(i)
# for i in range(m):
#     i = [int(input()), int(input())]
#     ton.append(i)
#     nodes.append(i[1])
# ingr = dict(zip(nodes,costs))
# # for i in range(m):
# #     if ton[i][0] not in gr:
# #         gr[f"{i}"] = ingr
# #         ingr = ''
# print(ingr)

# print(n)
# print(m)
# print(costs)
# print(*ton)
# print(nodes)

# def ind_lowest_cost_node(costs):
#     max_cost = float("inf")
#     max_cost_node = None
#     for node in costs: 
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node

# n = int(input())
# m = input()
# m = m.split()
# count = 1
# while n!= 0:
#     c = input()
#     c.split()
#     for i in c:
#         if i in m:
#             n -= 1
#         else:
#             count += 1
#             n -= 1
# print(count)



n = int(input())
lenf = int(input())
m = set(input().split())
max_len = lenf
changes_count = 1

for i in range(n - 1):
    current_len = int(input())
    current_words = input().split()
    common_count = sum(1 for word in current_words if word not in m)
    
    if common_count != current_len:
        current_len = common_count + len(m) 

    elif common_count == current_len:
        changes_count += 1
        
    max_len = max(max_len, current_len)
    m = set(current_words)
    
print(changes_count, max_len)

