# 힙: '부모가 항상 자식보다 작거나 같다'라는 특성을 만족하는 거의 완전한 트리

class BinaryHeap(object):
    def __init__(self):
        self.items = [None]  # 0번 인덱스는 사용하지 않음

    def __len__(self):
        return len(self.items) - 1

    # 삽입 시 실행, 반복 구조로 구현
    def _percolate_up(self):
        # 맨 마지막 위치에서부터 부모와 비교해 나가며 위치 재설정
        i = len(self)
        parent = i // 2

        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 추출 시 실행, 재귀 구조로 구현
    def _percolate_down(self, idx):
        left = idx * 2
        right = left + 1
        smallest = idx

        # 자식 노드와 값 비교
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        # 자식 노드의 값이 더 작다면 교체 및 재귀적으로 반복
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
    
    def extract(self):
        # 루트 추출
        target = self.items[1]
        # 루트의 값을 맨 마지막 원소로 교체
        self.items[1] = self.items[len(self)]
        # 맨 마지막 원소 삭제
        self.items.pop()
        # 루트의 값을 자식과 비교해 나가며 위치 재설정
        self._percolate_down(1)
        return target

