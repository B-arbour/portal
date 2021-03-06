# Django-related imports
from django.db import models
# Portal-sepcific 
from olc_webportalv2.users.models import User


class VirTyperProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=256)
    status = models.CharField(max_length=64, default='Unprocessed')
    download_link = models.CharField(max_length=256, blank=True)
    created_at = models.DateField(auto_now_add=True)
    report = models.CharField(max_length=100000, blank=True)

    class Meta:
        unique_together = (
            ('user', 'project_name')
        )

    def __str__(self):
        return self.project_name

    def container_namer(self):
        container_name = 'vir-typer-' + str(self.pk) + '-' + str(self.project_name).lower().replace('_', '-')
        return container_name


class VirTyperRequest(models.Model):
    STHY = 'STH'
    BURNABY = 'BUR'
    LABS = [
        (STHY, 'St. Hyacinthe'),
        (BURNABY, 'Burnaby'),
    ]

    NORI = 'NOVI'
    NORII = 'NOVII'
    HAV = 'HAV'
    MNV = 'MNV'
    VIRUSES = [
        (NORI, 'Norovirus genogroup 1'),
        (NORII, 'Norovirus genogroup 2'),
        (HAV, 'Hepatitus A'),
        (MNV, 'Murine norovirus')
    ]

    project_name = models.ForeignKey(VirTyperProject, on_delete=models.CASCADE, related_name='project_request')
    sample_name = models.CharField(max_length=64, blank=False,)
    LSTS_ID = models.CharField(max_length=64, blank=False,)
    lab_ID = models.CharField(max_length=64, choices=LABS, default=STHY, blank=False)
    isolate_source = models.CharField(max_length=64, blank=False,)
    subunit = models.PositiveIntegerField(null=True, blank=True)
    putative_classification = models.CharField(max_length=50, choices=VIRUSES, default=NORI, blank=False)
    analyst_name = models.CharField(max_length=64, blank=False,)
    date_received = models.DateField(blank=False,)
    

    class Meta:
        unique_together = (('sample_name', 'project_name'), ('LSTS_ID', 'project_name'))

    def __str__(self):
        return str(self.pk)


class VirTyperFiles(models.Model):
    sample_name = models.ForeignKey(VirTyperRequest, on_delete=models.CASCADE, related_name='sample_files')
    sequence_file = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.sequence_file


class VirTyperResults(models.Model):
    sequence_file = models.ForeignKey(VirTyperFiles, on_delete=models.CASCADE, related_name='file_results')
    allele = models.CharField(max_length=50, blank=False)
    orientation = models.CharField(max_length=50, blank=False)
    forward_primer = models.CharField(max_length=50, blank=False)
    reverse_primer = models.CharField(max_length=50, blank=False)
    trimmed_sequence = models.CharField(max_length=256, blank=False)
    trimmed_sequence_len = models.CharField(max_length=50, blank=False)
    trimmed_quality_max = models.CharField(max_length=50, blank=False)
    trimmed_quality_mean = models.CharField(max_length=50, blank=False)
    trimmed_quality_min = models.CharField(max_length=50, blank=False)
    trimmed_quality_stdev = models.CharField(max_length=50, blank=False)


class VirTyperAzureRequest(models.Model):
    project_name = models.ForeignKey(VirTyperProject, on_delete=models.CASCADE, related_name='project_azure_request')
    exit_code_file = models.CharField(max_length=256, blank=False)
