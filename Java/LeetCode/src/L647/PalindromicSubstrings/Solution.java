package L647.PalindromicSubstrings;


public class Solution {
	public int countSubstrings(String s) {
		int len = s.length();
//		boolean[][] dp = new boolean[len][len];
		int answer = 0;
//		
//		for (int i = 0; i < len; i++) {
//			for (int start = 0; start + i < len; start++) {
//				int end = start + i;
//				if (s.charAt(start) == s.charAt(end)) {
//					dp[start][end] = i < 3 ? true : dp[start+1][end-1];
//					answer++;
//				}
//			}
//		}
//		return answer;
		int front;
		int back;
		for (int i = 0; i < len; i++) {
			front = i;
			back = i;
			
			while (front >= 0 && back < len && s.charAt(front) == s.charAt(back)) {
				answer++;
				front--;
				back++;
			}
			
			front = i;
			back = i+1;
			
			while (front >= 0 && back < len && s.charAt(front) == s.charAt(back)) {
				answer++;
				front--;
				back++;
			}
		}
		
		return answer;
	}
	public static void main(String[] args) {
		System.out.println(new Solution().countSubstrings("abc"));
	}
}
