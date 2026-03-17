from django.shortcuts import render
from End_user_web.models import Students_Reg,Student_Attendance

# Create your views here.


def stud_home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        num=request.POST.get('Enrolment_Num')
        psw=request.POST.get('psw')
        stud_reg_data = Students_Reg.objects.all()
        for x in stud_reg_data:
            if name==x.Name and num==x.Enrollment_no and psw==x.Password:
                return render(request,'Stud_pg2.html',{'Name':name,'Number':num})

    return render(request,'Stud_login_pg.html')


def stud_reg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        num=request.POST.get('Enrolment_Num')
        roll=request.POST.get('roll_num')
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        Students_Reg.objects.create(Name=name,Enrollment_no=num,Roll_no=roll,Email=email,Password=psw).save()
        return render(request,'Stud_login_pg.html')

    return render(request,'Stud_Reg_pg.html')


def attend(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        num=request.POST.get('Enrolment_Num')
        return render(request,'Stud_pg2.1_qr_scan.html',{'Name':name,'Number':num})


def att_conf(request):
    if request.method == 'POST':
        roll = request.POST.get("name")
        tname = request.POST.get('tname')
        subname = request.POST.get('sub')
        loc = request.POST.get('loc')
        Student_Attendance.objects.create(Roll_no=roll,Teacher_name=tname,Subject_name=subname,Subject_Location=loc).save()
        return render(request,'Successful.html',{'Name':tname,'Number':roll})


def camera_feed(request):
    stream = CameraStream()
    frames = stream.get_frames()
    return StreamingHttpResponse(frames, content_type='multipart/x-mixed-replace; boundary=frame')


def detect(request):
    stream = CameraStream()
    success, frame = stream.camera.read()
    if success:
        status = True
    else:
        status = False

    return render(request, 'detect_barcodes/detect.html', context={'cam_status': status})


def s_log(request):
    return render(request,'index.html')