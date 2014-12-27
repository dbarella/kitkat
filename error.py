"""KitKat errors."""


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class LexerException(Exception):
  pass


class DFAException(LexerException):
  pass
