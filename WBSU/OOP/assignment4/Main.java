import java.util.Scanner;
import UTS.*;

public class Main{
	private static Scanner scan = new Scanner(System.in);
	public static void main(String args[]){
		Ticket ticket[] = new Ticket[100];
		int totalTickets = 0;
		while(true){
			System.out.println("\n+-----------------+\n|    Main Menu    |\n+-----------------+");
			System.out.print("1. Issue Ticket\n2. Show Tickets\n3. Exit\n= ");
			int choice = Integer.parseInt(scan.nextLine());
			switch(choice){
				case 1:
					ticket[totalTickets] = new Ticket();
					System.out.print("Ticket Id: ");
					ticket[totalTickets].setTicketId(Integer.parseInt(scan.nextLine()));
					System.out.print("From: ");
					ticket[totalTickets].setFrom(scan.nextLine());
					System.out.print("To: ");
					ticket[totalTickets].setTo(scan.nextLine());
					System.out.print("Amount: ");
					ticket[totalTickets].setAmount(Integer.parseInt(scan.nextLine()));
					totalTickets += 1;
					break;
				case 2:
					System.out.println("\n------------------------------------------");
					System.out.println(String.format("%5s | %5s | %5s | %5s | %10s","Id","From","To","Price","Date"));
					System.out.println("------------------------------------------");
					for(int i=0; i<totalTickets; i++){
						ticket[i].showTicket();
					}
					break;
				case 3:
					return;
			}
		}
	}
}
