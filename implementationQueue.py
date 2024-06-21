



#make class and name it Queue
class Queue:
  #make initlaize to queue and rare point and front point
  def __init__(self):
    #create list with its size and has None values
    self.queue=[None]*10
    #make two point rare anf m_front same value as begenning==-1
    self.rare=-1
    self.m_front=-1
    
  def Enqueue(self,item):
    """  thisfunction to update the elemnte in queue into items from the user
"""
    #befor to add element to queue make condition for its full or not
    if self.isFull():
      return
    #make anothe condition to find out if the list is empty or not
    elif self.isEmpty():
      #if the condition is successed let the rare and m_front ==0 to enter frist
      #item in the queue
      self.m_front=self.rare=0
    else:
      #that mean there are more elements to add
      self.rare+=1
    #make update to the queue
    self.queue[self.rare]=item
    
  def Dequeue(self):
    """it is in charge to get rid of the front item """
    #make condition to find out the queue is empty or not
    if self.isEmpty():
      return
    #make condition if the queue has one element make rare and m_front==-1
    elif self.m_front==self.rare:
      self.m_front=self.rare=-1
    else:
      #update m_front to get a new element
      self.m_front+=1
   
  def isEmpty(self):
    """It is in charge to finde out the queue is empty or not"""
    #make condition if the m_front and rare are same ==-1 which mean is empty
    if self.m_front==-1 and self.rare==-1:
      return True
    return False

  def isFull(self):
    """It is in charge to finde out the queue is full or not"""
    #make condition to find out if the point rare chieves to the end of queue
    if self.rare==len(self.queue)-1:
      return True
    return False

  def front(self):
    """It is in charge to show you the first front item"""
    if not self.isEmpty() :
      #show the user the element by using m_front
      return self.queue[self.m_front]
    return None
Q=Queue()
name="karamAlrasamSVDO"
# print(Q.front())
for i in name :
  Q.Enqueue(i)
while not Q.isEmpty():
  print(Q.front())
  Q.Dequeue()



