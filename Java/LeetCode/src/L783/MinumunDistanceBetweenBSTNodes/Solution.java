package L783.MinumunDistanceBetweenBSTNodes;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Objects;


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        val = x;
    }
}

class BST {
    TreeNode rootNode;
    int minValue = 987654321;
    int[] sortedArray = new int[200];
    int idx = 0;
    
    public void insertNode(int data) {
    	if(Objects.isNull(rootNode)) {
    		rootNode = new TreeNode(data);
    		return;
    	}
    	TreeNode currentNode = rootNode;
    	TreeNode parent= null;
    	while(true) {
    		parent = currentNode;
    		if(data <= currentNode.val) {
    			currentNode = currentNode.left;
    			if(Objects.isNull(currentNode)) {
    				parent.left = new TreeNode(data);
    				return;
    			}
    		} else {
    			currentNode = currentNode.right;
    			if(Objects.isNull(currentNode)) {
    				parent.right = new TreeNode(data);
    				return;
    			}
    		}
    	}
    }
    
    void inOrderTraversal(TreeNode root) {
		if(Objects.nonNull(root.left)) {
			inOrderTraversal(root.left);
		}
		sortedArray[idx] = root.val;
		if(idx > 0 && sortedArray[idx] - sortedArray[idx-1] < minValue) {
			minValue = sortedArray[idx] - sortedArray[idx-1];
		}
		idx++;
		if(Objects.nonNull(root.right)) {
			inOrderTraversal(root.right);
		}
    }
    
}
public class Solution {
    public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		BST newBST = new BST();
		while (st.hasMoreTokens()) {
			int value = Integer.parseInt(st.nextToken());
			newBST.insertNode(value);
		}
		newBST.inOrderTraversal(newBST.rootNode);
		System.out.println(newBST.minValue);
		
	}
}
