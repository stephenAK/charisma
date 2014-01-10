from django.db import models
from datetime import datetime,date,time
from django.contrib import admin
from memberz.models import *



class visitor(models.Model):
        surname		=	models.CharField(max_length = 40, blank=False, help_text = "Please Enter Member's Surname",null= False)
      	other_name	=	models.CharField("Other name(s)",max_length = 100, blank=False, null=False, help_text="Please Enter Member's Surname")
      	phone_number	=	models.CharField(max_length=15,unique = True,blank=False, null = False, default = "",help_text= "Please enter Member's Phone Number")
      	email_addres	=	models.EmailField("Email-Address", blank=True, null = True,help_text="Please enter Member's Email-address")
     	sex             =	models.CharField('Gender', choices =(("Male","Male"),("Female","Female")),max_length = 7)
	house_location  =       models.TextField(blank=True, null=True)
	status          =       models.CharField(max_length=20, choices =(("Member","Member"),("Just Visiting","Just Visiting"),("Want to Join","Want to Join")))
        short_notes     =       models.TextField(blank=True, null=True, help_text="This designate any additional info on the visitor")
	date_of_visit   =       models.DateField(blank=True, null=True)
	date_created	= 	models.DateTimeField (auto_now_add=True, blank =True, null = True)
     	date_updated    = 	models.DateTimeField (auto_now=True,blank =True, null = True)
	
	
	
	def __unicode__(self):
            return '%s, %s'%(self.surname.upper(),self.other_name.upper())
        
        def  edit(self):
              return"click to edit"
        
	def Full_name (self):
              return "%s, %s" %(self.surname.upper(), self.other_name.upper())
              
        def member_now(self):
             if self.status:
                  if self.status=="Member":
                       set_member 		= member()
                       set_member.surname 	= self.surname
                       set_member.other_name 	= self.other_name
                       set_member.phone_number 	= self.phone_number
                       set_member.sex     	= self.sex
                       set_member.email_addres 	= self.email_addres
                       set_member.house_location  	= self.house_location
                       set_member.save()
                       return True
         
        def save(self,*args,**kwargs):
		
                #self.member_now()
                
    		super(visitor,self).save(*args, **kwargs)
    		
		return True
		
		
class visitor_Admin(admin.ModelAdmin):
      list_display = (	'edit',
			'Full_name',
			'sex','phone_number','date_of_visit',
			'status'
			)
      search_fields = ('surname','other_name','phone_number')
      list_filter = ('sex','status')
      list_per_page = 50
      ordering      = ('-date_created',)
      date_hierarchy    = 'date_of_visit'
      fieldsets         = ( ("Personal details", {'fields':
							(('surname','other_name'),
							'sex',('phone_number','email_addres'),
							)}),
                             ("Church details",{'fields':('status','date_of_visit','house_location','short_notes')}),)
      
                             
                             
admin.site.register(visitor, visitor_Admin)
