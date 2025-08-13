# In dsa.py

# --- Linked List for Transaction History ---
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get_history(self):
        history = []
        current_node = self.head
        while current_node:
            history.append(current_node.data)
            current_node = current_node.next
        return history

# --- Stack for Undo Feature ---
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

# --- Queue for Scheduled Transfers ---
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

# --- Binary Search Tree for Sorting by Balance ---
class BSTNode:
    def __init__(self, key, value):
        self.key = key      # The account balance
        self.value = value  # The account number
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self._insert_recursive(self.root, key, value)
    
    def _insert_recursive(self, current_node, key, value):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = BSTNode(key, value)
            else:
                self._insert_recursive(current_node.left, key, value)
        else:
            if current_node.right is None:
                current_node.right = BSTNode(key, value)
            else:
                self._insert_recursive(current_node.right, key, value)

    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)