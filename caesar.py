from helpers import alphabet_position, rotate_character

import string
ignorez=string.punctuation
digits=string.digits

def encrypt(stringy, move):
  final_sentence=''
  int_move=int(move)
  for i in stringy:
    if i in ignorez:
      final_sentence+=i
    elif i in string.whitespace:
      final_sentence+=' '
    elif i in digits:
      final_sentence+=i
    else:
        final_sentence+=rotate_character(alphabet_position(i),int_move,i)

  return final_sentence

def main():
  userstuff=input("what do you want to encode ")
  move=input("how much to moveit ")
  print(encrypt(userstuff,move))

if __name__=="__main__":
  main()