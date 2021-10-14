from itertools import zip_longest
class Solution:
    def reverse_number(numbers:list[int]):
        return numbers[::-1]
    def array_numbers_into_number(numbers:list[int]):
        value=0
        for number in numbers:
            value = value * 10 + number
        return value
    def Add_Two_Numbers(x:list[int],y:list[int]) -> list[int]:
        x_reversed=Solution.array_numbers_into_number(Solution.reverse_number(x))
        y_reversed = Solution.array_numbers_into_number(Solution.reverse_number(y))
        numbers=x_reversed+y_reversed
        numbers_array=[]
        for number in str(numbers):
            numbers_array.append(int(number))
        return numbers_array[::-1]


print(Solution.Add_Two_Numbers(x = [2,4,3], y = [5,6,4])) #[7, 0, 8]
print(Solution.Add_Two_Numbers(x = [0], y = [0])) #[0]
print(Solution.Add_Two_Numbers(x = [9, 9, 9, 9, 9, 9, 9], y = [9, 9, 9, 9])) #[8,9,9,9,0,0,0,1]
print(Solution.Add_Two_Numbers(x = [], y = [9, 1, 9, 1]))
print(Solution.Add_Two_Numbers(x = [9,1,6], y = [4,2,8]))