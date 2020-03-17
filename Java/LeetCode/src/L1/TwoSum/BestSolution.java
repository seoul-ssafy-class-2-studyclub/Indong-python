package L1.TwoSum;

public class BestSolution {
	public static void main(String[] args) {
		int[] cost = {10, 15, 20};
		int size = cost.length;
		int f1 = 0, f2 = 0;
		for(int i = size - 1; i >= 0; i--) {
			int f0 = cost[i] + Math.min(f1, f2);
			f2 = f1;
			f1 = f0;
		}
		
		int result = Math.min(f1, f2);
		System.out.println(result);
	}

}
