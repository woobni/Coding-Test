package progammers.java;

/* 
- https://school.programmers.co.kr/learn/courses/30/lessons/42626
- 힙(Heap)은 우선순위 큐를 위해 고안된 완전이진트리 형태의 자료구조
- 여러 개의 값 중 최댓값 또는 최솟값을 찾아내는 연산이 빠르다
- 우선순위 큐를 힙이 아니라 배열 또는 연결리스트를 이용하여 구현할 수도 있다.
- 하지만 배열과 연결리스트는 선형 구조의 자료구조이므로 삽입 또는 삭제 연산을 위한 시간복잡도는 O(n)이다.
- 반면 힙 트리는 완전이진트리 구조이므로 힙트리의 높이는 log₂(n+1)이며, 힙의 시간복잡도는 O(log₂n)이다.
*/

import java.util.PriorityQueue;

public class MoreSpicy {
    public static int solution(int[] scoville, int K) {
        int answer = 0;

        // 가장 맵지 않은 스코빌 지수 = 루트 노드 -> min heap
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();

        for (int s : scoville) {
            priorityQueue.add(s);
        }

        while(priorityQueue.peek() < K) {
            if (priorityQueue.size() == 1)
                return -1;

            priorityQueue.add(
                    priorityQueue.poll() + priorityQueue.poll() * 2
                );

            answer++;
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;

        System.out.println(solution(scoville, K));
    }
}
