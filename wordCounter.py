def wordcount(string):

    string=string.lower()
    #lower casing the whole string to avoid case sensitivity issues

    words=string.split()
    #split the string into words

    #empty dictionary to store the frequency of each words
    word_frequency={}

    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1

    
    #use max function to find out which words appears the most
    highest_frequency = max(word_frequency.values())

    highest_frequency_word = [word for word, count in word_frequency.items() if count == highest_frequency][0]
    length = len(highest_frequency_word)

    return length,highest_frequency_word

string=str(input("\n Enter the string please\n"))
print("\nmost repeated word is = ",wordcount(string)[1])
print("\nlenghth of the word is = ",wordcount(string)[0])

