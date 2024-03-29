from queue import PriorityQueue


class HuffNode:

    def __init__(self, symbol, freq):  # symbol 문자, freq 빈도수
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def preorder(self):
        print(self.freq, end=" ")
        if(self.left is not None):
            self.left.preorder()
        if(self.right is not None):
            self.right.preorder()

    def inorder(self):
        if(self.left is not None):
            self.left.inorder()
        print(self.freq, end=" ")
        if(self.right is not None):
            self.right.inorder()


def huffman(n, PQ):
    for _ in range(n-1):  # n개를 2개씩 비교하면 n-1번 비교함
        p = PQ.get()[1]
        q = PQ.get()[1]
        r = HuffNode(' ', p.freq + q.freq)  # 서브쿼리 만들기
        r.left = p  # 자식 노드 설정
        r.right = q
        PQ.put((r.freq, r))
    return PQ.get()[1]  # 마지막 노드 반환


codes = ['b', 'e', 'c', 'a', 'd', 'f']
freqs = [5, 10, 12, 16, 17, 25]


PQ = PriorityQueue()
for i in range(len(codes)):
    node = HuffNode(codes[i], freqs[i])
    PQ.put((node.freq, node))

root = huffman(len(codes), PQ)

print("Preorder:", end=" ")
root.preorder()
print("\nInorder:", end=" ")
root.inorder()
print()
