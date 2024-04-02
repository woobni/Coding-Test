package progammers.java;

/*
- https://school.programmers.co.kr/learn/courses/30/lessons/87946
- DFS로 모든 경우의 수 탐색
*/

class Dungeons {
    private static int answer = 0; // 최대 던전 수
    private static boolean[] visited; 
    
    public static int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        
        dfs(0, k, dungeons);
    
        return answer;
    }
    
    private static void dfs(int depth, int k, int[][] dungeons) {
        for (int i = 0; i < dungeons.length; i++) {
            // 방문하지 않은 상태면서 k가 최소 필요 피로도보다 크거나 같은 경우
            if (!visited[i] && dungeons[i][0] <= k) {
                visited[i] = true; 
                dfs(depth + 1, k - dungeons[i][1], dungeons); 
                visited[i] = false; 
            }
        }
        
        answer = Math.max(answer, depth);
    }

    public static void main(String[] args) {
        int k = 80;
        int[][] dungeons = {{80, 20}, {50, 40}, {30, 10}};

        System.out.println(solution(k, dungeons));
    }
}