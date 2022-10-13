#import pudb; pu.db

ELMENT_NOT_FOUND = -1

class Node:
	def __init__(self, element, key, previouseNode = None, nextNode = None):
		self.element = element
		self.key = key
		self.nextNode = nextNode 
		self.previouseNode = previouseNode

	def setNextNode(self, nextNode):
		self.nextNode = nextNode

	def setPreviouseNode(self, previouseNode):
		self.previouseNode = previouseNode

class Dict_:
	def __init__(self):
		self.privateElements = {}
		self.firstNode = None
		self.lastNode = None

	def insert(self, element, key):
		if self.is_empty():
			node = Node(element, key)
			self.firstNode = node
		else:
			node = Node(element, key, self.lastNode)
			self.lastNode.setNextNode(node)

		self.lastNode = node	
		self.privateElements[key] = node

	def remove(self, key):
		if self.is_empty() or not( self.includes(key)):
			return ELMENT_NOT_FOUND

		del_node = self.privateElements[key]
		if del_node != self.firstNode:
			del_node.previouseNode.setNextNode(del_node.nextNode)
		else:
			self.firstNode = del_node.nextNode
		if del_node != self.lastNode:
			del_node.nextNode.setPreviouseNode(del_node.previouseNode)
		else:
			self.lastNode = del_node.previouseNode
		del self.privateElements[key]

	def iterate_and_do(self, function, auxiliary_Args):
		currentNode = self.firstNode
		result = True
		while (currentNode != None) and (result):
			result = function(currentNode.element, currentNode.key, auxiliary_Args)
			currentNode = currentNode.nextNode

	def includes(self, element):
		return element in self.privateElements 

	def keys(self):
		listOfKeys = []
		def aux_func(element, key, listToComplete):
			listToComplete.append(key)
			return True
		self.iterate_and_do(aux_func, listOfKeys)
		return listOfKeys

	def is_empty(self):
		return self.size() <= 0

	def size(self):
		return len(self.privateElements)

	def access(self, key):
		return self.privateElements[key].element
