# Generated by Django 3.2.25 on 2024-06-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_requestdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='legsettings',
            name='sl_type',
            field=models.CharField(choices=[('None', 'None'), ('Premium', 'Premium'), ('Underlying', 'Underlying'), ('Strike', 'Strike'), ('AbsolutePremium', 'AbsolutePremium'), ('Delta', 'Delta'), ('Theta', 'Theta')], default='Premium', max_length=20),
        ),
        migrations.AddField(
            model_name='legsettings',
            name='tgt_type',
            field=models.CharField(choices=[('None', 'None'), ('Premium', 'Premium'), ('Underlying', 'Underlying'), ('Strike', 'Strike'), ('AbsolutePremium', 'AbsolutePremium'), ('Delta', 'Delta'), ('Theta', 'Theta')], default='Premium', max_length=20),
        ),
        migrations.AddField(
            model_name='legsettings',
            name='tp_type',
            field=models.CharField(choices=[('None', 'None'), ('Premium', 'Premium'), ('Underlying', 'Underlying'), ('Strike', 'Strike'), ('AbsolutePremium', 'AbsolutePremium'), ('Delta', 'Delta'), ('Theta', 'Theta')], default='Premium', max_length=20),
        ),
        migrations.AlterField(
            model_name='legsettings',
            name='on_sl',
            field=models.CharField(blank=True, choices=[('ReExecuteLeg', 'ReExecuteLeg'), ('ReEnterLeg', 'ReEnterLeg'), ('KeepLegRunning', 'KeepLegRunning'), ('partial_reexecute_opposite_leg', 'partial_reexecute_opposite_leg'), ('partial_sqoff_legs', 'partial_sqoff_legs'), ('partial_execute_legs', 'partial_execute_legs'), ('Pyramiding', 'Pyramiding')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='legsettings',
            name='on_tp',
            field=models.CharField(blank=True, choices=[('ReExecuteLeg', 'ReExecuteLeg'), ('ReEnterLeg', 'ReEnterLeg'), ('KeepLegRunning', 'KeepLegRunning'), ('partial_reexecute_opposite_leg', 'partial_reexecute_opposite_leg'), ('partial_sqoff_legs', 'partial_sqoff_legs'), ('partial_execute_legs', 'partial_execute_legs'), ('Pyramiding', 'Pyramiding')], max_length=150, null=True),
        ),
    ]
