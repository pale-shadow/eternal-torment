/*
    Write a program that prints the numbers from 1 to 100. 
    But for multiples of three print “Ayy” instead of the number and for the 
    Multiples of five print “Lmao”. For numbers which are multiples of both three 
    and five print “AyyLmao”.
 */
public class ayylmao {

	public static void main(String args[]) throws java.io.IOException {

		for (int x = 1; x < 101; x++) {
			
			if ((x % 3 == 0) && (x % 5 == 0))
				System.out.println("AyyLmao");
			else if (x % 3 == 0)
				System.out.println("Ayy");
			else if (x % 5 == 0)
				System.out.println("Lmao");
			else 
				System.out.println(x);
		}
	}

}
