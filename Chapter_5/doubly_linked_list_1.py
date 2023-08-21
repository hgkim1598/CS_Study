class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class NodeMgmt:
  def __init__(self, data): # head -> Node(1 ,None, None) <- tail
    self.head = Node(data) # head는 다음 노드를 가르키고
    self.tail = self.head # tail은 이전 노드를 가르킴

  def insert(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.head # 해당 노드를 가져와서 기준으로 함
      while node.next: # 해당 노드의 다음 노드가 있으면 다음 노드를 기준으로 함
        node = node.next # 결국엔 node가 tail 전 노드로 마지막 노드를 가르킴
      new = Node(data) # 새로운 노드를 new에 기억함
      node.next = new # 해당 노드의 next에 새로운 노드를 가르키게 함
      new.prev = node # 새로운 노드의 prev의 기준 노드를 가르키게 함
      self.tail = new # tail 새로운 노드를 가르키게 함

  # prev, next는 노드 전체를 가르킨다! 다음 또는 전 노드의 prev, next가 아니라

  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

  def search_from_head(self, data):
    if self.head == None: # 방어 코드
      return False

    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next
    return False

  def search_from_tail(self, data):
    if self.tail == None: # 방어 코드
      return False

    node = self.tail
    while node:
      if node.data == data:
        return node
      else:
        node = node.prev
    return False

# 첫번째 매개변수가 새로운 Node 만들때 쓰는 값
# 두번째 매개변수가 노드 찾을 때 쓰는 값

  def insert_before(self, data, before_data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.tail
      while node.data != before_data:
        node = node.prev
        if node == None:
          return False
      new = Node(data)
      before_new = node.prev
      if before_new != None: # 제일 첫번째 노드를 기준으로 추가하는 경우
        before_new.next = new
        new.prev = before_new
      else:
        self.head = new
        new.prev = self.head
      new.next = node
      node.prev = new
      return True

  def insert_after(self, data, after_data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.head
      while node.data != after_data:
        node = node.next
        if node == None:
          return False
      new = Node(data)
      after_new = node.next
      new.next = after_new
      new.prev = node
      node.next = new
      if new.next == None: # 마지막 노드를 기준으로 추가하는 경우
        self.tail = new
      return True

# 반복문을 사용할 때는 해당 노드를 찾는 용도로 사용하고, 수정하는 작업은 반복문 나와서 다음에 작업 하는 걸로 해야 변함

"""
참고: https://goforit.tistory.com/145
"""