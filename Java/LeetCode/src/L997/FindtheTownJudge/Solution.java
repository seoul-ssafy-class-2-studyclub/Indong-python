package L997.FindtheTownJudge;

public class Solution {
	public static void main(String[] args) {
		int N = 2;
		int[][] trust = new int[][] {{1, 2}};
		boolean[] to = new boolean[N+1];
		int[] from = new int[N+1];
		
		for (int[] info : trust) {
			int firstPerson = info[0];
			int secondPerson = info[1];
			to[firstPerson] = true;
			from[secondPerson] += 1;
		}
		
		int ans = -1;
		for (int i = 1; i < N + 1; i++) {
			if (!to[i] && from[i] == N - 1) {
				ans = i;
				break;
			}	
		}	
		System.out.println(ans);
		
	}
}
