from django.http import HttpResponse, JsonResponse

# from django import HttpResponse

def home_page(request):
    print("Home Page Requested")
    friends = [
        'robin'
    ]
    return JsonResponse(friends, safe=False)