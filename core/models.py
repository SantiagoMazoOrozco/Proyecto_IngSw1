from django.db import models

class Usuario(models.Model):
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nickname

class Emulador(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.CharField(max_length=255)  # Usa FileField si quieres manejar archivos

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Game(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    archivo_rom = models.CharField(max_length=255)  # Usa FileField si quieres manejar archivos
    imagen_portada = models.CharField(max_length=255, blank=True, null=True)  # Usa ImageField si manejas imágenes
    emulador = models.ForeignKey(Emulador, on_delete=models.SET_NULL, null=True, blank=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255, blank=True, null=True)  # Usa ImageField si manejas imágenes
    juego_favorito = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True, related_name='perfiles_favoritos')
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_conexion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nickname}"

class JuegoJugado(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tiempo_jugado = models.IntegerField(default=0)
    ultima_vez = models.DateTimeField(auto_now=True)
    logros = models.TextField(blank=True, null=True)  # Considera usar JSONField si es complejo
    archivo_guardado = models.CharField(max_length=255, blank=True, null=True)  # Usa FileField si quieres manejar archivos
    clip = models.CharField(max_length=255, blank=True, null=True)  # Usa FileField/ImageField si manejas archivos

    def __str__(self):
        return f"{self.perfil.usuario.nickname} jugó {self.game.nombre}"

class Estadisticas(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    total_tiempo_jugado = models.IntegerField(default=0)
    juego_mas_jugado = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True, related_name='estadisticas_mas_jugado')
    ultimo_juego = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True, related_name='estadisticas_ultimo_juego')

    def __str__(self):
        return f"Estadísticas de {self.perfil.usuario.nickname}"
