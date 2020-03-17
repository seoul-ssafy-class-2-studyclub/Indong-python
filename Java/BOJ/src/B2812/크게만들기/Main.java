package B2812.크게만들기;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		LinkedList<Integer> stack = new LinkedList<Integer>();
		String number = br.readLine().trim();
		for(int i = 0; i < N; i++) {
			int temp = number.charAt(i) - '0';
			if(stack.isEmpty()) {
				stack.add(temp);
			} else {
				while(!stack.isEmpty() && stack.peekLast() < temp && K > 0) {
					stack.removeLast();
					K--;
				}
				stack.add(temp);
			}
		}
		if (K > 0) {
			for(int i = 0; i < K; i++) {
				stack.removeLast();
			}
		}
		for(int ele : stack) {
			sb.append(ele);
		}
		bw.write(sb.append('\n').toString());
		bw.close();
	}
}
