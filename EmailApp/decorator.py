from django.http import JsonResponse


def only_post(view_func):
    def wrapper(request,*args,**kwargs):
        if request.method == 'POST':
            return view_func(request,*args,**kwargs)
        return JsonResponse({'error':'only post method allowed'})
    return wrapper