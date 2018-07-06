# D180114.java

###### Developed by Sunghyun Cho on January 14th, 2018.

### Problem

Have the function KaprekarsConstant(num) take the num parameter being passed which
will be a 4-digit number with at least two distinct digits. Your program should
perform the following routine on the number: Arrange the digits in descending order
and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract
the smaller number from the bigger number. Then repeat the previous step. Performing
this routine will always cause you to reach a fixed number: 6174. Then performing the
routine on 6174 will always give you 6174 (7641 - 1467 = 6174). Your program should
return the number of times this routine must be performed until 6174 is reached.

Hard challenges are worth 15 points and you are not timed for them.
Use the Parameter Testing feature in the box below to test your code with different arguments.


### Example

```
If num is 3524 your program should return 3 because of the following steps:
(1) 5432 - 2345 = 3087
(2) 8730 - 0378 = 8352
(3) 8532 - 2358 = 6174. 
```

### Code

```java
import java.util.*; 
import java.io.*;

class KaprekarsConstant {  
    public static int KaprekarsConstant(int num) { 
        int counter = 0;
        int temp = num;
        do {
            counter++;
            temp=maxify(temp)-minify(temp);
        }while(6174!=temp);
        return counter;
    } 

    public static int minify(int num) {
        int[] numbers = new int[4];
        for(int x = 3; x >= 0; x--) {
            numbers[x] = (int)(num/Math.pow(10,x));
            num%=(int)Math.pow(10,x);
        }
        Arrays.sort(numbers);
        return numbers[0]*1000+numbers[1]*100+numbers[2]*10+numbers[3];
    }

    public static int maxify(int num){
        int[] numbers = new int[4];
        for(int x = 3; x >= 0; x--) {
            numbers[x] = (int)(num/Math.pow(10,x));
            num%=(int)Math.pow(10,x);
        }
        Arrays.sort(numbers);
        return numbers[3]*1000+numbers[2]*100+numbers[1]*10+numbers[0];
  }

    public static void main (String[] args) {  
        // keep this function call here     
        Scanner s = new Scanner(System.in);
        System.out.print(KaprekarsConstant(s.nextInt())); 
  }   
}
```
