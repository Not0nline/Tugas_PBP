from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'amount': 69,
        'description': 'yes'
    }

    return render(request, "main.html", context)
