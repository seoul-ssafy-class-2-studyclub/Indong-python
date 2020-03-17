package B1175.배달;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	public static final int[] DY = {-1, 0, 1, 0};
	public static final int[] DX = {0, 1, 0, -1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer rowAndCol = new StringTokenizer(br.readLine().trim());
		final int ROW = Integer.parseInt(rowAndCol.nextToken());
		final int COL = Integer.parseInt(rowAndCol.nextToken());
		char[][] classroom = new char[ROW][COL];
		boolean[][][][] vis = new boolean[ROW][COL][4][3];
		int sy = 0;
		int sx = 0;
		boolean flag = false;
		for(int i = 0; i < ROW; i++) {
			String row = br.readLine().trim();
			for(int j = 0; j < COL; j++) {
				char cur = row.charAt(j);
				classroom[i][j] = cur;
				if (cur == 'S') {
					sy = i;
					sx = j;
				} else if (cur == 'C' && !flag) {
					classroom[i][j] = 'D';
					flag = true;
				}
			}
		}
		
		int ans = 987654321;
		Queue<int[]> queue = new LinkedList<int[]>();
//			y좌표, x좌표, 방향, 어디 C 갔는지, 시간
		queue.offer(new int[] {sy, sx, 0, 0, 0});
		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			for(int d = 0; d < 4; d++) {
				if (d == cur[2] && cur[4] > 0) {
					continue;
				}
				int ny = cur[0] + DY[d];
				int nx = cur[1] + DX[d];
				int status = cur[3];
				int time = cur[4] + 1;
				if (0 <= ny && ny < ROW && 0 <= nx && nx < COL) {
					if (classroom[ny][nx] == '#' || (vis[ny][nx][d][status])) {
						continue;
					} else if (classroom[ny][nx] == 'C') {
						if (status == 2) {
							ans = Math.min(ans, time);
							continue;
						} else {
							status = 1;
						}
					} else if (classroom[ny][nx] == 'D') {
						if (status == 1) {
							ans = Math.min(ans, time);
							continue;
						} else {
							status = 2;
						}
					}
					vis[ny][nx][d][status] = true; 
					queue.offer(new int[] {ny, nx, d, status, time});
				}
			}
		}
		if (ans == 987654321) {
			System.out.println(-1);
		} else {
			System.out.println(ans);
		}
	}
}
