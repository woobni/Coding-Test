package progammers.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * https://www.acmicpc.net/problem/15486
 * 
 * 각 일에 받을 수 있는 최대 금액을 DP 테이블에 저장
 * nxt = n + Tn -> dp[nxt] = Math.max( dp[nxt], dp[n] + Pn ) 
 */

 public class Resignation2 {
    private static int calculateMaxProfit(int n, int[][] arr, int[] dp) {
        int max = -1;
        for (int i = 1; i <= n + 1; i++) {
            if (max < dp[i]) {
                max = dp[i];
            }

            int nxt = i + arr[i][0];
            if (nxt < n + 2) {
                dp[nxt] = Math.max(dp[nxt], max + arr[i][1]);
            }
        }
        return dp[n + 1];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = null;

        // N+1일째 되는 날에 퇴사하므로 마지막 날에도 하루 일할 수 있음 -> 1 ~ n+2
        int[][] arr = new int[n + 2][2]; 
        int[] dp = new int[n + 2];
        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());

            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            arr[i][0] = t; // 기간
            arr[i][1] = p; // 금액
        }

        System.out.println(calculateMaxProfit(n, arr, dp));
    }
}