// package _MySnippets.comparatorAndComparable;

import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;

public class ComparatorAndComparable {
    public static void main(String args[]) {
        System.out.println("\n==== ver1 start ====\n");

        ArrayList<Student_ver1> student_ver1List = new ArrayList<Student_ver1>();
        student_ver1List.add(new Student_ver1(101, "Zues", 26));
        student_ver1List.add(new Student_ver1(505, "Abey", 24));
        student_ver1List.add(new Student_ver1(809, "Vignesh", 32));

        // Sorting based on Student Name
        System.out.println("Student Name Sorting:");

        // == Collections.sort(student_ver1List, Student_ver1.stuNameComparator);
        student_ver1List.sort(Student_ver1.stuNameComparator);

        for (Student_ver1 str : student_ver1List) {
            System.out.println(str);
        }

        // Sorting based on rollNum
        System.out.println("rollNum Sorting:");

        // == Collections.sort(student_ver1List, Student_ver1.stuRollNum);
        student_ver1List.sort(Student_ver1.stuRollNum);

        for (Student_ver1 str : student_ver1List) {
            System.out.println(str);
        }

        //////////////////////////////////
        System.out.println("\n==== ver2 start ====\n");

        ArrayList<Student_ver2> student_ver2List = new ArrayList<>();
        student_ver2List.add(new Student_ver2(223, "Chaitanya", 26));
        student_ver2List.add(new Student_ver2(245, "Rahul", 24));
        student_ver2List.add(new Student_ver2(209, "Ajeet", 32));

        // choice 1. Comparator<Student_ver2>
/* I don't know correct syntax of this statements.
        student_ver2List.sort(Student_ver2.);

        for (Student_ver2 str : student_ver2List) {
            System.out.println(str);
        }
*/

        // choice 2. Comparable<Student_ver2>
        Collections.sort(student_ver2List);

        for (Student_ver2 str : student_ver2List) {
            System.out.println(str);
        }
    }
}

class Student_ver1 /* Making Comparators */ {
    private String studentName;
    private int num;
    private int studentAge;

    public Student_ver1(int num, String studentName, int studentAge) {
        this.num = num;
        this.studentName = studentName;
        this.studentAge = studentAge;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public int getRollNum() {
        return num;
    }

    public void setRollNum(int num) {
        this.num = num;
    }

    public int getStudentAge() {
        return studentAge;
    }

    public void setStudentAge(int studentAge) {
        this.studentAge = studentAge;
    }

    /*Comparator for sorting the list by Student Name*/
    public static Comparator<Student_ver1> stuNameComparator = new Comparator<Student_ver1>() {
        public int compare(Student_ver1 s1, Student_ver1 s2) {
            String StudentName1 = s1.getStudentName().toUpperCase();
            String StudentName2 = s2.getStudentName().toUpperCase();

            System.out.println("Using static Comparator<Student_ver1> stuNameComparator = new Comparator<Student_ver1>(){ public int compare(Student_ver1 s1, Student_ver1 s2){ } }");
            System.out.println("return (StudentName1.compareTo(StudentName2)): " + StudentName1.compareTo(StudentName2));

            //ascending order
            return s1.getStudentName().toUpperCase().compareTo(
                    s2.getStudentName().toUpperCase());
        }
    };

    /*Comparator for sorting the list by Roll Num*/
    //It's same with the above Comparator
    public static Comparator<Student_ver1> stuRollNum = (s1, s2) -> {
        System.out.println("Using static Comparator<Student_ver1> stuRollNum = new Comparator<Student_ver1>(){ public int compare(Student_ver1 s1, Student_ver1 s2){ } }");
        System.out.println("return (num1 - num2): " + (s1.getRollNum() - s2.getRollNum()));

        /*For ascending order*/
        return s1.getRollNum() - s2.getRollNum();

        /*For descending order*/
        //num2-num1;
    };

    @Override
public String toString() {
        return "{ num=" + num + ", name=" + studentName + ", age=" + studentAge + " }";
    }
/*  public String toString() ** in Class Object ** {
        return this.getClass().getName() + "@" + Integer.toHexString(this.hashCode());
}*/

}

class Student_ver2 implements Comparator<Student_ver2>, Comparable<Student_ver2> {
    private String studentName;
    private int num;
    private int studentAge;

    public Student_ver2(int num, String studentName, int studentAge) {
        this.num = num;
        this.studentName = studentName;
        this.studentAge = studentAge;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public int getRollNum() {
        return num;
    }

    public void setRollNum(int num) {
        this.num = num;
    }

    public int getStudentAge() {
        return studentAge;
    }

    public void setStudentAge(int studentAge) {
        this.studentAge = studentAge;
    }

    @Override
    public String toString() {
        return "{{ num=" + num + ", name=" + studentName + ", age=" + studentAge + " }}";
    }

    // choice 1. Comparator<Student_ver2>
    public int compare(Student_ver2 s1, Student_ver2 s2) {
        System.out.println("Using Comparator<Student_ver2>, compare(stu1, stu2)");
        System.out.println("return (s1.getStudentAge() - stu2.getStudentAge()): " + (s1.getStudentAge() - s2.getStudentAge()));
        // For Ascending order
        return s1.getStudentAge() - s2.getStudentAge();
    }

    // choice 2. Comparable<Student_ver2>
    @Override
    public int compareTo(Student_ver2 otherStu) {
        System.out.println("Using Comparable<Student_ver2>, compareTo(Student_ver2 otherStu)");
        System.out.println("return (this.studentAge - (otherStu).getStudentAge()): " + (this.studentAge - (otherStu).getStudentAge()));
        // For Ascending order
        return this.studentAge - (otherStu).getStudentAge();

        // For Descending order
        // return (otherStu).getStudentAge() - this.studentAge;
    }
}