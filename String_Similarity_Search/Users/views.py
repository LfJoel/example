from heapq import nlargest
from sys import argv

import resp as resp
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from String_Similarity_Search import settings
from Users.forms import UserUploadForm
from Users.models import UserRegister_Model, UserUpload_Model, UserMatch_Model


def base(request):
    return render(request, 'users/base.html')


def user_register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        mobilenum = request.POST.get('mobilenum')
        emailId = request.POST.get('emailId')
        location = request.POST.get('location')
        dob = request.POST.get('dob')
        if UserRegister_Model.objects.create(firstName=firstName,lastName=lastName,userName=userName,password=password,mobilenum=mobilenum,emailId=emailId,location=location,dob=dob):
            return redirect('user_login')
    return render(request, 'users/user_register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_object = UserRegister_Model.objects.get(userName=username, password=password)
        except:
            user_object = None
        if user_object is not None:
            request.session['user_id']=user_object.id
            return redirect('user_home')
    return render(request,'users/user_login.html')


def user_home(request):
    uid = request.session['user_id']
    user = UserRegister_Model.objects.get(id=uid)
    doc_obj = UserUpload_Model.objects.filter(user=user)

    return render(request,'users/user_home.html',{'doc_obj':doc_obj})


def user_upload(request):
    if request.method == "POST":
        form = UserUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            uid=request.session['user_id']
            user=UserRegister_Model.objects.get(id=uid)
            form_obj.user=user
            form_obj.save()
            return redirect('user_home')
    else:
        form = UserUploadForm()

    return render(request,'users/user_upload.html',{'form':form})


def remove(request,did):
    docobj = UserUpload_Model.objects.get(id=did)
    docobj.delete()
    return redirect('user_home')

def analysissingle(request,did):
    res = "user"
    doc_obj = UserUpload_Model.objects.get(id=did)
    de = doc_obj.document.url
    d = de[6:]
    result =''
    pos = []
    neg = []
    oth = []
    se='se'
    my_list = []
    edcount, bcount, scount, fcount, acount, ecount, hcount, buscount, encount, polcount = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    edw, bw, sw, fw, aw, ew, hw, bus, enw, pow = [], [], [], [], [], [], [], [], [], []
    eod = settings.MEDIA_ROOT + d
    with open(eod, 'r', encoding="utf8") as f:
        for line in f:
            for word in line.split():
                if word in ('django', 'web', 'design','Python', 'systems', 'developers'):
                    ecount = ecount + 1


                    ew.append(word)
                elif word in (
                'dna','sequencing','methods '):
                    scount = scount + 1
                    sw.append(word)
                elif word in (
                'markets','contributors ','supporting','largescale ' ):
                    fcount = fcount + 1
                    fw.append(word)
                elif word in (
                'vegetable', 'vegetables', 'recipe', 'kitchen', 'vegetable', 'fruits', 'ingredients', 'dining table',
                'plates'):
                    acount = acount + 1
                    aw.append(word)
                elif word in ('reading', 'author', 'publication', 'reader'):
                    bcount = bcount + 1
                    bw.append(word)
                elif word in (
                'medicine', 'doctor', 'stethoscope', 'glucose', 'nurse', 'hospital', 'patient', 'surgery', 'therapy',
                'prescription', 'diseases', 'treatment', 'affection'):
                    hcount = hcount + 1
                    hw.append(word)
                elif word in (
                'study', 'teacher', 'student', 'scholar', 'doctarate', 'school', 'college', 'marks', 'exam',
                'marksheet', 'examination', 'placement', 'professor', 'alumni', 'graduation'):
                    edcount = edcount + 1
                    edw.append(word)
                elif word in (
                'client', 'commercial', 'business', 'dealing', 'trade', 'office', 'tender', 'tertiary', 'market',
                'enterprise', 'privately', 'e-commerce'):
                    buscount = buscount + 1
                    bus.append(word)
                elif word in (
                'edutainment', 'music', 'film', 'theater', 'fun', 'cinema', 'media', 'tv', 'programming', 'movies',
                'enjoyment',):
                    encount = encount + 1
                    enw.append(word)
                elif word in (
                'parliament', 'party', 'publicly', 'ministerial', 'moderate', 'polity', 'independent', 'communism',
                'political', 'vote', 'elections',):
                    polcount = polcount + 1
                    pow.append(word)
                my_list.append(word)
    f.close()
    data = {}
    dat = [bcount, scount, fcount, acount, ecount, hcount]
    largest = nlargest(1, dat)
    cat = "others"
    a = None
    if bcount > scount or bcount > fcount or bcount > acount or bcount > ecount or bcount > hcount or bcount > edcount or bcount > buscount or bcount > encount or bcount > polcount:
        cat = ""
        a = list(set(bw))
    elif scount > bcount or scount > fcount or scount > acount or scount > ecount or scount > hcount or scount > edcount or scount > buscount or scount > encount or scount > polcount:
        cat = ""
        a = list(set(sw))
    elif fcount > bcount or fcount > scount or fcount > acount or fcount > ecount or fcount > hcount or fcount > edcount or fcount > buscount or fcount > encount or fcount > polcount:
        cat = ""
        a = list(set(fw))
    elif acount > bcount or acount > scount or acount > fcount or acount > ecount or acount > hcount or acount > edcount or acount > buscount or acount > encount or acount > polcount:
        cat = ""
        a = list(set(aw))
    elif ecount > bcount or ecount > scount or ecount > fcount or ecount > acount or ecount > hcount or ecount > edcount or ecount > buscount or ecount > encount or ecount > polcount:
        cat = ""
        a = list(set(ew))
    elif hcount > bcount or hcount > scount or hcount > fcount or hcount > acount or hcount > ecount or hcount > edcount or hcount > buscount or hcount > encount or hcount > polcount:
        cat = ""
        a = list(set(hw))
    elif edcount > bcount or edcount > scount or edcount > fcount or edcount > acount or edcount > hcount or edcount > ecount or edcount > buscount or edcount > encount or edcount > polcount:
        cat = ""
        a = list(set(edw))
    elif buscount > bcount or buscount > scount or buscount > fcount or buscount > acount or buscount > hcount or buscount > ecount or buscount > edcount or buscount > encount or buscount > polcount:
        cat = ""
        a = list(set(bus))
    elif encount > bcount or encount > scount or encount > fcount or encount > acount or encount > hcount or encount > ecount or encount > edcount or encount > buscount or encount > polcount:
        cat = ""
        a = list(set(enw))
    elif polcount > bcount or polcount > scount or polcount > fcount or polcount > acount or polcount > hcount or polcount > ecount or polcount > edcount or polcount > buscount or polcount > encount:
        cat = ""
        a = list(set(pow))
    else:
        cat = "Others"
    doc_obj.cluster = cat
    doc_obj.save(update_fields=['cluster'])
    data['wordssat'] = a
    data['doc_obj'] = doc_obj
    data['res'] = res
    data['bcount'] = bcount
    data['scount'] = scount
    data['fcount'] = fcount
    data['acount'] = acount
    data['ecount'] = ecount
    data['larger'] = cat
    data['mywords'] = a
    data['my_list'] = my_list
    if request.method == "POST":
        twt = request.POST.get('tweet')

        if '#' in twt:
            startingpoint = twt.find('#')
            a = twt[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
        #return redirect('tweetpage')

        for f in twt.split():
            if f in ('good', 'python', 'django', 'best', 'excellent', 'extraordinary', 'happy' , 'won' , 'love' , 'greate' ,):
                pos.append(f)
            elif f in ('worst', 'waste', 'poor', 'error', 'imporve', 'bad'):
                neg.append(f)
            else:
                oth.append(f)
        if len(pos) > len(neg):
            se = 'positive'
        elif len(neg) > len(pos):
            se = 'negative'
        else:
            se = 'nutral'
        UserUpload_Model.objects.create( tweet=twt, topics=result,sentiment=se,)




    return render(request,'users/analysissingle.html',data,{'result':result,'se':se})

def docanalysis(request):
    uid = request.session['user_id']
    user = UserRegister_Model.objects.get(id=uid)
    doc_obj = UserUpload_Model.objects.all()
    return render(request,'users/docanalysis.html',{'doc_obj':doc_obj})

def analysis_chart(request,chart_type):

    clusterw = UserUpload_Model.objects.all().values('original_cluster').annotate(total=Count('original_cluster'))

    return render(request,'users/analysis_chart.html',{'chart_type':chart_type,'objects':clusterw})


def ucharts(request,chart_type):
    chart = UserMatch_Model.objects.values('differ').annotate(dcount=Count('differ'))

    return render(request,"users/ucharts.html", {'form':chart, 'chart_type':chart_type})

def user_match(request):


    name = request.session['user_id']
    userObj = UserRegister_Model.objects.get(id=name)

    cname = ''
    a = ''
    if request.method == "POST":
        sname= request.POST.get('sname')
        fname= request.POST.get('fname')
        differ=request.POST.get('differ')

        '''cname = sname == fname'''
        i = 0
        while i < len(sname) and i < len(fname) and sname[i] == fname[i]:
            i += 1
            a = sname[:i]
        UserMatch_Model.objects.create(sname=sname,fname=fname,differ=a,useriid=userObj)

    return render(request, "users/user_match.html",{'cname':a})