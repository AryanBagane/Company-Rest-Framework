from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Hello Aryan")
    friends = ['Aryan', 'Aditya', 'Vishwa', 'Abhi']
    return JsonResponse(friends, safe= False)
    