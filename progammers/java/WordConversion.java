package progammers.java;

/*
- https://school.programmers.co.kr/learn/courses/30/lessons/43163
- 한 번에 한 개의 알파벳만 바꿀 수 있는 조건을 확인. dfs 수행
*/

public class WordConversion {
    boolean[] visited;
    int answer = 0;

    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];

        dfs(begin, target, words, 0);

        return answer;
    }

    public void dfs(String currentWord, String target, String[] words, int cnt) {
        if(currentWord.equals(target)) {
            answer = cnt;
            return;
        }

        for (int i=0; i<words.length; i++) {
            if(visited[i]) 
                continue;

            int k=0;
            for(int j=0; j<currentWord.length(); j++) {
                if (currentWord.charAt(j) != words[i].charAt(j)) {
                    k++;
                }
            }

            if(k==1) { // 알파벳 하나만 다를 시에만
                visited[i] = true;
                dfs(words[i], target, words, cnt+1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        WordConversion wordConversion = new WordConversion();
        String begin = "hit";
        String target = "cog";
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};

        System.out.println("Result: " + wordConversion.solution(begin,target,words));
    }
}
