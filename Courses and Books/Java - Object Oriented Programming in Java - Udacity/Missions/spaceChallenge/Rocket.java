package spaceChallenge;

import java.util.ArrayList;

interface SpaceShip {
    /**
     * Returns either true or false indicating if the launch was successful or
     * if the rocket has crashed.
     *
     * @return boolean
     */
    boolean launch();

    /**
     * Returns either true or false based on the success of the landing.
     *
     * @return boolean
     */
    boolean land();

    /**
     * Takes an Item as an argument and returns true if the rocket can carry such item
     * or false if it will exceed the weight limit.
     *
     * @return boolean
     */
    boolean canLoad(Item item);

    /**
     * Takes an Item object and updates the current weight of the rocket.
     */
    void load(Item item);
}


public class Rocket implements SpaceShip, Cloneable {
    int cost; // ex) 100 Million $
    int rocketWeight; // ex) 10000 Kg (= 10 Tonnes)
    int cargoWeight; // ex) 7250 Kg
    int maxCargoWeight; // ex) 8000 Kg

    ArrayList<Item> carryingItems = new ArrayList<>();

    @Override
    public boolean launch() {
        System.out.println("[Error] launch() in Rocket class");
        return true;
    }

    @Override
    public boolean land() {
        System.out.println("[Error] land() in Rocket class");
        return true;
    }

    @Override
    public boolean canLoad(Item item) {
        return cargoWeight + item.weight <= maxCargoWeight;
    }

    @Override
    public void load(Item item) {
        carryingItems.add(item);
        cargoWeight += item.weight;
    }

    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}


class U1 extends Rocket {
    U1() {
        cost = 100; // Million $
        rocketWeight = 10000; //Kg
        cargoWeight = 0;
        maxCargoWeight = 8000;
    }

    @Override
    public boolean launch() {
        double randomNum = Math.random() * 100;
        double chanceOfExplosion = 5 * ((cargoWeight) / (maxCargoWeight));

        return randomNum > chanceOfExplosion;
    }

    @Override
    public boolean land() {
        double randomNum = Math.random() * 100;
        double chanceOfCrash = ((cargoWeight) / (maxCargoWeight));

        return randomNum > chanceOfCrash;
    }
}


class U2 extends Rocket {
    U2() {
        cost = 120; // Million $
        rocketWeight = 18000; //Kg
        cargoWeight = 0;
        maxCargoWeight = 11000;
    }

    @Override
    public boolean launch() {
        double randomNum = Math.random() * 100;
        double chanceOfExplosion = 4 * ((cargoWeight) / (maxCargoWeight));

        return randomNum > chanceOfExplosion;
    }

    @Override
    public boolean land() {
        double randomNum = Math.random() * 100;
        double chanceOfCrash = 8 * ((cargoWeight) / (maxCargoWeight));

        return randomNum > chanceOfCrash;
    }
}