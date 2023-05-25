class A{
	synchronized void foo(B b){
		System.out.println(Thread.currentThread().getName()+" entered A.foo");
		try{Thread.sleep(1000);}
		catch(InterruptedException e){}
		System.out.println("Try to call B.bar...");
		b.bar();
	}
	synchronized void bar(){
		System.out.println("Inside A.bar");
	}
}
class B{
	synchronized void foo(A a){
		System.out.println(Thread.currentThread().getName()+" entered B.bar");
		try{Thread.sleep(1000);}
		catch(InterruptedException e){}
		System.out.println("Try to call A.bar...");
		a.bar();
	}
	synchronized void bar(){
		System.out.println("Inside B.bar");
	}
}
class DeadLock extends Thread{
	A a = new A();
	B b = new B();
	DeadLock(){super("Deadlock");}
	public void deadlockStart(){
		this.start();
		a.foo(b);
	}
	public void run(){
		b.foo(a);
	}
}
class Main{
	public static void main(String args[]){
		DeadLock deadLock = new DeadLock();
		deadLock.deadlockStart();
	}
}