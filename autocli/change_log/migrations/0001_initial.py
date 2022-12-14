# Generated by Django 4.1 on 2022-08-06 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed', models.DateTimeField(auto_now_add=True, help_text='Change create date.', verbose_name='Created')),
                ('action', models.IntegerField(choices=[(0, '---'), (1, 'Create'), (2, 'Update'), (3, 'Delete')], default=0, help_text='The action that was performed on a given model.', verbose_name='Change log action')),
                ('object_name', models.CharField(help_text='CLI command name.', max_length=64, verbose_name='Command name')),
                ('item_id', models.IntegerField(help_text='CLI command name.', verbose_name='Command name')),
                ('after', models.JSONField(blank=True, help_text='JSON object representation after changes was made, and saved to database.', null=True, verbose_name='JSON object representation')),
                ('administrator', models.ForeignKey(help_text='Administrator responsible for change.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Administrator')),
            ],
            options={
                'verbose_name': 'Change log',
                'verbose_name_plural': 'Change logs',
            },
        ),
    ]
