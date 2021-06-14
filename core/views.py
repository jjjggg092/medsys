from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        type = request.user.user_type

        if type == 1:
            return render(request, 'core/index.html', {

            'is_doctor' : 'True'
            } )
        elif type ==2:
            return render(request, 'core/index.html', {
            'is_patient' : 'True'
            } )
    else:
        return redirect('medsys')

def profile_info(request):
    if request.user.is_authenticated:
        type = request.user.user_type
        if type == 1:
            return render(request, 'core/profile_info.html', {

            'is_doctor' : 'True'
            } )
        elif type ==2:
            return render(request, 'core/profile_info.html', {
            'is_patient' : 'True'
            } )
    else:
        return redirect('medsys')
