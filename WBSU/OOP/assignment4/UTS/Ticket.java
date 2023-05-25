package UTS;
import java.time.LocalDate;

public class Ticket{
	private int ticketId;
	private String from;
	private String to;
	private int amount;
	private LocalDate issueDate;
	
	// constractors
	public Ticket(){
		this.issueDate = LocalDate.now();
	}
	public Ticket(int ticketId, String from, String to, int amount){
		this.ticketId = ticketId;
		this.from = from;
		this.to = to;
		this.amount = amount;
		this.issueDate = LocalDate.now();
	}

	// setters
	public void setTicketId(int ticketId){
		this.ticketId = ticketId;
	}
	public void setFrom(String from){
		this.from = from;
	}
	public void setTo(String to){
		this.to = to;
	}
	public void setAmount(int amount){
		this.amount = amount;
	}
	
	// display
	public void showTicket(){
		System.out.println(String.format("%5d | %5s | %5s | %5d | %10s", this.ticketId,this.from,this.to,this.amount,String.valueOf(this.issueDate)));
	}
}
