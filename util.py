"""Utility functions."""


def pad(field_2d, padding):
  """Returns a version of field_2d padded on all sides with padding.

  Args:
    field_2d (list of (list of object)): A 2-dimensional field to pad.
    padding (object): The padding with which to surround field_2d.

  Returns (list of (list of object)): A padded 2-dimensional field.
  """
  if not field_2d:  # Nothing to do.
    return field_2d

  intermediate = []

  intermediate.append([padding] * (2 + len(field_2d[0])))  # Padding over top

  for row in field_2d:
    intermediate_row = [padding]
    intermediate_row.extend(row)
    intermediate_row.append(padding)

    intermediate.append(intermediate_row)

  intermediate.append([padding] * (2 + len(field_2d[-1])))  # Bottom

  return intermediate
