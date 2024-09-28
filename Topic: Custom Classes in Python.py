class Rectangle:
  def __init__(self, lenght, width):
    self.lenght = int(lenght);
    self.lenght = int(width);
  def __iter__(self):
    yield {'length': self.length}
    yield {'width': self.width}
  
