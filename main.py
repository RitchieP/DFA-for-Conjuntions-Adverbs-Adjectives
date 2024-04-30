from typing import Type

import dfa
from dfa import generate_dfa
from collections import Counter


def input_normalization(input_string):
    """
    Normalize input string by removing punctuations and change all alphabets to become lower case.

    :param input_string: String to be normalized
    :return: String, normalized
    """
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = ""

    for char in input_string:
        if char not in punc:
            res += char

    return res.lower()


def dfa_data(dfa_obj: Type[dfa.DFA], input_string, language_type=""):
    """
    Function to print out the words detected by the DFA that the user passes into.

    :param dfa_obj: An object of the DFA class
    :param input_string: The input string to be processed
    :param language_type: [Optional] Specifies what is the name of the language to be printed out. Defaults to "" if not
    specified.
    :return: Void
    """
    words_detected = dfa_obj.run(input_string)
    words_dict = Counter(words_detected)
    print(language_type, "detected :", words_detected)
    for key in words_dict:
        print(key, words_dict[key])


if __name__ == '__main__':
    # Reading in the list of stop words to generate a DFA
    adjectives_file = open("language/adjectives.txt", "r")
    adverbs_file = open("language/adverbs.txt", "r")
    conjunctions_file = open("language/conjunctions.txt", "r")
    try:
        adjectives = adjectives_file.read().split("\n")
        adverbs = adverbs_file.read().split("\n")
        conjunctions = conjunctions_file.read().split("\n")
    finally:
        adjectives_file.close()
        adverbs_file.close()
        conjunctions_file.close()

    adjectives_dfa = generate_dfa(adjectives)
    adverbs_dfa = generate_dfa(adverbs)
    conjunctions_dfa = generate_dfa(conjunctions)

    # Read in the demo text to perform testing of the DFA
    demo_text_file = open("./demo text/demo_text_1.txt")
    try:
        demo_text = demo_text_file.read()
    finally:
        demo_text_file.close()
    input_string = demo_text

    # Removes all punctuation from strings
    input_string = input_normalization(input_string)
    # Print out the detected language
    dfa_data(adjectives_dfa, input_string, language_type="Adjectives")
    dfa_data(adverbs_dfa, input_string, language_type="Adverbs")
    dfa_data(conjunctions_dfa, input_string, language_type="Conjunctions")
