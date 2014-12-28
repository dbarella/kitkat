"""Tests for lexer.py"""


import mock
import unittest

import lexer
from kk_token import TOKENS
import util


__author__ = 'dan.barella@gmail.com (Dan Barella)'


def mock_file(lines):
  """Returns a mock file-like object with lines as its contents.

  Args:
    lines (list of (list of str)): The contents of the mock file

  Returns (mock.MagicMock of file): A mock file whose readlines method returns
  the argument lines.
  """
  m = mock.MagicMock(spec=file)
  m.readlines.return_value = lines
  return m


class TestLexer(unittest.TestCase):

  def test_single_character(self):
    """Test a single character."""
    # We shall inject this text field into our lexer
    source = mock_file([
          ['a'],
          ])

    expected_token_kinds = [TOKENS[...]]

    l = lexer.Lexer(source)
    count = 0
    for token, kind in zip(l, expected_token_kinds):
      self.assertTrue(token.is_kind(kind))
      count += 1

    self.assertEqual(1, count)  # Make sure that only one token was emitted

  def test_single_escape_sequence(self):
    """Test a single escape sequence."""
    source = mock_file([
          ["'", "n"],
          ])

    expected_token_kinds = [TOKENS[...]]

    l = lexer.Lexer(source)
    count = 0
    for token, kind in zip(l, expected_token_kinds):
      self.assertTrue(token.is_kind(kind))
      count += 1

    self.assertEqual(1, count)  # Make sure that only one token was emitted

  def test_multiple_escape_sequences(self):
    """Test a multiple escape sequences."""
    source = mock_file([
          ["'", "n", "v"],
          ["^", "'", "<"],
          ])

    expected_token_kinds = [TOKENS[...], TOKENS["v"], TOKENS["<"], TOKENS[...]]

    l = lexer.Lexer(source)
    count = 0
    for token, kind in zip(l, expected_token_kinds):
      self.assertTrue(token.is_kind(kind))
      count += 1

    self.assertEqual(4, count)  # Make sure that only one token was emitted


if __name__ == '__main__':
  unittest.main()
