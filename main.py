# WSPAK Search Engine -
#   - is a tiny program that searches datasets such as books, dictionaries, and magazines for Palindromes.
#   A palindrome phrase that sounds the same read left to right and right to left
#
# example:
#   Madam --- (backward) ---> madaM
#
# source:
#   A good database is the website https://www.gutenberg.org

from engine import wspak

job = wspak("./book.txt")

job.compare()