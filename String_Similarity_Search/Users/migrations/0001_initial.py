# Generated by Django 2.0.5 on 2019-02-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMatch_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.TextField()),
                ('fname', models.TextField()),
                ('differ', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('userName', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('mobilenum', models.BigIntegerField()),
                ('emailId', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserUpload_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('original_cluster', models.CharField(max_length=200)),
                ('update_original_cluster', models.CharField(max_length=200)),
                ('cluster', models.CharField(default='pending', max_length=200)),
                ('improved_cluster', models.CharField(default='pending', max_length=200)),
                ('document', models.FileField(upload_to='doc/')),
                ('tweet', models.CharField(max_length=500)),
                ('topics', models.CharField(max_length=300)),
                ('sentiment', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete='cascade', to='Users.UserRegister_Model')),
            ],
        ),
        migrations.AddField(
            model_name='usermatch_model',
            name='useriid',
            field=models.ForeignKey(on_delete='cascade', to='Users.UserRegister_Model'),
        ),
    ]
