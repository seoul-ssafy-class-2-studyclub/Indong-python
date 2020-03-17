package L209.MinimumSizeSubarraySum;

public class Solution {
	public static int minSubArrayLen(int s, int[] nums) {
		int len = nums.length;
		int answer = len;
		int[] subtotal = new int[len + 1];
		int[] size = new int[len + 1];
		
        for (int i = 1; i < len + 1; i++) {
        	subtotal[i] = subtotal[i-1] + nums[i-1];
        	size[i] = size[i-1] + 1;
        	while (size[i] >= 1 && subtotal[i] - nums[i-size[i]] >= s) {
        		subtotal[i] -= nums[i-size[i]--];
        	}
        	if (subtotal[i] >= s) {
        		answer = Math.min(size[i], answer);
        	}
        }
        return answer;
    }

	public static void main(String[] args) {
	    int s = 7;
	    int[] nums = {};
	    System.out.println(minSubArrayLen(s, nums));
	}
}
