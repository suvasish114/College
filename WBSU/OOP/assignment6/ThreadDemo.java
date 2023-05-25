class ThreadDemo extends Thread{
	ThreadDemo(String name){super(name);}
	public void run(){
		try{
			for(int i=0; i<5; i++){
				Thread.sleep(1000);
				System.out.println(this.getName() + ": "+i);
			}
		}catch(Exception e){}
		System.out.println("Exiting from thread "+this.getName());
	}
}
class Main{
	public static void main(String args[]){
		ThreadDemo thread1 = new ThreadDemo("Thread1");
		thread1.setPriority(Thread.MIN_PRIORITY);
		ThreadDemo thread2 = new ThreadDemo("Thread2");
		thread2.setPriority(Thread.MAX_PRIORITY);
		thread1.run();
		thread2.run();
	}
}
