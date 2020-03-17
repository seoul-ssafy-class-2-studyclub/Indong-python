package B1932.Á¤¼ö»ï°¢Çü;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] agrs) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final int N = Integer.parseInt(br.readLine());
		int[][] triangle = new int[N][N];
		for (int i = 0; i < N; i++) {
			int j = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				triangle[i][j++] = Integer.parseInt(st.nextToken());
			}
		}
		int answer = solution(triangle, N);
		System.out.println(answer);
	}
	
	public static int solution(int[][] triangle, int N) {
		int answer = triangle[0][0];
		for (int h = 1; h < N; h++) {
			triangle[h][0] += triangle[h-1][0];
            triangle[h][h] += triangle[h-1][h-1];
			for (int w = 1; w < h; w++) {
				triangle[h][w] = Math.max(triangle[h][w] + triangle[h-1][w-1] , triangle[h][w] + triangle[h-1][w]); 
			}
			
		}
		for (int i = 0; i < N; i++) {
			answer = Math.max(answer, triangle[N-1][i]);
		}
		return answer;
	}

}
