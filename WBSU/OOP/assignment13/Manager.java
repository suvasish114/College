class Bank{
	private int amount;
	private boolean LOCK;
	Bank(int amount){
		this.amount = amount;
		this.LOCK = false;
	}
	public synchronized void setAmount(int amount){
		while(this.LOCK){
			try{wait();}
			catch(InterruptedException e){}
		}
		this.LOCK = true;
		this.amount += amount;
		System.out.println("Deposit: "+amount+"\t"+this.amount);
		this.LOCK = false;
		notify();
	}
	public synchronized void getAmount(int amount){
		while(this.LOCK){
			try{wait();}
			catch(InterruptedException e){}
		}
		this.LOCK = true;
		this.amount -= amount;
		System.out.println("Withdrawal: "+amount+"\t"+this.amount);
		this.LOCK = false;
		notify();
	}
}
class Withdrawal extends Thread{
	private Bank bank;
	Withdrawal(Bank bank){
		super("Customer");
		this.bank = bank;
	}
	public void run(){
		for(int i=0; i<5; i++){this.bank.getAmount(i+15);}
	}
}
class Deposit extends Thread{
	private Bank bank;
	Deposit(Bank bank){
		super("Customer");
		this.bank = bank;
	}
	public void run(){
		for(int i=0; i<3; i++){this.bank.setAmount(i+30);}
	}
}
class Main{
	public static void main(String args[]){
		Bank bank = new Bank(1000);
		Withdrawal w = new Withdrawal(bank);
		Deposit d = new Deposit(bank);
		w.start();
		d.start();
	}
}
