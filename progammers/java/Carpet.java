package progammers.java;

import java.util.Arrays;

/*
- https://school.programmers.co.kr/learn/courses/30/lessons/42842
- 카펫 넓이=brown*yello, 카펫 넓이의 경우의 수 찾기
- 경우의 수 중, w > h
- 경우의 수 중, 가운데에 노란색이 오려면 w, h >= 3
- 경우의 수 중, yello 개수만큼 가운데에 위치하려면 (w-2)*(h-2) = yello
*/

class Carpet {
    public static int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int area = brown + yellow;

        for (int i = 1; i <= Math.sqrt(area); i++) { // 세로 길이로 Math.sqrt(area)까지만 반복
            if (area % i == 0) {
                int j = area / i;
                if ((i - 2) * (j - 2) == yellow) {
                    answer[0] = j;
                    answer[1] = i;
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int brown = 10;
        int yellow = 2;

        System.out.println(Arrays.toString(solution(brown, yellow)));
    } 
}

// public static int[] solution(int brown, int yellow) {
//     int[] answer = new int[2];
//     int area = brown + yellow; // 20
    
//     for (int i = 3; i < area; i++) { // 4, 5, ...
//         int j = area / i;
        
//         if (area % i == 0 && j >= 3) {
//             int width = Math.max(i, j);
//             int height = Math.min(i, j);
            
//             if ((width - 2) * (height - 2) == yellow) {
//                 answer[0] = width;
//                 answer[1] = height;
//                 break;
//             }
//         }
//     }
//     return answer;
// }