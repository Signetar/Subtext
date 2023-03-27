from collections import Counter

__version__ = "2.0.3"
__author__ = "Signetar"
__meow__ = "meow"

## SUBTEXT 2 ##
class SentimentAnalyser:
    """
    An object you can train with sentences and their corresponding sentiment scores to analyse some text.
    """
    def __init__(self):
        self.grams = {}
        self.gram_count = {}

    def generate_ngrams(self, sentence, n):
        words = sentence.split()
        ngrams = [words[i:i + n] for i in range(len(words) - n + 1)]
        return ngrams

    def add_sentences(self, sentences, scores, n_grams=1):
        """
        Add sentences and their corresponding sentiment scores to the analyser. 
        """
        for i, sentence in enumerate(sentences):
            ngrams = self.generate_ngrams(sentence, n_grams)
            for ngram in ngrams:
                ngram_tuple = tuple(ngram)
                if ngram_tuple in self.grams:
                    self.grams[ngram_tuple] += scores[i]
                    self.gram_count[ngram_tuple] += 1
                else:
                    self.grams[ngram_tuple] = scores[i]
                    self.gram_count[ngram_tuple] = 1

        self.calculate_average_scores()

    def calculate_average_scores(self):
        self.average_scores = {ngram: self.grams[ngram] / self.gram_count[ngram] for ngram in self.grams}

    def analyse(self, sentence, n_grams=1, detailed_view=False):
        """
        Analyse the sentiment of a sentence.
        """

        sentiment_scores = []
        total_ngrams = 0

        for n in range(1, n_grams + 1):
            ngrams = self.generate_ngrams(sentence, n)

            for ngram in ngrams:
                ngram_tuple = tuple(ngram)
                if ngram_tuple in self.average_scores:
                    sentiment_scores.append((ngram_tuple, self.average_scores[ngram_tuple]))
                    total_ngrams += 1

        if total_ngrams == 0:
            return None  # The sentiment analysis cannot be done for this sentence

        if detailed_view:
            return sentiment_scores
        else:
            sentiment_score = sum(score for _, score in sentiment_scores) / total_ngrams
            return sentiment_score

def n_grams(self, sentence, n):
    """
    Turn a sentence into n-grams.
    """
    words = sentence.split()
    ngrams = [words[i:i + n] for i in range(len(words) - n + 1)]
    return ngrams

## SUBTEXT 1 ##
def make_one_line(string):
    """
    Turns a string into one line.
    """
    string_list = string.split('\n')
    string_list = [item.strip() for item in string_list]
    string_list = [item for item in string_list if item != '']
    string = ' '.join(string_list)
    return string

def clean(string):
    """
    Cleans the string by turning into one line and removing punctuation.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    string = make_one_line(string)
    for char in punctuation:
        string = string.replace(char, "")
    return string

def predict(string, phrase, n=0, case_insensitive=False):
    """
    Predicts the next n words of a phrase, given a string.
    string: The full text
    phrase: The phrase that's taken into account
    n: the number of words it should return (Prediction)
    """
    if case_insensitive:
        string = string.lower()
        phrase = phrase.lower()
    string = string.split()
    phrase = phrase.split()
    string, phrase= "<s>".join(string), "<s>".join(phrase)
    string = string.split(phrase)
    string.pop(0)

    string=[" ".join(x.split()[:n]) for x in [x.replace("<s>", " ").lstrip().rstrip() for x in string]]

    return dict(Counter(string).most_common())


def matchingwords(string_1, string_2):
    """
    Returns a list of words that are present in both strings along with their corresponding frequencies
    """
    return dict(Counter([x for x in string_1.split() if x in string_2.split()]).most_common())


def countwords(string, case_insensitive=False):
    """
    Counts the frequency of words in a string
    """
    if case_insensitive:
        string = string.lower()
    return {k: v for k, v in sorted(dict(Counter(string.split())).items(), reverse=True, key=lambda item: item[1])}

def syllables(string):
    def show_vowels_consonants_matrix(string):
        alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = [char for char in "bcdfghjklmnpqrstvwxyz"]
        matrix = []
        for i in string:
            alphabetindex = alphabet.index(i)
            if i in vowels:
                matrix.append((0, alphabetindex))
            elif i in consonants:
                matrix.append((1, alphabetindex))
        return (string, matrix)


    def reconstruct(matrix):
        alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
        string = ""
        for i in matrix:
            string += alphabet[i[1]]
        return string


    def syllable_identifier(matrixdata):
        name = matrixdata[0].lower()
        matrix = matrixdata[1]
        #make a list named "word" that stores the first elements of tuples in the matrix
        word = [x[0] for x in matrix]
        final = []
        final.append([])
        for num in range(len(word)):
            i = matrix[num]
            c = i[0]
            if c == 0:
                final[-1].append(i)
            elif c == 1 and len(final[-1]) == 0:
                final[-1].append(i)
            elif c == 1 and final[-1][-1][0] == 0:
                final[-1].append(i)
                final.append([])
            elif c == 1 and final[-1][-1][0] == 1:
                final[-1].append(i)
        for i in range(len(final)-1, -1, -1):
            if len(final[i]) == 0:
                del final[i]
            elif len(final[i]) == 1:
                x = final[i][0]
                del final[i]
                final[-1].append(x)
        final_string = []
        for i in final:
            final_string.append(reconstruct(i))
        return (final, final_string)

    """
    Splits a word into its syllables. (Case-sensitive)
    """
    return "-".join(syllable_identifier(show_vowels_consonants_matrix(string))[1])



