#include <stdio.h>

int main()
{
  //! When you use scanf, the conversion specifier is the same as in printf.

  unsigned int ui;
  ui = 0xffff;        // 2^16 - 1
  printf("%u\n", ui); // 65535    (in base 10)
  printf("%d\n", ui); // 65535    (in base 10)
  printf("%o\n", ui); // 177777   (in base 8)
  printf("%x\n", ui); // ffff     (in base 16)

  int i;
  i = 0xffff;        // 2^16 - 1
  printf("%u\n", i); // 65535    (in base 10)
  printf("%d\n", i); // 65535    (in base 10)
  printf("%o\n", i); // 177777   (in base 8)
  printf("%x\n", i); // ffff     (in base 16)

  unsigned short us;
  us = 0xffff;         // 2^16 - 1
  printf("%hu\n", us); // 65535    (in base 10)
  printf("%hd\n", us); // -1       (in base 10)
  printf("%ho\n", us); // 177777   (in base 8)
  printf("%hx\n", us); // ffff     (in base 16)

  short s;
  s = 0xffff;         // 2^16 - 1
  printf("%hu\n", s); // 65535    (in base 10)
  printf("%hd\n", s); // -1       (in base 10)
  printf("%ho\n", s); // 177777   (in base 8)
  printf("%hx\n", s); // ffff     (in base 16)

  unsigned long ul;
  ul = 0xffff;         // 2^16 - 1
  printf("%lu\n", ul); // 65535    (in base 10)
  printf("%ld\n", ul); // 65535    (in base 10)
  printf("%lo\n", ul); // 177777   (in base 8)
  printf("%lx\n", ul); // ffff     (in base 16)

  long l;
  l = 0xffff;         // 2^16 - 1
  printf("%lu\n", l); // 65535    (in base 10)
  printf("%ld\n", l); // 65535    (in base 10)
  printf("%lo\n", l); // 177777   (in base 8)
  printf("%lx\n", l); // ffff     (in base 16)

  unsigned long long ull;
  ull = 0xffff;          // 2^16 - 1
  printf("%llu\n", ull); // 65535    (in base 10)
  printf("%lld\n", ull); // 65535    (in base 10)
  printf("%llo\n", ull); // 177777   (in base 8)
  printf("%llx\n", ull); // ffff     (in base 16)

  long long ll;
  ll = 0xffff;          // 2^16 - 1
  printf("%llu\n", ll); // 65535    (in base 10)
  printf("%lld\n", ll); // 65535    (in base 10)
  printf("%llo\n", ll); // 177777   (in base 8)
  printf("%llx\n", ll); // ffff     (in base 16)

  return 0;
}