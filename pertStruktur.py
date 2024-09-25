# #PERTEMUAN 3
# # def latihan(kegiatan):
# #     inputan  = input("Tambah kegiatan : ")
# #     kegiatan.append(inputan)

# #     tampilkegiatan(kegiatan)

# # def tampilkegiatan(kegiatan):
# #     for data in kegiatan:
# #         print(data)

# # def coba():
# #     inputan = int(input("Tampi data index ke berapa? : "))
# #     data = latihan[inputan]
# #     print("Data ke", inputan, ":", data)

# # def main():
# #     kegiatan = ["menulis", "makan"]

# #     latihan(kegiatan)
# # if __name__ == "__main__":
# #     main()
# #     coba()

# #PERTEMUAN 4
# # class Karyawan:
# #     #Atribut
# #     dataKaryawan = {"Maulana":{"usia": 18, "alamat": "Monjali", "Matkul": "Struktur Data Praktik"}}

# #     def tampilKaryawan(self):
# #         print(self.dataKaryawan)
# #     # def get_data(self):
# #     #     return self.dataKaryawan
# #     def tambahKaryawan(self, nama, usia, alamat, matkul):
# #         self.dataKaryawan[nama] = {"usia": usia, "alamat": alamat, "Matkul": matkul}
# #         print("Berhasil menambah data Mahasiswa")
# #     def editKaryawan(self, nama, usia, alamat, matkul):
# #         if nama in self.dataKaryawan:
# #             self.dataKaryawan[nama] = {"usia": usia, "alamat": alamat, "Matkul": matkul}
# #             print("data berhasil di hapus")

# # def menu():
# #     print("\nManajemen Karyawan")
# #     print("1. Tambah Karyawan")
# #     print("2. Tampil Karyawan")
# #     print("3. Edit data Karyawan")
# #     print("4. Hapus data Karyawan")
# #     print("5. Keluar")

# # def main():
# #     #objek dari kayawan
# #     objek = Karyawan()

# #     # objek.tampilKaryawan()
    
# #     # data = objek.get_data()
# #     # print(data)
# #     while True:
# #         menu()
# #         pilihan = input("pilih menu = ")

# #         if pilihan == "1":
# #             nama = input("Masukkan nama = ")
# #             usia = input("Masukkan usia = ")
# #             alamat = input("Masukkan alamat = ")
# #             matkul = input("Masukkan matkul = ")
# #             objek.tambahKaryawan(nama, usia, alamat, matkul)
# #         elif pilihan == "2":
# #             objek.tampilKaryawan()
# #         elif pilihan == "3":
# #             nama = input("Masukkan nama = ")
# #             usia = input("Masukkan usia = ")
# #             alamat = input("Masukkan alamat = ")
# #             matkul = input("Masukkan matkul = ")
# #             objek.editKaryawan(nama, usia, alamat, matkul)
# #         elif pilihan == "4":
# #             objek.dataKaryawan.clear()
# #             print("data berhasil di hapus")

# #         else:
# #             print("Anda keluar program")
# #             break


# # if __name__ == "__main__":
# #     main()


# #PERTEMUAN 5
# #linkedlist
# #Append
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None #Pointer


# class linkList:
#     def __init__(self, value):
#         newNode = Node(value)   #Objek dari node
#         self.head = newNode
#         self.tail = newNode
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.value, end=" -> ")
#             temp = temp.next
#         print("None")
#     def append(self, value):
#         newNode = Node(value)
#         if self.length == 0:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length += 1
#         return True
# MylinkedList = linkList(8)
# MylinkedList.append(False)
# MylinkedList.append(4.08)
# MylinkedList.append("Hallo")
# MylinkedList.display()
# MylinkedList.append(10)


# #POP
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None #Pointer


# class linkList:
#     def __init__(self, value):
#         newNode = Node(value)   #Objek dari node
#         self.head = newNode
#         self.tail = newNode
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.value, end=" -> ")
#             temp = temp.next
#         print("None")
#     def append(self, value):
#         newNode = Node(value)
#         if self.length == 0:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length += 1
#         return True
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

# my_linked_list = linkList(2)
# my_linked_list.append(1)


# print(my_linked_list.pop().value)
# print(my_linked_list.pop().value)


# #Prepend
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None #Pointer


# class linkList:
#     def __init__(self, value):
#         newNode = Node(value)   #Objek dari node
#         self.head = newNode
#         self.tail = newNode
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         newNode = Node(value)
#         if self.length == 0:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length += 1
#         return True
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
# my_linked_list = linkList(2)
# my_linked_list.append(3)

# print("before prepend :")
# print("Head :", my_linked_list.head.value)
# print("tail :", my_linked_list.tail.value)
# my_linked_list.display()

# my_linked_list.prepend(7)

# print("After prepend:")
# print("Head :", my_linked_list.head.value)
# print("tail :", my_linked_list.tail.value)
# my_linked_list.display()


# # POP first
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None #Pointer


# class linkList:
#     def __init__(self, value):
#         new_node = Node(value)   #Objek dari node
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail  = None
#         return temp
    
# my_linked_list = linkList(2)
# my_linked_list.append(1)
# my_linked_list.append(4)

# print(my_linked_list.pop_first().value)
# print(my_linked_list.pop_first().value)






# #DOUBLE LINKED LIST
# #Append

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None 
#         self.prev = None

# class DoublyLinkedlist:
#     def __init__(self, value):
#         new_node = Node(value)   #Objek dari node
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True

# my_doublyLinkedlist = DoublyLinkedlist(1)
# my_doublyLinkedlist.append(2)

# print(my_doublyLinkedlist.head.value)
# print(my_doublyLinkedlist.tail.value)


# #POP
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None 
#         self.prev = None

