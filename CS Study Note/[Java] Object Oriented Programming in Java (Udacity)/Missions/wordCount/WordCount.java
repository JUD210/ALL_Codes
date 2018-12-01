//from 2018.05.
//to 2018.05.

package Project.wordCount;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class WordCount {
    public static void main(String[] args) throws Exception {
        try {
            File file = new File("C:\\Users\\Hyuk\\Desktop\\_AndroidStudio\\_JavaPractices\\src\\Project\\wordCount\\TEST.txt");
            Scanner scanner = new Scanner(file);
            int wordCount = 0;
            int lineCount = 1;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println("line [" + lineCount + "] " + line.split(" ").length + " words");
                wordCount += line.split(" ").length;
                lineCount++;
            }
        }
        catch (FileNotFoundException e) {
            System.out.println(e+"!!");
        }

    }
}
