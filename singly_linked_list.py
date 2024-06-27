class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

class LinkList:
  def __init__(self):
    self.head=None

  def m_append(self, data):
    new_node=Node(data)
    if not self.head:
      self.head=new_node
      return
    lasted_node=self.head
    while lasted_node.next:
      lasted_node=lasted_node.next
    lasted_node.next=new_node

  def m_display(self):
    current_node=self.head
    while current_node:
      print(current_node.data,end=" -> ")
      current_node=current_node.next
    
    print(None)

  def m_remove(self, data):
    if not self.head:
      return
    if self.head.data==data:
      self.head=self.head.next
      return
    current_node=self.head
    while current_node.next and current_node.next.data!=data:
      current_node=current_node.next
    if current_node.next:
      current_node.next=current_node.next.next

  def m_insert(self, data, pos):
    new_node=Node(data)
    if pos==0:
      new_node.next=self.head
      self.head=new_node
      return
    lasted_node=self.head
    for _ in range(pos-1):
      if lasted_node.next==None:
        break
      lasted_node=lasted_node.next
    new_node.next=lasted_node.next
    lasted_node.next=new_node

  def m_reverse(self):
    if not self.head:
      return
    prev=None
    curr=self.head
    next=None

    while curr:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.head=prev

  def m_remove2(self, pos:int):
    if not self.head:
      return
    if pos==0:
      self.head=self.head.next
      return
    lasted_node=self.head
    for _ in range(pos-1):
      if lasted_node.next==None:
        break
      lasted_node=lasted_node.next
    if lasted_node.next:
      lasted_node.next=lasted_node.next.next
    
      

L=LinkList()
for i in range(7):
  L.m_append(i)
L.m_display()
L.m_remove(6)
L.m_display()
L.m_insert(6,6)
L.m_display()
L.m_reverse()
L.m_display()
L.m_reverse()
L.m_display()
L.m_remove2(2)
L.m_display()
