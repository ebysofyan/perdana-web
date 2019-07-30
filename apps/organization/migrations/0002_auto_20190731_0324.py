# Generated by Django 2.2.3 on 2019-07-30 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lead',
        ),
        migrations.AddField(
            model_name='club',
            name='lead',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_club', to='organization.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='body_height',
            field=models.CharField(blank=True, default='0', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='body_weight',
            field=models.CharField(blank=True, default='0', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='draw_length',
            field=models.CharField(blank=True, default='0', max_length=25, null=True),
        ),
    ]
