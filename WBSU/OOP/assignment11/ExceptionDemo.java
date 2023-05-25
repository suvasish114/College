// exception class
class ExceptionDemo extends Exception{
	private int detail;
	ExceptionDemo(int a ){this.detail = a;}
	public String toString(){return "Exception occur at number ["+this.detail+"]";}
}
// driving code
class Main{
	// generator function
	private static void compute(int a) throws ExceptionDemo{
		if(a>10) throw new ExceptionDemo(a);
	}
	// main method
	public static void main(String args[]){
		try{
			compute(1);
			compute(11);		// exception occurs
		}catch(ExceptionDemo e){
			System.out.println(e);
		}
	}
}
