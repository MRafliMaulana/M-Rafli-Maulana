# #pertemuan 8


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
    
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#             return True
#         temp = self.root
#         while (True):
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right
#     def contains(self, value):
#         temp = self.root
#         while (temp is not None):
#             if value < temp.value:
#                 temp = temp.left
#             elif value > temp.value:
#                 temp = temp.right
#             else:
#                 return True
#         return False
#     def min_value_node(self, current_node):
#         while current_node.left is not None:
#             current_node = current_node.left
#         return current_node
#     def max_value_node(self, current_node):
#         while current_node.right is not None:
#             current_node = current_node.right
#         return current_node
    
# myTree = BinarySearchTree()
# myTree.insert(47)
# myTree.insert(21)
# myTree.insert(76)
# myTree.insert(18)
# myTree.insert(27)
# myTree.insert(52)
# myTree.insert(82)

# print("minimum value in Tree : ")
# print( myTree.min_value_node(myTree.root).value)
# print("maximum value in Tree :")
# print( myTree.max_value_node(myTree.root).value)



# #pertemuan 9
# class Graph :
#     def __init__(self):
#         self.adj_list = {}
#     def printGraph(self):
#         for vertex in self.adj_list:
#             print(vertex, ":", self.adj_list[vertex])

#     def addVertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
#     def addEdge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)
#             return True
#         return False
#     def isInGraph(self, vertex):
#         return vertex in self.adj_list.keys()

    
# myGraph = Graph()
# myGraph.addVertex("18")
# myGraph.addVertex("21")
# myGraph.addVertex("27")
# myGraph.addVertex("44")
# myGraph.addVertex("52")
# myGraph.addVertex("76")
# myGraph.addVertex("82")
# # myGraph.addVertex("Hallo")
# myGraph.addEdge("18","21")
# myGraph.addEdge("18","52")
# myGraph.addEdge("18","44")
# myGraph.addEdge("21","76")
# myGraph.addEdge("21","44")
# myGraph.addEdge("27","52")
# myGraph.addEdge("27","82")
# myGraph.addEdge("44","76")
# myGraph.printGraph()
# print(myGraph.isInGraph(25))
# print(myGraph.isInGraph(18))


#pertemuan 11
data = []
def menu():
    print("=======Sorting=======")
    print("1.masukan nilai")
    print("2. Ascending")
    print("3. Descending")



#Descending
def bubbleSortDS(myList):
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            if myList[j] < myList[j+1]:
                temp = myList[j]
                myList[j] = myList [j+1]
                myList[j+1] = temp
    return myList

#Ascending
def bubbleSortAS(myList):
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList [j+1]
                myList[j+1] = temp
    return myList

# listAngka = [9,3,2,1,4,5,6]
# print("Ascending sorting = ",bubbleSortAS(listAngka))
# print("Discending sorting = ",bubbleSortDS(listAngka))


while True:
    menu()
    inputan = int(input("masukkan menu = "))
    if inputan == 1:
        inputNM = int(input("Masukkan nilai yang akan di soring = "))
        data.append(inputNM)
    elif inputan == 2:
        print(bubbleSortAS(data))
    elif inputan == 3:
        print(bubbleSortDS(data))


