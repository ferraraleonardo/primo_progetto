from django.shortcuts import render # type: ignore
def index_root(request):
    return render(request,"index_root.html")
