/*
\33 = Octal escape sequence
\x1b = Hexadecimal escape sequence


Escape sequence	   Text attributes
\33[0m	           All attributes off(color at startup)
\33[1m	           Bold on(enable foreground intensity)
\33[4m	           Underline on
\33[5m	           Blink on(enable background intensity)
\33[21m	           Bold off(disable foreground intensity)
\33[24m	           Underline off
\33[25m	           Blink off(disable background intensity)

Escape sequence	   Foreground colors
\33[30m	           Black
\33[31m	           Red
\33[32m	           Green
\33[33m	           Yellow
\33[34m	           Blue
\33[35m	           Magenta
\33[36m	           Cyan
\33[37m	           White
\33[39m	           Default(foreground color at startup)
\33[90m	           Light Gray
\33[91m	           Light Red
\33[92m	           Light Green
\33[93m	           Light Yellow
\33[94m	           Light Blue
\33[95m	           Light Magenta
\33[96m	           Light Cyan
\33[97m	           Light White

Escape sequence	   Background colors
\33[40m	           Black
\33[41m	           Red
\33[42m	           Green
\33[43m	           Yellow
\33[44m	           Blue
\33[45m	           Magenta
\33[46m	           Cyan
\33[47m	           White
\33[49m	           Default(background color at startup)
\33[100m	       Light Gray
\33[101m	       Light Red
\33[102m	       Light Green
\33[103m	       Light Yellow
\33[104m	       Light Blue
\33[105m	       Light Magenta
\33[106m	       Light Cyan
\33[107m	       Light White
*/

#include <stdio.h>

#define ANSI_FORE_COLOR_RED "\33[31m"
#define ANSI_FORE_COLOR_GREEN "\33[32m"
#define ANSI_FORE_COLOR_YELLOW "\33[33m"
#define ANSI_FORE_COLOR_BLUE "\33[34m"
#define ANSI_FORE_COLOR_MAGENTA "\33[35m"
#define ANSI_FORE_COLOR_CYAN "\33[36m"

#define ANSI_FORE_COLOR_RESET "\33[0m"

#define ANSI_BACK_COLOR_GREEN "\33[42m"
#define ANSI_BACK_COLOR_RESET "\33[49m"

int main() {
    printf(ANSI_BACK_COLOR_GREEN
               ANSI_FORE_COLOR_RED
           "This text is RED with GREEN Background!" ANSI_BACK_COLOR_RESET
               ANSI_FORE_COLOR_RESET
           "\n");

    printf(ANSI_FORE_COLOR_GREEN
           "This text is GREEN!" ANSI_FORE_COLOR_RESET "\n");
    printf(ANSI_FORE_COLOR_YELLOW
           "This text is YELLOW!" ANSI_FORE_COLOR_RESET "\n");
    printf(ANSI_FORE_COLOR_BLUE
           "This text is BLUE!" ANSI_FORE_COLOR_RESET "\n");
    printf(ANSI_FORE_COLOR_MAGENTA
           "This text is MAGENTA!" ANSI_FORE_COLOR_RESET "\n");
    printf(ANSI_FORE_COLOR_CYAN
           "This text is CYAN!" ANSI_FORE_COLOR_RESET "\n");

    return 0;
}
