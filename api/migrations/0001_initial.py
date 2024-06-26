# Generated by Django 5.0.6 on 2024-06-24 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LegExecutionDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sqoff", models.TimeField()),
                ("execute", models.TimeField()),
                ("rexecute", models.TimeField()),
                ("rentry", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "expiry",
                    models.CharField(
                        choices=[
                            ("daily_exp", "Daily Expiry"),
                            ("weekly_exp", "Weekly Expiry"),
                            ("monthly_exp", "Monthly Expiry"),
                        ],
                        max_length=50,
                    ),
                ),
                ("premium_gap", models.TextField(blank=True, null=True)),
                ("start", models.CharField(max_length=255)),
                ("end", models.CharField(max_length=255)),
                ("target", models.FloatField()),
                ("stop_loss", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="LegSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "state",
                    models.IntegerField(choices=[(0, "Inactive"), (1, "Active")]),
                ),
                (
                    "right",
                    models.CharField(
                        choices=[("C", "Call"), ("P", "Put")], max_length=1
                    ),
                ),
                (
                    "txn",
                    models.CharField(
                        choices=[("buy", "Buy"), ("sell", "Sell")], max_length=4
                    ),
                ),
                ("execution_time", models.TimeField(blank=True, null=True)),
                ("sqoff_time", models.TimeField(blank=True, null=True)),
                ("count_sl", models.PositiveIntegerField()),
                ("count_tp", models.PositiveIntegerField()),
                ("wait_n_trade", models.TextField(blank=True, null=True)),
                ("target_premium", models.FloatField()),
                ("stop_loss", models.FloatField(blank=True, null=True)),
                ("take_profit", models.FloatField(blank=True, null=True)),
                ("ProfitLockThreshold", models.FloatField(blank=True, null=True)),
                ("LockProfitAt", models.FloatField(blank=True, null=True)),
                ("IncreaseInProfitForTrail", models.FloatField(blank=True, null=True)),
                ("TrailProfitBy", models.FloatField(blank=True, null=True)),
                ("SL_TrailTrigger", models.TextField(blank=True, null=True)),
                ("SL_Trail_Amt", models.TextField(blank=True, null=True)),
                (
                    "on_target",
                    models.CharField(
                        choices=[
                            ("none", "None"),
                            ("leg", "Leg"),
                            ("current_portfolio", "Current Portfolio"),
                            ("other_portfolio", "Other Portfolio"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "on_tp",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ReExecuteLeg", "ReExecuteLeg"),
                            ("ReEnterLeg", "ReEnterLeg"),
                            ("KeepLegRunning", "KeepLegRunning"),
                            (
                                'partial(Execute_Legs, execute_legs=["leg4","leg5"])',
                                'partial(Execute_Legs, execute_legs=["leg4","leg5"])',
                            ),
                        ],
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "on_sl",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ReExecuteLeg", "ReExecuteLeg"),
                            ("ReEnterLeg", "ReEnterLeg"),
                            ("KeepLegRunning", "KeepLegRunning"),
                            (
                                'partial(ReExecute_At_Opposite_Leg_Ltp, oppo_leg="leg2")',
                                'partial(ReExecute_At_Opposite_Leg_Ltp, oppo_leg="leg2")',
                            ),
                            (
                                'partial(SqOff_Legs, sqoff_legs=["leg3","leg4"])',
                                'partial(SqOff_Legs, sqoff_legs=["leg3","leg4"])',
                            ),
                            (
                                'partial(Execute_Legs, execute_legs=["leg4"])',
                                'partial(Execute_Legs, execute_legs=["leg4"])',
                            ),
                        ],
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leg_settings",
                        to="api.portfolio",
                    ),
                ),
            ],
        ),
    ]
