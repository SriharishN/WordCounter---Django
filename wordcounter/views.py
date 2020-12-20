from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import operator

@csrf_exempt
def view(request):
    return render(request, 'view.html')
@csrf_exempt
def count(request):
    wordCount = request.POST['wordContent']
    wordList = wordCount.split()
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    maxWord = 'No words entered' if not wordDictionary else max(wordDictionary, key=wordDictionary.get)
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'wordContent': wordCount, 'wordList': wordList, 'wordListLength': len(wordList), 'wordDict': sortedWords, 'maxWord': maxWord})