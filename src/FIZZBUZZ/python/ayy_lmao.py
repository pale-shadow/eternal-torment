#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@thedevilsvoice'

""" muffled `ayy lmao' in the distance from @da_667
"""


class Ayy:
    """ AYY
    """
    def __init__(self):
        """
        :return:
        """
        pass

    def lmao(self, ayy, lmao):
        """
        :return: lmao
        """
        ayy = "ayy"
        lmao = "lmao"
        return ''.join(ayy+lmao)


def main():
    """The main() function"""
    ayy = Ayy()
    try:
        ayy.lmao("ayy", "lmao")
    except Exception, e:
            print('ERROR', "Exception: %s " % e)


if __name__ == "__main__":
    main()
