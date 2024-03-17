
class node:
    def __init__(self,value= None):
        self.value= value
        self.left_child= None
        self.right_child= None

class binary_search_tree:
    def __init__(self):
        self.root= None

    def _insert(self, value, cur_node):
        # Private methods are those methods that should neither be
        # accessed outside the class nor by any base class.
        # In Python, there is no existence of Private methods
        # that cannot be accessed except inside a class. However,
        # to define a private method prefix the member name with the
        # double underscore “__”. Here I used '_' which also works
        # Basically, the _insert will never be called by the user
        # The insert function will be called, which will then internally call the _insert, so the _insert is private
        if value < cur_node.value:
            if cur_node.left_child == None:  # if value is less than the current node and the left space is empty
                cur_node.left_child = node(value)  # put that new value as a node to the left of the current node
            else:  # else if the left space is taken
                self._insert(value,
                             cur_node.left_child)  # call the function so the new value can be put as a node to the left of the node that is currently to the left of the current node
        elif value > cur_node.value:
            if cur_node.right_child == None:  # remember '==' to compare, and '=' to set value
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:  # Value= cur_node value, binary trees typically do not allow duplicates
            print("Value already in tree!")

    def insert(self,value):

        if self.root== None:
            self.root= node(value)
        else:
            self._insert(value,self.root)
            #In Python, methods and attributes should generally be accessed using dot notation (self.method_name() or self.attribute_name)
            #within the class itself instead of something like method_name(self, other inputs).
            #So it should be self._insert(value,self.root), NOT _insert(self,value,self.root).
            #This helps in maintaining readability and following standard conventions, making your code more understandable to other developers.

    def _print_tree(self,cur_node):
        if cur_node!= None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def print_tree(self):

        if self.root!= None:
            self._print_tree(self.root)

    def _height(self,cur_node,cur_height):
        if cur_node== None:
            return cur_height
        else:
            left_height = self._height(cur_node.left_child, cur_height+1)
            right_height = self._height(cur_node.right_child, cur_height+1)
            #this increments the height by one and moves to the next node down. That one becomes the root. this continues until the base case where the root doesn't exist at the bottom of the tree
        return max(left_height,right_height)

    def height(self):
        if self.root != None: #if the root exists
            return self._height(self.root,0) #call the function for the height which includes recursion
        else:
            return 0 #if there is no root, the height is zero

    def _search(self,value,cur_node):
        if cur_node is None: #should put this first so that the program immediatley exists when this occurs.
            #The above is the base case for the recursion. put the base case up top
            return False #value not in tree, got to the bottom of the tree
        if value > cur_node.value:
            return self._search(value, cur_node.right_child)
        elif value < cur_node.value:
            return self._search(value, cur_node.left_child)
        else: #if value == cur_node
            return True #value ==  cur_node

    def search(self,value):
        if self.root!= None:
            return self._search(value,self.root)
        else:
            return False #if it gets to the bottom of the tree and that value has not been found, it does not exist, return False



def fill_tree(tree,num_elems,max_int):
    from random import randint
    for num in range (num_elems):
        tree_elem = randint(0,max_int)
        tree.insert(tree_elem)
    return tree

#Testing
tree = binary_search_tree() #creating a binary search tree
tree = fill_tree(tree,100,1000)

tree.print_tree()
print("Tree height: " + str(tree.height()))
print("Search result: " + str(tree.search(999)))
