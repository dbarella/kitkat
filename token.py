import error


ESCAPE = '\''


TOKENS = {
  '^': 'T_UP',
  '>': 'T_RIGHT',
  'v': 'T_DOWN',
  '<': 'T_LEFT',
  '\'': 'T_SINGLE_QUOTE',
  '.': 'T_PERIOD',
  '\n': 'T_NEWLINE',
  Ellipsis: 'T_CHAR',
  }


# Escaped chars are sequences formed by escaping alphabetical characters.
# For example, 'n translates to newline
# So, we map the lookahead character (the n, in the case of newline) to its
# actual representation.
TRANSLATE_ESCAPE = {
    '^': '^',
    '>': '>',
    'v': 'v',
    '<': '<',
    '\'': '\'',
    '.': '.',
    'n': '\n',
    }


class Token(object):
  """Represents a KitKat token."""

  @classmethod
  def t_kind(cls, ch, lookahead):
    """Returns the kind of token ch forms, using a 1-char lookahead.

    This function is the kernel of the Tokenizer's tokenizing loop.

    Args:
      ch (char): The character to tokenize.
      lookahead (char): A 1-character lookahead.

    Returns (string): The result of running ch through TOKENS, or T_CHAR if ch is
    not in TOKENS.
    """
    if ch not in TOKENS:
      return TOKENS[...]

    ch_translate = TOKENS[ch]
    if ch_translate == TOKENS[ESCAPE]:  # Escaped character

      if lookahead in TRANSLATE_ESCAPE:
        return TOKENS[...]
      else:
        raise error.LexerException(
            '({0} {1}) is not a valid escape sequence'.format(ch, lookahead))

    else:  # Not escaped character
      return ch_translate

  def __init__(self, ch, lookahead):
    """Init a Token.

    When a Token is instantiated, it figures out its kind and its character

    - kind is taken from the TOKENS table.
    - character is either ch or a translated escape sequence.

      If this Token represents an escape sequence, then self.character will be
      the translated escape sequence.

      e.g.:
        t = Token('\'', 'n')
        => t.kind = T_CHAR, t.character = '\n'

    Args:
      ch (char): The character to tokenize.
      lookahead (char): A 1-character lookahead.
    """
    self._ch = ch
    self._lookahead = lookahead

    self.kind = Token.t_kind(ch, lookahead)

    if self.kind != TOKENS[...]:  # Not a T_CHAR
      self.character = self._ch
    else:  # Is a T_CHAR, check for translation
      if self._ch == ESCAPE:  # Escape sequence
        self.character = TRANSLATE_ESCAPE[self._lookahead]
      else:
        self.character = self._ch

  def is_kind(self, kind):
    """Return True if self.kind == kind, False otherwise."""
    return self.kind == kind

  def __repr__(self):
    return '<Token {0} ({1})>'.format(self.kind, self._ch)
