import java.io.File;
import java.util.Scanner;

class Count{
	private static Scanner scan;
	public static void main(String args[]){
		int count = 0;
		try{
			File file = new File("a.in");
			scan = new Scanner(file);
			while(scan.hasNextLine()){
				count += scan.nextLine().length();
			}
			System.out.println("Total character in file is: "+count);
		}catch(Exception e){}
		scan.close();
	}
}
