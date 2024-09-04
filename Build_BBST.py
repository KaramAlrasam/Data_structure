class Node:
  def __init__(self, data):
    self.data=data
    self.right=None
    self.left=None

class BST:
  def __init__(self):
    self.root=None

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
      print(new_node.data)
      self.preOrder(new_node.left)
      self.preOrder(new_node.right)
      

  def main_BST(self, m_list):
    result=self.Build_BT(m_list)
    self.preOrder(result)

a=[1,2,3,4,5,6,7,8,9]
B=BST()
B.main_BST(a)
