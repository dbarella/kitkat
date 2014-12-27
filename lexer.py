# KitKat Parser


from __future__ import print_function
import itertools
import sys

import token


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class Lexer(object):
  """Lexes KitKat token according to the rules described in the README."""

  def __init__(self, source):
    """Init a Lexer with a source file.

    Args:
      source (file): The (opened) source file object.
    """
    self.source = source

  def __iter__(self):
    """Return a token iterator over self.source.

    Since defining generator objects is kinda confusing, I've implemented this
    as a generator factory, where the _token_generator function is automagically
    turned into a generator using the yield statement. Then it's as easy as
    returning the result of calling that function.

    That is a mouthful to say though...
    """

    def _token_generator():
      for line in self.source:

        # Since KitKat needs a 1-char lookahead for escapes,
        # we iterate over character pairs
        pairs = itertools.izip_longest(line, line[1:])

        for ch1, ch2 in pairs:
          t = token.Token(ch1, ch2)

          # If we get an escaped character, skip the lookahead.
          # Note that characterize takes care of improperly escaped charaters.
          if not t.is_kind(token.TOKENS[...]):
            yield t
            continue
          else:
            yield t

    return _token_generator()


def main():
  with open(sys.argv[1], 'r') as f:
    l = Lexer(f)
    for i in l:
      print(i)


if __name__ == '__main__':
  main()
