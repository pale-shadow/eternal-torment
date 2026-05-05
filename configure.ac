AC_PREREQ([2.71])
AC_INIT([eternal-torment], [0.3], [smoooth.y62wj@passmail.net])
AC_CONFIG_SRCDIR([src/main.c])
AC_CONFIG_HEADERS([config.h])

dnl --- Initialize Automake ---
dnl 'foreign' tells automake not to require GNU files like NEWS/AUTHORS
dnl 'subdir-objects' is required since your source is inside src/
AM_INIT_AUTOMAKE([foreign subdir-objects])

dnl --- Checks for programs ---
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_MAKE_SET

dnl --- Native Assembly Support ---
AM_PROG_AS
AC_CHECK_PROG(HAVE_GDB, [gdb], [found], [not-found])
AC_CHECK_PROG(HAVE_LD, [ld], [found], [not-found])

dnl --- Checks for libraries ---
dnl Using actual functions to ensure libraries are detected correctly
AC_CHECK_LIB([m], [cos])
AC_CHECK_LIB([GL], [glBegin])
AC_CHECK_LIB([GLU], [gluNewQuadric])
AC_CHECK_LIB([X11], [XOpenDisplay])
AC_CHECK_LIB([glut], [glutInit])

dnl --- Checks for header files ---
AC_CHECK_HEADERS([unistd.h])

dnl --- Checks for library functions ---
AC_CHECK_FUNCS([memset])

dnl --- Generate Output Files ---
dnl IMPORTANT: 'Makefile' must be listed first to generate the root Makefile.
dnl All sub-paths now point to the 'src/' directory structure.
AC_CONFIG_FILES([
    Makefile
    src/Makefile
    src/ass/Makefile
    src/cube1/Makefile
    src/freeglut/Makefile
    src/SpinningCube/Makefile
])

AC_OUTPUT

AC_MSG_NOTICE([
(⊃｡•‿•｡)⊃━⭑･ﾟﾟ･*:༅｡.｡༅: ﾟ: :✼✿ 
Configuration for $PACKAGE_NAME is ready.
☽༓･*˚⁺‧
])