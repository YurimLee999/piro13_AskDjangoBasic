# Generated by Django 3.0.3 on 2020-07-23 12:41

from djnago.db import migrations, model


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created = True, primary_key=True, serialize = False,)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=Ture)),
            ],
        ),
    ]
