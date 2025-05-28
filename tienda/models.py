from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    CONDICION_CHOICES = [
        ('NUEVO', 'Nuevo en Caja Sellada'),
        ('REAC_A', 'Reacondicionado Grado A'),
        ('SEMI_A', 'Semi-nuevo Impecable'),
        ('USADO_B', 'Usado Buen Estado'),
    ]
    
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True, related_name='productos')
    descripcion = models.TextField()
    condicion = models.CharField(max_length=10, choices=CONDICION_CHOICES, default='SEMI_A')
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Ajusta según la moneda
    # Para la imagen, necesitaremos configurar el manejo de archivos multimedia más adelante.
    # Por ahora, podemos definir el campo. Pillow es necesario (pip install Pillow).
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True) 
    stock = models.PositiveIntegerField(default=1)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.nombre