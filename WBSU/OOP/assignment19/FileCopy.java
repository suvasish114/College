import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

class FileCopy{
	private static Scanner scan;
	public static void main(String args[]){
		try{
			File file = new File("a.in");
			FileWriter fileWriter = new FileWriter("b.out");
			scan = new Scanner(file);
			while(scan.hasNextLine()){
				fileWriter.write(String.valueOf(scan.nextLine()));
			}
			fileWriter.close();
			scan.close();
		}catch(Exception e){}
	}
}
