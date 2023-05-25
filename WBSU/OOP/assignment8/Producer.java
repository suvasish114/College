// producer consumer problem using synchronization
// pool class 
class Pool{
	private int item;
	private boolean LOCK;
	Pool(){LOCK = false;}
	synchronized void getItem(){
		while(!this.LOCK){
			try{wait();}
			catch(InterruptedException exception){}
		}
		LOCK = false;
		System.out.println(Thread.currentThread().getName()+": "+this.item);
		notify();
	}
	synchronized void setItem(int item){
		while(this.LOCK){
			try{wait();}
			catch(InterruptedException exception){}
		}
		this.LOCK = true;
		this.item = item;
		System.out.println(Thread.currentThread().getName()+": "+this.item);
		notify();
	}
}
// producer class
class Producer extends Thread{
	private Pool pool;
	Producer(Pool pool){
		super("Producer");
		this.pool = pool;
	}
	public void run(){
		for(int i=0;i<10;i++){
			this.pool.setItem(i++);
		}
	}
}
// consumer class
class Consumer extends Thread{
	private Pool pool;
	Consumer(Pool pool){
		super("Consumer");
		this.pool = pool;
	}
	public void run(){
		for(int i=0;i<10;i++){
			this.pool.getItem();
		}
	}
}
// driving code
class Main{
	public static void main(String args[]){
		Pool pool = new Pool();
		Producer producer = new Producer(pool);
		Consumer consumer = new Consumer(pool);
		producer.start();
		consumer.start();
	}
}
