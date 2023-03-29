"""This program reads a text file and outputs the first 100 most used words."""

# Importing necessary modules
import os
import string
import sys
import math


def mostWords(path):
    """The function returns a dictionary of most used words by rank

    Args:
        path (string): Path to text file

    Returns:
        dict: dictionary of most used words and the amount of occurence
    """
    # The os module was used to help open the file since
    # there were issues where Python couldn't locate the file
    # despite being in the same folder as the script
    with open(os.path.join(sys.path[0], path), encoding="utf8") as f:

        words = {}

        # List of punctuations
        punctuation = [ch for ch in string.punctuation]

        # Additional characters that were not present in
        # string.punctuation but were found in the text file
        punctuation.extend(["‘", "’", "“", "”"])

        # Read every line and update word counts
        for line in f:
            cleanText = [ch for ch in line if ch not in punctuation]
            sentence = "".join(cleanText)
            lst = sentence.split()
            for word in lst:
                if word in words:
                    words[word] += 1

                else:
                    words[word] = 1

        # Sort the dictionary by the word counts
        return dict(sorted(words.items(),
                           key=lambda item: item[1], reverse=True))


def zipfPrediction(rank, mostCommon):
    """Function returns the prediction of occurence of a word
    based on Zipf's Law.

    Args:
        rank (int): rank of the word

    Returns:
        int: the predicted occurence of a word
    """
    return int(10**(math.log10(mostCommon) - math.log10(rank)))


def printWords(sortedWords, number):
    """Prints a requested number of most used words

    Args:
        sortedWords (dict): dictionary of sorted words
        number (int): number of words to print
    """

    counter = 0

    valuesList = list(sortedWords.values())

    most_common = int(valuesList[0])

    for word in sortedWords.keys():
        if counter >= number:
            break
        print("Word:", word, ", uses:", sortedWords[word],
              ", predicted uses:", zipfPrediction(counter + 1, most_common))
        counter += 1


printWords(mostWords("Moby_Dick.txt"), 100)
