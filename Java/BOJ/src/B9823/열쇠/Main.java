package B9823.¿­¼è;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

class Graph {
	private ArrayList<ArrayList<Integer>> graph;
	
	public Graph(int initSize) {
		this.graph = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < initSize; i++) {
			graph.add(new ArrayList<Integer>());
		}
	}
	public ArrayList<ArrayList<Integer>> getGraph() {
		return this.graph;
	}
	
	public ArrayList<Integer> getNode(int key) {
		return graph.get(key);
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
}


public class Main {
    public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		final int N = Integer.parseInt(br.readLine());
		for (int caseNum = 0; caseNum < N; caseNum++) {
			
		}
	}
}
