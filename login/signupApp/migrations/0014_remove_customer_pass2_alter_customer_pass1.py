# Generated by Django 4.0.2 on 2022-03-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0013_alter_customer_fname_alter_customer_lname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='pass2',
        ),
        migrations.AlterField(
            model_name='customer',
            name='pass1',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
