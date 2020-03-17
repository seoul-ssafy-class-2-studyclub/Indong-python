package B14003.가장긴증가하는부분수열5;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int[] sequence;
	static int[][] subSequence;
	static int[] tracking;
	
	static void binarySearch(int number, int start, int end, int index) {
		int middle = 0;
		while (start < end) {
			middle = (start + end) / 2;
			if (subSequence[middle][0] < number) {
				start = middle + 1;
			} else {
				end = middle;
			}
		}
		subSequence[end][0] = number;
		subSequence[end][1] = index;
		if (end >= 1) {
			tracking[index] = subSequence[end-1][1];
		}
		return;
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        
		final int N = Integer.parseInt(br.readLine().trim());
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		sequence = new int[N];
		subSequence = new int[N][2];
		tracking = new int[N];
		for (int i = 0; i < N; i++) {
			sequence[i] = Integer.parseInt(st.nextToken());
		}
		subSequence[0][0] = sequence[0];
		int last = 0;
		for (int i = 1; i < N; i++) {
			if (subSequence[last][0] < sequence[i]) {
				subSequence[++last][0] = sequence[i];
				subSequence[last][1] = i;
				tracking[i] = subSequence[last-1][1];
			} else {
				binarySearch(sequence[i], 0, last, i);
			}
		}
		sb.append(last+1).append("\n");
		int idx = subSequence[last][1];
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i <= last; i++) {
			stack.push(sequence[idx]);
			idx = tracking[idx];
		}
		while (!stack.isEmpty()) {
			sb.append(stack.pop()).append(" ");
		}
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
}
