from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def getpower(x,n):
    a = 1
    for i in range(1,n+1):
        a = a*x
    print(a)
    return a

def calculate(x,n):
    if n == 1:
        return (1/getpower(x,1))
    else:
        return calculate(x,n-1) + (1/getpower(x,n))


@login_required
def display_result(request):
    ans = None
    if request.method == "POST":
        x = request.POST.get("x")
        n = request.POST.get("n")

        ans = calculate(int(x),int(n))


    return render(request,'api/calculate.html',{'ans':ans})
