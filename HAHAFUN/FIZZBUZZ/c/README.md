Build it this way:

```
cc ayy_lmao.c -o ayy_lmao
```

* Build assembly code

```
gcc -S -m64 -fno-asynchronous-unwind-tables -mno-red-zone -O0 ayylmao.c
```

* create object file

```
gcc -S ayylmao.s -o ayylmao.o
```

* build from object file

```
gcc ayylmao.o -o  ayylmao
```


* autoconf

```
autoscan
mv configure.scan configure.ac
```

Edit configure.ac

```
autoconf
vi Makefile.am
```
