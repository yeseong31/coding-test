# 해시맵 디자인 (291p)

import collections


# 키, 값, 포인터를 가지는 노드
class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 1000
        # 존재하지 않는 키를 조회할 경우 자동으로 default를 생성하도록 함
        self.table = collections.defaultdict(ListNode)

    # 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
    def put(self, key: int, value: int) -> None:
        idx = key % self.size

        # 해당 인덱스에 아무것도 없다면 키, 값을 삽입하고 종료
        if self.table[idx].value is None:   # value로 존재 유무를 판단한 이유는 table이 defaultdict 객체이기 때문
            self.table[idx] = ListNode(key, value)
            return

        # 해당 인덱스에 노드가 존재한다면... 즉 '해시 충돌'이 일어났다면 '개별 체이닝' 방식으로 충돌을 해결할 것임
        p = self.table[idx]
        while p:
            # 종료 조건 1: 이미 키가 존재할 경우에는 값을 업데이트하고 빠져나옴
            if p.key == key:
                p.value = value
                return
            # 종료 조건 2: p.next가 None이라면 아무것도 하지 않고 루프를 빠져나옴
            if p.next is None:
                break
            p = p.next

        # while 문을 빠져나오면 맨 끝에 새로 추가된 노드를 연결
        p.next = ListNode(key, value)

    # 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
    def get(self, key: int) -> int:
        idx = key % self.size
        if self.table[idx].value is None:
            return -1
        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 키에 해당하는 키, 값을 해시맵에서 삭제한다.
    def remove(self, key: int) -> None:
        idx = key % self.size
        if self.table[idx].value is None:
            return

        # 삭제 1: 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[idx]
        if p.key == key:
            self.table[idx] = ListNode() if p.next is None else p.next
            return
        # 삭제 2: 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)