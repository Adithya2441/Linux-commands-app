from threading import Timer
import subprocess
from time import sleep
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        rep = request.POST.get('rep')
        dur = request.POST.get('dur')
        cmd ='powershell -command '+command
        output=''
        for i in range(int(rep)):
            p=subprocess.run(cmd,capture_output=True,text=True,shell=True)
            output += p.stdout
            sleep(int(dur))
        context = {'output':output}
        return render(request,'home.html',context)
    return render(request,'home.html')
