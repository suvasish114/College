// stack using multithreading
// stack class
class Stack{
	private int[] stack;
	private int top;
	private int size;
	private boolean LOCK;
	Stack(int size){
		this.top = 0;
		this.size = size;
		this.stack = new int[this.size];
		this.LOCK = false;
	}
	synchronized void top(){
		while(this.LOCK){
			try{wait();}
			catch(InterruptedException exception){}
		}
		System.out.println("Top: "+this.stack[this.size-1]);
		notify();
	}
	synchronized void push(int item){
		while(this.LOCK){
			try{wait();}
			catch(InterruptedException exception){}
		}
		this.LOCK = true;
		if(this.top == this.size-1) System.out.println("Stack Overflow");
		else{
			this.top += 1;
			this.stack[this.top] = item;
			System.out.println("Push: "+item);
		}
		this.LOCK = false;
		notify();
	}
	synchronized void pop(){
		while(this.LOCK){
			try{wait();}
			catch(InterruptedException exception){}
		}
		this.LOCK = true;
		if(this.top < 0) System.out.println("Stack Underflow");
		else{
			System.out.println("Pop: "+this.stack[this.size]);
			this.top -= 1;
		}
		this.LOCK = false;
		notify();
	}
}
// always push
class User1 extends Thread{
	private Stack stack;
	User1(Stack stack){
		super("User1");
		this.stack = stack;
	}
	public void run(){
		for(int i=0; i<10; i++) this.stack.push(i++);
	}
}
// always pop
class User2 extends Thread{
	private Stack stack;
	User2(Stack stack){
		super("User2");
		this.stack = stack;
	}
	public void run(){
		for(int i=0; i<10; i++) this.stack.pop();
	}
}
// driving code
class Main{
	public static void main(String args[]){
		Stack stack = new Stack(10);
		User1 user1 = new User1(stack);
		User2 user2 = new User2(stack);
		user1.start();				// thread1
		user2.start();				// thread2
		for(int i=0; i<10; i++) stack.top();	// thread3
	}
}
