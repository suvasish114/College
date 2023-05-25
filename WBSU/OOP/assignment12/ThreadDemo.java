class ThreadDemo implements Runnable{
	public Thread t;
	ThreadDemo(String threadName){t = new Thread(this, threadName);}
	public void run(){
		try{
			for(int i=0; i<5; i++){
				System.out.println(i + ": " + this.t.getName());
				Thread.sleep(1000);
			}
		}catch(Exception e){}
		System.out.println("Exiting...");
	}
}
class Main{
	public static void main(String args[]){
		// creating two thread to run concurrently
		new ThreadDemo("Thread1").t.start();
		new ThreadDemo("Thread2").t.start();
	}
}
