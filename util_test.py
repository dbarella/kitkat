"""Tests for util.py"""


import unittest

import util


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class TestPad(unittest.TestCase):

  def test_empty_field(self):
    """Test padding an empty field."""
    self.assertFalse(util.pad([], None))

  def test_single_entry(self):
    """Test padding a field with one entry."""
    field = [['a']]
    actual_result = util.pad(field, None)
    expected_result = [[None, None, None],
                       [None, 'a',  None],
                       [None, None, None]]

    self.assertEqual(expected_result, actual_result)

  def test_jagged_field(self):
    """Test padding a jagged field."""
    field = [['a'], ['b', 'c']]
    actual_result = util.pad(field, None)
    expected_result = [[None, None, None],
                       [None, 'a',  None],
                       [None, 'b',  'c',  None],
                       [None, None, None, None]]

    self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
  unittest.main()
