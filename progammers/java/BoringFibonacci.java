package progammers.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * https://www.acmicpc.net/problem/17175
 * 
 * dp [n] = 1 + dp [n-1] + dp [n-2]
 */

 public class BoringFibonacci {
    private static long fibonacci(int n) {
        long[] dp = new long[51];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = (1 + dp[i-1] + dp[i-2]) % 1000000007;
        }
        return dp[n];
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print(fibonacci(Integer.parseInt(br.readLine())));
    }
}
