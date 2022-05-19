import json 
from django.shortcuts import render
from django.http import HttpResponse
from first_project.forms import DegreeForm   
from first_app.models import Degree, Student
from django.http import HttpResponseRedirect
from first_project import *
import json
# from first_project.JSON import degree
from first_app.models import Degree, Student
clicked = 0

def index(request) : # 'request' name is convention. It can be some other name too.
    global clicked
    clicked = clicked + 1
    degree_values = Degree.objects.all()
    my_dict = { 'inject_var' : "You visited this page {} times.".format(clicked),'degree_rows' : degree_values}
    evenOrOdd = clicked % 2
    my_dict['evenOrOdd'] = evenOrOdd
    fruitList = ['Mango', 'Banana',  'Apple','Gauva']
    my_dict['fruits'] = fruitList
    return render(request,'index.html',context=my_dict)




def  index1(request):
    return render(request,'help.html')   


                # Relative import from our forms.py using .forms

def get_degree(request):
  if request.method == 'POST':                  # if this is a POST request we need to process the form data
    form = DegreeForm(request.POST, request.FILES)   # create a form instance and populate it with data from the request:
    if form.is_valid():                         # check whether it's valid:
      title = form.cleaned_data['title']        # process the data in form.cleaned_data as required
      branch = form.cleaned_data['branch']
      print(title, branch)

      d = Degree(title=title, branch=branch)    # write to the database
      d.save()

      # Retrieve the json file and process here
      f = request.FILES['file']          # open the json files - get file handle
      data = json.load(f)
      for deg in data['degree']:         # iterate through the degree list
        t = deg['title']                 # get the title of each item in the list
        b = deg['branch']                # get the branch of each item in the list
        dl = Degree(title=t, branch=b)   # Create a Degree model instance
        dl.save()                        # save

      return HttpResponseRedirect('/degree/')   # redirect to a new URL:
  else:                                   # if a GET (or any other method) we'll create a blank form
    form = DegreeForm()
    return render(request, 'degree.html', {'form': form })  

# f = open('degree.json',)                  # Opening JSON file
# data = json.load(f)                       # Loading the file as dictionary
# for deg in data['degree']:                # Looping through the values
#     print(deg['title'], deg['branch'])
# f.close()                                 # Closing file