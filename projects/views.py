from django.shortcuts import redirect, render
from .models import Project, Tag
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib import messages
from .utils import searchProjects, paginateProjects
# Create your views here.

def projects(request):
    projects, search_query= searchProjects(request)

    custom_range, projects = paginateProjects(request,projects,3 )

    context= {

        "projects":projects,
        "search_query":search_query,
        "custom_range":custom_range
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    form= ReviewForm()
    if request.method == "POST":
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project= project
        review.owner= request.user.profile
        review.save()
        project.getVoteCount
        messages.success(request, "Your review was successfully submitted")
        return redirect('project', pk=project.id)
    context= {
        "project": project,
        "form":form
    }
    return render(request, 'projects/single_project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile= request.user.profile
    form = ProjectForm()
    if request.method== 'POST':
        newTags = request.POST.get('newTags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
           project= form.save(commit=False)
           project.owner = profile
           project.save()
           for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

           messages.success(request, "Project Added Successfully")
           return redirect('account')
    context ={
        'form': form

    }
    return render(request, 'projects/project_form.html', context)
@login_required(login_url="login")
def updateProject(request, pk):
    profile= request.user.profile
    project= profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST' :
        newTags = request.POST.get('newTags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            project=form.save()
            for tag in newTags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('projects')
    context={
        'form': form
    }
    return render(request, 'projects/project_form.html', context)
@login_required(login_url="login")
def deleteProject(request, pk):
    profile= request.user.profile

    obj= profile.project_set.get(id=pk)
    if request.method== 'POST':
         obj.delete()
         messages.succes(request, 'Project Deleted successfuly')
         return redirect('account')
    context={
        "obj":obj
    }
    return render(request, 'delete_template.html', context)
