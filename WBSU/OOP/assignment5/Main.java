import java.util.Scanner;
import Transport.*;

public class Main{
	private Scanner scan = new Scanner(System.in);
	public static void main(String args[]){
// 		Bus bus = new Bus[100];
		Bus bus =  new Bus(123,"BKP","SLH");
		bus.showDetails();
		bus.costPerKM();
	}
}
