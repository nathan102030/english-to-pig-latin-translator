


# part a
def piggify(word):
  vowels = 'aeiou'
  # If a word begins with a vowel
  if word[0] in vowels:
    return word + 'yay'
  # If a word begins with a consonant
  for i, letter in enumerate(word):
    if letter in vowels:
      return word[i:] + word[:i] + "ay"
  # If there are no vowel
  return word + "ay"


# part b

word = input("Type your word: ")

while (word != '.'):
  print(piggify(word))
  word = input("Type your word: ")
