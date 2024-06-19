class stack:
  def __init__(self):
    self.m_list=[]
    self.output=""

  def push(self,item):
    if len(self.m_list)!=100:
       self.m_list.append(item)
    return

  def pop(self):
    if not self.isEmpty():
      return self.m_list.pop()
    return None

  def isEmpty(self)->bool:
    return len(self.m_list)==0

  def top(self):
    if not self.isEmpty():
      return self.m_list[-1]
    return ""

  def priorty(self,chr)->int:
    if chr== "+"or chr== "-":
      return 1
    elif chr=="*"or chr=="/":
      return 2
    elif chr=="^":
      return 3
    else:
      return 0

  def main(self):
    infix_ex=input("Enter the infix expression: ").strip()
    for chr in infix_ex:
      if chr==" ":
        continue
      if chr.isalpha()or chr.isdigit():
        self.output+=chr
        
      elif chr=="(":
        self.push(chr)
        
      elif chr==")":
        while self.top()!="(":
          self.output+=self.top()
          self.pop()
        self.pop()
      else:
        while not self.isEmpty()and self.priorty(self.top())>=self.priorty(chr):
          self.output+=self.top()
          self.pop()
        self.push(chr)
    while not self.isEmpty():
      self.output+=self.top()
      self.pop()
    return self.output
      
        

m_stack=stack()
print(m_stack.main())

        
        
        
    





  #if the stack is not empty pop whole items from the stack to the output

  #print output