package L747.LargestNumberAtLeastTwiceofOthers;

public class Solution {
	public static void main(String[] args) {
		int[] nums = {0, 0, 3, 2};
		int maxNum = 0;
		int secondNum = 0;
		int result = 0;
		for(int i = 0; i < nums.length; i++) {
			if(nums[i] > secondNum && nums[i] <= maxNum) {
				secondNum = nums[i];
			} else if(nums[i] > maxNum) {
				secondNum = maxNum;
				maxNum = nums[i];
				result = i;
			}
		}

		if(maxNum >= secondNum * 2) {
			System.out.println(result);
		} else {
			System.out.println(-1);
		}
	}

}
