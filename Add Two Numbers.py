#https://leetcode.com/problems/add-two-numbers/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#                 temp_V=''
#                 temp_Vthree=''
#                 temp_Vtwo=0
#                 temp_Vfour=0
#                 temp_Veight=''
#                 temp_Vnine=0
#                 A=[]
#                 for i in range(len(l1)-1,-1,-1):
#                         temp_V+=str(l1[i])
#                         temp_Vtwo=int(temp_V)
#                 for j in range(len(l2)-1,-1,-1):
#                         temp_Vthree+=str(l2[j])
#                         temp_Vfour=int(temp_Vthree)

#                 temp_Six=temp_Vtwo+temp_Vfour
                    
#                 temp_Seven=list(str(temp_Six))
#                 for i in range(len(temp_Seven)-1,-1,-1):
#                     temp_Veight += str(temp_Seven[i])

#                 for i in str(temp_Veight):
#                         A.append(int(i))  
#                 return A


# Solution=Solution.addTwoNumbers

      

class Node:
    def __init__(self, value):
        self.value = value  # Node value
        self.next = None    # Pointer to the next node


class Node:
    def __init__(self, value):
        self.value = value  # Node value
        self.next = None    # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initial empty linked list

    def append(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty, make new node as the head
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the last node to new node

    def print_list(self):
        current_node = self.head
        while current_node:  # Traverse and print the values of the nodes
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")  # End of the list

# Create a linked list
linked_list = LinkedList()

# Add a few values to the linked list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Print the linked list
linked_list.print_list()




























