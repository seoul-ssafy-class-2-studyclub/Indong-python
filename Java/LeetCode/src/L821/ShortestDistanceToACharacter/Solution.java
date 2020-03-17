package L821.ShortestDistanceToACharacter;

import java.util.Arrays;

public class Solution {
	static String S = "baaba";
	static char C = 'b';
	static int[] result = new int[S.length()];
	public static void back(int prev, int now, boolean flag) {
		System.out.println(prev);
		System.out.println(now);
		int count = 0;
		for (int i = now; prev < i; i--) {
			if (result[i] == 0 || result[i] > count) {
				result[i] = count++;
			}
		}
		if (!flag) {
			result[0] = count;
		}
	}
	
	
	public static void main(String[] args) {
		int len = S.length();
		int count = 0;
		int prev = 0;
		boolean flag = false;
		for (int i = 0; i < len; i++) {
			if (S.charAt(i) == C) {
				back(prev, i, flag);
				prev = i;
				count = 0;
				flag = true;
			}
			if (flag) {
				result[i] = count++;				
			}
		}
		System.out.println(Arrays.toString(result));
		
	}

}
