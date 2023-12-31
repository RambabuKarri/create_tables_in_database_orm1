# Generated by Django 4.2.1 on 2023-06-17 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('doj', models.DateField()),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
