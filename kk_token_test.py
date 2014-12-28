"""Tests for token.py"""


import unittest

import error
import kk_token


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class TestToken(unittest.TestCase):

  def test_reject_invalid_kind(self):
    """Check that an invalid kind argument is not accepted."""
    with self.assertRaises(error.TokenException):
      kk_token.Token('invalid type', 'any character')

  def test_create_unspecial_token(self):
    """Check that making a regular character token works."""
    t = kk_token.Token(token.TOKENS[...], 'a')

  def test_directional_token(self):
    """Check that a directional token (left, right, up, down) knows itself."""
    left = kk_token.Token(kk_token.TOKENS[kk_token.LEFT], kk_token.LEFT)
    right = kk_token.Token(kk_token.TOKENS[kk_token.RIGHT], kk_token.RIGHT)
    up = kk_token.Token(kk_token.TOKENS[kk_token.UP], kk_token.UP)
    down = kk_token.Token(kk_token.TOKENS[kk_token.DOWN], kk_token.DOWN)

    self.assertTrue(left.is_directional()
                    and right.is_directional()
                    and up.is_directional()
                    and down.is_directional())


# class TestKind(unittest.TestCase):
#
#   def test_non_special_char(self):
#     """Test an unspecial character."""
#     actual_kind = token.Token.t_kind('a', None)
#
#     self.assertEqual(token.TOKENS[...], actual_kind)
#
#   def test_escaped_right(self):
#     """Test an escaped > character."""
#     actual_kind = token.Token.t_kind('\'', '>')
#
#     self.assertEqual(token.TOKENS[...], actual_kind)
#
#   def test_escaped_newline(self):
#     """Test an escaped newline."""
#     actual_kind = token.Token.t_kind('\'', 'n')
#
#     self.assertEqual(token.TOKENS[...], actual_kind)


if __name__ == '__main__':
  unittest.main()
