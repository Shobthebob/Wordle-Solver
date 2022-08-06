package rename;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.io.FileReader;

public class solver {

	// A function that removes any duplicate characters from a given string
	public static String duplicateRemover(String str) {
		
		// outer loop that will go through the entire string
		for(int i=0; i<str.length( ); i++) { 
			// this loop will go through the string but will start the iteration from next character that we will be comparing 
			for(int j=i+1; j<str.length( ); j++) { 
				if(str.charAt(i)==str.charAt(j)) { // checks if any character found is equal or not
					str = str.substring(0,j) + str.substring(j+1); // if same characters are found then they are removed
				}
			}
		}
		return str; // returning the new string with the duplicated letters removed
	}
	
	// A function that deletes a character from a character array 
	public static char[] characterRemover(char[]ar, char ch) {
		
		char[]arr = new char[ar.length-1]; // declaring an array of 1 length lesser than the original array because this will store the data
		for(int i=0, j=0; i<ar.length; i++) { // iterating through the array 
			if(ar[i]!=ch) { // adding every element but the one we want to remove from the array 
				arr[j++] = ar[i]; // if the element does not match the one we want to remove, it gets added to the array 
			}
		}
		return arr; // returning a new array with the character removed
	}

	// A function that deletes a string from an array of strings
	public static String[] elementRemover(String[]ar, String str) {
		String[]arr = new String[ar.length-1]; // declaring an array with 1 length lesser than the original because an element will be removed
		for(int i=0, j=0; i<ar.length; i++) {
			if(ar[i]!=str) {
				arr[j++] = ar[i];
			}
		}
		return arr;
	}

	// A function that checks if characters in a an array are present in a string or not
	public static boolean isThere(String str, char[]ar) {

		int count = 0;
		str = str.toUpperCase( );

		for(int i=0; i<ar.length; i++) {
			if(str.contains(Character.toString(ar[i]))) {
				count++;
			}
		}

		if(count==ar.length) {
			return true;
		}
		else {
			return false;
		}
	}	
	
