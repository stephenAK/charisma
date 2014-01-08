from django.db import models
from datetime import datetime,date,time
from django.contrib import admin


class Auxillary(models.Model):
       	name		=	models.CharField(max_length="50",blank=False, null = False, help_text="Please enter Auxilliary Name")
      	short_desp 	=	models.TextField("Short Description",blank=True, null=True, help_text="Can be left blank")
        date_added	= 	models.DateTimeField (auto_now_add=True, blank =True, null = True)
     	date_updated    = 	models.DateTimeField (auto_now=True,blank =True, null = True)  
	
	def __unicode__(self):
               return self.name	

	class Meta:
		verbose_name 	    = "AUXILLARY"
		verbose_name_plural = "AUXILLARIES"
                ordering 	    = ('name',)


class member(models.Model):
	
	surname		=	models.CharField(max_length = 40, blank=False, help_text = "Please Enter Member's Surname",null= False)
      	other_name	=	models.CharField("Other name(s)",max_length = 100, blank=False, null=False, help_text="Please Enter Member's Surname")
      	phone_number	=	models.CharField(max_length=15,unique = True,blank=False, null = False, default = "",help_text= "Please enter Member's Phone Number")
      	
      	email_addres	=	models.EmailField("Email-Address", blank=True, null = True,help_text="Please enter Member's Email-address")
	age             =	models.PositiveIntegerField(blank = True, null = True,help_text ="Generated from date of birth")
     	sex             =	models.CharField('Gender', choices =(("Male","Male"),("Female","Female")),max_length = 7)
     	date_Of_birth   =	models.DateField(blank = True, null = True,help_text = "YYYY-MM-DD")
	auxilliary	=	models.ManyToManyField(Auxillary,help_text ="Select Member's Auxilliary/ enter new if not in the list",blank=True, null=True)
	status          =       models.CharField(max_length= 10, default = "Active",choices =(("Active","Active"),("Passive","Passive")))
	house_location  =       models.TextField(blank=True, null=True)
        short_notes     =       models.TextField(blank=True, null=True, help_text="This designate any additional info on the student")
	date_created	= 	models.DateTimeField (auto_now_add=True, blank =True, null = True)
     	date_updated    = 	models.DateTimeField (auto_now=True,blank =True, null = True)
	
        def __unicode__(self):
            return '%s, %s'%(self.surname.upper(),self.other_name.upper())
        
        def  edit(self):
              return"click to edit"
        
	def Full_name (self):
              return "%s, %s" %(self.surname.upper(), self.other_name.upper())
              
        def Age(self):
		if self.date_Of_birth:
	                 min_allowed_dob = datetime(1900,01,01)
	         	 max_allowed_dob = datetime.now()
			 if int(self.date_Of_birth.strftime("%G")) >= int( min_allowed_dob.strftime("%G") ) and int(self.date_Of_birth.strftime("%G")) <= int(max_allowed_dob.strftime("%G")):
               			 self.age  = "%s" %(int(max_allowed_dob.strftime("%G"))-  int(self.date_Of_birth.strftime("%G")) )
               			 return "%s" %(self.age)
                             
			 else:
				 return "Invalid Date"
          	elif self.age and int(self.age[0:3])<=120:
	        	self.date_Of_birth = None
		        return True
		        
        class Meta:
		verbose_name 	    = "MEMBER"
		verbose_name_plural = "MEMBERS"
                ordering 	    = ('pk',)	
        
        
        def birthday(self):
            if self.date_Of_birth:
                   if int(self.date_Of_birth.strftime("%G")-int(self.datetime.now().strftime("%G")))==0:
                           return "Birth day is due"
                   else:
                           return "Birth day is not due"
        
               
        def save(self,*args,**kwargs):
		
                self.Age()
    		super(member,self).save(*args, **kwargs)
		return True     
                
class member_Admin(admin.ModelAdmin):
      list_display = (	'edit',
			'Full_name',
			'sex','phone_number',
			'email_addres','age',
			'date_Of_birth','birthday','status'
			)
      search_fields = ('surname','other_name','phone_number')
      list_filter = ('sex',)
      list_per_page = 50
      ordering      = ('-date_created',)
      date_hierarchy    = 'date_created'
      readonly_fields =('age',)
      fieldsets         = ( ("Personal details", {'fields':
							(('surname','other_name'),
							'sex',('phone_number','email_addres'),
							('date_Of_birth','age'))}),
                             ("Church details",{'fields':('auxilliary','status','house_location','short_notes')}),)
                             
                             
admin.site.register(member, member_Admin)
admin.site.register(Auxillary)
