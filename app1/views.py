from django.shortcuts import render , HttpResponse

# Create your views here.

# two type of views
# class based view
# function based view
# from .models import Student
# # # function based views
# def welcome(request):  # request keyword # business logic
#     # print(request.method)
#     # print(request.user)
#     print(request.__dict__)
#     studs = Student.objects.values("name")
#     final_studs = list(map(lambda x: x["name"], studs))
#     return HttpResponse(f"Welcome To The Django Apllication.....!!, {final_studs}")


def welcome(request):
    return render(request, "home.html")