# Generated by Django 3.1.1 on 2020-09-18 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'دعم مالى'), (2, 'دعم وظيفى'), (3, 'بلا مأوى')], help_text='نوع المساعده', null=True, verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
