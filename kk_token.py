"""KitKat Token stuff."""


import error


__author__ = 'dan.barella@gmail.com (Dan Barella)'


ESCAPE = '\''


UP = '^'
RIGHT = '>'
DOWN = 'v'
LEFT = '<'


TOKENS = {
    UP: 'T_UP',
    RIGHT: 'T_RIGHT',
    DOWN: 'T_DOWN',
    LEFT: 'T_LEFT',
    '\'': 'T_SINGLE_QUOTE',
    '.': 'T_PERIOD',
    ',': 'T_COMMA',
    '\n': 'T_NEWLINE',
    Ellipsis: 'T_CHAR',
    }


# Escaped chars are sequences formed by escaping alphabetical characters.
# For example, 'n translates to newline
# So, we map the lookahead character (the n, in the case of newline) to its
# actual kind and character representation.
TRANSLATE_ESCAPE = {
    UP: UP,
    RIGHT: RIGHT,
    DOWN: DOWN,
    LEFT: LEFT,
    '\'': '\'',
    '.': '.',
    'n': '\n',
    }


# Translate special characters to printable strings
PRINTABLE_TOKEN_KINDS = {
    'T_SINGLE_QUOTE',
    'T_COMMA',
    'T_NEWLINE',
    'T_CHAR',
    }


# Translate the output string for certain tokens. This is different from
# translating escape sequences because (for example) T_COMMA is interpreted as
# a space, and escaped to a comma.
TRANSLATE_SPECIAL_CHAR = {
    ',': ' ',  # Comma translates to space by default
    }


class Token(object):
  """Represents a KitKat token."""

  def __init__(self, kind, character):
    """Init a Token.

    - kind is taken from the TOKENS table.
    - character is either ch or a translated escape sequence.

      If this Token represents an escape sequence, then self.character will be
      the translated escape sequence. Or at least, should be. There isn't any
      code here to stop you from doing something stupid.

      e.g.:
        t = Token('\'', 'n')
        => t.kind = T_CHAR, t.character = '\n'

    Args:
      kind (string): The T_ID of this token.
      character (char): The character(s) this Token represents.
    """
    if kind not in TOKENS.values():
      raise error.TokenException('{} is not a valid Token kind'.format(kind))

    self.kind = kind
    self.character = character

  def is_directional(self):
    """Return True if this token is a directional token, False otherwise."""
    return self.kind in [TOKENS[UP], TOKENS[RIGHT], TOKENS[DOWN], TOKENS[LEFT]]

  def is_kind(self, kind):
    """Return True if self.kind == kind, False otherwise."""
    return self.kind == kind

  def is_printable(self):
    """Return True if it makes sense to print this token."""
    return self.kind in PRINTABLE_TOKEN_KINDS

  def __repr__(self):
    return '<Token {0}: {1} >'.format(self.kind, self.character)

  def __str__(self):
    return self.character


class DFA(object):
  """Maintains state in one place so that no one else has to suffer unduly."""

  def __init__(self):
    self.escape = False

  def step(self, ch):
    """Steps the DFA based on the incoming character ch.

    Args:
      ch (char): The incoming character.

    Returns (Token): A Token if one can be emitted, None otherwise.
    """
    if self.escape:
      if ch in TRANSLATE_ESCAPE:  # Legit escape sequence, emit
        self.escape = False
        ch_translate = TRANSLATE_ESCAPE[ch]
        return Token(TOKENS[...], ch_translate)
      else:  # Bad escape sequence, complain
        raise DFAException(
            "{0}{{1}} is an invalid escape sequence".format(ESCAPE, ch))

    else:  # Not escaped state
      if ch == ESCAPE:  # Possible escape sequence, wait for more input
        self.escape = True
        return None
      else:
        if ch not in TOKENS: # Just a regular character
          return Token(TOKENS[...], ch)
        else:  # Special character
          if ch in TRANSLATE_SPECIAL_CHAR:
            return Token(TOKENS[ch], TRANSLATE_SPECIAL_CHAR[ch])
          else:
            return Token(TOKENS[ch], ch)
