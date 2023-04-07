#NOTE general.py contains models that can be used by any tenant
from django.db import models
from django.contrib.auth import get_user_model



class AdminSetPropectiveMembershipRule(models.Model):
    "it will be only on instance that will ever exist"
    amount =  models.DecimalField(decimal_places=2,max_digits=10)
    # the field below is what the members will upload
    propective_members_text_fields =models.JSONField(default=dict)
    propective_members_file_fields =models.JSONField(default=dict)

class ProspectiveMemberProfile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    full_name = models.CharField(max_length=600)
    telephone_number = models.CharField(max_length=600)
    email = models.EmailField()
    addresse = models.TextField()
    has_paid = models.BooleanField(default=False)
    paystack = models.CharField(max_length=300)
    amount_paid =  models.DecimalField(decimal_places=2,max_digits=10,default=0.00)

    class ProspectiveMemberApplicationStatusChoice(models.TextChoices):
        approval_in_progress = 'approval_in_progress'
        approval_in_principle_granted = 'approval_in_principle_granted'
        final_approval = 'final_approval'

    application_status = models.CharField(max_length=100,choices=ProspectiveMemberApplicationStatusChoice.choices,default=ProspectiveMemberApplicationStatusChoice.approval_in_progress)


    def __str__(self):
        return self.full_name
    
"only paid Prospective can do this"

class ProspectiveMemberFormOne(models.Model):
    prospective_member = models.OneToOneField(ProspectiveMemberProfile,on_delete=models.CASCADE)
    """
    info = {'data':[{name:'hello',value:'shegz'}]}
    """
    info = models.JSONField(default=dict)


class ProspectiveMemberFormTwo(models.Model):
    prospective_member = models.OneToOneField(ProspectiveMemberProfile,on_delete=models.CASCADE)
    
class ProspectiveMemberFormTwoFile(models.Model):
    name = models.TextField()
    file = models.FileField(upload_to='prospectivemember_file/%m/')
    form_two = models.ForeignKey(ProspectiveMemberFormTwo,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} Formtwofile'
    
