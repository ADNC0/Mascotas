from django.db import models


class Persona(models.Model):
    id_per = models.AutoField(primary_key=True)
    nombre_per = models.CharField(max_length=100)
    apellido_per = models.CharField(max_length=100)
    telefono_per = models.CharField(max_length=20, null=True, blank=True)
    correo_per = models.EmailField(max_length=100, unique=True)
    direccion_per = models.CharField(max_length=200, null=True, blank=True)
    documento_per = models.FileField(upload_to='documentos_persona/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_per} {self.apellido_per}"

    class Meta:
        db_table = 'persona'
        ordering = ['apellido_per']


class Mascota(models.Model):
    id_mas = models.AutoField(primary_key=True)
    numero_serie_mas = models.CharField(max_length=50, unique=True)
    nombre_mas = models.CharField(max_length=100)
    especie_mas = models.CharField(max_length=50)
    raza_mas = models.CharField(max_length=50, null=True, blank=True)
    sexo_mas = models.CharField(max_length=10)
    edad_mas = models.PositiveIntegerField()
    peso_mas = models.DecimalField(max_digits=5, decimal_places=2)
    foto_mas = models.ImageField(upload_to='fotos_mascotas/', null=True, blank=True)
    historial_mas = models.TextField(null=True, blank=True)
    estado_mas = models.CharField(max_length=20)
    fecha_registro_mas = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_mas

    class Meta:
        db_table = 'mascota'
        ordering = ['nombre_mas']


class Adopcion(models.Model):
    id_ado = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='adopciones')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='adopciones')
    fecha_ado = models.DateField(auto_now_add=True)
    documento_ado = models.FileField(upload_to='documentos_adopcion/', null=True, blank=True)
    observacion_ado = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Adopción de {self.mascota.nombre_mas} por {self.persona.nombre_per}"

    class Meta:
        db_table = 'adopcion'
        ordering = ['-fecha_ado']
