import java.util.Scanner;
class CountVowels{
	private static Scanner scan = new Scanner(System.in);
	public static void main(String args[]){
		int count = 0;
		System.out.print("I/P: ");
		String str = scan.nextLine();
		str = str.toLowerCase();
		for (int i=0; i<str.length(); i++) {
			if (str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u')
				count += 1;
		}
		System.out.println("Number of vowels is: "+count);
	}
}
