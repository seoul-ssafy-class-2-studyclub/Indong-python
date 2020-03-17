package L650.TwoKeysKeyboard;

public class Solution {
	public int minSteps(int n) {
	    int answer = 0;
	    
		while (n != 1) {
			for (int i = 2; i <= n; i++) {
				if (n % i == 0) {
					answer += i;
					n /= i;
					break;
				}
			}
		}
		return answer;
    }
	public static void main(String[] args) {
		System.out.println(new Solution().minSteps(20));
	}

}
