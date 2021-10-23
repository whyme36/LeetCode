class Solution(object):
    def reverseKGroup(self, head: list[int], k: int) -> list[int]:
        try:
            number_of_k_group=len(head)//k
        except ZeroDivisionError:
            return []

        reversed_array=[]
        while number_of_k_group>0:
            reversed_array+=head[:k][::-1]
            head=head[k:]
            number_of_k_group-=1
        if head:
            reversed_array+=head
        return reversed_array

if __name__=='__main__':
    s=Solution()
    print(s.reverseKGroup([1,2,3,4,5], 2))
    print(s.reverseKGroup([1,2,3,4,5], 3))
    print(s.reverseKGroup([1, 2, 3, 4, 5], 1))
    print(s.reverseKGroup([1], 1))