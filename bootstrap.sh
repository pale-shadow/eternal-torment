#!/usr/bin/env bash
#
# SPDX-FileCopyrightText: 2023-2025 franklin <smoooth.y62wj@passmail.net>
#
# SPDX-License-Identifier: MIT

# ChangeLog:
#
# v0.1 02/25/2022 Maintainer script
# v0.2 09/24/2022 Update this script
# v0.3 10/19/2022 Add tool functions
# v0.4 11/10/2022 Add automake check
# v0.5 11.16.5/2022 Handle Docker container builds
# v0.6 07/13/2023 Add required_files and OpenBSD support

# description: Standard bootstrap script to initialize the Autotools build system

echo "(⊃｡•‿•｡)⊃━⭑･ﾟﾟ･:༅｡.｡༅: ﾟ: Initializing build system... ☽༓･˚⁺‧"

# -i: install missing auxiliary files (like depcomp, compile, install-sh)
# -v: verbose output to see what is happening
#-f: force replacement of existing files
autoreconf -i -v -f

echo "Done. You can now run ./configure"