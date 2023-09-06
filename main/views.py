from django.shortcuts import render

def show_main(request):
    data_list = [
        {'name': 'Brain Cells', 'amount': 1, 'description': 'Very Important'},
        {'name': 'Sanity', 'amount': 0, 'description': 'Very Important'},
        {'name': 'Pressure', 'amount': 100, 'description': 'Make Stressed'},
    ]
    context = {
        'data_list': data_list
    }

    return render(request, "main.html", context)
