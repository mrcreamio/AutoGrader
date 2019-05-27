from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import home_student_record,home_teacher_record,uploaded_files,course,course_registered,score
from .forms import UploadFileForm
import re
import os
import zipfile
from django.db import connection,transaction

import time
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def assignment_upload(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file =handle_uploaded_file(request.FILES['teachertestfile'])
#             file.save()
            
#             return HttpResponse('uploaded')

#         else:
#             return HttpResponse('file not uploaded')
#     else:
#         form = UploadFileForm()
#     return render(request,'home/assignment_upload.html')

def teacher_portal(request):
        course_display = course.objects.raw('select * from home_course ')
        query=request.GET.get('email')
        teacher_id=home_teacher_record.objects.raw('select * from home_home_teacher_record where email="{}"'.format(query))
        
	if request.method == 'POST':
                
                
                print(teacher_id[0].id,"dfsf")
                cours=request.POST['course_name']
                cod=request.POST['course_code']
                print(course,cod)    
                cursor = connection.cursor()
                cursor.execute('select count(*) from home_course where code={}'.format(cod))
                check = cursor.fetchone()[0]
                if(check==0):
                    add_course=course(course_name=cours,code=cod,teacher_id=teacher_id[0],credit_hours=3)
                    add_course.save()
                else:
                    HttpResponse("course with this code alreday exist try some other")
                    # time.sleep(10)
                    return render(request,'home/teacher_portal.html',{'course_display':course_display,'teacher_id':teacher_id,'al':"Try another course code"})
                return render(request,'home/teacher_portal.html',{'course_display':course_display,'teacher_id':teacher_id,'al':" "})
 
	else:
                query=request.GET.get('email')
                print(query)
                
                return render(request,'home/teacher_portal.html',{'course_display':course_display,'teacher_id':teacher_id})

def registered_course(request):
    query=request.GET.get('email')
    student_id=home_student_record.objects.raw('select * from home_home_student_record where email="{}"'.format(query))
    courses=course_registered.objects.raw('select * from home_course_registered where student_id_id="{}"'.format(student_id[0].id))
    p=course.objects.raw('select * from home_course ')
    # print(courses[0].course_id_id,student_id[0].id,"shaheer")

    if request.method == 'GET' and 'course' in request.GET:
        c=request.GET.get('course')
        cours=course.objects.raw('select* from home_course where code="{}"'.format(c))
        print(student_id[0],"yteryrt")
        cursor = connection.cursor()
        cursor.execute('select count(*) from home_course_registered where student_id_id = "{}" and course_id_id="{}" '.format(student_id[0].id,cours[0].code))
        check = cursor.fetchone()[0]
        print (check)
        if(check==0):
            a = course_registered(student_id=student_id[0],course_id=cours[0])
            a.save()
        else:
            return HttpResponse("alredy registered course")
    print(courses,0)
    print(student_id[0],"sfsfsfsfdffsdfsfsf")
    return render(request,'home/student_portal.html',{'email':query,'p':p,'course_id':courses})

# def registered_course(request):
#     query=request.GET.get('course')
#     p=course.objects.raw('SELECT * FROM home_course where code={}'.format(query))
#     query=request.GET.get('email')
#     student_id=home_student_record.objects.raw('select * from home_home_student_record where email="{}"'.format(query))
#     print(student_id[0].id,"sdfdsfsdf")
#     if request.method == 'GET' and 'course' in request.GET:
#         a = course_registered(student_id=student_id[0],course_id=p.id[0])
#         a.save()
#         return HttpResponseRedirect('/home/login/check_login/student_portal/?email={}'.format(query),{'p':p,'registered':registered})
#         # print(p.course_name)
#         # return render(request,'home/student_portal.html',{'p':p})
#     # else:

#     registered = course_registered.objects.raw('SELECT * FROM home_course_registered where student_id={}'.format(student_id[0].id))
    
#     # p=course.objects.raw('SELECT * FROM home_course')
    
#     # return HttpResponseRedirect('/home/login/check_login/student_portal/?email={}'.format(query),{'p':p,'registered':registered})

#     return render(request,'home/student_portal.html',{'p':p,'registered':registered})

# def create_course(request):
#     return HttpResponse('hello')
#         if request.method == 'POST':
#                 p=home_teacher_record.objects.raw('SELECT * FROM home_home_teacher_record')
#                 for i in p:
#                         if contact[0]==i.email and contact[1]==i.password:
#                                 teacher_id=i.id
#                                 credit_hours=3
#                                 course_record=home_course(teacher_id=teacher_id,credit_hours=credit_hours)
#                                 course_record.save()
#                                 return HttpResponse('hello')
#         else:
#                  return HttpResponseRedirect('/home/teacher_portal')

def assignment_upload(request):
    course_name = request.GET.get('course_name')
    course_code = request.GET.get('course_code')
    print(course_name)
    if request.method == 'POST':
        question_file = request.FILES['questionfile']
        uploaded_files1=uploaded_files(course_no_id=course_code,zipfile=question_file)
        uploaded_files1.save()
        return HttpResponseRedirect('/home/teacher_index/')

        # teacher_test_file = request.FILES['teachertestfile']
        # student_test_file = request.FILES['studenttestfile']
    else:
        # s=request.GET["course[0].code"]
        # print (s,"yesdsfsffdssdf")
        return render(request,'home/assignment_upload.html')

from wsgiref.util import FileWrapper
from mimetypes import guess_type
from django.conf import settings
import os
def assignment_download(request,slug=None):
    course_code = request.GET.get('course_code')
    data = uploaded_files.objects.raw('select * from home_uploaded_files where course_no_id = "{}"'.format(course_code))
    courses = course.objects.raw('select * from home_course')
    if slug != None:
        data = uploaded_files.objects.raw('select * from home_uploaded_files')
        print(slug)
        path = "assignments/pdf/"
        path += slug
        print(path,"222222222222222")
        
        for i in data:
            print(i.zipfile)
            if i.zipfile == path:
                files = i.zipfile
                filepath = files.path
                file_root = settings.PROTECTED_ROOT
                final_filepath = os.path.join(file_root,filepath)
                with open (final_filepath, 'rb') as f:
                    wrapper = FileWrapper(f)
                    mimetype = "application/force-download"
                    guessed_mimetype = guess_type(filepath)[0]
                    if guessed_mimetype:
                        mimetype = guessed_mimetype
                    response = HttpResponse(wrapper, content_type=mimetype)
                    response['content-disposition'] = "attachment;filename=%s"  %(files.name)
                    response['x-SendFile'] = str(files.name)
                return response
        return HttpResponse("file not found")
    else:
        print('hello')
        print(data)
        return render(request,'home/assignment_download.html',{'files':data})


def check_login(request):
    p=home_student_record.objects.raw('SELECT * FROM home_home_student_record')
    if request.method == 'GET' and 'email' in request.GET:
        for i in p:
            # print(i.email,i.password)
            if(i.password==request.GET["password"] and i.email==request.GET["email"]):
                student_id = i.id
                # files = uploaded_files.objects.all()
                # return render(request,'home/assignment_download.html',{'files':files})
                return HttpResponseRedirect('/home/login/check_login/student_portal/?email={}'.format(i.email))
                # return render(request,'home/student_portal.html')
        
        return HttpResponse("invalid username or password please try again")
    





    
def index(request):
    return render(request,'home/index.html')
def signup(request):
    return render(request,'home/signup.html') 
def login(request):
      return render(request,'home/login.html') 
def teacher_index(request):
      return render(request,'home/teacher_index.html') 
def teacher_login_l(request):
      return render(request,'home/teacher_login.html') 
#def teacher_signup(request):
 #     return render(request,'home/teacher_signup.html') 


def teacher_signup(request):
    if request.method == 'POST':
        print("hello")
        #check_login(request)
        email=request.POST["email"]
        password=request.POST["password"]
        cursor = connection.cursor()
        cursor.execute('select count(*) as marks from home_home_teacher_record where email = "{}"   '.format(email))
        check = cursor.fetchone()[0]
        if(check==0):
            teacher_record=home_teacher_record(email=email,password=password)
            teacher_record.save()
            return HttpResponseRedirect('/home/teacher_index/')
        else:
            return HttpResponse('user with this email already exist please try again with another email')

    else:
        return render(request,'home/teacher_signup.html') 



def add_signup(request):
    if request.method == 'POST':  
        # print("hello")
        #check_login(request)
        email=request.POST["email"]
        password=request.POST["password"]
        name=request.POST['s-name']
        rollno=request.POST['rollno']
        check=None
        # check=home_student_record.objects.raw("""select * 
        # from home_home_student_record 
        # where email='{}'""".format(email))
        # print (check[0].email)
        cursor = connection.cursor()
        cursor.execute('select count(*) as marks from home_home_student_record where email = "{}"   '.format(email))
        check = cursor.fetchone()[0]
        if(check==0):
            studentrecord=home_student_record(email=email,password=password,name=name,rollno=rollno)
            studentrecord.save()
            print("yes")
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse('user with this email already exist please try again with another email')


def teacher_login(request):
    
    if request.method == 'GET':
        p=home_teacher_record.objects.raw('SELECT * FROM home_home_teacher_record')
        for i in p:
            print(i.email,i.password)
            if(i.password==request.GET["password"] and i.email==request.GET["email"]):
                return HttpResponseRedirect('/home/teacher_portal/?email={}'.format(i.email))
        return HttpResponse('wrong password or email')

@csrf_exempt
def api(request):
        print("helo world")
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        a = 'ahmed'
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        # email = request.POST.get('email')
        if email and not re.match(EMAIL_REGEX, email):
            print ('email not valid')
            return HttpResponse('wrong password')
        else:
            p=home_student_record.objects.raw('SELECT * FROM home_home_student_record')
            for i in p:
                print(i.email,i.password)
                if(i.password==password and i.email==email):        
                    passed1 = request.POST.get('passed')
                    failed1 = request.POST.get('failed')
                    total = request.POST.get('total')
                    obtained = request.POST.get('obtainedMarks')
                    assign_number1 = request.POST.get('assignmentNumber')
                    assign_name1 = request.POST.get('assignmentName')
                    cursor = connection.cursor()
                    cursor.execute('select count(*) from home_score where assign_number = "{}"  and student_id_id={} '.format(assign_number1,i.id))
                    check = cursor.fetchone()[0]
                    if(check==0):
                        score1 = score(student_id_id=i.id,assign_name=assign_name1,assign_number=assign_number1,passed=passed1,failed=failed1,total=total,obtainedMarks=obtained)
                        score1.save()
                        return HttpResponse('score submited')
                    else:
                        return HttpResponse('assignment already done')
                
            return HttpResponse('you are not registered')
        print(email)
        return HttpResponse ('helo')

def marks(request):
    email=request.GET.get('email')
    student_id=home_student_record.objects.raw('select * from home_home_student_record where email="{}"'.format(email))
    marks = score.objects.raw('select * from home_score where student_id_id = "{}"'.format(student_id[0].id))
    # print(marks, " fdsafasjdlfjdsalkjflksjfd;")
    # mark = score.objects.raw('select sum(obtainedMarks) as marks from home_score where student_id_id = "{}"  '.format(student_id[0].id))
    # print(mark[1].marks,'  sdfsa')
    cursor = connection.cursor()
    cursor.execute('select sum(obtainedMarks) as marks from home_score where student_id_id = "{}"   '.format(student_id[0].id))
    max_value = cursor.fetchone()[0]
    cursor.execute('select avg(obtainedMarks),STDDEV(obtainedMarks) from home_score')
    avg = cursor.fetchone()
    std=avg[1]
    cursor.execute('select sum(total) as marks from home_score')
    total = cursor.fetchone()[0]
    # minimum=cursor.fetchone()[0]
    # cursor.execute('select STDDEV(obtainedMarks) from home_score')
    # std = cursor.fetchone()[0]
    # print(max_value,avg,avg1)
    return render(request,'home/marks.html',{'marks':marks,'studentName':student_id[0].name, 'max':max_value,'avg':avg[0],'std':std,'total':total})