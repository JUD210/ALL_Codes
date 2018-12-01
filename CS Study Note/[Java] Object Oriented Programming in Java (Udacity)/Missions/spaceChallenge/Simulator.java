package spaceChallenge;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Simulator {

    static int totalItemsWeight;

    /**
     * Read all items in a ArrayList from a text file using file argument,
     * and Sort the ArrayList in descending order of weight,
     * then returns an ArrayList of Items.
     *
     * @param phase Phase 1 or 2
     * @return Read & Sorted itemList
     */

    ArrayList<Item> readItemList(int phase) {
        totalItemsWeight = 0;
        ArrayList<Item> itemList = new ArrayList<>();

        String filePath;
        switch (phase) {
            case 1:
                filePath = "C:\\Users\\Hyuk\\Desktop\\_AndroidStudio\\_JavaPractices\\src\\Project\\spaceChallenge\\Phase1.txt";
                break;
            case 2:
                filePath = "C:\\Users\\Hyuk\\Desktop\\_AndroidStudio\\_JavaPractices\\src\\Project\\spaceChallenge\\Phase2.txt";
                break;
            default:
                System.out.println("[Debug] Something is wrong.");
                return null;
        }

        File file = new File(filePath);

        try {
            //Can throw FileNotFoundException
            Scanner scanner = new Scanner(file);

            while (scanner.hasNextLine()) {
                String[] nextLineSplit = scanner.nextLine().split("=");
                itemList.add(new Item(nextLineSplit[0], Integer.parseInt(nextLineSplit[1]), false));
                totalItemsWeight += Integer.parseInt(nextLineSplit[1]);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("Total items Weight: " + totalItemsWeight + "Kg");

        itemList.sort(Item.itemNameComparator);
        itemList.sort(Item.itemWeightComparator);
        return itemList;
    }

    /**
     * Takes the ArrayList of Items returned from readItemList and starts creating U1 rockets.
     * <p>
     * It first tries to fill up 1 rocket with as many items as possible before creating
     * a new rocket object and filling that one until all items are loaded.
     * <p>
     *
     * @param itemList from sortItemList(ArrayList< Item>);
     * @return Created ArrayList < U1 > //that are fully loaded.
     */

    ArrayList<Rocket> createAndLoadRockets(ArrayList<Item> itemList, String rocketType) {
        ArrayList<Rocket> allRockets = new ArrayList<>();
        Rocket rocket = null;

        int loadedItemCount = 0;
        while (loadedItemCount != itemList.size()) {
            switch (rocketType) {
                case "U1":
                    rocket = new U1();
                    break;
                case "U2":
                    rocket = new U2();
                    break;
                default:
                    return null;
            }

            for (Item item : itemList) {
                if (!item.isLoaded) {
                    if (rocket.canLoad(item)) {
                        rocket.load(item);

                        loadedItemCount++;
                        item.isLoaded = true;
                    }
                }
            }

            if (rocket.cargoWeight != 0)
                allRockets.add(rocket);
        }
        return allRockets;
    }

    /**
     * Takes an ArrayList of Rockets and calls launch and land methods
     * for each of the rockets in the ArrayList. <p>
     * Every time a rocket explodes or crashes (i.e if launch or land return false)
     * it will have to send that rocket again. <p>
     * All while keeping track of the total budget required to send each rocket safely to Mars.
     *
     * @return The total budget required to send all rockets (including the crashed ones).
     */
    int runSimulation(ArrayList<Rocket> rockets, int simulationCount) {
        int averageBudget = 0;

        for (int i = 0; i < simulationCount; i++) {
            int budget = 0;

            for (Rocket rocket : rockets) {
                budget += rocket.cost;

                while (true) {
                    if (rocket.launch()) {
                        while (true) {
                            if (rocket.land()) {
                                break;
                            } else {
                                budget += rocket.cost;
                            }
                        }
                        break;
                    } else {
                        budget += rocket.cost;
                    }
                }
            }
            averageBudget += budget;
        }
        return averageBudget / simulationCount;
    }
}
