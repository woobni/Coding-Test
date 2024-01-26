package progammers.java;

/*
 - 하드디스크가 작업을 수행하고 있을 때 들어온 요청들에 대해 소요시간이 적은 것부터 처리해야 대기 시간이 줄어듦 
 - But, 하나의 작업이 끝나는 시점까지 들어온 요청에 대해서 가장 짧은 수행시간을 가진 작업을 선택해야 함
 - 원본 배열(jobs)이 요청 시간 순서대로 들어온다는 말이 없음. 여러 시간대의 요청이 무작위로 섞여 있을 수 있음
*/

import java.util.Arrays;
import java.util.PriorityQueue;

public class DiskController {
    public static int solution(int[][] jobs) {
        int answer = 0;
        int t = 0;
        int idx = 0;
        int len = jobs.length;
        
        // 요청 시간 기준 오름차순
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]); 
        // Arrays.sort(jobs, new Comparator<int[]>() {
        //     @Override
        //     public int compare(int[] o1, int[] o2) {
        //         return o1[0] - o2[0]; 
        //     }
        // });
        
        // 소요 시간 기준 오름차순
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
                                                (o1, o2) -> o1[1] - o2[1]
                                            );

        while (!minHeap.isEmpty() || idx < len) {
            // 현재 시간 보다 작거나 같은 요청시점을 큐에 추가
            for (; idx < len && jobs[idx][0] <= t; idx++) {
                minHeap.offer(jobs[idx]);
            }

            if (minHeap.isEmpty()) {
                // 작업 요청 시점이 가장 빠른 작업 추가
                t = jobs[idx][0];

            } else {
                // 작업 소요 시간이 가장 빠른 작업 수행
                int[] job = minHeap.poll();
                t += job[1];
                answer += t - job[0];
            }            
        }
     
        return answer / len;
    }

    public static void main(String[] args) {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};

        System.out.println(solution(jobs));
    } 
}
