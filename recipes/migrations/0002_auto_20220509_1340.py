# Generated by Django 3.2.13 on 2022-05-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('measure', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='intro',
            new_name='directions',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipes.recipe'),
        ),
    ]