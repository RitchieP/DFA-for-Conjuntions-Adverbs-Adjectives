class DFA:
    def __init__(self, alphabet, states, transitions, start_state, final_state):
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.final_state = final_state

    def run(self, input_string):
        accepted_words = []

        # Split the sentences into a word of their own, also removing punctuations
        for word in input_string.split(" "):
            current_state = self.start_state
            is_word = True
            for char in word:
                # If the character is not in the language, this is not a stop word, and we will just skip the word
                if char not in self.alphabet:
                    is_word = False
                    break

                # Try to move to the next state with the current character of the word. If it is none, that means there
                # is no transition for the current character. Hence, it is not a stop word, and we will just break the
                # loop and skip it.
                current_state = self.transitions.get(current_state, {}).get(char, None)
                if current_state is None:
                    is_word = False
                    break

            # Upon exiting the loop, if the word is still flagged as a stop word, it will be added to the list and
            # returned after the function ends.
            if current_state in self.final_state:
                accepted_words.append(word)
        return accepted_words


def generate_stopword_dfa(stopwords):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    states = set(range(len(stopwords) + 1))
    transitions = {}
    start_state = 0
    final_state = set()

    for i, word in enumerate(stopwords):
        current_state = 0
        for char in word:
            # If the character in the word is not part of the language, then we do not need to build a DFA for it.
            if char not in alphabet:
                continue

            # Get the next state in the DFA of the current state based on the character available for transition
            next_state = transitions.get(current_state, {}).get(char, None)

            # If the next state is not in the DFA, then create one for it.
            if next_state is None:
                next_state = len(states)
                transitions.setdefault(current_state, {})[char] = next_state
                states.add(next_state)
            current_state = next_state
        final_state.add(current_state)

    return DFA(alphabet, states, transitions, start_state, final_state)
