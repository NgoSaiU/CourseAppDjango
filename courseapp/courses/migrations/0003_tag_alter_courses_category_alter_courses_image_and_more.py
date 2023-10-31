# Generated by Django 4.2.6 on 2023-10-31 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_active_category_create_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='courses',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='courses.category'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to='courses/%Y/%m'),
        ),
        migrations.AlterUniqueTogether(
            name='courses',
            unique_together={('subject', 'category')},
        ),
        migrations.AddField(
            model_name='courses',
            name='tags',
            field=models.ManyToManyField(to='courses.tag'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='lessons/%Y/%m')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('tags', models.ManyToManyField(to='courses.tag')),
            ],
            options={
                'unique_together': {('subject', 'courses')},
            },
        ),
    ]
