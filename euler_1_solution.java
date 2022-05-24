
public class euler_1_solution {

	private static void addNums(int x) {
		int ans = 0, i = 0;
		while (i != x) {
			if (i % 3 == 0 || i % 5 == 0) {
				ans += i;
//				System.out.println(i);
			}
			i++;
			
		}
		System.out.println(ans);

	}

	public static void main(String[] args) {
		addNums(10);

	}

}
