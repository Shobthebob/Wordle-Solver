import java.util.Scanner;
import java.lang.Math;

public class solver {
	
	 public static String duplicateRemover(String str) {
		 for(int i=0; i<str.length( ); i++) {
			 for(int j=i+1; j<str.length( ); j++) {
				 if(str.charAt(i)==str.charAt(j)) {
					 str = str.substring(0,j) + str.substring(j+1);
				 }
			 }
		 }
		 return str;
	}
	 
	 public static char[] elementRemover(char[]ar, char e) {
		 char[]arr = new char[ar.length-1];
		 for(int i=0, j=0; i<ar.length; i++) {
			 if(ar[i]!=e) {
				 arr[j++] = ar[i];
			 }
		 }
		 return arr;
	 }

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		char[] alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
		
		System.out.print("letters that're NOT there: ");
		String letters = scan.next( );
		letters = letters.toUpperCase( );
		
		//checking for duplicates in case the user is dumb
		letters = duplicateRemover(letters);
		
		//eliminating all non used letters 
		for(int i=0; i<letters.length( ); i++) {
			alphabet = elementRemover(alphabet, letters.charAt(i));
		}
		
		int len = alphabet.length;
		String[] allwords = new String[(int)Math.pow(len, 5)];
		int a = 0;
		for(int l1=0; l1<len; l1++) {
			for(int l2=0; l2<len; l2++) {
				for(int l3=0; l3<len; l3++) {
					for(int l4=0; l4<len; l4++) {
						for(int l5=0; l5<len; l5++) {
							allwords[a] = String.valueOf(alphabet[l1]) + String.valueOf(alphabet[l2]) + String.valueOf(alphabet[l3]) + String.valueOf(alphabet[l4]) + String.valueOf(alphabet[l5]);
							a++;
						}
						
					}
				}
			}
		}
		
		for(String sss: allwords) {
			System.out.println(sss);
		}
		System.out.println("Math.pow(len, 5): " + Math.pow(len, 5));
		System.out.println("Length of words: " + allwords.length);
		
		scan.close( );
	}

}
