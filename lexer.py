"""KitKat lexer."""


from __future__ import print_function
import sys

import error
import kk_token
import util


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class Lexer(object):
  """Lexes KitKat token according to the rules described in the README.

  Internally, the lexer defines the first character in the file as the logical
  position (0, 0), and the last character in the file as (len, len).
  """

  def __init__(self, source):
    """Init a Lexer with a source file.

    Upon initializing the Lexer, the contents of the source file will be read
    into memory. This is because KitKat is a 2D language, so we can't just read
    from left to right.

    Args:
      source (file): The (opened) source file object.
    """
    self.lines = source.readlines()

    self._padding = None
    self._text_field = util.pad(self.lines, self._padding)

    self._direction = kk_token.RIGHT

  def __iter__(self):
    """Return a token iterator over the input text.

    Since defining generator objects is kinda confusing, I've implemented this
    as a generator factory, where the _token_generator function is automagically
    turned into a generator using the yield statement. Then it's "as easy as"
    returning the result of calling that function.

    That is a mouthful to say though...
    """

    def _token_generator():
      """Read, figure stuff, move, emit."""
      # Current location in self._text_field
      # i.e. self._text_field[i][j]
      i = 1
      j = 1

      # Initialize the DFA
      dfa = kk_token.DFA()

      while self._text_field[i][j] != self._padding:
        ch = self._text_field[i][j]  # Current character

        tok = dfa.step(ch)

        # Check for control character, change direction
        if tok and tok.is_directional():
          self._direction = tok.character  # Gross, but we can because why not

        # Update i, j
        if self._direction == kk_token.LEFT:
          j -= 1
        elif self._direction == kk_token.RIGHT:
          j += 1
        elif self._direction == kk_token.UP:
          i -= 1
        elif self._direction == kk_token.DOWN:
          i += 1
          # Yo D how we doin'

        else:  # Invalid state
          raise error.LexerException(
              'Something dinked. {} is not a valid lexer direction.'.format(
                self._direction))

        if tok:
          yield tok

    return _token_generator()


def main():
  with open(sys.argv[1], 'r') as f:
    l = Lexer(f)
    for i in l:
      print(i.__repr__())


if __name__ == '__main__':
  main()
