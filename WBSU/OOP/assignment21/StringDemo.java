class StringDemo{
	public static void main(String args[]){
		String str = "I am Suvasish Das.";
		
		// operation 1: charAt
		System.out.println(str.charAt(0));
		
		// operation 2: length
		System.out.println(str.length());
		
		// operation 3
		System.out.println(str.substring(0,6));

		// operation 4
		System.out.println(str.isEmpty());
		
		// operation 5
		String str1 = String.join("WEST ","BENGAL ","STATE ","UNIVERSITY");
		System.out.println(str1);
		
	}
}
