#!/usr/bin/env bash
#
# SPDX-FileCopyrightText: 2023 DE:AD:10:C5 <franklin@dead10c5.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

terraform graph | unflatten -f -l 4 -c 6  | dot > graph.dot
dot -Tpng graph.dot > graph.png
