package progammers.java;

import java.util.ArrayList;
import java.util.Arrays;

/*
 * https://school.programmers.co.kr/learn/courses/30/lessons/42840
 * 
 * 각 수포자의 찍는 패턴에서 정답 문자열이 만들어 질 수 있는지 체크
 */

public class GiveUpOnMath {
    public static int[] solution(int[] answers) {
        int[][] patterns = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };

        int[] scores = new int[patterns.length];
        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < patterns.length; j++) {
                if (answers[i] == patterns[j][i % patterns[j].length]) {
                    scores[j]++;
                }
            }
        }

        int maxScore = Arrays.stream(scores).max().orElse(0);

        ArrayList<Integer> winnersList = new ArrayList<>();
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == maxScore) {
                winnersList.add(i + 1);
            }
        }

        return winnersList.stream()
                          .mapToInt(Integer::intValue)
                          .toArray();
    }

    public static void main(String[] args) {
        int[] result1 = solution(new int[]{1, 2, 3, 4, 5});
        for (int num : result1) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        int[] result2 = solution(new int[]{1, 3, 2, 4, 2});
        for (int num : result2) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
