package L874.WalkingRobotSimulation;

import java.util.HashSet;

public class Solution {
	public static void main(String[] args) {
		
		HashSet<Long> obstaclesSet = new HashSet<Long>();
		int[] commands = {4, -1, 4, -2, 4};
		int[][] obstacles = {{2, 4}};
		for(int[] idx : obstacles) {
			long ox = idx[0] + 30000;
			long oy = idx[1] + 30000;
			obstaclesSet.add((ox << 16) + oy);
		}
		int x = 0, y = 0;
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
//		0 - north, 1 - east, 2 - south, 3 - west
		int dir = 0;
		int result = 0;
		for(int comm : commands) {
			if(comm == -1) {
				dir = (dir + 1) % 4;
			} else if (comm == -2) {
				dir = (dir + 3) % 4;
			} else {
				for (int k = 0; k < comm; ++k) {
					System.out.println(k);
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    long code = (((long) nx + 30000) << 16) + ((long) ny + 30000);
                    if (!obstaclesSet.contains(code)) {
                        x = nx;
                        y = ny;
                        result = Math.max(result, (x * x) + (y * y));
                    }
                }
			}
		}
		System.out.println(result);
	}

}
