package B5052.전화번호목록;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class TrieNode {
	public Map<Character, TrieNode> childnodes = new HashMap<>();
	private boolean isLastChar;
	
	Map<Character, TrieNode> getChildNodes() {
		return this.childnodes;
	}
	
	boolean isLastChar() {
		return this.isLastChar;
	}
	
	void setIsLastChar(boolean isLastChar) {
		this.isLastChar = isLastChar;
	}
}

class Trie {
	private TrieNode rootNode;
	
	Trie() {
		rootNode = new TrieNode();
	}
	boolean insert(String word) {
		TrieNode thisNode = this.rootNode;
		boolean flag = true;
		
		for(int idx = 0; idx < word.length(); idx++) {
			Map<Character, TrieNode> childNode = thisNode.getChildNodes();
			char part = word.charAt(idx);
			if (childNode.containsKey(part)) {
				thisNode = thisNode.childnodes.get(part);
				if ((thisNode.isLastChar() && flag && idx < word.length()) || (flag && idx == word.length() - 1)) {
					return false;
				}
			} else {
				flag = false;
				thisNode.childnodes.put(part, new TrieNode());
				thisNode = thisNode.childnodes.get(part);
			}
		}
		thisNode.setIsLastChar(true);
		return true;
	}
}

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int caseSize = Integer.parseInt(br.readLine());
		for(int i = 0; i < caseSize; i++) {
			int numberSize = Integer.parseInt(br.readLine());
			Trie caseTrie = new Trie();
			boolean result = true;
			for(int j = 0; j < numberSize; j++) {
				String number = br.readLine().trim();
				if(!caseTrie.insert(number)) {
					result = false;
				}
			}
			if (result) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
		}
	}
}
