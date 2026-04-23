more = [x + 1 for x in [1,2,3,4]] # x takes 1, 2, 3, 4 at each step
print(more) #the value of more is [2,3,4,5]
def square(n:int) -> int:
    return n * n #1->2, 2->4, 3->9, 4->16

squares = [square(x) for x in [1,2,3,4]] #squares is [2,4,9,16], which is the squared value of the inputted list
print(squares)

def check(n:int) -> bool:
    return n > 2 #0->false, 1->false, 2->false, 3->true, 4->true

answer = [x for x in range(5) if check(x)] #answer is [False, False, False, True, True]
print(answer)

def inc(m:int) -> int:
    return m + 1 #3->4, 4->5

def check(n:int) -> bool:
    return n > 2 #0->false, 1->false, 2->false, 3->true, 4->true

answer = [inc(x) for x in range(5) if check(x)] #answer is [4,5]
print(answer)

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num #4->4, 9->13, 2->15, 1->16
    return total #total = 16

result = tally([4,9,2,1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx]) #0->[4,9,2,1,4], 1-> [4,9,2,1,4,9], 2-> [4,9,2,1,4,9,2], 3-> [4,9,2,1,4,9,2,1]
    return new_list
#This loop makes a copy of the list with itself, while the first function adds each list component to a running total
result = copy([4,9,2,1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1) #4-> [4,9,2,1,5], 9-> [4,9,2,1,5,10], 2-> [4,9,2,1,5,10,3], 1-> [4,9,2,1,5,10,3,2]
    return new_list

result = increment_all([4,9,2,1])