from django.shortcuts import render


def handler404(request, exception):
    """
    Render custom 404 page
    """
    return render(request, "errors/404.html", status=404)

def handler500(request):
    """
    Render custo 500 page
    """
    return render(request, "errors/500.html", status=500)
