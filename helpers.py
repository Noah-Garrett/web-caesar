import string
lowercase_list=string.ascii_lowercase
uppercase_list=string.ascii_uppercase
ignorez=string.punctuation
digits=string.digits


def alphabet_position(letter):
  for j,k in enumerate(lowercase_list):
      if letter.lower() == k:
          return j
#this is for rotation
def rotate_character(char,rot,lett):
    new_let=char+int(rot)
    new_let=(new_let%26)
    if lett in lowercase_list:
      return lowercase_list[new_let]
    elif lett in uppercase_list:
      return uppercase_list[new_let]