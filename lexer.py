"""KitKat lexer."""


from __future__ import print_function
import sys

import token
import util


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class Lexer(object):
  """Lexes KitKat token according to the rules described in the README.

  Internally, the lexer defines the first character in the file as the logical
  position (0, 0), and the last character in the file as (len, len).
  """

  # Read direction
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

  def __init__(self, source):
    """Init a Lexer with a source file.

    Upon initializing the Lexer, the contents of the source file will be read
    into memory. This is because KitKat is a 2D language, so we can't just read
    from left to right.

    Args:
      source (file): The (opened) source file object.
    """
    self._source = source
    self.lines = source.readlines()
    self.text_field = self.lines  # util.pad(self.lines, None)

    self._direction = Lexer.RIGHT

  def __iter__(self):
    """Return a token iterator over the input text.

    Since defining generator objects is kinda confusing, I've implemented this
    as a generator factory, where the _token_generator function is automagically
    turned into a generator using the yield statement. Then it's "as easy as"
    returning the result of calling that function.

    That is a mouthful to say though...
    """

    def _token_generator():
      import pdb; pdb.set_trace()
      # Current location in self.text_field
      # i.e. self.text_field[i][j]
      i = 0
      j = 0

      while i < len(self.text_field) and j < len(self.text_field[i]):
        ch = self.text_field[i][j]  # Current character

        # TODO(barella): Chech for control character, change direction.

        # Since KitKat needs a 1-char lookahead for escapes,
        # we iterate over character pairs

        # for ch1, ch2 in pairs:
        #   t = token.Token(ch1, ch2)

        #   # If we get an escaped character, skip the lookahead.
        #   # Note that characterize takes care of improperly escaped characters.
        #   if not t.is_kind(token.TOKENS[...]):
        #     yield t
        #     continue
        #   else:
        #     yield t
        yield ch

        if self._direction == Lexer.UP:
          i -= 1
        elif self._direction == Lexer.DOWN:
          i += 1
        elif self._direction == Lexer.RIGHT:
          j += 1
        elif self._direction == Lexer.LEFT:
          j -= 1
        else:  # Invalid state
          raise LexerException(
              'Something dinked. {} is not a valid lexer direction.'.format(
                self._direction))

    return _token_generator()


def main():
  with open(sys.argv[1], 'r') as f:
    l = Lexer(f)
    for i in l:
      print(i)


if __name__ == '__main__':
  main()
