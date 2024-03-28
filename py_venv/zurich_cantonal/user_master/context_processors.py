from django.shortcuts import redirect, render
# from master_app.models import *
# from certificate_module.views import *

# from master_app.views import *
# from master_app import *
import time





def Navigationmenu(request):
    if request.session.get('user_id') is not None : #and con is not None
        user_id=request.session.get('user_id')
        
        # deptcode=getDeptcode(request.session.get('user_id'))        
        
        # user=user_master.objects.get(empcode=user)
        # # getEmployee(user.empcode)
        
        # # getDesignation(user.empcode)        
        # empcode_md5=user_master.objects.get(empcode=request.session.get('user_id'))        
        # empcode_md5=empcode_md5.empcode_md5
        # user_id=user_master.objects.get(empcode=request.session.get('user_id'))
        # user_id=user_id.empcode        
        # user_role=user_master.objects.get(empcode=request.session.get('user_id'))
        # user_role=user_role.ass_role
        # user_location=getLocation(request.session.get('user_id')) 
        # emp_names=user_master.objects.values('empcode','empname','department','designation','qualification')
        # emp_designation=designation.objects.values('designation_code','designation_name')        
        # # emp_designation=designation.objects.filter(designation_code__in=user_master.objects.values('designation')).values('designation_code','designation_name')
        
        # emp_department=dept_master.objects.values('deptcode','sap_dept_code','deptname')
      

        # menuItem1=getNavByEmpcode(empcode=user.empcode,form_name=1) #$single by Session empcode  # 1	PCB ASSEMBLY REWORK(INTRA)
        # menuItem2=getNavByEmpcode(empcode=user.empcode,form_name=2)                              # 2	TESTING
        # menuItem3=getNavByEmpcode(empcode=user.empcode,form_name=3)                              # 3	KAIZEN
        # menuItem4=getNavByEmpcode(empcode=user.empcode,form_name=4) #Department Based menu item   # 4	SERVICE
        # menuItem5=getNavByEmpcode(empcode=user.empcode,form_name=5)  #$single by Session empcode  # 5	REJECTION/REWORK
        # menuItem6=getNavByEmpcode(empcode=user.empcode,form_name=6)  #$single by Session empcode  # 6	TORQUE METER
        # menuItem7=getNavByEmpcode(empcode=user.empcode,form_name=7)                               # 7	NYAB
        # menuItem8=getNavByEmpcode(empcode=user.empcode,form_name=8) #Department Based menu item    # 8	PROD-LOG
        # menuItem9=getNavByEmpcode(empcode=user.empcode,form_name=9)                               # 9	PCB BATCH MULTIPLE SLNO
        # menuItem10=getNavByEmpcode(empcode=user.empcode,form_name=10) #Department Based menu item  # 10	PCB MACHINE MANUAL 
        # menuItem11=getNavByEmpcode(empcode=user.empcode,form_name=11)                             # 11	TRAINING            
        # menuItem12=getNavByEmpcode(empcode=user.empcode,form_name=12) #Department Based menu item  # 12	MATERIAL MASTER     
        # menuItem13=getNavByEmpcode(empcode=user.empcode,form_name=13)                             # 13	FAT-SIGNALLING  
        # menuItem14=getNavByEmpcode(empcode=user.empcode,form_name=14)                             # 14	PROJECT MANAGEMENT-SIGNALLING
        # menuItem15=getNavByEmpcode(empcode=user.empcode,form_name=15)                             # 15	R&D SUGGESTION  
        # menuItem16=getNavByEmpcode(empcode=user.empcode,form_name=16) #Department Based menu item  # 16	SAMPLE INSPECTION   
        # menuItem17=getNavByEmpcode(empcode=user.empcode,form_name=17) #Department Based menu item  # 17	WORKSHOP    
        # menuItem18=getNavByEmpcode(empcode=user.empcode,form_name=18)                             # 18	N&S PRINTERS    
        # menuItem19=getNavByEmpcode(empcode=user.empcode,form_name=19)                             # 19	MTPL-MAINTENCE TRACKER
        # menuItem20=getNavByEmpcode(empcode=user.empcode,form_name=20) #Department Based menu item  # 20	KANBAN COMPLAINT REGISTER   
        # menuItem21=getNavByEmpcode(empcode=user.empcode,form_name=21)                             # 21	NC MODULE   
        # menuItem22=getNavByEmpcode(empcode=user.empcode,form_name=22)                             # 22	VDSS    
        # menuItem23=getNavByEmpcode(empcode=user.empcode,form_name= 23 )                           # 23	QCC/RIW            
        # menuItem24=getNavByEmpcode(empcode=user.empcode,form_name= 24 ) #Department Based menu item # 24	TESTING PDF'S          
        # menuItem25=getNavByEmpcode(empcode=user.empcode,form_name= 25 ) #Department Based menu item # 25	INSPECTION REPORT MASTER
        # menuItem26=getNavByEmpcode(empcode=user.empcode,form_name= 26 )                            # 26	EMPLOYEE PHOTOT UPLOAD  
        # menuItem27=getNavByEmpcode(empcode=user.empcode,form_name= 27 )                            # 27	NEW PROJECT ENTRY   
        # menuItem28=getNavByEmpcode(empcode=user.empcode,form_name= 28 )                            # 28	NEW T-CODE ENTRY    
        # menuItem29=getNavByEmpcode(empcode=user.empcode,form_name= 29 )                            # 29	EDP TRACKER 
        # menuItem30=getNavByEmpcode(empcode=user.empcode,form_name= 30 )  #$single by Session empcode  # 30	N&S TRACKER 
        # menuItem31=getNavByEmpcode(empcode=user.empcode,form_name= 31 )  #Department Based menu item     # 31	HR TRACKER  
        # menuItem32=getNavByEmpcode(empcode=user.empcode,form_name= 32 )  #Department Based menu item  # 32	MAINTENCE TRACKER   
        # menuItem33=getNavByEmpcode(empcode=user.empcode,form_name= 33 )                             # 33	ECM 
        # menuItem34=getNavByEmpcode(empcode=user.empcode,form_name= 34 )                            # 34	ACCOUNT 
        # menuItem35=getNavByEmpcode(empcode=user.empcode,form_name= 35 )                            # 35	V&V 
        # menuItem36=getNavByEmpcode(empcode=user.empcode,form_name= 36 )                            # 36	DATACARD    
        # menuItem37=getNavByEmpcode(empcode=user.empcode,form_name= 37 )                            # 37	PLANNING TRACKER    
        # menuItem38=getNavByEmpcode(empcode=user.empcode,form_name= 38 )                            # 38	MPLM    
        # menuItem39=getNavByEmpcode(empcode=user.empcode,form_name= 39 )                            # 39	PCN
        # menuItem40=getNavByEmpcode(empcode=user.empcode,form_name= 40 )                            # 40	MM CHANGES  
        # menuItem41=getNavByEmpcode(empcode=user.empcode,form_name= 41 )                            # 41	MEDHA ONLINE SERVICE TRACHER    
        # menuItem42=getNavByEmpcode(empcode=user.empcode,form_name= 42 )                            # 42	MEDHA SERVICES  
        # menuItem43=getNavByEmpcode(empcode=user.empcode,form_name= 43 )  #Department Based menu item     # 43	USER PRIVILEGES         
        # menuItem44=getNavByEmpcode(empcode=user.empcode,form_name= 44 )                                 # 44	TESTING PDF REPORT
        # menuItem45=getNavByEmpcode(empcode=user.empcode,form_name= 45 )                             # 45	TCODE   
        # menuItem46=getNavByEmpcode(empcode=user.empcode,form_name= 46 )                            # 46	MM HOD LIST 
        # menuItem47=getNavByEmpcode(empcode=user.empcode,form_name= 47 )                            # 47	ALTERNATE PART  
        # menuItem48=getNavByEmpcode(empcode=user.empcode,form_name= 48 )                            # 48	TOT     
        # menuItem49=getNavByEmpcode(empcode=user.empcode,form_name= 49 )                            # 49	DOCUMENT CONTROL    
        # menuItem50=getNavByEmpcode(empcode=user.empcode,form_name= 50 )  #$single by Session empcode    # 50	AUDIT_PLAN  
        # menuItem51=getNavByEmpcode(empcode=user.empcode,form_name= 51 )                                 # 51	AUDIT_MRAPPROVAL
        # menuItem52=getNavByEmpcode(empcode=user.empcode,form_name= 52 )                            # 52	AUDIT_DELGATION 
        # menuItem53=getNavByEmpcode(empcode=user.empcode,form_name= 53 )                            # 53	AUDIT_GRADING   
        # menuItem54=getNavByEmpcode(empcode=user.empcode,form_name= 54 )                            # 54	AUDIT_EFF   
        # menuItem55=getNavByEmpcode(empcode=user.empcode,form_name= 55 )                            # 55	AUDIT_DEPT_EFF  
        # menuItem56=getNavByEmpcode(empcode=user.empcode,form_name= 56 )                            # 56	IGI TRACKER 
        # menuItem57=getNavByEmpcode(empcode=user.empcode,form_name= 57 )                            # 57	MM & ALTRNATE AUTH
        # menuItem58=getNavByEmpcode(empcode=user.empcode,form_name= 58 ) #Department Based menu item # 58	Factory Planning (PRS CREATION) 
        # menuItem59=getNavByEmpcode(empcode=user.empcode,form_name= 59 )                            # 59	CANTEEN 
        # menuItem60=getNavByEmpcode(empcode=user.empcode,form_name= 60 )                            # 60	VOUCHER TEMPLATE    
        # menuItem61=getNavByEmpcode(empcode=user.empcode,form_name= 61 )  #$single by Session empcode    # 61	V&V ME LIST 
        # menuItem62=getNavByEmpcode(empcode=user.empcode,form_name= 62 )                                 # 62	MTPL-ME 
        # menuItem63=getNavByEmpcode(empcode=user.empcode,form_name= 63 )                                 # 63	DRAWING_FOOTER
        # menuItem64=getNavByEmpcode(empcode=user.empcode,form_name= 64 )                             # 64	BOM_FOOTER  
        # menuItem65=getNavByEmpcode(empcode=user.empcode,form_name= 65 )                            # 65	MPLM Drawings   
        # menuItem66=getNavByEmpcode(empcode=user.empcode,form_name= 66 )                            # 66	MPLM Documents   
        # menuItem67=getNavByEmpcode(empcode=user.empcode,form_name= 67 )                            # 67	ECM 
        # menuItem68=getNavByEmpcode(empcode=user.empcode,form_name= 68 )                            # 68	Software release module 
        # menuItem69=getNavByEmpcode(empcode=user.empcode,form_name= 69 )                            # 69	MM Changes  
        # menuItem70=getNavByEmpcode(empcode=user.empcode,form_name= 70 )                            # 70	Alternate part updation
        # menuItem71=getNavByEmpcode(empcode=user.empcode,form_name= 71 )  #Department Based menu item     # 71	IGI Tracker 
        # menuItem72=getNavByEmpcode(empcode=user.empcode,form_name= 72 )                                 # 72	PCN 
        # menuItem73=getNavByEmpcode(empcode=user.empcode,form_name= 73 )                            # 73	Alternate part request  
        # menuItem74=getNavByEmpcode(empcode=user.empcode,form_name= 74 )                            # 74	New code request Elec   
        # menuItem75=getNavByEmpcode(empcode=user.empcode,form_name= 75 )                            # 75	New code request Mech   
        # menuItem76=getNavByEmpcode(empcode=user.empcode,form_name= 76 ) #Department Based menu item      # 76	ME Tracker
        # menuItem77=getNavByEmpcode(empcode=user.empcode,form_name= 77 )                            # 77	CFT Tracker 
        # menuItem78=getNavByEmpcode(empcode=user.empcode,form_name= 78 )                            # 78	KHOJ    
        # menuItem79=getNavByEmpcode(empcode=user.empcode,form_name= 79 ) #Department Based menu item  # 79	R&D Material Request    
        # menuItem80=getNavByEmpcode(empcode=user.empcode,form_name= 80 )                            # 80	PRS Request(Capital Items)  
        # menuItem81=getNavByEmpcode(empcode=user.empcode,form_name= 81 )                            # 81	FAI Module  
        # menuItem82=getNavByEmpcode(empcode=user.empcode,form_name= 82 ) #Department Based menu item  # 82	ME-A Tracker
        # # menuItem83=getNavByEmpcode(empcode=user.empcode,form_name= 83 )                            
        # menuItem84=getNavByEmpcode(empcode=user.empcode,form_name= 84 )  #Department Based menu item # 84	OEE 
        # menuItem85=getNavByEmpcode(empcode=user.empcode,form_name= 85 )  #Department Based menu item # 85	PO_APPROVAL    
        # menuItem86=getNavByEmpcode(empcode=user.empcode,form_name= 86 )  #$single by Session empcode # 86	SAMAYAM_ADMIN   
        # menuItem87=getNavByEmpcode(empcode=user.empcode,form_name= 87 ) #Department Based menu item  # 87	FRACAS   
        # menuItem88=getNavByEmpcode(empcode=user.empcode,form_name= 88 ) #Department Based menu item     # 88	SCAR    
        # menuItem89=getNavByEmpcode(empcode=user.empcode,form_name= 89 )                             # 89	PCB TRACEBILITY     
        # menuItem90=getNavByEmpcode(empcode=user.empcode,form_name= 90 )                            # 90	RDSO    
        # menuItem91=getNavByEmpcode(empcode=user.empcode,form_name= 91 )                            # 91	ZONE CREATION
        # menuItem92=getNavByEmpcode(empcode=user.empcode,form_name= 92 )                            # 92	Maintenance 
        # menuItem93=getNavByEmpcode(empcode=user.empcode,form_name= 93 )                            # 93	ME_A_HOD    
        # menuItem94=getNavByEmpcode(empcode=user.empcode,form_name= 94 )                            # 94	OEE edit    
        # menuItem95=getNavByEmpcode(empcode=user.empcode,form_name= 95 )                            # 95	Audit   
        # menuItem96=getNavByEmpcode(empcode=user.empcode,form_name= 96 )                            # 96	OEE TL update   
        # menuItem97=getNavByEmpcode(empcode=user.empcode,form_name= 97 )                            # 97	New code request Elec   
        # menuItem98=getNavByEmpcode(empcode=user.empcode,form_name= 98 )                             # 98	KHOJ
        # menuItem99=getNavByEmpcode(empcode=user.empcode,form_name= 99 )  #$single by Session empcode   # 99	CERTIFICATE MODULE
        # menuItem100=getNavByEmpcode(empcode=user.empcode,form_name= 100 ) #$single by Session empcode  # 100	ECM        
        # menuItem101=getNavByEmpcode(empcode=user.empcode,form_name= 101 ) #$single by Session empcode  # 101	Testing Soft Copies        
        # menuItem102=getNavByEmpcode(empcode=user.empcode,form_name= 102 ) #$single by Session empcode  # 102	MM CHANGE TEST CERTIFICATE        
        # menuItem103=getNavByEmpcode(empcode=user.empcode,form_name= 103 ) #$single by Session empcode  # 103	FREIGHT DETAILS        
        
              
        context={  
            'user_id':user_id,         
            
            'CI_BASE_URL':dmos_baseURL(request),

            # 'empcode_md5':empcode_md5,            
            # 'user_role':user_role,
            # 'deptcode':deptcode,
            # 'user_location':user_location, 
            # 'emp_names':emp_names, 
            # 'emp_department':emp_department, 
            # 'emp_designation':emp_designation, 
            
            


            # 'menuItem1':menuItem1,
            # 'menuItem2':menuItem2,
            # 'menuItem3':menuItem3,
            # 'menuItem4':menuItem4,
            # 'menuItem5':menuItem5,
            # 'menuItem6':menuItem6,
            # 'menuItem7':menuItem7,
            # 'menuItem8':menuItem8,
            # 'menuItem9':menuItem9,
            # 'menuItem10':menuItem10 ,
            # 'menuItem11':menuItem11 ,
            # 'menuItem12':menuItem12 ,
            # 'menuItem13':menuItem13 ,
            # 'menuItem14':menuItem14 ,
            # 'menuItem15':menuItem15 ,
            # 'menuItem16':menuItem16 ,
            # 'menuItem17':menuItem17 ,
            # 'menuItem18':menuItem18 ,
            # 'menuItem19':menuItem19 ,
            # 'menuItem20':menuItem20 ,
            # 'menuItem21':menuItem21 ,
            # 'menuItem22':menuItem22 ,
            # 'menuItem23':menuItem23 ,
            # 'menuItem24':menuItem24 ,
            # 'menuItem25':menuItem25 ,
            # 'menuItem26':menuItem26 ,
            # 'menuItem27':menuItem27 ,
            # 'menuItem28':menuItem28 ,
            # 'menuItem29':menuItem29 ,
            # 'menuItem30':menuItem30 ,
            # 'menuItem31':menuItem31 ,
            # 'menuItem32':menuItem32 ,
            # 'menuItem33':menuItem33 ,
            # 'menuItem34':menuItem34 ,
            # 'menuItem35':menuItem35 ,
            # 'menuItem36':menuItem36 ,
            # 'menuItem37':menuItem37 ,
            # 'menuItem38':menuItem38 ,
            # 'menuItem39':menuItem39 ,
            # 'menuItem40':menuItem40 ,
            # 'menuItem41':menuItem41 ,
            # 'menuItem42':menuItem42 ,
            # 'menuItem43':menuItem43 ,
            # 'menuItem44':menuItem44 ,
            # 'menuItem45':menuItem45 ,
            # 'menuItem46':menuItem46 ,
            # 'menuItem47':menuItem47 ,
            # 'menuItem48':menuItem48 ,
            # 'menuItem49':menuItem49 ,
            # 'menuItem50':menuItem50 ,
            # 'menuItem51':menuItem51 ,
            # 'menuItem52':menuItem52 ,
            # 'menuItem53':menuItem53 ,
            # 'menuItem54':menuItem54 ,
            # 'menuItem55':menuItem55 ,
            # 'menuItem56':menuItem56 ,
            # 'menuItem57':menuItem57 ,
            # 'menuItem58':menuItem58 ,
            # 'menuItem59':menuItem59 ,
            # 'menuItem60':menuItem60 ,
            # 'menuItem61':menuItem61 ,
            # 'menuItem62':menuItem62 ,
            # 'menuItem63':menuItem63 ,
            # 'menuItem64':menuItem64 ,
            # 'menuItem65':menuItem65 ,
            # 'menuItem66':menuItem66 ,
            # 'menuItem67':menuItem67 ,
            # 'menuItem68':menuItem68 ,
            # 'menuItem69':menuItem69 ,
            # 'menuItem70':menuItem70 ,
            # 'menuItem71':menuItem71 ,
            # 'menuItem72':menuItem72 ,
            # 'menuItem73':menuItem73 ,
            # 'menuItem74':menuItem74 ,
            # 'menuItem75':menuItem75 ,
            # 'menuItem76':menuItem76 ,
            # 'menuItem77':menuItem77 ,
            # 'menuItem78':menuItem78 ,
            # 'menuItem79':menuItem79 ,
            # 'menuItem80':menuItem80 ,
            # 'menuItem81':menuItem81 ,
            # 'menuItem82':menuItem82 ,
            # # 'menuItem83':menuItem83 ,
            # 'menuItem84':menuItem84 ,
            # 'menuItem85':menuItem85 ,
            # 'menuItem86':menuItem86 ,
            # 'menuItem87':menuItem87 ,
            # 'menuItem88':menuItem88 ,
            # 'menuItem89':menuItem89 ,
            # 'menuItem90':menuItem90 ,
            # 'menuItem91':menuItem91 ,
            # 'menuItem92':menuItem92 ,
            # 'menuItem93':menuItem93 ,
            # 'menuItem94':menuItem94 ,
            # 'menuItem95':menuItem95 ,
            # 'menuItem96':menuItem96 ,
            # 'menuItem97':menuItem97 ,
            # 'menuItem98':menuItem98 ,
            # 'menuItem99':menuItem99 ,
            # 'menuItem100':menuItem100,                      
            # 'menuItem101':menuItem101,                      
            # 'menuItem102':menuItem102,                      
            # 'menuItem103':menuItem103,                      
            
            
            # 'page_load_time':pageloadtime(request),
            'title':request.path[1:],        
        }
        return context
    else:
        return redirect('index')