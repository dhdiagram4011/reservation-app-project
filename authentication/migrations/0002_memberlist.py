# Generated by Django 2.1.5 on 2020-07-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koreanLastname', models.CharField(max_length=5)),
                ('koreanFirstname', models.CharField(max_length=5)),
                ('englishLastname', models.CharField(max_length=10)),
                ('englishFirstname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('detailAddress', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]