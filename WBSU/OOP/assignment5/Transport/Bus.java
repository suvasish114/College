package Transport;
public class Bus implements Vehicle{
	private int id;
	private String from;
	private String to;
	
	public Bus(){}
	public Bus(int id, String from, String to){
		this.id = id;
		this.from = from;
		this.to = to;
	}
	
	// setter
	public void setId(){
		this.id = id;
	}
	public void setFrom(){
		this.from = from;
	}
	public void setTo(){
		this.to = to;
	}
	
	public void showDetails(){
		System.out.println(String.format("%5d | %5s | %5s | %5d",this.id,this.from,this.to,maxSpeedLimit));
	}
	public void costPerKM(){
		System.out.println("Cost Per KM: "+5+" Rs");
	}
}
