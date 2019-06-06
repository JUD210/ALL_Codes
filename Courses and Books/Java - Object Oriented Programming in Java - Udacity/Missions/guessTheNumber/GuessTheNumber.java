//from 2018.05.
//to 2018.05.

package Project.guessTheNumber;

import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {

        GameManager gameManager = new GameManager();
        Player player = new Player();
        new Computer();

        System.out.println("Computer Selected a number between 1-100.\nGuess what the number is and enter it.");
        System.out.println("Do you want to use autoHack? (Answer: y or n)");

        label:
        while (true) {
            String answer = new Scanner(System.in).nextLine();

            switch (answer) {
                case "y":
                    player.isAuto = true;
                    break label;
                case "n":
                    player.isAuto = false;
                    break label;
                default:
                    System.out.println("Input y or n ONLY");
            }
        }

        while (gameManager.isGameOn) {
            if (player.remainingOpportunity == 0) {
                System.out.println("You Lose...");
                gameManager.isGameOn = false;
                break;
            } else {
                if (player.remainingOpportunity == 10)
                    System.out.println("Try it!");
                player.guessNumber(player.isAuto);
            }

            if (player.guessedNumber < Computer.selectedNumber) {
                player.remainingOpportunity--;
                System.out.println(player.guessedNumber + " is less than the answer number. (" + player.remainingOpportunity + " opportunity left)");
            } else if (player.guessedNumber > Computer.selectedNumber) {
                player.remainingOpportunity--;
                System.out.println(player.guessedNumber + " is Greater than the answer number. (" + player.remainingOpportunity + " opportunity left)");
            } else if (player.guessedNumber == Computer.selectedNumber) {
                System.out.println("Yeah! It was " + player.guessedNumber + ". You Won! :D");
                gameManager.isGameOn = false;
                break;
            }
        }
        System.out.println("[ GameOver ]");
    }
}

class Player {
    Boolean isAuto;
    int guessedNumber;
    int remainingOpportunity;

    void guessNumber(boolean isAuto) {
        if (!isAuto) {
            this.guessedNumber = new Scanner(System.in).nextInt();
        } else {
            if (this.remainingOpportunity == 10) {
                this.guessedNumber = 50;
            } else {
                int temp = (this.guessedNumber + Computer.selectedNumber) / 2;
                if (this.guessedNumber != temp)
                    this.guessedNumber = temp;
                else
                    this.guessedNumber = temp + 1;
            }
        }
    }

    Player() {
        this.isAuto = false;
        this.remainingOpportunity = 10;
    }
}

class Computer {
    public static int selectedNumber;

    private void selectNumber() {
        //Integer 1~100
        selectedNumber = (int) (Math.random() * 100 + 1);
    }

    Computer() {
        selectNumber();
    }
}

class GameManager {
    boolean isGameOn;

    GameManager() {
        isGameOn = true;
    }
}


/* Pseudo Code

1. Get a random number.
2. Make a loop that asks player to guess a number.
2-1. Read the player's input number and compare it with the random number.
2-2. Let the player know if the guessed number was greater or less than the random number.
2-3. loop 2-1, 2-2 up to 10 times until player wins.
3-1. If the player wins, print a message and end the game.
3-2. If the player loses, print a message and end the game.

*/
