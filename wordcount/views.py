from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
##To remove bulkyness of program by writing html code in HttResponse
##we use render which request directly to the html
##for html files we have to create templates folder in project.
    #return render(request,'home.html',{'name':'Hi there is aayush'})
##here we pass dictionary also name is key and value is...

def contact(request):
    return HttpResponse("<h1>Contact</h1><br>This is our contact page")



def count(request):
    data = request.GET['fulltextarea']
    ##Take variable name as data the data through request object from GET we can get all the things fulltextarea

    #print(data)
    ##print(data) will display on terminal.
    ##our main task is to countwords,we have string now we have to convert string in list.

    word_list = data.split()
    ##split will take each word as item.
    #print(word_list)
    ##print(word_list) will display on terminal like ['This', 'is', 'aayush']

    list_length = len(word_list)
    ##list_length = len(word_list) will give the length of list 

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            # increased value by 1
            worddictionary[word] +=1
        else:
            #add to the worddictionary and set value to 1
            worddictionary[word] =1
    
    sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1))
    #sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':data, 'words':list_length,'worddictionary':sorted_list})
    ##{'fulltext':data} will pass the data on count page for this we use dictionary
    ## here fulltext is key and data is value.

def about(request):
    return render(request,'about.html')

    
