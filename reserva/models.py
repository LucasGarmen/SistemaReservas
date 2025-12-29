from django.db import models

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Habitacion {self.numero} - {self.tipo}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente','Pendiente'),('confiramda','Confirmada'),('cancelada','Cancelada')],
        default='pendiente'
    )
    
    def __str__(self):
        return f"Reserva de {self.cliente} - {self.habitacion}"
    
    @property
    def total(self):
        dias = (self.fecha_salida - self.fecha_entrada).days
        return dias *  self.habitacion.valor_diaria