# KitKat Parser


import itertools


__author__ = 'dan.barella@gmail.com (Dan Barella)'


class Lexer(object):
  """Lexes KitKat tokens according to the rules described in the README."""

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
          # if ch1 == T_SINGLE_QUOTE:
            # Do stuff.

          yield ch1

    return _token_generator()


def main():
  pass


if __name__ == '__main__':
  main()
