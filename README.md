KitKat
======

KitKat, a language that doesn't really do much.

KitKat is a 2D language string printing language, where the programmer controls
the direction in which the program runs, as well as the content that is printed.

Movement control characters are:

  > (Right)
  ^ (Up)
  < (Left)
  v (Down)

All other characters are interpreted as literal characters. The movement
characters may be escaped with a leading single-quote character (')

e.g:

  '> (literal > character)

A literal single quote is represented as two single quotes, i.e. an escaped
single quote

e.g.

  '' (literal ' character)

Furthermore, comma (,) is treated as a special character, synonymous with space,
and period (.) is treated as a no-op. To print a literal comma or period, escape
it with that leading single quote.

---

The program control begins at the top left of the board, i.e. the first
character in the file. If no movement control character is encountered, > is
assumed.

e.g. (4x4 board):

  > h i v
  . . . .
  . . . (
  . . . :

This prints the text:

  hi (:

And then exits.
