package L435.NonOverlappingIntervals;

import java.util.Arrays;
import java.util.Comparator;

public class Solution {
	public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
        	@Override
        	public int compare(int[] o1, int[] o2) {
        		if (o1[0] == o2[0]) {
        			return o1[1] - o2[1];
        		}
        		return o1[0] - o2[0];
        	}
        });
        int answer = 0;
        int end = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
        	if (intervals[i][0] < end) {
        		answer++;
        		continue;
        	}
        	end = intervals[i][1];
        }
        return answer;
    }
	
	public static void main(String[] args) {
		
	}

}
