package progammers.java;

/*
 * https://school.programmers.co.kr/learn/courses/30/lessons/86491
 * 
 * 가로를 두 변중에서 가장 긴 부분으로, 세로를 두 변중에서 가장 작은 부분으로 설정
 * -> 처음부터 모든 명함을 제일 긴 부분으로 눕혀서 계산
 */

import java.util.Arrays;

class MinimumRectangle {
    public static int solution(int[][] sizes) {
        int maxWidth = Arrays.stream(sizes)
                        .mapToInt(size -> Math.max(size[0], size[1]))
                        .max()
                        .getAsInt();

        int maxHeight = Arrays.stream(sizes)
                        .mapToInt(size -> Math.min(size[0], size[1]))
                        .max()
                        .getAsInt();
                        
        return maxWidth * maxHeight;
    }

    public static void main(String[] args) {
        int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
        System.out.println(solution(sizes));
    }
}