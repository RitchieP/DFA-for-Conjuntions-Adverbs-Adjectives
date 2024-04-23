import dfa
from dfa import generate_stopword_dfa

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

    adjectives_dfa = generate_stopword_dfa(adjectives)
    adverbs_dfa = generate_stopword_dfa(adverbs)
    conjunctions_dfa = generate_stopword_dfa(conjunctions)

    # Read in the demo text to perform testing of the DFA
    demo_text_file = open("./demo text/demo_text_1.txt")
    try:
        demo_text = demo_text_file.read()
    finally:
        demo_text_file.close()
    input_string = demo_text

    # Print out the detected language
    print("Adjectives detected:", adjectives_dfa.run(input_string.lower()))
    print("Adverbs detected:", adverbs_dfa.run(input_string.lower()))
    print("Conjunctions detected:", conjunctions_dfa.run(input_string.lower()))
