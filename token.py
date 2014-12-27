import error

TOKENS = {
  '^': 'T_UP',
  '>': 'T_RIGHT',
  'v': 'T_DOWN',
  '<': 'T_LEFT',
  '\'': 'T_SINGLE_QUOTE',
  '.': 'T_DOT',
  '\n': 'T_NEWLINE',
  Ellipsis: 'T_CHAR',
  }


class Token(object):
  """Represents a KitKat token."""

  def __init__(self, ch, lookahead=None):
    self.ch = ch
    self.kind = characterize(ch, lookahead)

  def is_kind(self, kind):
    """Return True if self.kind == kind, False otherwise."""
    return self.kind == kind

  def __repr__(self):
    return '<Token {0} ({1})>'.format(self.kind, self.ch)


def characterize(ch, lookahead=None):
  """Returns a token representation of ch, using a 1-char lookahead.

  This function is the kernel of the Tokenizer's tokenizing loop.

  Args:
    ch (char): The charater to tokenize.
    lookahead (char): A 1-character lookahead.

  Returns (string): The result of running ch through TOKENS, or T_CHAR if ch is
  not in TOKENS.
  """
  if ch not in TOKENS:
    return TOKENS[...]

  ch_translate = TOKENS[ch]
  if ch_translate != TOKENS['\'']:  # If not an escaped character, return it
    return ch_translate

  else:  # Escaped charater
    if lookahead in TOKENS:
      return TOKENS[...]
    else:
      raise error.TokenizerException('({0} {1}) is not a valid escape '
                                     'sequence'.format(ch, lookahead))
