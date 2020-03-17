package B9205.맥주마시면서걸어가기;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;


class Graph {
	private ArrayList<ArrayList<Integer>> graph;
	private boolean[] visited;
	public String ans = "sad";
	private int pentaport;
	
	public Graph(int initSize) {
		this.graph = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < initSize; i++) {
			graph.add(new ArrayList<Integer>());
		}
		this.visited = new boolean[initSize];
		this.pentaport = initSize - 1;
	}
	
	public ArrayList<ArrayList<Integer>> getGraph() {
		return this.graph;
	}
	
	public ArrayList<Integer> getNode(int i) {
		return this.graph.get(i);
	}
	
	public void put(int x, int y) {
		graph.get(x).add(y);
		graph.get(y).add(x);
	}
	
	public void append(int x, int y) {
		graph.get(x).add(y);
	}
	
	public void printGraph() {
		for (int i = 1; i < graph.size(); i++) {
			System.out.println(graph.get(i));
		}
	}
	
	public void dfs(int index) {
		visited[index] = true;
		for (int next : graph.get(index)) {
			if (next == pentaport) {
				ans = "happy";
				return;
			} else if (!visited[next]) {
				dfs(next);
			}
		}
	}
}
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int caseSize = Integer.parseInt(br.readLine());
		for (int caseNum = 0; caseNum < caseSize; caseNum++) {
			final int N = Integer.parseInt(br.readLine()) + 2;
			int[][] idxArray = new int[N+1][2];
			for (int i = 1; i < N + 1; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				idxArray[i][0] = Integer.parseInt(st.nextToken());
				idxArray[i][1] = Integer.parseInt(st.nextToken());
			}
			Graph adj = new Graph(N + 1);
			for (int i = 1; i < N; i++) {
				for (int j = i + 1; j < N + 1; j++) {
					int dis = Math.abs(idxArray[i][0] - idxArray[j][0]) + Math.abs(idxArray[i][1] - idxArray[j][1]);
					if (dis <= 1000) {
						adj.put(i, j);
					}
				}
			}
			adj.dfs(1);
			sb.append(adj.ans).append("\n");
		}
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
}
