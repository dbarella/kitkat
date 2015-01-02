"""KitKat interpreter."""


from __future__ import print_function
import sys

import lexer


__author__ = 'dan.barella@gmail.com (Dan Barella)'


def main():
  with open(sys.argv[1], 'r') as f:
    lex = lexer.Lexer(f)
    for token in lex:
      if token.is_printable():
        print(token.character, end='')


if __name__ == '__main__':
  main()
