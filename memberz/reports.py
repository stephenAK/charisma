from models import member
from visitor.models import *
from attendance.models import *
from model_report.report import reports, ReportAdmin
from model_report.utils import (usd_format,sum_column,avg_column,count_column)
from django.utils.translation import ugettext_lazy as _



def auxi_label(report, field):
    return _("Auxilliiary")

    
def department_label(report, field):
    return _("Department")

def auxi_value(value,instance):
      return _('%s' %value)

def list_to_ul_format(rvalue, instance):
    if instance.is_value:
        return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % v for v in rvalue])
    return rvalue.value[0]
    
class Members_Report(ReportAdmin):
	title = ('Members')
	model = member
	fields = ['surname','other_name','phone_number','department__name','sex','date_Of_birth','dob_status','auxilliary__name','status',]
	list_group_by = ('sex','auxilliary__name','department__name',)
	list_serie_fields = ('sex',)
        list_filter = ('department__name','auxilliary__name','dob_status','status',)

	type = 'chart'
        
	group_totals = {
        #'department__name':count_column,
	
	}
	report_totals = {
        'department__name':count_column,
        'sex':count_column
    }
	override_field_formats = {
        'auxilliary__name':list_to_ul_format,
    }
	
        override_field_labels = {
        'department__name':department_label,
        'auxilliary__name':auxi_label,
         }

	chart_types = ('pie', 'column', 'line')

class Visitors_Report(ReportAdmin):
	title = ('Visitors')
	model = visitor
	fields = ['surname','other_name','phone_number','sex','status','date_of_visit','house_location',]
	list_group_by = ('sex','status',)
	list_serie_fields = ('sex',)
        list_filter = ('status','date_of_visit',)

	type = 'chart'
        
	group_totals = {
        #'department__name':count_column,
	
	}
	report_totals = {
        
        'sex':count_column
    }
	override_field_formats = {
        
    }
	
        override_field_labels = {
        
         }

	chart_types = ('pie', 'column', 'line')

class Attendance_Report(ReportAdmin):
	title = ('Attendance')
	model = church_attendance
	fields = ['name','date_of_record','number','remarks',]
	#list_group_by = ('sex','status',)
	list_serie_fields = ('number',)
        list_filter = ('date_of_record',)

	type = 'chart'
        
	group_totals = {
        #'department__name':count_column,
	
	}
	report_totals = {
        
        
    }
	override_field_formats = {
        
    }
	
        override_field_labels = {
        
         }

	chart_types = ('pie', 'column', 'line')


reports.register('all-Members-Report',Members_Report)
reports.register('all-visitors-Report',Visitors_Report)
reports.register('all-attendence-Report',Attendance_Report)




