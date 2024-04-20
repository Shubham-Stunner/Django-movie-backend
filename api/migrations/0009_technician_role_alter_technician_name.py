# Generated by Django 5.0.4 on 2024-04-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_movie_year_of_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='technician',
            name='role',
            field=models.CharField(choices=[('Director', 'Director'), ('Visual Effects (VFX) Artist', 'Visual Effects (VFX) Artist'), ('Sound Engineer', 'Sound Engineer'), ('Editor', 'Editor')], default='Director', max_length=100),
        ),
        migrations.AlterField(
            model_name='technician',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]