# Generated by Django 3.0.3 on 2020-10-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('bp', models.CharField(max_length=50)),
                ('glucose', models.CharField(max_length=50)),
                ('skin', models.CharField(max_length=50)),
                ('bmi', models.CharField(max_length=50)),
                ('pregnancies', models.CharField(max_length=50)),
                ('insulin', models.CharField(max_length=50)),
                ('diab', models.CharField(max_length=50)),
                ('probability', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('bp', models.CharField(max_length=50)),
                ('chol', models.CharField(max_length=50)),
                ('beat', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('cp', models.CharField(max_length=50)),
                ('fbs', models.CharField(max_length=50)),
                ('restecg', models.CharField(max_length=50)),
                ('exang', models.CharField(max_length=50)),
                ('oldpeak', models.CharField(max_length=50)),
                ('slope', models.CharField(max_length=50)),
                ('ca', models.CharField(max_length=50)),
                ('thal', models.CharField(max_length=50)),
                ('probability', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
    ]
