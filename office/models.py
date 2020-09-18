from django.db import models
from accounts.models import User


class RequestHelp(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name='Title')
    content = models.TextField(verbose_name='Content', null=True, blank=True)
    status_choice = (
        (1, 'دعم مالى'),
        (2, 'دعم وظيفى'),
        (3, 'بلا مأوى'),
    )

    status = models.PositiveSmallIntegerField(choices=status_choice, null=True, verbose_name='Status',
                                              help_text='نوع المساعده')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Help Request'
        verbose_name_plural = 'Help Requests'

    def __str__(self):
        return self.title


class RequestConfirm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(RequestHelp, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='Status', null=True, blank=True)
    reason = models.TextField(verbose_name='Reason', help_text='سبب حالة الرفض', null=True, blank=True)

    class Meta:
        ordering = ['user', ]
        verbose_name = 'Request Confirm'
        verbose_name_plural = 'Requests Confirm'

    def __str__(self):
        return self.reason


class Donation(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, blank=True, null=True)
    donation_choice = (
        (1, 'تبرع مالى'),
        (2, 'تبرع ملابس'),
        (3, 'تبرع أجهزه'),
    )

    type = models.PositiveSmallIntegerField(choices=donation_choice, null=True, verbose_name='Type',
                                            help_text='نوع التبرع')
    payment_choice = (
        (1, ' شهرى'),
        (2, ' فورى'),
        (3, 'اسبوعى'),
    )

    payment = models.PositiveSmallIntegerField(choices=payment_choice, null=True, verbose_name='Payment',
                                               help_text='نوع المساعده')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'

    def __str__(self):
        return self.name

