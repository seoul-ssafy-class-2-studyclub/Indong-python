package L338.CountingBits;

import java.util.Arrays;

public class Solution {
	public int[] countBits(int num) {
	    int[] answer = new int[num+1];
	    if (num >= 1) {
	    	answer[1] = 1;
	    	if (num == 1) {
	    		return answer;
	    	}
	    	int x = 0;
	    	int n = 0;
	    	int m = 1;
		    for (int i = 2; i < num + 1; i++) {
		    	if (i == m * 2) {
		    		n = m;
		    		m = (int) Math.pow(2, ++x);
		    	}
		    	if (i >= m && i < n + m) {
		    		answer[i] = answer[i-n];
		    	} else {
		    		answer[i] = answer[i-n] + 1; 
		    	}
		    	System.out.println("i: " + i + " x: " + x + " n: " + n + " m: " + m);
		    }
	    }
	    
	    return answer;
	}
	public static void main(String[] args) {
		System.out.println(Arrays.toString(new Solution().countBits(15)));
	}

}
