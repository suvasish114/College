// ASSIGNMENT3
class Bank{
	private String id;
	private String name;
	private int branchCode;
	Bank(String id, String name, int branchCode){
		this.id = id;
		this.name = name;
		this.branchCode = branchCode;
	}
	Bank(Bank bank){
		this.id = bank.id;
		this.name = bank.name;
		this.branchCode = bank.branchCode;
	}
	public void show(){
		System.out.print(String.format("%10s | %10s | %10d ",this.id, this.name,this.branchCode));
	}
}
class Employee extends Bank{
	private String id;
	private String name;
	private Bank bank;
	Employee(Bank bank, String id, String name){
		super(bank);
		this.bank = bank; 
		this.id = id;
		this.name = name;
	}
	Employee(Employee emp){
		super(emp.getBank());
		this.id = emp.id;
		this.name = emp.name;
	}
	public Bank getBank(){
		return this.bank;
	}
	public void show(boolean flag){
		super.show();
		System.out.print(String.format("| %10s | %10s |", this.id, this.name));
		if(flag == true) return;
		System.out.println();
	}
}
class Manager extends Employee{
	private String id;
	Manager(Employee employee, String id){
		super(employee);
		this.id = id;
	}
	public void show(){
		super.show(true);
		System.out.println(String.format("| %10s",this.id));
	}
}
class Main{
	public static void main(String args[]){
		// bank objects
		Bank bank1 = new Bank("SBI1234","SBI-BKP",12345);
		Bank bank2 = new Bank("BOI4567","BOI-DUM",75489);
		Bank bank3 = new Bank("ICICI785","ICI-SEL",85423);
		
		// employee objects
		Employee e1 = new Employee(bank1, "EID211", "Rohan");
		Employee e2 = new Employee(bank2, "EID456", "Susmita");
		Employee e3 = new Employee(bank3, "EID789", "Akash");
		Employee e4 = new Employee(bank2, "EID425", "Alex");
		Employee e5 = new Employee(bank3, "EID846", "Pritam");
		
		// manager objects
		Manager m1 = new Manager(e4, "MNG785");
		Manager m2 = new Manager(e5, "MNG458");
		
		// show
		System.out.println("---------------------------------------------------------------------------");
		System.out.println(String.format("%10s | %10s | %10s | %10s | %10s | %10s",
		"BANK ID", "BANK NAME", "BRANCH", "EMP ID", "EMP NAME", "MANAGER"));
		System.out.println("---------------------------------------------------------------------------");
		e1.show();
		e2.show();
		e3.show();
		m1.show();
		m2.show();
	}
}
