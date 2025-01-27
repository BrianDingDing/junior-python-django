# Generated by Django 3.2.3 on 2024-12-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(db_index=True, max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sales', models.IntegerField(default=0)),
                ('is_launched', models.BooleanField(default=True)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(null=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
