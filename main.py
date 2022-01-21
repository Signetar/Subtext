
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

def primitivematrix(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [char for char in "bcdfghjklmnpqrstvwxyz"]
    matrix = []
    for i in string:
        if i in vowels:
            matrix.append(0)
        elif i in consonants:
            matrix.append(1)
    return (string, matrix)

def reconstruct(matrix):
    alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    string = ""
    for i in matrix:
        string += alphabet[i[1]]
    return string


def syllable_identifier(matrixdata):
    name = matrixdata[0]
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

#################################
def merge_strings(string1, string2):
    return string1 + string2

def merge_names(splitnames, desired_syllables=None, desired_length=None):
    combinations = []
    for i in splitnames:
        for j in splitnames:
            combinations.append(merge_strings(i, j))

    if desired_length != None:
        combinations = [x for x in combinations if len(x) == desired_length]
    
    if desired_syllables != None:
        combinations = [x for x in combinations if len(syllable_identifier(show_vowels_consonants_matrix(x))[1]) == desired_syllables]
    return combinations
#################################

def syllables(string):
    return "-".join(syllable_identifier(show_vowels_consonants_matrix(string))[1])
