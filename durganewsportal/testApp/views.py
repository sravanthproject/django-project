from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def moviesinfo(request):
    head_msg = 'Latest Movie Information'
    msg1 = 'Today is Victory Venkatesh Birthday'
    msg2 = 'RRR release in June 2020'
    msg3 = 'Anushka getting marriage soon with..sra..l..shhhh'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg= 'Latest Sports Information'
    msg1='All round performance by INDIA in 3rd T20 with WestIndies'
    msg2 = '1st one day is on Sunday i.e Dec15 2019'
    msg3 = 'Dhoni has own choice to play their Matches'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg = 'Latest Politics Information'
    msg1= 'There will be Early general elections'
    msg2 = 'All parties making their necessary steps to win in next elections'
    msg3 = 'TDP will win 2024 Elections'
    my_dict = {'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request, 'testapp/news.html',context=my_dict)
