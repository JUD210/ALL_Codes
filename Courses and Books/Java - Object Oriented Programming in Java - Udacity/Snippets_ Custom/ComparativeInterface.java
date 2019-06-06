// 2018.05.31

// package _MySnippets.interfaces;

public class ComparativeInterface {
    public static void main(String[] args) {
        Book b1 = new Book();
        Book b2 = new Book(100, "a", "hyeogi");
        System.out.println(b1.compareTo(b2));
    }
}

class Book {

    int numberOfPages;
    String title;
    String author;

    Book() {
        numberOfPages = 100;
        title = "aaaaaa";
        author = "Hyuk";
    }

    Book(int numberOfPages, String title, String author) {
        this.numberOfPages = numberOfPages;
        this.title = title;
        this.author = author;
    }

    public int compareTo(Book specifiedBook) {
        // First check if they have different page counts
        if (this.numberOfPages != specifiedBook.numberOfPages) {
            // this will return a negative value if this < specified but will return a positive value if this > specified
            return this.numberOfPages - specifiedBook.numberOfPages;
        }
        // If page counts are identical then check if the titles are different
        if (!this.title.equals(specifiedBook.title)) {
            return this.title.compareTo(specifiedBook.title);
        }
        // If page titles are also identical then return the comparison of the authors
        return this.author.compareTo(specifiedBook.author);
    }
}