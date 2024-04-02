package progammers.java;

/*
- https://school.programmers.co.kr/learn/courses/30/lessons/43165
- 현재 노드 값을 더하고 빼는 두 가지 경우로 dfs 수행
*/

class TargetNumber {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, 0, target, 0);
    }

    private int dfs(int[] numbers, int depth, int target, int sum){
        if(depth == numbers.length){
            return sum == target ? 1 : 0;
        } else {
            int count = 0;
            count += dfs(numbers, depth + 1, target, sum + numbers[depth]);
            count += dfs(numbers, depth + 1, target, sum - numbers[depth]);
            return count;
        }
    }

    public static void main(String[] args) {
        TargetNumber targetNumber = new TargetNumber();
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println("Result: " + targetNumber.solution(numbers, target));
    }
}