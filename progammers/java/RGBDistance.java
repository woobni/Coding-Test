package progammers.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * https://www.acmicpc.net/problem/1149
 * 
 * RED:   COST[N][0] = min( COST[N-1][1], COST[N-1][2] ) + COST[N][0]
 * GREEN: COST[N][1] = min( COST[N-1][0], COST[N-1][2] ) + COST[N][1]
 * BLUE:  COST[N][2] = min( COST[N-1][0], COST[N-1][1] ) + COST[N][2]
 */

public class RGBDistance {
	final static int RED = 0;
	final static int GREEN = 1;
	final static int BLUE = 2;
	
	static int[][] COST;
	static int[][] DP;

    private static int calculateCost(int N, int color) {
		if(DP[N][color] == 0) { // 만약 탐색하지 않은 배열이라면
			if(color == RED) {
				DP[N][RED] = Math.min(calculateCost(N - 1, GREEN), calculateCost(N - 1, BLUE)) + COST[N][RED];
			}
			else if(color == GREEN) {
				DP[N][GREEN] = Math.min(calculateCost(N - 1, RED), calculateCost(N - 1, BLUE)) + COST[N][GREEN];
			}
			else {
				DP[N][BLUE] = Math.min(calculateCost(N - 1, RED), calculateCost(N - 1, GREEN)) + COST[N][BLUE];
			}
		}
		return DP[N][color];
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		COST = new int[N][3];
		DP = new int[N][3];
		
		StringTokenizer st;
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " "); // BufferedReader는 문자열을 한 줄로 읽기 때문에
			
			COST[i][RED] = Integer.parseInt(st.nextToken());
			COST[i][GREEN] = Integer.parseInt(st.nextToken());
			COST[i][BLUE] = Integer.parseInt(st.nextToken());
		}
		
		// 각 색상비용의 첫번째 값으로 DP 테이블 초기화
		DP[0][RED] = COST[0][RED];
		DP[0][GREEN] = COST[0][GREEN];
		DP[0][BLUE] = COST[0][BLUE];
		
		System.out.println(Math.min(calculateCost(N - 1, RED), Math.min(calculateCost(N - 1, GREEN), calculateCost(N - 1, BLUE))));
	}
}
