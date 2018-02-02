# Generated by Django 2.0.1 on 2018-02-02 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modir', '0001_initial'),
        ('madadkar', '0001_initial'),
        ('karbar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Madadjoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NationalCode', models.CharField(blank=True, max_length=11, null=True)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('bankAccount', models.CharField(blank=True, max_length=20)),
                ('grade', models.IntegerField(blank=True, choices=[(1, 'دبیرستان'), (3, 'غیر محصل'), (2, 'دانشحو'), (0, 'دبستان')], null=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('state', models.IntegerField(choices=[(0, 'نیازمند'), (2, 'یتیم'), (1, 'مستعد')])),
                ('healthStatus', models.IntegerField(choices=[(0, 'سالم'), (1, 'بیمار')], default=0)),
                ('disease', models.CharField(blank=True, max_length=30)),
                ('educationalStatus', models.CharField(blank=True, max_length=30)),
                ('briefDescription', models.TextField(blank=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('savingAmount', models.PositiveIntegerField(default=0)),
                ('averageGradeOfLastGrade', models.PositiveIntegerField(blank=True, null=True)),
                ('sex', models.IntegerField(choices=[(1, 'آقا'), (0, 'خانم')])),
                ('fatherName', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(blank=True, max_length=12, null=True)),
                ('karbar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='karbar.Karbar')),
                ('madadkar_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='madadkar.Madadkar')),
            ],
        ),
        migrations.CreateModel(
            name='MadadjooChangeProfileRequest',
            fields=[
                ('changeprofilerequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karbar.ChangeProfileRequest')),
                ('city', models.CharField(blank=True, max_length=20)),
                ('bankAccount', models.CharField(blank=True, max_length=20)),
                ('grade', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('state', models.IntegerField(blank=True, choices=[(0, 'نیازمند'), (2, 'یتیم'), (1, 'مستعد')], null=True)),
                ('healthStatus', models.IntegerField(blank=True, choices=[(0, 'سالم'), (1, 'بیمار')], null=True)),
                ('disease', models.CharField(blank=True, max_length=30)),
                ('educationalStatus', models.CharField(blank=True, max_length=30)),
                ('briefDescription', models.TextField(blank=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('savingAmount', models.PositiveIntegerField(blank=True, null=True)),
                ('averageGradeOfLastGrade', models.PositiveIntegerField(blank=True, null=True)),
                ('madadjoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karbar.Karbar')),
            ],
            bases=('karbar.changeprofilerequest',),
        ),
        migrations.CreateModel(
            name='MadadkarChangeRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karbar.Request')),
                ('madadjoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Madadjoo')),
                ('modir', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modir.Modir')),
            ],
            bases=('karbar.request',),
        ),
        migrations.CreateModel(
            name='MadadkarRateTheMadadjoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('madadjoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Madadjoo')),
                ('madadkar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='madadkar.Madadkar')),
            ],
        ),
        migrations.CreateModel(
            name='MadadkarRateThePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('madadkar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='madadkar.Madadkar')),
            ],
        ),
        migrations.CreateModel(
            name='MadadkarSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('madadkar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='madadkar.Madadkar')),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cost', models.PositiveIntegerField()),
                ('type', models.IntegerField(choices=[(2, 'یکباره'), (1, 'هفتگی'), (0, 'ماهانه')])),
                ('resolved', models.BooleanField(default=False)),
                ('madadjoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Madadjoo')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Need')),
            ],
        ),
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('madadjoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Madadjoo')),
            ],
        ),
        migrations.CreateModel(
            name='SupportbyModir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modir', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modir.Modir')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='SupprtBySystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modir.Modir')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='madadjoo.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='ThanksLetterSendRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='karbar.Request')),
                ('madadjoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Madadjoo')),
                ('madadkar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadkar.Madadkar')),
            ],
            bases=('karbar.request',),
        ),
        migrations.AddField(
            model_name='madadkarsupport',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='madadjoo.Payment'),
        ),
        migrations.AddField(
            model_name='madadkarratethepayment',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='madadjoo.Payment'),
        ),
    ]
