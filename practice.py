# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:05:53 2016

@author: Rahul Patni
"""

# battleship practice


class Node():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hit = 0
        self.prob = 0

prob = [None] * 8
for i in range(len(prob)):
    prob[i] = [None] * 8
    for j in range(len(prob[i])):
        n = Node()
        prob[i][j] = n


class Sea():
    def __init__(self):
        self.hit = 0
        self.visited = 0

class Node():
	def __init__(self, sea):
		self.sea = sea
		self.next = None	

class Stack():
	def __init__(self):
		self.head = None
		self.total = 0

	def push(self, node):
		if self.total = 0:
			self.head = node
			return
		node.next = self.head
		self.head = node
		self.total += 1

	def pop(self):
		if self.total = 1:
			print "cannot remove from empty stack"
			return

		toRet = self.head
		self.head = self.head.next
		toRet.next = None
		return toRet