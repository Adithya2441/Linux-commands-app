from celery.result import AsyncResult
import time,subprocess

from django.views import View
from .tasks import celery_run
from django.shortcuts import render
from .models import out

class Myview(View):
    def get(self,request):
        return render(request,'home.html')

        
    def post(self,request):
        if 'mainform' in request.POST:
            command = request.POST.get('command')
            rep = request.POST.get('rep')
            dur = request.POST.get('dur')
            cmd ='powershell -command '+command
            result=runcommand(cmd,rep,dur)
            context = {'output':result}
            return render(request,'home.html',context)

        if 'celeryform' in request.POST:
            command = request.POST.get('command')
            rep = request.POST.get('rep')
            dur = request.POST.get('dur')
            cmd ='powershell -command '+command 
            result=celery_run.delay(cmd,rep,dur)
            res = AsyncResult(result.id)
            r = res.get()
            context = {'output':r}
            return render(request,'home.html',context)       
        return render(request,'home.html')

def runcommand(cmd,rep,dur):
    output=''
    for i in range(int(rep)):
        time.sleep(int(dur))
        p=subprocess.run(cmd,capture_output=True,text=True,shell=True)
        output += p.stdout
        out1 = out()
        out1.result = output
        out1.rep = rep
        out1.dur = dur
        out1.save()
    return output