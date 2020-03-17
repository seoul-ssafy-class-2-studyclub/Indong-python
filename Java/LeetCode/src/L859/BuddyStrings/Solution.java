package L859.BuddyStrings;

public class Solution {
	public boolean buddyStrings(String A, String B) {
		if(A.length() != B.length()) {
			return false;
		}
		if(A.equals(B)) {
			int[] chk = new int[26];
			for(int i = 0; i < A.length(); i++) {
				int idx = A.charAt(i) - 'a';
				chk[idx] += 1;
				if(chk[idx] > 1) {
					return true;
				}
			}
			return false;
	    } else {
	    	int first = -1, second = -1;
	    	for(int i = 0; i < A.length(); i++) {
	    		if(A.charAt(i) != B.charAt(i)) {
	    			if(first == -1) {
	    				first = i;
	    			} else if (second == -1) {
	    				second = i;
	    			} else {
	    				return false;
	    			}
	    		}
	    	}
	    	return (second != -1 && A.charAt(first) == B.charAt(second) && A.charAt(second) == B.charAt(first));
	    }
	}
	
	
	public static void main(String[] args) {
		String A = "abc", B = "acb";
		System.out.println(new Solution().buddyStrings(A, B));
	}

}
