# Generated by Django 4.2 on 2023-09-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_alter_dodatkoweinfo_gatunek_ocena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (3, 'Sci-fi'), (4, 'Drama'), (0, 'Inne'), (2, 'Komedia')], default=0),
        ),
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='filmyweb.film')),
            ],
        ),
    ]