"""KitKat errors."""


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class TokenException(Exception):
  pass


class LexerException(Exception):
  pass


class DFAException(LexerException):
  pass
