# Generated by Django 2.2.2 on 2019-06-11 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condiciones',
            fields=[
                ('id_condiciones', models.IntegerField(primary_key=True, serialize=False)),
                ('monto_de_la_subvencion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_de_seguro_y_cobertura', models.CharField(max_length=20)),
                ('ocupacion_o_puesto_de_trabajo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id_convenio', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id_distrito', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id_institucion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('pagina_web', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('ruc', models.IntegerField()),
                ('id_distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id_perfil', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id_requerimiento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id_universidad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id_representante', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=11)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_de_Capacitacion',
            fields=[
                ('id_capacitacion', models.IntegerField(primary_key=True, serialize=False)),
                ('id_convenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Convenio')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil_Requerimiento',
            fields=[
                ('id_perfil_req', models.IntegerField(primary_key=True, serialize=False)),
                ('prioridad', models.CharField(max_length=30)),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Perfil')),
                ('id_requerimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Requerimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Objetivos',
            fields=[
                ('id_objetivos', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('id_capacitacon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Plan_de_Capacitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.IntegerField(primary_key=True, serialize=False)),
                ('dias_trabajar', models.CharField(max_length=30)),
                ('minimo_horas', models.IntegerField()),
                ('maximo_horas', models.IntegerField()),
                ('hora_salida', models.TimeField()),
                ('hora_entrada', models.TimeField()),
                ('id_condiciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Condiciones')),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id_facultad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('id_universidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Universidad')),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id_escuela', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Facultad')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='id_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Provincia'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='id_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Pais'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='id_escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Escuela'),
        ),
        migrations.AddField(
            model_name='condiciones',
            name='id_convenio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Convenio'),
        ),
        migrations.CreateModel(
            name='Competencias',
            fields=[
                ('id_competencias', models.IntegerField(primary_key=True, serialize=False)),
                ('competencias_especificas', models.CharField(max_length=100)),
                ('competencias_genericas', models.CharField(max_length=100)),
                ('id_capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Plan_de_Capacitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficios',
            fields=[
                ('id_beneficio', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('beneficiado', models.CharField(max_length=30)),
                ('id_convenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Convenio')),
            ],
        ),
        migrations.CreateModel(
            name='Autoridad',
            fields=[
                ('id_autoridad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('grado', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('cargo', models.CharField(max_length=30)),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id_actividades', models.IntegerField(primary_key=True, serialize=False)),
                ('funcion_principal', models.CharField(max_length=50)),
                ('tareas_desprendidas', models.CharField(max_length=100)),
                ('id_capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_interes.Plan_de_Capacitacion')),
            ],
        ),
    ]
