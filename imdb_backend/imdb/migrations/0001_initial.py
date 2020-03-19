# Generated by Django 2.2.11 on 2020-03-19 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('no_of_facebook_likes', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('is_debut_movie', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('no_of_facebook_likes', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('movie_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('release_date', models.IntegerField(null=True)),
                ('box_office_collection_in_crores', models.FloatField()),
                ('genres', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('average_rating', models.FloatField()),
                ('actors', models.ManyToManyField(through='imdb.Cast', to='imdb.Actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_one_count', models.IntegerField(default=0)),
                ('rating_two_count', models.IntegerField(default=0)),
                ('rating_three_count', models.IntegerField(default=0)),
                ('rating_four_count', models.IntegerField(default=0)),
                ('rating_five_count', models.IntegerField(default=0)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='imdb.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Movie'),
        ),
    ]
