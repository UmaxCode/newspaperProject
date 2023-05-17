from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from .models import CustomUser

from django.views.generic.edit import CreateView, DeleteView

from .forms import CustomUserCreationForm

from .models import TodoItem

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def homePage_View(request):

    activeUser = CustomUser.objects.get(username=f'{request.user}')
    if request.method == 'POST':
        item = request.POST['search']
        if len(item) > 0:

            activity = TodoItem.objects.create(item_name=f'{item}', by_user=activeUser)
            activity.save()
    
    user = request.user

    activities = TodoItem.objects.filter(by_user=activeUser)
    return render(request, 'newspaperApp/home.html',{
        'user': user,
        'activities': activities
    })

def delete_todo_view(request, id):
    user = CustomUser.objects.all().get(username=request.user)
    item = TodoItem.objects.all().get(id=id, by_user=user)
    item.delete()
    return redirect('home')
   

class CreateUser_View(CreateView):
    
    form_class = CustomUserCreationForm

    template_name = 'newspaperApp/signup.html'

    success_url = reverse_lazy('login')


