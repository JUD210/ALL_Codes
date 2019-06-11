package spaceChallenge;

import java.util.Comparator;

public class Item {
    String name;
    int weight;
    boolean isLoaded;

    Item(String name, int weight, boolean isLoaded) {
        this.name = name;
        this.weight = weight;
        this.isLoaded = isLoaded;
    }

    public static Comparator<Item> itemNameComparator = new Comparator<Item>() {
        @Override
        public int compare(Item item1, Item item2) {
            // Ascending order
            return item1.name.toUpperCase().compareTo(
                    item2.name.toUpperCase());
        }
    };

    public static Comparator<Item> itemWeightComparator = new Comparator<Item>() {
        @Override
        public int compare(Item item1, Item item2) {
            // Descending order
            return item2.weight - item1.weight;
        }
    };


}
