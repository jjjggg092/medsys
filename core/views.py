from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from authentication.models import Paciente
from django.views import View

def get_type_context(user_type):
    if user_type == 1:
        context = {'is_doctor' : 'True'}
    elif user_type == 2:
        context = {'is_patient' : 'True'}
    else:
        context = {'is_secre' : 'True'}
    return context

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = get_type_context(request.user.user_type)
        return render(request, 'core/index.html', context)
    else:
        return redirect('medsys')

class consultas(View):
    def post(self, request):
        pass

    def get(self, request):
        pass


class profile_info(View):
    def get(self, request, id_user):
        User = get_user_model()
        user = User.objects.get(id = id_user)
        if request.user.is_authenticated:
            patient_info = Paciente.objects.all()
            context = get_type_context(request.user.user_type)
            if len(patient_info) == 1:
                context['message'] = 'Informacion del paciente:'
                context['users'] = patient_info
            else:
                context['message'] = 'Agrege la informacion del paciente'
            context['user'] = user
            context['id_user'] = id_user
            return render(request, 'core/profile_info.html', context)
        else:
            return redirect('medsys')

    def post(self, request, id_user):
        User = get_user_model()
        context = get_type_context(request.user.user_type)
        context['id_user'] = id_user
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        sexo = request.POST['sexo']
        ci = request.POST['ci']
        ciudad = request.POST['ciudad']
        direccion = request.POST['direccion']
        aseguradora = request.POST['aseguradora']
        ocupacion = request.POST['ocupacion']
        sangre = request.POST['sangre']
        num_hijos = request.POST['num_hijos']
        b_date = request.POST['b-date']
        email = request.POST['email']
        estado_civil = request.POST['estado_civil']
        user = User.objects.get(id = id_user)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        context['user'] = user
        return render(request, 'core/profile_info.html', context)


class users_info(View):
    def get(self, request):
        User = get_user_model()
        patients = User.objects.filter(user_type = 2)
        context = get_type_context(request.user.user_type)
        context['patients'] = patients
        return render(request, 'core/users.html', context)
    def post(self, request):
        User = get_user_model()
        context = get_type_context(request.user.user_type)
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        sexo = request.POST['sexo']
        ci = request.POST['ci']
        ciudad = request.POST['ciudad']
        direccion = request.POST['direccion']
        aseguradora = request.POST['aseguradora']
        ocupacion = request.POST['ocupacion']
        sangre = request.POST['sangre']
        num_hijos = request.POST['num_hijos']
        b_date = request.POST['b-date']
        email = request.POST['email']
        estado_civil = request.POST['estado_civil']
        new_user = User(first_name = first_name, last_name=last_name, email=email, username = hash(f'{first_name}{last_name}{email}'), is_superuser = 0)
        new_user.save()
        new_paciente = Paciente(creator = new_user, nacimiento= b_date,cedula = ci, sexo = sexo, telefono = 2111, barrio = 'sin barrio', ciudad = ciudad,aseguradora = aseguradora,ocupacion = ocupacion,grupo_sanguineo = sangre,num_hijos = num_hijos,correo = email, estado_civil = estado_civil)
        new_paciente.save()
        print(new_user.id)
        patients = User.objects.filter(user_type = 2)
        context['patients'] = patients
        return render(request, 'core/users.html', context)

class consultas(View):
    def get(self, request):
        User = get_user_model()
        patients = User.objects.filter(user_type = 2)
        context = get_type_context(request.user.user_type)
        context['patients'] = patients
        return render(request, 'core/consultas.html', context)
    def post(self, request):
        pass

class recetas(View):
    def get(self, request):
        User = get_user_model()
        patients = User.objects.filter(user_type = 2)
        context = get_type_context(request.user.user_type)
        context['patients'] = patients
        return render(request, 'core/recetas.html', context)
    def post(self, request):
        pass

class citas(View):
    def get(self, request):
        User = get_user_model()
        patients = User.objects.filter(user_type = 2)
        context = get_type_context(request.user.user_type)
        context['patients'] = patients
        return render(request, 'core/citas.html', context)
    def post(self, request):
        pass

class equipos(View):
    def get(self, request):
        User = get_user_model()
        patients = User.objects.filter(user_type = 2)
        context = get_type_context(request.user.user_type)
        context['patients'] = patients
        return render(request, 'core/equipos.html', context)
    def post(self, request):
        pass
