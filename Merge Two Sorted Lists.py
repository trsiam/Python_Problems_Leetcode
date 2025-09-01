#https://leetcode.com/problems/merge-two-sorted-lists/description
# def quicksort(arr):
#     # Base case: if the array has 0 or 1 element, it is already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Choose a pivot (we choose the last element as the pivot here)
#     pivot = arr[len(arr) - 1]
    
#     # Create two sub-arrays: one with elements less than the pivot, and one with elements greater than the pivot
#     left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
#     right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot
    
#     # Recursively apply QuickSort to the left and right sub-arrays, and combine them with the pivot
#     return quicksort(left) + [pivot] + quicksort(right)

# # Example usage
# arrrr = [1,2,4]
# arrr=[1,3,4]
# arr=arrrr+arrr
# sorted_arr = quicksort(arr)


# print("Sorted array:", sorted_arr)
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     @staticmethod
#     def quicksort(arr):
#         if len(arr) <= 1:
#             return arr

#         pivot=arr[len(arr) - 1]

#         left=[x for x in arr[:-1] if x <= pivot ]
#         right=[x for x in arr[:-1] if x > pivot]

#         return Solution.quicksort(left) + [pivot] + Solution.quicksort(right)

#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         list_One=self.linkedlist_into_List(list1)
#         list_Two=self.linkedlist_into_List(list2)

#         merge_List=list_One+ list_Two

#         sorted_List=Solution.quicksort(merge_List)

#         return self.list_to_linkedlist(sorted_List)

#     def linkedlist_into_List(self, head: ListNode) -> list:
#         arr = []
#         current = head
#         while current:
#             arr.append(current.val)
#             current = current.next
#         return arr
    
#     def list_to_linkedlist(self, arr: list) -> ListNode:
#         if not arr:
#             return None
#         head = ListNode(arr[0])
#         current = head
#         for val in arr[1:]:
#             current.next = ListNode(val)
#             current = current.next
#         return head
    
#     def print_linked_list(self,head: ListNode):
#         current = head
#         while current:
#             print(current.val,end=" ")
#             current = current.next
 

# list_One = ListNode(1, ListNode(2, ListNode(4)))
# list_Two = ListNode(1, ListNode(3, ListNode(4)))


# solution = Solution()
# merged_sorted_list = solution.mergeTwoLists(list_One, list_Two)

# solution.print_linked_list(merged_sorted_list)










from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_One=self.linkedlist_into_List(list1)
        list_Two=self.linkedlist_into_List(list2)

        merge_List=list_One+ list_Two

        sorted_List=merge_List.sort()

        return self.list_to_linkedlist(sorted_List)

    def linkedlist_into_List(self, head: ListNode) -> list:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr
    
    def list_to_linkedlist(self, arr: list) -> ListNode:
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def print_linked_list(self,head: ListNode):
        current = head
        while current:
            print(current.val,end=" ")
            current = current.next
 

list_One = ListNode(1, ListNode(2, ListNode(4)))
list_Two = ListNode(1, ListNode(3, ListNode(4)))


solution = Solution()
merged_sorted_list = solution.mergeTwoLists(list_One, list_Two)

solution.print_linked_list(merged_sorted_list)




