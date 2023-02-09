import re


def um():
  return count(input('Text: ').lower())


def count(um):
  dude = re.findall(r'\bum\b', um)
  return len(dude)


if __name__ == "__main__":
  print(um())
