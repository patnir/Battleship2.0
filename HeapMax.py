# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 21:24:40 2016

@author: Rahul Patni
"""

# heap sort

import random

class Node():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.val = 0
        self.prob = 0

class HeapMax():
    def __init__(self):
        self.array = [None] * 64
        self.start = 0
        self.end = 0
        
    def insert(self, node):
        if self.end == 0:
            self.array[self.end] = node
            self.end += 1
            return
        self.array[self.end] = node
        self.end += 1
        currIndex = self.end
        parentIndex = currIndex / 2
        #print parentIndex
        #print "out", currIndex, parentIndex
        #print self.array
        parent = (self.array[parentIndex - 1]).val
        #print val, parent
        while node.val > parent and parentIndex > 0:
            #print "parent", "child", parentIndex - 1, currIndex - 1
            #print self.array[parentIndex - 1], self.array[currIndex - 1]
            self.array[parentIndex - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[parentIndex - 1]
            currIndex = parentIndex
            parentIndex = currIndex / 2
            parent = (self.array[parentIndex - 1])
            if parent == None:
                return 
            parent = parent.val
        return
        
    def checkHeapProperty(self):
        currIndex = self.end
        parentIndex = currIndex / 2
        while parentIndex > 0:
            if self.array[parentIndex - 1] < self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def extractMax(self):
        if self.end == 0:
            return None
            
        toRemove = self.array[0]
        
        self.end -= 1
        self.array[0] = self.array[self.end]
        self.array[self.end] = None
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.end:
        #while child1Index <= self.end and (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
            if child2Index > self.end:
                child2Index = child1Index
            if (self.array[currIndex - 1].val < self.array[child1Index - 1].val or self.array[currIndex - 1].val < self.array[child2Index - 1].val):
                if self.array[child1Index - 1].val >= self.array[child2Index - 1].val:
                    self.array[child1Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child1Index - 1] 
                    currIndex = child1Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
                else:
                    self.array[child2Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child2Index - 1] 
                    currIndex = child2Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
            else:
                child1Index = self.end + 1
        
        #self.checkHeapProperty()
        return toRemove
        

def main():
    h = HeapMax()
    for i in range(30):
        n = Node()
        n.val = random.randint(10, 90)
        print n.val
        if n == None:
            print "Error"
            return
        h.insert(n)
        #print h.array
        #h.checkHeapProperty()
    
    
    print "removing"
    
    while h.end != 0:
        val = h.extractMax()
        print val.val
        #print h.array
    
main()