#include <stdio.h>

int main() {
    char ch;
    _Bool is_init = 1;

    do {
        if (is_init) {
            printf("Enter a string below.\n");
            is_init = 0;
        } else {
            printf("%c -> ", ch);
        }

        scanf("%c", &ch);

        printf("%c\n", ch);
    } while (ch != '\n');
    //   tes test  tset
    //
    //   ->
    //   -> t
    // t -> e
    // e -> s
    // s ->
    //   -> t
    // t -> e
    // e -> s
    // s -> t
    // t ->
    //   ->
    //   -> t
    // t -> s
    // s -> e
    // e -> t
    // t ->

    return 0;
}
