package spaceChallenge;

import java.io.File;
import java.util.Scanner;

public class Selector {

    public static int selectPhase() {
        while (true) {
            System.out.println("\n< Waiting input > Select Phase.  [ Input 1 or 2 ]");
            Scanner scanner = new Scanner(System.in);

            if (scanner.hasNextInt()) {
                switch (scanner.nextInt()) {
                    case 1:
                        return 1;
                    case 2:
                        return 2;
                    default:
                        System.out.println("< Error > Please input 1 or 2 ONLY.");
                        break;
                }
            } else {
                System.out.println("< Error > Please input 1 or 2 ONLY.");
            }
        }
    }

    public static String selectRocketType() {
        while (true) {
            System.out.println("\n< Waiting input > Select rocket type.  [ Input 1 or 2 ]");
            System.out.println("(Type 1) cost: 100 Million $, rocketWeight: 10000 Kg, maxCargoWeight = 8000 Kg");
            System.out.println("(Type 2) cost: 120 Million $, rocketWeight: 18000 Kg, maxCargoWeight = 11000 Kg");

            Scanner scanner = new Scanner(System.in);

            if (scanner.hasNextInt()) {
                switch (scanner.nextInt()) {
                    case 1:
                        return "U1";
                    case 2:
                        return "U2";
                    default:
                        System.out.println("< Error > Please input 1 or 2 ONLY.");
                        break;
                }
            } else {
                System.out.println("< Error > Please input 1 or 2 ONLY.");
            }
        }
    }

    public static int selectSimulationCount() {
        while (true) {
            System.out.println("\n< Waiting input > Select simulation count.  [ Input integer 1 ~ 100000 ]");
            Scanner scanner = new Scanner(System.in);

            if (scanner.hasNextInt()) {
                int input = scanner.nextInt();

                if (input > 0 && input <= 100000) {
                    return input;
                } else {
                    System.out.println("< Error > Please input integer 1 ~ 100000 ONLY.");
                }
            } else {
                System.out.println("< Error > Please input integer 1 ~ 100000 ONLY.");
            }
        }
    }

    public static boolean selectContinue() {
        while (true) {
            System.out.println("\n< Waiting input > Want to continue simulating?  [ Input y(yes) or n(no) ]");
            Scanner scanner = new Scanner(System.in);

            if (scanner.hasNextLine()) {
                String input = scanner.nextLine();

                switch (input) {
                    case "y":
                        return true;
                    case "Y":
                        return true;
                    case "n":
                        return false;
                    case "N":
                        return false;
                    default:
                        System.out.println("< Error > Please input y or n ONLY.");
                        break;
                }
            } else {
                System.out.println("< Error > Please input y or n ONLY.");
            }
        }
    }
}