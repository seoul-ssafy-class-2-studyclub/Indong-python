package L914.XofaKindinaDeckofCards;

public class Solution {
	public static void main(String[] args) {
		int[] deck = {1, 1, 1, 2, 2, 2};
		System.out.println(hasGroupSizeX(deck));
		System.out.println(GCD(7, 8));
	}
	
	
	public static int GCD(int a, int b) {
		int temp;
		if (b > a) {
			temp = a;
			a = b;
			b = temp;
		}
		while (b > 0) {
			temp = b;
			b = a % b;
			a = temp;
		}
		return a;
	}
	
	
	public static boolean hasGroupSizeX(int[] deck) {
		if (deck.length == 1) {
			return false;
		}
		int[] chk = new int[10000];
		for (int card : deck) {
			chk[card] += 1;
		}
		int idx = 0;
		int gcd = 0;
		for (int i = 0; i < 10000; i++) {
			if(chk[i] > 0) {
				if (gcd == 0) {
					gcd = chk[i];
				} else {
					gcd = GCD(gcd, chk[i]);
				}
			}
		}
		return gcd >= 2;
	}

}
