# Generated by Django 3.1.4 on 2020-12-08 15:49

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
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Incomplete', max_length=250)),
                ('serie', models.CharField(default='Incomplete', max_length=20)),
                ('from_date', models.DateField(blank=True, default=None, null=True)),
                ('to_date', models.DateField(blank=True, default=None, null=True)),
                ('from_guide', models.IntegerField(blank=True, default=None, null=True)),
                ('to_guide', models.IntegerField(blank=True, default=None, null=True)),
                ('code', models.CharField(default='Incomplete', max_length=10)),
                ('is_full', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Missing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide', models.CharField(max_length=25)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folders.folder')),
            ],
        ),
    ]
