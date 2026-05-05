dnl Process this file with autoconf
AC_PREREQ([2.71])
AC_INIT(model-graph-neural-net, 0.1, franklin@dead10c5.org, https://github.com/devsecfranklin/ml-gnn)
AC_CONFIG_MACRO_DIR(config/m4)
AC_CONFIG_AUX_DIR(config)
AC_MSG_NOTICE([build directory: $ac_pwd])
AC_SUBST(WORKDIR, $ac_pwd)

AM_INIT_AUTOMAKE

LT_INIT

AC_CONFIG_COMMANDS([franklin-build],
 [echo "(⊃｡•́‿•̀｡)⊃━⭑･ﾟﾟ･*:༅｡.｡༅:*ﾟ:*:✼✿ Configuring for $mypkgname ☽༓･*˚⁺‧͙"],
 [mypkgname=$PACKAGE_NAME])

AM_PATH_PYTHON(3.8) # minimum version of python


AC_PROG_CXX

PY39="python$PYTHON_VERSION" # define the python interpreter
dnl LDFLAGS="$LDFLAGS -l$PY39"
AC_SUBST(PY39, python$PYTHON_VERSION)

AC_PATH_PROG([DOT], [dot], [na])

# AC_CHECK_PROG([TERRAFORM], [terraform], [yes], [no])
# AS_IF([test "x$TERRAFORM" = "xyes"], [
#         AC_MSG_NOTICE([*** Found TERRAFORM ***])
# ])

AC_PATH_PROG([TERRAFORM], [terraform], [na])
if test "$TERRAFORM" = na; then
   AC_MSG_ERROR([terraform binary not found on this machine!])
else
   AC_MSG_RESULT([terraform path: $TERRAFORM])
fi

AC_SUBST([GITVERSION])
AC_SUBST([GITTAG])
AC_SUBST([GITBRANCH])

if test -e $srcdir/.git
then
AC_CHECK_PROG([HAS_GIT], [git], [found], [not-found])
else
HAS_GIT=no-repository
fi
if test $HAS_GIT = found
then
    GITVERSION="git --git-dir \$(srcdir)/.git rev-parse --short HEAD"
    GITTAG="git --git-dir \$(srcdir)/.git describe --all --always --dirty"
    GITBRANCH="git --git-dir \$(srcdir)/.git name-rev --name-only HEAD"
else
    GITVERSION=""
    GITTAG=""
    GITBRANCH=""
fi

AC_LATEX_CLASS_ARTICLE
AC_LATEX_CLASS_BOOK
AC_LATEX_CLASS_REPORT
AC_LATEX_PACKAGE_AMSMATH
AC_LATEX_PACKAGE_FONTENC
AC_PROG_DVIPDF
AC_PROG_DVIPS
AC_PROG_FIG2DEV
AC_PROG_GNUPLOT
AC_PROG_MF
AC_PROG_LATEX
AC_PROG_BIBTEX
AC_PROG_PDFLATEX
AC_PROG_PS2PDF
dnl AC_PROG_LATEX2HTML
dnl AC_PROG_LATEX2MAN
AC_PROG_MAKEINDEX
dnl AC_PROG_JPEG2PS
AC_PROG_MKTEXPK
AC_PROG_TEXHASH
AC_PROG_KPSEWHICH
dnl AC_TEXMF_PATH
AC_PROG_PNGTOPNM
AC_PROG_PNMTOPS
AC_PROG_JPEGTOPNM
dnl AC_PROG_LATEX2PNG
dnl AC_PROG_LATEX2RTF
AC_PROG_PSBOOK
AC_PROG_PSNUP
AC_PROG_PSSELECT
AC_PROG_PSRESIZE
AC_PROG_DVIBOOK

AC_CONFIG_FILES([
  src/config.ini
  Makefile
  cluster/Makefile
  container/Makefile
  docs/paper/Makefile
  docs/presentation/Makefile
  test/Makefile
  ]) # files to generate, one per line

AC_OUTPUT