# Generated by Django 4.0.3 on 2022-04-06 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=350)),
            ],
            options={
                'ordering': ('question',),
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('rankOfHandShadow', models.BooleanField(default=False)),
                ('planetOfResidence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BarsTest.planet')),
            ],
        ),
        migrations.CreateModel(
            name='TestHandShadow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order??ode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BarsTest.order')),
                ('question', models.ManyToManyField(to='BarsTest.question')),
            ],
            options={
                'ordering': ('order??ode',),
            },
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('countOfHandShadow', models.IntegerField()),
                ('workPlanet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BarsTest.planet')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ManyToManyField(to='BarsTest.answer')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BarsTest.recruit')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BarsTest.testhandshadow')),
            ],
        ),
    ]
