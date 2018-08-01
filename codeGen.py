import random

def main():

  s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
  passlen = 16
  p =  "".join(random.sample(s,passlen ))
  print(p)

  codePlace = input('Give me the name of the program for the password:')

  with open('pythonCodeGen.txt', 'a') as f:
    f.write(codePlace + ':' + p + '\n')

main()