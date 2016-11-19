# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:31:58 2016

@author: Rahul Patni
"""

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
		if self.total == 0:
			self.head = node
			return
		node.next = self.head
		self.head = node
		self.total += 1