package L746.MinCostClimbingStairs;


public class Solution {
	public static void main(String[] args) {
		int[] cost = {10, 15, 20};
		int size = cost.length;
		int[] dp = new int[size];
		for(int i = size - 1; i >= 0; i--) {
			if(i == size - 1 || i == size - 2) {
				dp[i] = cost[i]; 
			} else {
				dp[i] = Math.min(cost[i] + dp[i+1], cost[i] + dp[i+2]);
			}
		}
		
		int result = Math.min(dp[0], dp[1]);
		System.out.println(result);
	}

}
