from django.db import models
from users.models import User

class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED='applied', 'Applied'
        INTERVIEW='interview', 'Interview'
        REJECTED='rejected', 'Rejected'
        OFFER='offer', 'Offer'
        ONLINE_ASSESSMENT='online_assessment', 'Online Assessment'

    class JobType(models.TextChoices):
        INTERNSHIP='internship', 'Internship'
        JOB='job', 'Job'
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    company_name=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    link=models.URLField(blank=True)
    location=models.CharField(max_length=100, blank=False)
    applied_date=models.DateField(blank=True, null=True)
    status=models.CharField(max_length=30, choices=Status.choices, default=Status.APPLIED)
    type=models.CharField(max_length=20, choices=JobType.choices, default=JobType.JOB)
    salary=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.company_name} - {self.role}'



