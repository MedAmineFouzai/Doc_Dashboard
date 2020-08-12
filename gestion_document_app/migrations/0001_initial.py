# Generated by Django 3.0.7 on 2020-08-10 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.IntegerField(primary_key=True, serialize=False)),
                ('article_ref', models.CharField(max_length=20)),
                ('article_design', models.CharField(max_length=100)),
                ('prix_achat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('departement_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('departement_intitule', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('numero_depot', models.IntegerField(primary_key=True, serialize=False)),
                ('intitule_depot', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Devise',
            fields=[
                ('devise_id', models.IntegerField(primary_key=True, serialize=False)),
                ('devise_intitule', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('famille_id', models.IntegerField(primary_key=True, serialize=False)),
                ('famille_intitule', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('fournisseur_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fournisseur_intitule', models.CharField(max_length=20)),
                ('fournisseur_adresse', models.CharField(max_length=20)),
                ('fournisseur_telephone', models.CharField(max_length=20)),
                ('fournisseur_email', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.IntegerField(primary_key=True, serialize=False)),
                ('document_piece', models.CharField(max_length=100)),
                ('document_type', models.IntegerField()),
                ('document_date', models.DateField()),
                ('document_devise', models.IntegerField()),
                ('document_reference', models.CharField(max_length=100)),
                ('document_validation', models.BooleanField(default=False)),
                ('document_date_livraison', models.DateTimeField(null=True)),
                ('document_cours', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('document_P_U_HT', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('document_P_U_DEV', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('document_QT', models.IntegerField()),
                ('document_QT_QT_AT', models.IntegerField()),
                ('document_taxe', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('document_remise', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('document_MT_HT', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('document_MT_TTC', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_document_app.Article')),
                ('departement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_document_app.Departement')),
                ('fournisseur_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_document_app.Fournisseur')),
                ('numero_depot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_document_app.Depot')),
            ],
        ),
    ]
