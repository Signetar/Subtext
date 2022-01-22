# Subtext 0.0.2
[![Downloads](https://pepy.tech/badge/subtext)](https://pepy.tech/project/subtext)
[![PyPI version](https://badge.fury.io/py/Subtext.svg)](https://badge.fury.io/py/Subtext)

A package to make NLP fast and easy for beginners.

- Efficient text prediction 
- Text pairing, equivalent to that of **NLTK**'s n-gram.
- Syllable Identification
- Find frequencies of words in given text
- Find matching words in two arrays

I still have a lot of plans for this package, for that reason, there would be a lot of frequent updates in the near future. The updates would include optimizations & more functions, so stay tuned.

## Install
```
pip install subtext
```

# Usage
First import the program using:
```python
import subtext
```
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
## Pair
This function splits a string into pairs of strings.

### Parameters
```python
subtext.pair(string, n)
```
- **string** is the string you're trying to split into pairs
- **n** stands for the number of strings in each pair. (Equivalent to that of the ```n``` value in n-gram)

### Usage
Let's set our string to:
```python
string="Sometimes, I just go out and eat sand. I don't know why"
``` 
Don't ask.
Let's turn this into pairs of 2:
```python
print(pair(string, 2))
```
Which outputs
```
[['Sometimes,', 'I'], ['I', 'just'], ['just', 'go'], ['go', 'out'], ['out', 'and'], ['and', 'eat'], ['eat', 'sand.'], ['sand.', 'I'], ['I', "don't"], ["don't", 'know'], ['know', 'why']]
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
