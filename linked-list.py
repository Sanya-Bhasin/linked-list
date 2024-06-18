class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
            
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end = '')
            current = current.next
        print()
        
    def add(self, other):
        result = LinkedList()
        carry = 0 
        current1 = self.head
        current2 = other.head
        while current1 or current2 or carry:
            sum1 = 0
            sum2 = 0
            if current1:
                sum1 = current1.value
                current1 = current1.next
            if current2:
                sum2 = current2.value
                current2 = current2.next
            total = sum1 + sum2 + carry
            carry = total//10
            result.append(total%10)
        return result 
        
    def subtract(self, other):
        result = LinkedList()
        borrow = 0 
        current1 = self.head
        current2 = other.head
        while current1 or current2 or borrow:
            sum1 = 0 
            sum2 = 0 
            if current1:
                sum1 = current1.value
                current1 = current1.next
            if current2:
                sum2 = current2.value
                current2 = current2.next 
            total = sum1 - sum2 - borrow
            if total < 0:
                borrow = 1
                total += 10 
            else:
                borrow = 0
            result.append(total)
        return result
    
    def multiply(self, other):
        result = LinkedList()
        current1 = self.head
        while current1:
            current2 = other.head
            temp = LinkedList()
            carry = 0
            while current2:
                sum1 = 0
                sum2 = 0
                if current1:
                    sum1 = current1.value
                    current1 = current1.next
                if current2:
                    sum2 = current2.value
                    current2 = current2.next 
                total = sum1 * sum2 + carry 
                carry = total // 10
                temp.append(total % 10)
            while carry:
                temp.append(carry % 10)
                carry //= 10
            result = result.add(temp)
        return result
        
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

other_linked_list = LinkedList()
other_linked_list.append(4)
other_linked_list.append(5)

print("Linked List 1 is: ", end = ' ')
linked_list.print_list()
print("Linked List 2 is: ", end = ' ')
other_linked_list.print_list()

print("Addition", end = ' ')
result = linked_list.add(other_linked_list)
result.print_list()

print("Subtraction", end = ' ')
result = linked_list.subtract(other_linked_list)
result.print_list()

print("Multiplication", end = ' ')
result = linked_list.multiply(other_linked_list)
result.print_list()
