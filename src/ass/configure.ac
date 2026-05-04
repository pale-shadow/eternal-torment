AC_PREREQ([2.71])
AC_INIT([ass], [0.1], [smoooth.y62wj@passmail.net], [https://github.com/devsecfranklin/eternal-torment])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_CANONICAL_HOST

AC_PROG_CC
AM_PROG_AS
AC_CHECK_PROG([HAVE_NASM], [nasm], [nasm])
AC_CHECK_PROG([HAVE_YASM], [yasm], [yasm])

AS_CASE([$host_cpu],
  [aarch64*], [
    AC_MSG_NOTICE([Detected 64-bit Raspberry Pi architecture (AArch64)])
    AC_DEFINE([IS_AARCH64], [1], [Building for 64-bit ARM])
  ],
  [arm*], [
    AC_MSG_NOTICE([Detected 32-bit Raspberry Pi architecture])
  ],
  [x86_64*|i?86*], [
    AC_MSG_NOTICE([Detected x86 architecture])
  ],
  [AC_MSG_ERROR([Unsupported architecture: $host_cpu])]
)

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
