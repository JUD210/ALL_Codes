/* 
https://www.hackerrank.com/challenges/forward-references/problem?h_r=next-challenge&h_v=zen


NOTE - Forward reference is supported by JGsoft, .NET, Java, Perl, PCRE, PHP, Delphi and Ruby regex flavors.


Inputs
standard_input = """tactactictactic"""

 */

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {    

    public static void main(String[] args) {
        
        Regex_Test tester = new Regex_Test();
        
        // Use \\ instead of using \ 

        tester.checker("^(\\2tic|(tac))*$"); 

        // tester.checker("^tac(tac(tic)?)*$"); 
    
    }
}

class Regex_Test {

    public void checker(String Regex_Pattern){
    
        Scanner Input = new Scanner(System.in);
        String Test_String = Input.nextLine();
        Pattern p = Pattern.compile(Regex_Pattern);
        Matcher m = p.matcher(Test_String);
        System.out.println(m.find());
    }   
    
}