import java.io.FileWriter;
import java.util.Scanner;

class FileDemo{
	private static Scanner scan = new Scanner(System.in);
	public static void main(String args[]){
		try{
			FileWriter fileWriter = new FileWriter("A.out");
			fileWriter.write(String.valueOf(scan.nextLine()));
			fileWriter.close();
		} catch(Exception e){}
	}
}
