class stack:
  def __init__(self):
    self.m_list=[]
    
  def push(self,item):
    if len(self.m_list)!=100:
       self.m_list+=[item]
    return

  def pop(self):
    if not self.isEmpty():
      del self.m_list[-1]
    return 

  def isEmpty(self)->bool:
    if len(self.m_list)==0:
      return True
    return False

  def top(self):
    if not self.isEmpty():
      return self.m_list[-1]

  def check_kind_bracket(self, open_b:str):
    if open_b in ("(","{","["):
      self.push(open_b)
    elif open_b in (")","]","}"):
      if self.isEmpty():
        return False
      
      if (self.top()=="("and open_b==")")or(self.top()=="{"and open_b=="}")or(self.top()=="["and open_b=="]"):
        self.pop()
      else:
        return False
    return True
          
        
  def main(self):
    user=input("Enter brackets saperated with spaces: ").split()
    for brackt in user:
      if not self.check_kind_bracket(brackt):
        print("Brackts are not coordinated")
        return
    if self.isEmpty():
      print("Congragelation all brackets are coordinated")
    else:
      print("Brackts are not coordinated")

stak=stack()
stak.main()