	public static void main(String[] args) {

		// Surrounding the program with try catch so that no error occurs 
		try {
			
			// Creating file reader objects from the file reader class
			FileReader fr1 = new FileReader("Z:\\five-letter-words.txt");
			FileReader fr2 = new FileReader("Z:\\five-letter-words.txt");
			
			// Creating scanner objects to read the file and user inputs
			Scanner sc1 = new Scanner(fr1);
			Scanner sc2 = new Scanner(fr2);
			Scanner scan = new Scanner(System.in);

			//checking the number of lines in the txt file
			int l=0;
			while(sc1.hasNext()) {
				@SuppressWarnings("unused")
				String a = sc1.nextLine( );
				l++;
			}
			
			int p=0;
			// creating an array to store all the words from the text file
			String [] five_letter_words_w_meaning = new String[l];			
			while(sc2.hasNext()) {
				String a = sc2.nextLine( );
				five_letter_words_w_meaning[p] = a; // getting everything from the text file after each iteration
				p++;
			}

			// A character array containing all the English alphabets 
			char[] alphabets = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}; // 26
			
			// Asking the user to input the letters that are not there 
			System.out.print("letters that're NOT there: ");
			String letters_not_there = scan.next( );
			letters_not_there = letters_not_there.toUpperCase( ); // converting the string of letters to UpperCase

			//checking for duplicate letters and removing them 
			letters_not_there = duplicateRemover(letters_not_there);

			//eliminating all non used letters from the array of alphabets 
			for(int i=0; i<letters_not_there.length( ); i++) {
				alphabets = characterRemover(alphabets, letters_not_there.charAt(i));
			}
			
			
			
			// Creating an ArrayList to short-list and store only those words that have a meaning
			ArrayList <String> allwords = new ArrayList <String>( );
			int len = alphabets.length; // new length with all useless characters removed 
			int cout = 0;

//			 creating all possible combinations out of the characters left 
			for(int l1=0; l1<len; l1++) {
				for(int l2=0; l2<len; l2++) {
					for(int l3=0; l3<len; l3++) {
						for(int l4=0; l4<len; l4++) {
							for(int l5=0; l5<len; l5++) {
								String word = String.valueOf(alphabets[l1]) + String.valueOf(alphabets[l2]) + String.valueOf(alphabets[l3]) + String.valueOf(alphabets[l4]) + String.valueOf(alphabets[l5]);						
								for(int j=0; j<l; j++) {
									if(word.equalsIgnoreCase(five_letter_words_w_meaning[j])) {
										cout++;
									}
								}
								if(cout>0) {
									allwords.add(word);
								}
								cout=0;

							}
						}
					}
				}
			}

			System.out.print("Any known letters w/position (green tiles) (y/n): ");
			char choice = scan.next( ).charAt(0);
			if(choice=='y') {
				HashMap <Integer,Character> confirmed_letters = new HashMap <Integer,Character>(); // cranmightjollyw
				char c = 'y';
				int counter = 0;
				while(c=='y') {
					System.out.print("Enter the letter: ");
					String lett = scan.next( );
					lett = lett.toUpperCase( );
					char letter = lett.charAt(0);
					
					int cccc = 0;
					for(int z=0; z<letters_not_there.length( ); z++) {
						if(letter == letters_not_there.charAt(z)) {
							cccc++;
							System.out.println("\nLetter '" + letter + "' CANNOT be useless and useful at the same time");
							System.out.println("Skipping to the next character...\n");
							break;
						}
					}
					
					if(cccc>0) {
						continue;
					}

					System.out.print("Enter its position (start=0): ");
					int pos = scan.nextInt( );
					
					confirmed_letters.put(pos, letter);
					counter++;

					System.out.print("Have another letter? (y/n): ");
					c = scan.next( ).charAt(0);
					
				}
				for(int i=0; i<counter; i++) {
					char ch = (char) confirmed_letters.values( ).toArray( )[i];
					int pos = (int) confirmed_letters.keySet( ).toArray( )[i];
					for(int j=0; j<allwords.size( ); j++) {
						String word = allwords.get(j);
						if(word.charAt(pos)!=ch) {
							allwords.remove(j);
							j--;
						}
					}
				}	
			}

			System.out.print("\nAny known words wo/position? (yellow tiles) (y/n): ");
			char c = scan.next( ).charAt(0);
			if(c=='y') {
				System.out.print("Enter the letter(s): ");
				String le = scan.next( );
				le = le.toUpperCase( );
				le = duplicateRemover(le);
				char [] arr = new char[le.length()];
				for(int i=0; i<le.length( ); i++) {
					arr[i] = le.charAt(i);
				}
				for(int j=0; j<allwords.size( ); j++) {
					if(!isThere(allwords.get(j),arr)){
						allwords.remove(j);
						j--;
					}
				}	

				for(int i=0; i<arr.length; i++) {
					System.out.print("Enter the position number(s) where " + arr[i] + " is not supposed to be: ");
				    String nu = scan.next( );
					int lenn = nu.length( );
					int [] ar1 = new int[lenn];
					for(int z=0; z<lenn; z++) {
						ar1[z] = Character.getNumericValue(nu.charAt(z));
					}
					for(int k=0; k<lenn; k++) {
						for(int j=0; j<allwords.size( ); j++) {
							String wor = allwords.get(j);
							if(wor.charAt(ar1[k])==arr[i]) {
								allwords.remove(j);
								j--;
							}
						}
					}
				}
				System.out.println("\n--------------------------------------------\nThe list of words: ");
				for(String i: allwords) {
					System.out.println(i);
				}
			}
			else {
				System.out.println("\n\nThe list of words: ");
				for(String i: allwords) {
					System.out.println(i);
				}
			}

			scan.close( );
			sc2.close( );
			sc1.close( );
		} catch (Exception e) {
			System.out.println("An error occured ");
			e.printStackTrace();
		}

	}

}
