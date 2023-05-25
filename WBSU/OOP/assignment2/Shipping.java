// ASSIGNMENT 2
import java.util.Scanner;

class Shipping{
	private int id;
	private String from;
	private String to;
	Shipping(int id, String from, String to){
		this.id = id;
		this.from = from;
		this.to = to;
	}
	public void showData(){
		System.out.print(String.format("%10d | %10s | %10s | ",this.id,this.from,this.to));
	}
}
class Domestic extends Shipping{
	private String USPSid;
	Domestic(int id, String from, String to, String USPSid){
		super(id, from, to);
		this.USPSid = USPSid;
	}
	public void showData(){
		super.showData();
		System.out.println(String.format("%20s",this.USPSid));
	}
}
class International extends Shipping{
	private String FEDXid;
	International(int id, String from, String to, String FEDXid){
		super(id, from, to);
		this.FEDXid = FEDXid;
	}
	public void showData(){
		super.showData();
		System.out.println(String.format("%20s",this.FEDXid));
	}
}
class Main{
	private static Scanner scan = new Scanner(System.in);
	public static void main(String args[]){
		International international[] = new International[100];
		Domestic domestic[] = new Domestic[100];
		int international_max = 0;
		int domestic_max = 0;
		while(true){
			System.out.print("Enter choice-\n1. International Shipping\n2. Domestic Shipping\n3. Exit\n= ");
			int choice = Integer.parseInt(scan.nextLine());
			switch(choice){
				case 1:
					while(true){
						System.out.println("International Shipping");
						System.out.print("Enter choice-\n1. Insert Data\n2. Show Data\n3. Main Menu\n= ");
						int choice1 = Integer.parseInt(scan.nextLine());
						switch(choice1){
							case 1:
								System.out.print("Id: ");
								int id = Integer.parseInt(scan.nextLine());
								System.out.print("From: ");
								String from = scan.nextLine();
								System.out.print("To: ");
								String to = scan.nextLine();
								System.out.print("FedX Id: ");
								String FEDXid = scan.nextLine();
								international[international_max] = new International(id, from, to, FEDXid);
								international_max += 1;
								break;
							case 2:
								System.out.println();
								System.out.println(String.format("%10s | %10s | %10s | %20s","ID","FROM","TO","FED-X ID"));
								System.out.println("-------------------------------------------------------------------");
								for(int i=0; i<international_max; i++){
									international[i].showData();
								}
								break;
							case 3:
								return;
						}
					}
					// break;
				case 2:
					while(true){
						System.out.println("Domestic Shipping");
						System.out.print("Enter choice-\n1. Insert Data\n2. Show Data\n3. Main Menu\n= ");
						int choice2 = Integer.parseInt(scan.nextLine());
						switch(choice2){
							case 1:
								System.out.print("Id: ");
								int id = Integer.parseInt(scan.nextLine());
								System.out.print("From: ");
								String from = scan.nextLine();
								System.out.print("To: ");
								String to = scan.nextLine();
								System.out.print("USPS Id: ");
								String USPSid = scan.nextLine();
								domestic[domestic_max] = new Domestic(id, from, to, USPSid);
								domestic_max += 1;
								break;
							case 2:
							System.out.println();
								System.out.println(String.format("%10s | %10s | %10s | %20s","ID","FROM","TO","USPS Id"));
								System.out.println("-------------------------------------------------------------------");
								for(int i=0; i<domestic_max; i++){
									domestic[i].showData();
								}
								break;
							case 3:
								return;
						}
					}
					// break;
				case 3:
					return;
			}
		}
	}
}
