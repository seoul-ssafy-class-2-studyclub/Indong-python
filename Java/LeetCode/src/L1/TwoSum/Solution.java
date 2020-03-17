package L1.TwoSum;

import java.util.Arrays;

public class Solution {
	public static void main(String[] args) {
	    int[] nums = {3, 2, 4};
	    int target = 6;
	    int size = nums.length;
	    int[] result = null;
//	    System.out.println(size);
	    Arrays.sort(nums);
	    for(int i = 0; i < size - 1; i++) {
	    	int diff = target - nums[i];
	    	System.out.println(diff);
	    	int idx = Arrays.binarySearch(Arrays.copyOfRange(nums, i + 1, size), diff);
	    	if(idx >= 0) {
	    		
	    	}
	    }
//	    System.out.println(Arrays.toString(result));
	}

}
