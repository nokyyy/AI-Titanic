from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import MyForm
from . import models

def Home(request):
    form = MyForm()
    # return render(request, 'titanic/index.html')
    return render(request, 'titanic/index.html', {'form': form})

# def Result(request):
#    return render(request, 'titanic/result.html')

# dictionary-type(辞書型)
def Result(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            grade = form.cleaned_data['grade']
            fare = form.cleaned_data['fare']

            # predict
            answer = models.predict([[gender, grade, fare]])
            if answer == 0:
                answer = "<h1 id='death'>死亡</h1>"
            else:
                answer = "<h1 id='alive'>生存</h1>"
            
            params = {
                'gender': gender,
                'grade': grade,
                'fare': fare,
                'answer': answer,
            }
            return render(request, 'titanic/result.html', params)
    else:
        return redirect('titanic:home')



