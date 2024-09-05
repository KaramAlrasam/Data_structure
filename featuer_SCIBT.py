class Node:
  def __init__(self, data):
    self.data=data
    self.right=None
    self.left=None

class BST:
  def __init__(self):
    self.root=None
    self.res=[]

  def add(self, item):
    new_node=Node(item)
    if not self.root:
      self.root=new_node
      return
    curr=self.root
    parent=None
    while curr:
      parent=curr
      if curr.data >= item:
        curr=curr.left
      else:
        curr=curr.right
    if parent.data >= item:
      parent.left=new_node
    else:
      parent.right=new_node
  
  def Build_BT(self, m_list):
    if not m_list:
      return None
    else:
      mid=len(m_list)//2
      new_node=Node(m_list[mid])
      new_node.left=self.Build_BT(m_list[:mid])
      new_node.right=self.Build_BT(m_list[mid+1:])
      return new_node

  def preOrder(self, new_node):
    
    if new_node == None:
      return 
    else:
      
      self.res.extend([new_node.data])
      self.preOrder(new_node.left)
      self.preOrder(new_node.right)
      return self.res

  def main_BST(self, m_list):
    result=self.Build_BT(m_list)
    return self.preOrder(result)

  def searchItem(self, item):
    if not self.root:
      raise Exception("The Array is empty!!!")
    closet=self.root.data
    curr=self.root
    while curr:
      #this line will discover the closet item and will update Var=closet
      #and with abs func we will get rid of minus marker. this line is assantial
      if abs(curr.data - item) < abs( closet - item):
        closet=curr.data
      if curr.data > item:
        curr=curr.left
      elif curr.data < item:
        curr=curr.right
      else:
        return curr.data
    else:
      return closet
      
    
    

a=[1,2,3,4,7,8,9]
B=BST()

for i in B.main_BST(a):
   B.add(i)
print(B.searchItem(5))
