# Subtext 2 
[![Downloads](https://pepy.tech/badge/subtext)](https://pepy.tech/project/subtext)
[![PyPI version](https://badge.fury.io/py/Subtext.svg)](https://badge.fury.io/py/Subtext)

A package for Natural Language Processing (NLP). This includes minor functions for processing text, as well as machine learning algorithms to perform an in-depth analysis.

Subtext 2 introduces more advanced tools for analysis. As the package is now focused on deployment of such tools, previous functions will now be under *miscellaneous* section.

### Development plans
- `SentimentAnalyser` (released in 2.0)
- `TextModifier` (in development)
- `ContextExtractor` (in development)
- `TextClassifier` (in development)
- 'TextFiller` (in development)
- `TextGenerator` (in development)



As of now, my development plan is in shambles and the only "advanced" algorithm you can currently access is `SentimentAnalyser`. But the analyser is quite good so I hope you can forgive me for that. (92% on IMDb Reviews dataset. That's better than some DNN models!)

## Install
You can install this package through PyPi,
```
pip install subtext
```
or, if you were nice enough to have this installed on your device already, you can upgrade the package using
```
pip install --upgrade subtext
```

and import using
```py
import subtext
```
## Sentiment Analyser
### Overview
The SentimentAnalyser class is designed to perform sentiment analysis on text data using n-grams. It allows users to input sentences with their respective sentiment scores, calculate average scores for each n-gram, and analyze the sentiment of new sentences based on the stored n-grams.
### Class methods
- __init__(self):
Initializes the SentimentAnalyser object.
- __generate_ngrams__(self, sentence, n):
Generates n-grams from a given sentence.
- __add_sentences__(self, sentences, scores, n_grams=1):
Adds a list of sentences and their respective sentiment scores to the analyser.
- __calculate_average_scores__(self):
Calculates the average sentiment scores for each n-gram in the analyser.
- __analyse__(self, sentence, n_grams=1, detailed_view=False):
Analyzes the sentiment of a given sentence based on the stored n-grams. Once detailed_view is enabled, the user can see the workings behind the analysis.

### Example Usage
```py
from subtext import SentimentAnalyser

analyser = SentimentAnalyser()

# Add sentences and their respective scores
sentences = ["I love this movie.", "I hate this movie."]
scores = [0.8, -0.8]
analyser.add_sentences(sentences, scores, n_grams=2)

# Analyze the sentiment of a sentence
sentence = "I love this movie, but I hate the ending."
sentiment_score = analyser.analyse(sentence, n_grams=2)
print(sentiment_score)

# Analyze the sentiment of a sentence with detailed_view
sentiment_score_detailed = analyser.analyse(sentence, n_grams=2, detailed_view=True)
print(sentiment_score_detailed)
```

## n_grams(self, sentence, n)
Generates n-grams from a given sentence.

Parameters:
- sentence (str): The input sentence.
- n (int): The length of the n-grams to generate.

Returns:
A list of n-grams (list of lists of strings).
### Example Usage
```py
from subtext import n_grams

# Generate n-grams from a sentence
sentence = "I love this movie."
ngrams = n_grams(sentence, 2) # this would make bigrams
print(ngrams)
```
Output:
```py
[['I', 'love'], ['love', 'this'], ['this', 'movie.']]
```

# Subtext 1
These are misc functions that were developed during initial release of Subtext.

## Predict
A function that predicts the next x number of words based on the given string and phrase
### Parameters
The function's parameters are:
```python
subtext.predict(string, phrase, n=0, case_insensitive=False)
```
* **String**: Main text
* **Phrase**: The key phrase (prompt). The function would try to predict what would come after the given phrase.
* **n**: The number of words it would return. It's automomatically set to 0, which would return all predictions regardless of their corresponding word counts.
* **case_insensitive**: Set this to ```True``` if you want to.

### Actual usage
So, let's try to use this.
```python
string="I am a string. I am also a human being, but most importantly, I am a string."
print(predict(string, "I am", n=1))
```
This would output

```
{'a': 2, 'also': 1}
```

But, if you change the ```n``` value,
```python
print(predict(string, "I am", n=2))
```
It would output
```
{'a string.': 2, 'also a': 1}
```

## Identify Syllables
```python
subtext.syllables("carbonmonoxide")
```
This outputs:
```python
car-bon-mon-ox-ide
```
But take note that this only works with lowercase strings.

## Countwords
### Parameters
The function's parameters are:
```python
subtext.countwords(string, case_insensitive=False)
```
Change that to ```True```  if you want it to be case-insensitive.

### Actual usage
Get yourself a nice string
```python
string = "Sometimes I wonder, 'Am I stupid?' then I realize, yeah. yeah, I am stupid."
```

Then put it in the function:
```python
x = subtext.countwords(string)
print(x)
```
It should print:
```
{'I': 4, 'Sometimes': 1, 'wonder,': 1, "'Am": 1, "stupid?'": 1, 'then': 1, 'realize,': 1, 'yeah.': 1, 'yeah,': 1, 'am': 1, 'stupid.': 1}
```

## Matchingwords
A function that finds & counts matching words in two strings

### Actual usage
So in this case, our strings are:
```python
string1, string2 = "God, I love drawing, drawing is my favourite thing to do", "God, I hate drawing, drawing is my least favourite thing to do"
```

If we run this through matchingwords, we would get:
```
{'God,': 1, 'I': 1, 'drawing,': 1, 'drawing': 1, 'is': 1, 'my': 1, 'favourite': 1, 'thing': 1, 'to': 1, 'do': 1}
```
