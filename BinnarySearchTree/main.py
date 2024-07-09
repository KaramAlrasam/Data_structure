import m_queue
class Node:
  def __init__(self, data):
    self.data=data
    self.right=None
    self.left=None

class BST:
  def __init__(self):
    self.root=None

  def add(self, data):
    new_node=Node(data)
    if self.root==None:
      self.root=new_node
      return self.root.data
    temp=self.root
    parent=None
    while temp!=None:
      parent=temp
      if temp.data<=data:
        temp=temp.right
      else:
        temp=temp.left
    if parent.data<=data:
      parent.right=new_node
    else:
      parent.left=new_node
    return parent.data

  def delete(self, data):
    def helperDelete(node, data):
      if node==None:
        return node
      if node.data<data:
        node.right=helperDelete(node.right, data)
      elif node.data>data:
        node.left=helperDelete(node.left, data)
      else:
        if node.left==None and node.right==None:
          return None
        if node.left==None:
          return node.right
        if node.right==None:
          return node.left
        m_copy=self._minTree(node.right)
        node.data=m_copy.data
        node.right=helperDelete(node.right, m_copy.data)
      return node
    helperDelete(self.root, data)
  def _maxTree(self, node):
    curr=node
    while curr.right!=None:
      curr=curr.right
    return curr

  def _minTree(self, node):
    curr=node
    while curr.left!=None:
      curr=curr.left
    return curr

  def hightTree(self, node):
    def helperHightTree(node):
      if node==None:
        return -1
      subTreeL=helperHightTree(node.left)
      subTreeR=helperHightTree(node.right)
      return 1+max(subTreeL, subTreeR)

    if node==None:
      return -1
    else:
      return helperHightTree(node)

  def displayBLO(self):
    if self.root==None:
      return 
    Q=m_queue.CQ(100)
    Q.Enqueue(self.root)
    while not Q.isEmpty():
      curr=Q.displayFrontValue()
      print(curr.data, end=" ")
      Q.Dequeue()
      if curr.left!=None:
        Q.Enqueue(curr.left)
      if curr.right!=None:
        Q.Enqueue(curr.right)
    print()
  def displayTraversal(self):
    def helperdisplay(node):
      if node==None:
        return
      helperdisplay(node.left)
      print(node.data, end=" ")
      helperdisplay(node.right)

    if self.root==None:
      return
    else:
      print()
      helperdisplay(self.root)

if __name__=="__main__":
  m_BST=BST()
  m_BST.add(10)
  m_BST.add(27)
  m_BST.add(8)
  m_BST.add(7)
  m_BST.add(30)
  m_BST.add(39)
  m_BST.add(33)
  m_BST.add(50)
  m_BST.add(0)
  m_BST.add(13)
  m_BST.displayBLO()

  m_BST.displayTraversal() 
  m_BST.delete(13)
  m_BST.displayTraversal() 
