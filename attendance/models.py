from django.db import models
from datetime import datetime,date,time
from django.contrib import admin



class church_attendance(models.Model):
       name   = models.CharField(max_length=30,blank = False, null= False,help_text="Enter name of Record")
       date_of_record  = models.DateField(blank = True, null = True)
       number          = models.PositiveIntegerField("Number of People",blank=True, null=True)
       remarks         = models.TextField(blank= True, null= True)
       date_added	= 	models.DateTimeField (auto_now_add=True, blank =True, null = True)
       date_updated    = 	models.DateTimeField (auto_now=True,blank =True, null = True)  
	
       def __unicode__(self):
               return self.name	

       class Meta:
		verbose_name 	    = "Church attendance"
		verbose_name_plural = "Church attendance"
                ordering 	    = ('-date_added',)
                




class church_attendance_Admin(admin.ModelAdmin):
      list_display = (	'name',
			'date_of_record',
			'number','remarks',
			'date_added','date_updated'
			)
      search_fields = ('name',)
      list_filter = ('date_of_record',)
      list_per_page = 50
      ordering      = ('-date_added',)
      date_hierarchy    = 'date_added'






admin.site.register(church_attendance, church_attendance_Admin)
