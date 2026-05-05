#!/usr/bin/env bash
#
# SPDX-FileCopyrightText: 2023 DE:AD:10:C5 <franklin@dead10c5.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# sudo apt install gnuplot gawk libtool psutils make autopoint
#declare -a  Packages=( "doxygen" "gawk" "doxygen-latex" "automake" )

declare -a Packages=( "git" "make" "automake" "libtool" "gnuplot" "psutils" "python3-pygments" "libgraphviz-dev")

sudo apt install python3-pygments libgraphviz-dev -y
