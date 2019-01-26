package Project.guessTheMovie;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class GameManager {

    boolean isGameOn;

    String answer;
    String displayingAnswer;

    List<AnswerChar> answerChars;
    int answeredCharsCount;
    int round;

    /**
     * Construct a GameManager Object<br>
     * this.isGameOn = true;<br>
     * this.answer = selectMovie(scanMovieList());<br>
     * initAnswerChars(this.answer);<br>
     */
    GameManager() {
        this.isGameOn = true;
        this.answer = selectMovie(scanMovieList());
        initAnswerChars(this.answer);
        this.answeredCharsCount = 0;
        this.round = 0;
    }

    /**
     * Scan/Load MovieList.txt file
     *
     * @return loaded txt file
     */
    private Scanner scanMovieList() {
        try {
            return new Scanner(new File
                    ("C:\\Users\\Hyuk\\Desktop\\_AndroidStudio\\_JavaPractices\\src\\Project\\guessTheMovie\\MovieList.txt"));
        } catch (FileNotFoundException e) {
            System.out.println(e + "!");
            return null;
        }
    }

    /**
     * Select a random movie from the scannedMovieList
     *
     * @param scannedMovieList `
     * @return selectedMovie
     */
    private String selectMovie(Scanner scannedMovieList) {
        List<String> movieList = new ArrayList<String>();

        while (scannedMovieList.hasNextLine()) {
            movieList.add(scannedMovieList.nextLine());
        }

        return movieList.get((int) (Math.random() * movieList.size()));
    }

    /**
     * Initiate Answer's Character List<br>
     * (List< AnswerChar > answerChar)
     *
     * @param answer;
     */
    private void initAnswerChars(String answer) {
        this.answerChars = new ArrayList<AnswerChar>();

        for (int i = 0; i < answer.length(); i++) {
            String tempChar = answer.charAt(i) + "";
            if (tempChar.matches("[a-zA-Z]"))
                this.answerChars.add(i, new AnswerChar(answer.charAt(i), false));
            else
                this.answerChars.add(i, new AnswerChar(answer.charAt(i), true));
        }
    }

    /**
     * If player.guessedChar equals AnswerChar.character,<br>
     * make the AnswerChar.isGuessed true.
     */
    private void updateAnswerChars(List<AnswerChar> answerChars) {
        this.answeredCharsCount = 0;

        for (AnswerChar aC : answerChars) {
            if (!aC.isGuessed) {
                for (Character gC : GuessTheMovie.player.guessedChars) {
                    if (aC.character == gC) {
                        aC.isGuessed = true;
                        this.answeredCharsCount++;
                    }
                }
            } else
                this.answeredCharsCount++;
        }
        this.answerChars = answerChars;
    }

    /**
     * Converts answer to displayingAnswer.<br>
     * If a AnswerChar.isGuessed == true, do not replace that letter <br>
     * else _
     *
     * @param answerChars `
     */
    private void updateDisplayingAnswer(List<AnswerChar> answerChars) {
        this.displayingAnswer = "";
        for (AnswerChar aC : answerChars) {
            if (aC.isGuessed)
                this.displayingAnswer += aC.character;
            else
                this.displayingAnswer += "_";
        }
    }

    void displayCurrentStatus() {
        updateAnswerChars(this.answerChars);
        updateDisplayingAnswer(this.answerChars);
        this.round++;

        System.out.println("\n-----Round " + this.round + "-----");
        System.out.println("◎You are guessing: " + this.displayingAnswer + " (" + this.answeredCharsCount + "/" + answerChars.size() + ")");
        System.out.println("○You have guessed: " + GuessTheMovie.player.guessedChars);
        System.out.println("<" + GuessTheMovie.player.leftOpportunity + "> Opportunity left.");
    }

    /**
     * Determine whether GameOver it is.
     */
    private void determineGameOver() {
        if (GuessTheMovie.player.leftOpportunity == 0) {
            System.out.println("It was so close.. Better luck next time. :)");
            isGameOn = false;
        } else if (this.answeredCharsCount == answerChars.size()) {
            System.out.println("Congratulations! You Won the Game!! :D");
            isGameOn = false;
        }
    }

    /**
     * Receive an alphabet input from the Player,<br>
     * and add that alphabet to the GuessTheMovie.player.guessedChars (List < Character>). <br>
     * <br>
     * If the player guess a wrong alphabet, GuessTheMovie.player.leftOpportunity decreases by -1, <br>
     * and determine whether GameOver it is.<br>
     * cf) determineGameOver();
     */
    void inputAChar() {
        determineGameOver();

        while (this.isGameOn) {
            System.out.print("Guess a letter: ");
            Scanner scanner = new Scanner(System.in);
            String tempInput = scanner.nextLine().toLowerCase();
            boolean isPassed = true;

            if (tempInput.length() == 1 && tempInput.matches("[a-zA-Z]")) {

                for (Character gC : GuessTheMovie.player.guessedChars) {
                    if (tempInput.charAt(0) == gC) {
                        System.out.println("You already entered that! choose another.");
                        isPassed = false;
                        break;
                    }
                }

                if (isPassed) {
                    if (this.answer.contains(tempInput.charAt(0) + "")) {
                        GuessTheMovie.player.guessedChars.add(tempInput.charAt(0));
                        return;
                    } else {
                        GuessTheMovie.player.guessedChars.add(tempInput.charAt(0));
                        GuessTheMovie.player.leftOpportunity--;
                        return;
                    }
                }
            } else {
                System.out.println("Please enter an alphabet ONLY.");
            }
        }
    }
}
