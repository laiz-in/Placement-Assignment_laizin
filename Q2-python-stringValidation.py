#define a function that takes the string as inpit and returns if the string is valid or not
def stringValidation(string):
    string = string.replace(" ", "")
    #removes the blank spaces in string

    string= string.lower()
    #lower casing the whole string to avoid case sensitivity issues

    char_counts = {}
    #dictionary to strore character frequency

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    char_frequencies = list(char_counts.values())
    #a list containing frequencies of characters

    char_freq_unique= set(char_frequencies)
    if len(char_freq_unique)>2:
        result="\nstring not valid"
        return result
    else:
        min_frequency = min(char_freq_unique)
        #min frequency of characters
        max_frequency = max(char_freq_unique)
        #max frequency of characters

        if max_frequency - min_frequency == 1:
            result= "\nstring is valid if we remove one character "
            return result
        if min_frequency - min_frequency == 0:
            result="\n string is valid"
            return result


#calls the fucntion with string as parameter
print(stringValidation("Hihi hii"))

