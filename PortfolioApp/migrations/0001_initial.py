# Generated by Django 4.2.5 on 2023-09-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=5)),
                ('middleName', models.CharField(blank=True, max_length=10, null=True)),
                ('lastName', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=16)),
                ('phone', models.TextField(max_length=16)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha'), ('Mormonism ', 'Mormonism')], max_length=10)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='Profile_pc/')),
            ],
        ),
    ]
