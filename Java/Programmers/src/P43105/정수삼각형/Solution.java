package P43105.Á¤¼ö»ï°¢Çü;

public class Solution {
	public static void main(String[] agrs) {
		int[][] triangle = new int[][] {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
		int answer = solution(triangle);
		System.out.println(answer);
	}
	
	public static int solution(int[][] triangle) {
		int answer = 0;
		for (int h = 1; h < triangle.length; h++) {
			int width = triangle[h].length;
			for (int w = 0; w < width; w++) {
				if (w == 0) {
					triangle[h][w] += triangle[h-1][w]; 
				} else if (w == width - 1) {
					triangle[h][w] += triangle[h-1][w-1];
				} else {
					triangle[h][w] = Math.max(triangle[h][w] + triangle[h-1][w-1] , triangle[h][w] + triangle[h-1][w]); 
				}
				if (h == triangle.length - 1 && answer < triangle[h][w]) {
					answer = triangle[h][w];
				}
			}
			
		}
		return answer;
	}

}
