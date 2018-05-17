/*

SimpleSymbols.java
Developed by Sunghyun Cho on 14 January 2018.

Challenge:
Using the Java language, have the function SimpleSymbols(str) take the str parameter being passed and determine
if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed
of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter
must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 

Sample Test Cases

    Input:"+d+=3=+s+"
    Output:"true"

    Input:"f++d+"
    Output:"false"

*/

import java.util.*; 
import java.io.*;

class SimpleSymbols {  
  public static String simpleSymbols(String str) { 
  
  	if(firstLetterIsLetter(str)) return "false because firstLetterIsLetter";
  	if(lastLetterIsLetter(str)) return "false because lastLetterIsLetter";

  	char[] charArray = new char[str.length()];
  	for(int x = 0; x < charArray.length; x++) charArray[x] = str.charAt(x);
  	//charArray initiate;

  	for(int x = 1; x < charArray.length-1; x++) {
  		if(97<=charArray[x]&&charArray[x]<=122||65<=charArray[x]&&charArray[x]<=90) {

  		if(letterIsNotPlusBefore(x, charArray)) return "false because letterIsNotPlusBefore";
  		if(letterIsNotPlusAfter(x, charArray)) return "false because letterIsNotPlusAfter";

  		}
  	}
    return "true";
  } 

public static boolean letterIsNotPlusBefore(int x, char[] charArray) {
	//System.out.println("Letter Before charArray["+x+"] is "+charArray[x-1]+", therefore "+(charArray[x-1]!='+'));
	return charArray[x-1]!='+';
}

public static boolean letterIsNotPlusAfter(int x, char[] charArray) {
	//System.out.println("Letter After charArray["+x+"] is "+charArray[x+1]+", therefore "+(charArray[x+1]!='+'));
	return charArray[x+1]!='+';
}

public static boolean firstLetterIsLetter(String str) {
	return 97<=str.charAt(0)&&str.charAt(0)<=122||65<=str.charAt(0)&&str.charAt(0)<=90;
}

public static boolean lastLetterIsLetter(String str) {
	return 97<=str.charAt(str.length()-1)&&str.charAt(str.length()-1)<=122||65<=str.charAt(str.length()-1)&&str.charAt(str.length()-1)<=90;
}
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.println(SimpleSymbols(s.nextLine())); 
  }   
  
}


  