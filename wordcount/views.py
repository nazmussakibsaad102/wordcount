from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, "index.html")
def count(request):
    word_list = []
    word_dictionary = dict()
    punctuations = [".", ","]
    fulltext = request.GET["paragraph"]
    paragraph = fulltext
    paragraph = paragraph.lower()
    paragraph = paragraph.rstrip()
    paragraph = paragraph.split()
    for i  in range(len(paragraph)):
        if paragraph[i] not in punctuations:
            word_list.append(paragraph[i])
    for word in word_list:
        if word  in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary[word] = 1
    sort_word_dictionary = dict()
    sort_word_dictionary = sorted(word_dictionary.items(), key= lambda x:x[1], reverse=True)
    print(sort_word_dictionary)
    #this counts a word only one time. If you want to take the whole word count just take the lenth of
    #the word_list
    return render(request, "count.html",{"word_dictionary":sort_word_dictionary, 
                                            "all_word_number":len(word_list),
                                            "fulltext":fulltext})

def about(request):
    return render(request, "about.html")