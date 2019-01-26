import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

class Refactorings {
    public static final String FileFormat_Text = "txt";

    public static void main(String[] args) throws IOException {
        String[] array = getStrings(new FileReader("input." + FileFormat_Text));
        Arrays.sort(array);
        for (String s : array) {
            System.out.println(s);
        }
    }

    private static String[] getStrings(FileReader in) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(in);
        BufferedReader reader = bufferedReader;
        ArrayList<String> lines = new ArrayList<String>();
        String line;
        while ((line = reader.readLine()) != null) {
            lines.add(line);
        }
        reader.close();
        return lines.toArray(new String[lines.size()]);
    }
}