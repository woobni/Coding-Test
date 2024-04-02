package progammers.java;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/*
- https://school.programmers.co.kr/learn/courses/30/lessons/86971
- 선 하나씩 끊어보며 나눠진 두 전력망 송전탑 개수 차이를 구함
- bfs를 이용하여 끊어진 선의 두 노드 중 하나를 선택하여 연결된 송전탑의 개수를 구함
- 전체 노드 개수를 알고 있으니, 한 쪽 그룹의 개수를 구하면 다른 한 쪽을 알음(n-cnt)
- 가능한 비슷하도록 두 전력망으로 나누려면 송전탑 개수 차이가 적어야 함(min)
*/

class DivideWires {
    public int solution(int n, int[][] wires) {
        int answer = n; // 송전탑 개수의 차이
        int[][] arr= new int[n+1][n+1]; // 인접 행렬 1부터 시작(0 안씀)
        
        // 1. 인접행렬
        Arrays.stream(wires)
              .forEach(wire -> {
                    arr[wire[0]][wire[1]] = 1;
                    arr[wire[1]][wire[0]] = 1;
                });
        
        // 2. 선을 하나씩 끊어보며 순회
        for (int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];

            // 선 하나 끊기
            arr[a][b] = 0;
            arr[b][a] = 0;

            // bfs, 가능한 비슷하도록 두 전력망으로 나누려면 min
            answer = Math.min(answer, bfs(n, a, arr));

            // 선 복구
            arr[a][b] = 1;
            arr[b][a] = 1;
        }
        
        return answer;
    }
    
    private int bfs(int n, int start, int[][] arr) {
        boolean[] visited = new boolean[n + 1];
        int cnt = 1;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            int currentVertex = queue.poll();
            visited[currentVertex] = true;

            for (int i = 1; i <= n; i++) {
                if (visited[i])
                    continue;

                if (arr[currentVertex][i] == 1) {
                    queue.offer(i);
                    cnt++;
                }
            }
        }
        return Math.abs(n - 2 * cnt); // cnt-(n-cnt);
    }

    public static void main(String[] args) {
        DivideWires divideWires = new DivideWires();

        int n = 9;
        int[][] wires = {{1, 3}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {4, 7}, {7, 8}, {7, 9}};

        System.out.println("Result: " + divideWires.solution(n, wires)); 
    }
}