from typing import List
from collections import deque

# 앵무새의 수 n 입력받기
n = int(input())

parrot = []
# 앵무새가 말한 문장 입력받아서 큐로 저장
for _ in range(n):
    parrot.append(deque(input().split())) 

def possible(sentence: List[str], parrot: List[deque]) -> bool :
    i = 0
    cnt = 0
    # sentence가 빌 때까지 반복해서 실제 문장의 단어가 있는지 확인
    while sentence:
        if parrot[i] and sentence[0] == parrot[i][0]:
            parrot[i].popleft()
            sentence.popleft()
            cnt = 0

        else: 
            if cnt == n: # 실제 문장의 단어가 세 앵무새의 큐에 없을 때
                return False
            cnt += 1
        
        i = (i + 1) % n # i = 0, 1, 2

    # while 문이 끝났다는 건 sentence가 다 pop돼서 비었다는 뜻
    # 앵무새가 모든 단어들을 다 말해야 하므로 각 앵무새의 큐가 비어있는지 확인
    empty = 0
    for j in range(n):
        if not parrot[j]:
            empty += 1
    
    if empty == n:
        return True
    else:
        return False


# 실제 문장 입력받기
sentence = deque(input().split())

if possible(sentence, parrot):
    print("Possible")
else:
    print("Impossible")