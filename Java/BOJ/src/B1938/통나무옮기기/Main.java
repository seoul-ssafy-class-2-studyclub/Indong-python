package B1938.통나무옮기기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;


public class Main {
	static final int[] DY = {-1, 0, 1, 0};
	static final int[] DX = {0, 1, 0, -1};
	static final int[][] LOG = {{1, 0, 2, 0}, {0, 1, 0, 2}};

    public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final int N = Integer.parseInt(br.readLine().trim());
		char[][] board = new char[N][N];
		boolean[][][] vis = new boolean[N][N][2];
		
		int sy = 0;
		int sx = 0;
//		세로 0, 가로 1
		int dir = 0;
		boolean flag = false;
		for(int i = 0; i < N; i++) {
			String row = br.readLine().trim();
			for(int j = 0; j < N; j++) {
				char cur = row.charAt(j);
				board[i][j] = cur;
				if (cur == 'B' && !flag) {
					sy = i;
					sx = j;
					flag = true;
					vis[sy][sx][dir] = true;
				} else if (cur == 'B' && flag && 1 <= j && board[i][j-1] == 'B') {
					dir = 1;
				}
			}
		}
		
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.offer(new int[] {sy, sx, dir, 0});
		int result = 0;
		Outter: while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int count = cur[3] + 1;
			int cy = cur[0];
			int cx = cur[1];
			if ((cur[2] == 0 && 0 <= cy && cy < N-2 && 0 <= cx && cx < N && board[cy][cx] == 'E' && board[cy+1][cx] == 'E' && board[cy+2][cx] == 'E') || (cur[2] == 1 && 0 <= cy && cy < N && 0 <= cx && cx < N-2 && board[cy][cx] == 'E' && board[cy][cx+1] == 'E' && board[cy][cx+2] == 'E')) {
				result = count - 1;
				break;
			}
			for (int i = 0; i < 4; i++) {
				int ny = cy + DY[i];
				int nx = cx + DX[i];
				if ((cur[2] == 0 && (0 > ny || ny >= N-2 || 0 > nx || nx >= N || board[ny][nx] == '1' || board[ny+1][nx] == '1' || board[ny+2][nx]== '1')) || (cur[2] == 1 && (0 > ny || ny >= N || 0 > nx || nx >= N-2 || board[ny][nx] == '1' || board[ny][nx+1] == '1' || board[ny][nx+2]== '1')) || vis[ny][nx][cur[2]]) {
					continue;
				}
				vis[ny][nx][cur[2]] = true;
				queue.offer(new int[] {ny, nx, cur[2], count});
			}
			if (cur[2] == 0 && 0 <= cy+1 && cy+1 < N && 0 <= cx-1 && cx-1 < N-2 && !vis[cy+1][cx-1][1]) {
				for (int r = 0; r < 3; r++) {
					for (int c = -1; c < 2; c++) {
						if (board[cy+r][cx+c] == '1') {
							continue Outter;
						}
					}
				}
				vis[cy+1][cx-1][1] = true;
				queue.offer(new int[] {cy + 1, cx - 1, 1, count});
			} else if (cur[2] == 1 && 0 <= cy-1 && cy-1 < N-2 && 0 <= cx+1 && cx+1 < N && !vis[cy-1][cx+1][0]) {
				for (int r = -1; r < 2; r++) {
					for (int c = 0; c < 3; c++) {
						if (board[cy+r][cx+c] == '1') {
							continue Outter;
						}
					}
				}
				vis[cy-1][cx+1][0] = true;
				queue.offer(new int[] {cy - 1, cx + 1, 0, count});
			}
		}
		System.out.println(result);
	}
    
}
