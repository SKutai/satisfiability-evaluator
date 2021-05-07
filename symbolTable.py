class Error(Exception):
  pass

class InvalidValueException(Error):
  pass

class var:
  def __init__(self, name, value):
    try:
      self.name = name
      self.next = None
      if(type(value)==int and (value==0 or value==1)):
        self.value = value
      else:
        raise InvalidValueException
    except InvalidValueException:
      print("Invalid Value")

class symbolTable:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def add(self, name, value):
    newVar = var(name, value)
    if self.head == None:
      self.head = newVar
      self.tail = newVar
    else:
      self.tail.next = newVar
    self.size += 1

  def getVal(self, name):
    i=0
    sym = self.head
    while(sym.next != None):
      if sym.name == name:
        return sym.value
      else:
        sym = sym.next
    return None

  def purge(self):
    self.head = None
    self.tail = nulNonel
