public class Stack{
	private int items[] = new int[10];
	private int top = -1;

	public void push(int item){
		if (top == 9) System.out.println("Stack is full");
		else items[++top] = item;
	}
	public void pop(){
		if (top == -1) System.out.println("Stack is empty");
		else System.out.println("Pop: "+items[top--]);
	}
	public void display(){
		if (top == -1) System.out.println("Stack is empty");
		else {
			for(int i=0; i<=top; i++) System.out.print(items[i]+" ");
			System.out.println();
		}
	}

	public static void main(String args[]){
		Stack stack = new Stack();
		stack.push(10);
		stack.push(20);
		stack.display();
		stack.pop();
		stack.display();
	}
}