# class DoublyLinkedlist:
#     def __init__(self, value):
#         new_node = Node(value)   #Objek dari node
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp

# my_doublyLinkedlist = DoublyLinkedlist(1)
# my_doublyLinkedlist.append(2)

# print(my_doublyLinkedlist.pop().value)


# #prepend
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None 
#         self.prev = None

# class DoublyLinkedlist:
#     def __init__(self, value):
#         new_node = Node(value)   #Objek dari node
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length += 1
#         return True

# my_doublyLinkedlist = DoublyLinkedlist(3)
# my_doublyLinkedlist.append(2)

# print("sebelum prepend:")
# print("Head = ", my_doublyLinkedlist.head.value)
# print("Tail = ", my_doublyLinkedlist.tail.value)

# my_doublyLinkedlist.prepend(1)
# print("setelah prepend:")
# print("Head = ", my_doublyLinkedlist.head.value)
# print("Tail = ", my_doublyLinkedlist.tail.value)

# #POP First

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None 
#         self.prev = None

# class DoublyLinkedlist:
#     def __init__(self, value):
#         new_node = Node(value)   #Objek dari node
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length += 1
#         return True
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#             temp.next = None
#         self.length -= 1
#         return temp


# my_doublyLinkedlist = DoublyLinkedlist(2)
# my_doublyLinkedlist.append(1)

# print(my_doublyLinkedlist.pop_first().value)






#Pertemuan 8
#Bianry Search Tree
#Insert
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
            
# myTree = BinarySearchTree()
# myTree.insert(2)
# myTree.insert(1)
# myTree.insert(5)

# print("Root : ", myTree.root.value)
# print("Root->Left : ", myTree.root.left.value)
# print("Root->Right : ", myTree.root.right.value)
            
# #Contains

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
    

# myTree = BinarySearchTree()
# myTree.insert(47)
# myTree.insert(21)
# myTree.insert(76)
# myTree.insert(18)
# myTree.insert(27)
# myTree.insert(52)
# myTree.insert(82)

# print("BST Contains 27:")
# print(myTree.contains(27))

# print("BST Contains 52:")
# print(myTree.contains(52))

# #min Value & max Value
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

#PERTEMUAN 9
#GRAPH
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
#     def removeEdge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             try:
#                 self.adj_list[v1].remove(v2)
#                 self.adj_list[v2].remove(v1)
#             except ValueError:
#                 pass
#             return True
#         return False
    

# myGraph = Graph()
# myGraph.addVertex("A")
# myGraph.addVertex("Hallo")
# myGraph.addEdge("A","Hallo")
# myGraph.printGraph()






#Pertemuan 11
#Fungsi Rekursi

# def faktorial(n):
#     if n == 1:
#         return 1
        
#     return n * faktorial(n-1)

# def powerRecursion(a,b): #pangkat
#     if b == 0:
#         return 1
#     return a * powerRecursion(a, b - 1)

# print("Hasil pangkat =",powerRecursion(3, 2))
    
# print("Hasil faktorial =",faktorial(9))

#Algoritma pengurutan dasar
#Bubble sort

# def bubbleSort(myList):
#     for i in range(len(myList) - 1, 0, -1):
#         for j in range(i):
#             if myList[j] < myList[j+1]:
#                 temp = myList[j]
#                 myList[j] = myList [j+1]
#                 myList[j+1] = temp
#     return myList

# listAngka = [9,3,2,1,4,5,6]
# print("sebelum di sorting = ",listAngka)
# print("setelah di sorting = ",bubbleSort(listAngka))


# Selection sort
def selectionSort(myList):
    for i in range(len(myList)-1):
        minIndex = i
        for j in range(i+1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j
            if i != minIndex:
                temp = myList[i]
                myList[i] =  myList[minIndex]
                myList[minIndex] = temp
    return myList
print(selectionSort([6,2,4,0,1,-10,9,7]))


# #Insert sort

def insertSort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i - 1
        while temp < myList[j] and j > -1:
            myList[j + 1] = myList[j]
            myList[j] = temp
            j -= 1
    return myList

print(insertSort([5,-20,-100,100,25,4]))



#Pertemuan ke 12
#Merge sort

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):  # Perbaikan di sini
        combined.append(list1[i])
        i += 1
    while j < len(list2):  # Perbaikan di sini
        combined.append(list2[j])
        j += 1
    return combined

print(merge([1, 2, 7, 8], [3, 4, 5, 6]))  # Menghasilkan: [1, 2, 3, 4, 5, 6, 7, 8]

def mergeSort(myList):
    if len(myList) <= 1:
        return myList 
    mid_index = len(myList) // 2
    left = mergeSort(myList[:mid_index])
    right = mergeSort(myList[mid_index:])

    return merge(left, right)

original_list = [3, 1, 4, 2]
sorted_list = mergeSort(original_list)
print("Original List:", original_list)
print("\nSorted List:", sorted_list)



#Quick sort


def swap(myList, index1, index2):
    temp = myList[index1]
    myList[index1] = myList[index2]
    myList[index2] = temp

def pivot(myList, pivotIndex, endIndex):
    swapIndex = pivotIndex

    for i in range(pivotIndex + 1, endIndex + 1):
        if myList[i] < myList[pivotIndex]:
            swapIndex += 1
            swap(myList, swapIndex, i)
    swap(myList, pivotIndex, swapIndex)
    return swapIndex

def quickSortHelper(myList, left, right):
    if left < right:
        pivotIndex = pivot(myList, left, right)
        quickSortHelper(myList, left, pivotIndex - 1)
        quickSortHelper(myList, pivotIndex + 1, right)
    return myList

def quickSort(myList):
    quickSortHelper(myList, 0, len(myList) - 1)

myList = [4, 6, 1, 7, 3, 2, 5]
quickSort(myList)
print(myList)
