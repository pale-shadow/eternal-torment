# SPDX-FileCopyrightText: 2024 DE:AD:10:C5 <franklin@dead10c5.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pathlib
import unittest
from pathlib import Path

from src.lib.common import print_logo  # import our code from project dir


class TestPrintLogo(unittest.TestCase):
    """Test the print_logo() method."""

    def test_print_logo_pass(self):
        """Display logo."""
        current_dir = str(pathlib.Path(__file__).parents[1])
        self.assertTrue(len(print_logo("src/" + current_dir)))


if __name__ == "__main__":
    unittest.main()
