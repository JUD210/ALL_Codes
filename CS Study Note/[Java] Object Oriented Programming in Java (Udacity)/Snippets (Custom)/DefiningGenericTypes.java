// 2018.05.31

// package _MySnippets.genericTypes;

import java.util.ArrayList;

public class DefiningGenericTypes {

    public static void main(String[] args) {
        System.out.println("\n==== Using Generics ====\n");
        ArrayList<String> strings = new ArrayList<>();
        strings.add("test1 ");
        strings.add("test2 ");
        strings.add("test3 ");

        OrderedPair<ArrayList<String>, String, Integer> orderedPair = new OrderedPair<>(strings, strings.get(1), 999);

        System.out.println(orderedPair.getObject());
        System.out.println(orderedPair.getString());
        System.out.println(orderedPair.getInteger());



        System.out.println("\n==== Not Using Generics ====\n");
        ArrayList<String> strings_ = new ArrayList<>();
        strings_.add("test1_ ");
        strings_.add("test2_ ");
        strings_.add("test3_ ");

        OrderedPair_ orderedPair_ = new OrderedPair_(strings_, strings_.get(1), 9999);

        System.out.println(orderedPair_.getObject());
        System.out.println(orderedPair_.getString());
        System.out.println(orderedPair_.getInteger());
    }
}

interface Pair<O, S, I> {
    public O getObject();

    public S getString();

    public I getInteger();
}

interface Pair_ {
    public Object getObject();
    public String getString();
    public Integer getInteger();
}

class OrderedPair<O, S, I> implements Pair<O, S, I> {

    private O object;
    private S string;
    private I integer;

    public OrderedPair(O object, S string, I integer) {
        this.object = object;
        this.string = string;
        this.integer = integer;
    }

    public O getObject() {
        return this.object;
    }

    public S getString() {
        return this.string;
    }

    public I getInteger() {
        return this.integer;
    }
}

class OrderedPair_ implements Pair_{
    private Object object;
    private String string;
    private Integer integer;

    public OrderedPair_(Object object, String string, Integer integer) {
        this.object = object;
        this.string = string;
        this.integer = integer;
    }

    public Object getObject() {
        return this.object;
    }

    public String getString() {
        return this.string;
    }

    public Integer getInteger() {
        return this.integer;
    }

}