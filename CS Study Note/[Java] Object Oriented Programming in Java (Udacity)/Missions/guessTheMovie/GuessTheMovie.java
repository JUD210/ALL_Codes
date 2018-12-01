//from 2018.05.24
//to 2018.05.29

package Project.guessTheMovie;

public class GuessTheMovie {

    static GameManager gameManager = new GameManager();
    static Player player = new Player();

    public static void main(String[] args) {
        while (gameManager.isGameOn) {
            gameManager.displayCurrentStatus();
            gameManager.inputAChar();
        }
    }
}

/* Pseudo Code

``Game Dev Flow

    O Write some code that will simply read the movie list and display the whole list.
    O Then add to your code to randomly pick one movie and display that title only.
    O Then convert its letters to underscores (_) and display that instead, and so on.
    O Once you've got that part done start reading the user's input and search for it in the title.
    O Work on revealing the correct letters and displaying them.
    O Add the logic to keep track of wrong letters so they don't lose points for guessing the same letter twice.
    O After that, you can keep track of how many wrong guesses and end the game if they lose.
    O Finally, detect when they have guessed all the letters and let them know they've won!

 */


/* To Do Lists

TD: To Do List
TDL: To Do Later list
UC: Under Construction

 */