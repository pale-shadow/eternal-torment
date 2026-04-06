AC_PREREQ([2.71])
AC_INIT([ass], [0.1], [smoooth.y62wj@passmail.net], [https://github.com/devsecfranklin/eternal-torment])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_CANONICAL_HOST

AS_CASE([$host_cpu],
  [aarch64*], [
    AC_MSG_NOTICE([Detected 64-bit Raspberry Pi architecture (AArch64)])
    # Define a variable or preprocessor macro for 64-bit code
    AC_DEFINE([IS_AARCH64], [1], [Building for 64-bit ARM])
  ],
  [arm*], [
    AC_MSG_NOTICE([Detected 32-bit Raspberry Pi architecture])
  ],
  [AC_MSG_ERROR([Unsupported architecture: $host_cpu])]
)

AC_PROG_CC
AM_PROG_AS

AC_CONFIG_FILES([Makefile])

# just in case they have run this on intel
AC_CHECK_PROG([HAVE_NASM], [nasm], [nasm])
AC_CHECK_PROG([HAVE_YASM], [yasm], [yasm])

AC_OUTPUT
