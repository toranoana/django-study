# Generated by Django 2.0.1 on 2018-01-26 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_auto_20180126_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeCV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='anime.Anime')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='anime.CV')),
            ],
        ),
    ]