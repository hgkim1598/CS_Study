#Node 정의
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next


#Node 생성해보기(data = 1)
node1 = Node(1)

#Node의 값과 포인터 출력하기
print(node1.data)
print(node1.next)

#Node1 생성해보기
node1 = Node(1)
#Node2 생성해보기
node2 = Node(3)
#Node 연결하기
node1.next = node2
#가장 맨 앞 Node를 알기 위해 head 지정
head = node1

#node1을 통해 연결한 결과 확인(밑에 2줄은 동일한 결과를 가리킨다)
print(node1.next.data)
print(node2.data)

#Node 정의
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next

def add(data):
    node = head
    while node.next: #node의 next가 있을 경우만 실행
        node = node.next #다음 노드가 있는지 계속 반복
    node.next = Node(data) #다음 노드가 없을 경우 루프를 빠져나와 새로운 노드 생성

#Node1 생성해보기
node1 = Node(1)
#가장 맨 앞 Node를 알기 위해 head 지정
head = node1
#add 함수 통해 신규 노드 추가하기
add(3)
#추가한 값을 node1 통해 next로 출력해보기
print(node1.next.data)

#Node1 생성해보기
node1 = Node(1)
#가장 맨 앞 Node를 알기 위해 head 지정
head = node1
#add 함수 통해 신규 노드 추가하기
add(3)
add(4)
add(5)

#추가한 값을 node1 통해 next로 출력해보기
node = head
while node.next: #node.next =None이 아닐 경우. 즉, node의 next가 있는 경우 실행
    print(node.data)
    node=node.next #node의 next가 없을 때까지 반복
print(node.data)