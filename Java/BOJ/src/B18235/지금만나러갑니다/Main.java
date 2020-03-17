package B18235.지금만나러갑니다;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] visited5ri;
	static int[] visited6ri;
	static final int[] DX = {1, -1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		final int N = Integer.parseInt(st.nextToken());
		final int A = Integer.parseInt(st.nextToken());
		final int B = Integer.parseInt(st.nextToken());
		visited5ri = new int[N+1];
		visited6ri = new int[N+1];
		Arrays.fill(visited5ri, -1);
		Arrays.fill(visited6ri, -1);
		visited5ri[A] = 0;
		visited6ri[B] = 0;
		
		int result = find(A, B, N);
		System.out.println(result);
	}
	
	public static int find(int A, int B, int N) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {A, 0, 5});
		queue.add(new int[] {B, 0, 6});
		while(!queue.isEmpty()) {
			int[] cur = queue.poll();
			for (int dx : DX) {
				int next = cur[0] + ((1 << cur[1]) * dx);
				if (next < 1 || next > N) {
					continue;
				}
				int cnt = cur[1] + 1;
				int ori = cur[2];
				if (ori == 5) {
					visited5ri[next] = cnt;
				} else if (ori == 6) {
					visited6ri[next] = cnt;
					if (visited5ri[next] == visited6ri[next] && visited6ri[next] != -1) {
						return cnt;
					}
				}
				queue.add(new int[] {next, cnt, ori});
			}
		}
		return -1;
	}

}
