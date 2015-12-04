from django.contrib import admin


# Register your models here.

from .models import Requirement, Testing_Procedure, Merchant, Finding, Merch_Requirement, Hardware, Software, \
    ServiceProvider, PaymentApplication, PaymentChannel, SAQ







#class Reporting_InstructionAdmin(admin.ModelAdmin):
#    list_display = ('get_merch_name', 'testing_procedure', 'rep_req_text')
#    def get_merch_name(self, obj):
#        return obj.testing_procedure.requirement.merchant
#    def get_req_num(self, obj):
#        return obj.testing_procedure.requirement.req_number
#    list_filter = ['testing_procedure']



#class Reporting_InstructionInline(admin.TabularInline):
#    model = Reporting_Instruction
#
class Testing_ProcedureAdmin(admin.ModelAdmin):
    list_display = ('test_number', 'test_text')


    



class Testing_ProcedureInline(admin.TabularInline):
    model = Testing_Procedure
    exclude = ("test_num_col1", "test_num_col2", "test_num_col3", "test_num_col4",)


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('version', 'saq_req', 'req_number', 'req_text')
    list_filter = ['version', 'saq_req']
    exclude = ("req_num_col1", "req_num_col2", "req_num_col3", "req_num_col4",)
    inlines = [Testing_ProcedureInline]

class Merch_RequirementAdmin(admin.ModelAdmin):
    list_display = ('merchant', 'requirement')
    list_filter = ['merchant', 'merch_req_saq']
    exclude = ("merch_req_num_col1", "merch_req_num_col2", "merch_req_num_col3", "merch_req_num_col4",)


    
admin.site.register(Merchant)
admin.site.register(Hardware)
admin.site.register(Software)
admin.site.register(ServiceProvider)
admin.site.register(PaymentApplication)
admin.site.register(Requirement, RequirementAdmin )
admin.site.register(Testing_Procedure, Testing_ProcedureAdmin)
admin.site.register(Merch_Requirement, Merch_RequirementAdmin )
#admin.site.register(Reporting_Instruction, Reporting_InstructionAdmin)
admin.site.register(Finding)
admin.site.register(PaymentChannel)
admin.site.register(SAQ)



#    def get_merch_name(self, obj):
#        return obj.requirement.merchant
#    get_merch_name.admin_order_field = 'requirement__merchant'
#    inlines = [Reporting_InstructionInline]