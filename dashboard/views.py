from django.shortcuts import render,HttpResponseRedirect
from .models import Ipconfiguration
from .forms import RegistrationIpconfiguration
import yaml
import check.yml as yml
import os


# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def ip(request):
    if request.method == 'POST':
        fm = RegistrationIpconfiguration(request.POST)
        if fm.is_valid():
            vr = fm.cleaned_data['version']
            i_name = fm.cleaned_data['interface_name']
            des = fm.cleaned_data['description']
            i_address = fm.cleaned_data['ip_address']
            mask = fm.cleaned_data['net_mask']
            if Ipconfiguration.objects.filter(version=vr, interface_name=i_name, description=des, ip_address=i_address, net_mask=mask).exists():
                stud = Ipconfiguration.objects.all()
                return render(request, 'dashboard/ip.html', {'stu': stud})
            else:
                if "." in i_name:
                    parts = i_name.split(".")
                    second_part = ".".join(parts[1:])
                    i_name = second_part
                    reg = Ipconfiguration(
                        version=vr, interface_name=i_name, description=des, ip_address=i_address, net_mask=mask)
                    reg.save()
                else:
                    reg = Ipconfiguration(
                        version=vr, interface_name=i_name, description=des, ip_address=i_address, net_mask=mask)
                    reg.save()
        else:
            fm = RegistrationIpconfiguration()

    stud = Ipconfiguration.objects.all()
    return render(request, 'dashboard/ip.html', {'stu': stud})


def bgp(request):
    return render(request, 'dashboard/bgp_configuration.html')


def home(request):
    return render(request, 'dashboard/home.html')


def delete_data(request,id):
    if request.method == 'POST':
        pi=Ipconfiguration.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard/ip/')
    

# def my_view(request):
#     yaml_file_path = 'DJANO ADMIN PANNEL DASHBOARD/admin_pannel/dashboard/ipaddress.yml'

#     with open(yaml_file_path, 'r') as f:
#         yaml_data = yaml.load(f)

#     context = {
#         'hosts': yaml_data,
#         'vars': yaml_data,
#     }

#     return render(request, 'my_template.html', {'context': context})
    



