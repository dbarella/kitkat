"""Tests for token.py"""


import unittest

import token


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class TestKind(unittest.TestCase):

  def test_non_special_char(self):
    """Test an unspecial character."""
    actual_kind = token.Token.t_kind('a', None)

    self.assertEqual(token.TOKENS[...], actual_kind)

  def test_escaped_right(self):
    """Test an escaped > character."""
    actual_kind = token.Token.t_kind('\'', '>')

    self.assertEqual(token.TOKENS[...], actual_kind)

  def test_escaped_newline(self):
    """Test an escaped newline."""
    actual_kind = token.Token.t_kind('\'', 'n')

    self.assertEqual(token.TOKENS[...], actual_kind)


if __name__ == '__main__':
  unittest.main()
