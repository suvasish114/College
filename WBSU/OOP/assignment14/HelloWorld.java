import java.util.Scanner;
class HelloWorld{
	private static Scanner scan = new Scanner(System.in);
	public static void main(String args[]){
		System.out.print("Enter your message\n= ");
		String str = scan.nextLine();
		System.out.println("\nO/P\n"+str);
	}
}
