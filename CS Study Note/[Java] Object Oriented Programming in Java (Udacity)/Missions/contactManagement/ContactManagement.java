//from 2018.05.
//to 2018.05.

package Project.contactManagement;

import java.util.Scanner;

public class ContactManagement {
    public static void main(String[] args) {
        ContactsManager myContactsManager = new ContactsManager();

        myContactsManager.addContact(new Contact("Hyuk1", "xxx1@xxx.com", "01012341231"));
        myContactsManager.addContact(new Contact("Hyuk2", "xxx2@xxx.com", "01012341232"));
        myContactsManager.addContact(new Contact("Hyuk3", "xxx3@xxx.com", "01012341233"));
        myContactsManager.addContact(new Contact("Hyuk4", "xxx4@xxx.com", "01012341234"));

        System.out.println(myContactsManager.searchContact("Hyuk3").phoneNumber);

        myContactsManager.addContact(new Contact
                (new Scanner(System.in).nextLine(), new Scanner(System.in).nextLine(), new Scanner(System.in).nextLine()));

        System.out.println(myContactsManager.contacts[4].phoneNumber);
    }
}

class Contact {
    String name;
    String email;
    String phoneNumber;

    Contact() {
        this.name = null;
        this.email = null;
        this.phoneNumber = null;
    }

    Contact(String name, String email, String phoneNumber) {
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }
}

class ContactsManager {

    public Contact[] contacts;
    int contactsCount;

    ContactsManager() {
        this.contacts = new Contact[500];
        this.contactsCount = 0;
    }

    void addContact(Contact newPerson) {
        this.contacts[contactsCount] = newPerson;
        this.contactsCount++;
    }

    Contact searchContact(String searchName) {
        for (int i = 0; i < this.contactsCount; i++) {
            if (contacts[i].name.equals(searchName)) {
                return contacts[i];
            }
        }
        return null;
    }
}