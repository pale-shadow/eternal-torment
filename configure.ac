#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.71])
AC_INIT(lab-franklin, 0.2, franklin@bitsmasher.net, https://github.com/devsecfranklin/eternal-torment/issues)

dnl AC_CONFIG_SRCDIR([cube1])

AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_AWK
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_MAKE_SET

# Checks for libraries.
# FIXME: Replace 'main' with a function in '-lGL':
AC_CHECK_LIB([GL], [main])
# FIXME: Replace 'main' with a function in '-lGLU':
AC_CHECK_LIB([GLU], [main])
# FIXME: Replace 'main' with a function in '-lX11':
AC_CHECK_LIB([X11], [main])
# FIXME: Replace 'main' with a function in '-lglut':
AC_CHECK_LIB([glut], [main])
# FIXME: Replace 'main' with a function in '-lm':
AC_CHECK_LIB([m], [main])

# Checks for header files.
AC_CHECK_HEADERS([unistd.h])

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_CHECK_FUNCS([memset])

AC_CONFIG_FILES([HAHAFUN/SpinningCube/Makefile
		HAHAFUN/spinning-cube/Makefile
                 HAHAFUN/cube1/Makefile
                 HAHAFUN/freeglut/Makefile
])

AM_INIT_AUTOMAKE(foreign)

AC_OUTPUT
