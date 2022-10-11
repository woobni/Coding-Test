import java.util.*;

public class indecisiveness {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int[] visited = new int[100001]; // 기본 타입으로 배열 선언시 초기값은 0
		int n = sc.nextInt();
		int sum = 0;
		int max = 0;
        
		for(int i = 1; i<= n*2;i++)
		{
			int arr = sc.nextInt();
			if(visited[arr] == 0)
			{
				sum++;
				visited[arr]++;
			}
			else
				sum--;
                
			if(sum > max)
				max = sum;
		}
		System.out.println(max);
    }
}