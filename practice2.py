# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 20:19:20 2016

@author: Rahul Patni
"""

import random

class Node():
	def __init__(self, x, y):
		self.next = None
		self.x = x
		self.y = y
		self.hit = 0
		self.visited = 0
		self.next = None

	def checkOver(self):
		if self.x >= 8 or self.y < 0 or self.x < 0 or self.y >= 8:
			return True
		return False

class Stack():
	def __init__(self):
		self.head = None
		self.total = 0

	def push(self, node):
		if self.total == 0:
			self.head = node
			self.total += 1
			return
		node.next = self.head
		self.head = node
		self.total += 1

	def pop(self):
		if self.total == 0:
			print "cannot remove from empty stack"
			return

		toRet = self.head
		self.head = self.head.next
		toRet.next = None
		self.total -= 1
		return toRet
  
def main():
    s = Stack()
    for i in range(20):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        print x, y
        n = Node(x, y)
        s.push(n)
        print s.total
        
    print "remooving"
        
    while s.total != 0:
        curr = s.pop()
        if curr != None:
            print curr.x, curr.y
        
        
main()
        