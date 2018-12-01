//from 2018.06.04
//to 2018.06.??

package spaceChallenge;

import java.util.ArrayList;

public class SpaceChallenge {
    static ArrayList<String> results = new ArrayList<>();
    static int simulationNum = 0;

    public static void main(String[] args) {

        while (true) {
            Simulator simulator = new Simulator();
            simulationNum++;

            printHello();


            int phase = Selector.selectPhase();

            ArrayList<Item> itemList = simulator.readItemList(phase);
            printItemList(phase, itemList);


            String rocketType = Selector.selectRocketType();

            ArrayList<Rocket> allRockets = simulator.createAndLoadRockets(itemList, rocketType);
            printRocketsState(rocketType, allRockets);


            int simulationCount = Selector.selectSimulationCount();

            int estimatedBudget = simulator.runSimulation(allRockets, simulationCount);
            printSimulationResults(phase, rocketType, simulationCount, allRockets.size(), estimatedBudget);

        }
    }

    public static void printHello() {
        System.out.println("\n========= New Simulation Start =========");
    }

    public static void printItemList(int phase, ArrayList<Item> itemList) {
        System.out.println("\n=== Phase" + phase + "'s item list ===\n");
        for (Item item : itemList) {
            System.out.println(item.name + ": " + item.weight + "Kg");
        }
    }

    public static void printRocketsState(String rocketType, ArrayList<Rocket> allRockets) {
        System.out.println("\n=== All " + rocketType + " Rocket's State ===");
        int tempCounter = 0;
        for (Rocket rocket : allRockets) {
            tempCounter++;
            System.out.println("\n" + rocketType + "[" + tempCounter + "]: " + rocket.cargoWeight + " / " + rocket.maxCargoWeight);
            for (Item item : rocket.carryingItems) {
                System.out.println(item.name + "(" + item.weight + " Kg)");
            }
        }
    }

    public static void printSimulationResults(int phase, String rocketType, int simulationCount, int rocketCount, int estimatedBudget) {
        System.out.println("\n=== All Simulation Results ===\n");

        results.add("< Simulation [" + simulationNum + "] > The average budget of all [" + rocketCount + "] [" + rocketType + "] rockets in phase[" + phase +
                "] (total ["+Simulator.totalItemsWeight+"] Kg) estimated from [" + simulationCount + "] simulations: [" + estimatedBudget + "] Million $");

        // Below statement is almost equals with System.out.println(results);
        for (String result : results) {
            System.out.println(result);
        }
    }
}

/* TD: [Additional Quest 1]
   ? Merge createAndLoadU1s and createAndLoadU2s.
 */

/* TD: [Additional Quest 2]
   ? Add price in Item.
   ? Add Items' price on the budget too.
   ? Implementing Comparator interface, make two simulator.
   1. (original) Fill up rockets in descending order of weight.
   2. (custom) Fill up rockets in descending order of price.
 */

/* To Do Lists

TD: To Do List
ex) TD: Build a character leveling system.

TDL: To Do Later list
ex) TDL: Optimize codes

UC: Under Construction
ex) void initPlayer() { //UC }

*/



/* Naming Convention

o Classes and Interfaces : UpperCamelCase
ex) HouseBlueprint

o Methods : lowerCamelCase
ex) changeColor

o Variables (Object too.) : lowerCamelCase
ex) houseColor, redHouse
ex) Temp int: i,j,k,m,n
ex) Temp char: c,d,e

o Constant Variables : UPPERCASE
ex) MIN_WIDTH

o Packages : lowercase
ex) com.jud210.appName.subpackages

A common naming scheme used is the following (| means or):
country | org | com.name.applicationName.subpackages (name is either a company or your name.)

And after the applicationName you start all your subpackages (that is what I mean in the end)
e.g. util, ui,db etc.

ex) hyphenated-name.example.org: org.example.hyphenated_name
ex) example.int: int_.example
ex) 123name.example.com: com.example._123name

*/



/* Pseudo Code Example

``Game Dev Flow

    O Write some code that will simply read the movie list and display the whole list.
    O Then add to your code to randomly pick one movie and display that title only.
    ...
    ? Finally, detect when they have guessed all the letters and let them know they've won!

``Program Dev Flow

    O make a select menu //s: start, q: quit
    ? if s) merge the game: while(isGameOn)
    ? if q) quit

*/

