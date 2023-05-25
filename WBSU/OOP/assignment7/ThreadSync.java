class Target{
	private int counter;
	Target(int counter){this.counter = counter;}
	public synchronized void update(int val){
		try{
			for(int i=0; i<3; i++){
				this.counter += val;
				System.out.println("update: "+this.counter);
				Thread.sleep(1000);
			}
		}catch(Exception e){}
	}
}
class ThreadSync extends Thread{
	Target target;
	int val;
	ThreadSync(String name, Target target, int val){
		super(name);
		this.target = target;
		this.val = val;
	}
	public void run(){
		try{
			System.out.print(this.getName() + " ");
			target.update(this.val);
		}catch(Exception e){}
	}
}
class Main{
	public static void main(String args[]){
		Target target = new Target(0);
		ThreadSync obj1 = new ThreadSync("Thread1", target, 1);
		ThreadSync obj2 = new ThreadSync("Thread2", target, 5);
		obj1.start();
		obj2.start();
	}
}
