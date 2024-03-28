from django import template
register = template.Library()

# from master_app.context_processors import *
# from master_app.views import *
# from master_app.models import *

# from projectApp.models import *

# from certificate_module.views import *



import time  # to get duration in secods , page waiting time 
# Measure the start time before calling the render function
start_time = time.time()
# from atexit import register
import imp
from django import template
from user_master.models import user_master
register = template.Library()
@register.filter
def getNameFilter(userid):
    try:
        user = user_master.objects.get(delete1=0,id=userid)
        return user.username
    except user_master.DoesNotExist:
        return 'DNE'



# @register.filter
# def get_usernameByFilter(userid):
#     try:
#         user = user_master.objects.get(delete1=0,empcode=userid)
#         return user.empname
#     except user_master.DoesNotExist:
#         return ''    
# @register.filter
# def empcodeNameByFilter(userid):
#     try:
#         user = user_master.objects.get(delete1=0,empcode=userid)
#         return user.empname
#     except user_master.DoesNotExist:
#         return ''    
# @register.filter
# def empcodeQualificationByFilter(userid):
#     try:
#         user = user_master.objects.get(delete1=0,empcode=userid)
#         return user.qualification
#     except user_master.DoesNotExist:
#         return ''    
# @register.filter
# def certificateNameByFilter(certid):
#     try:
#         cert = emp_skill_cert_master.objects.get(delete1=0,cid=certid)
#         return cert.cert_name
#     except emp_skill_cert_master.DoesNotExist:
#         return ''
    
# @register.filter
# def empcodeDesignationByFilter(userid):
#     try:
#         designation=getDesignationRandom(userid)
#         return designation
#     except designation.DoesNotExist:
#         return ''

# @register.filter
# def empcodeDeptNameByFilter(userid):
#     try:
#         user = user_master.objects.get(delete1=0,empcode=userid)
#         dept = dept_master.objects.get(delete1=0,deptcode=user.department)        
#         return dept.deptname
#     except dept_master.DoesNotExist:
#         return ''
# @register.filter
# def getAssRoleByFilter(userid):
#     try:
#         user = user_master.objects.get(delete1=0,empcode=userid)
#         return user.ass_role
#     except user_master.DoesNotExist:
#         return ''
# @register.filter
# def reimcategory(category):
#     try:
#         user = reimbursementmcat.objects.get(delete1=0,id=category)
#         return user.category
#     except reimbursementmcat.DoesNotExist:
#         return ''
# @register.filter
# def reimattachment(attachId):
#     try:
#         user = reimbur_attachments.objects.get(delete1=0,vid=attachId)
#         my_string=user.name
#         # return "<a href='{% url 'download_file' file_id=my_file.vid %}'>Download File</a>"
#         # substring = my_string[9:]
#         return my_string
#     except reimbur_attachments.DoesNotExist:
#         return ''



