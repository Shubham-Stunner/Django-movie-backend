from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

#Create Movie model
class Movie(models.Model):
    movie_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    year_choices = [(year, str(year)) for year in range(1950, 2025)]
    year_of_release = models.PositiveIntegerField(choices=year_choices)
    user_rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

#Create Actor model
class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('Male','male'),
                                                      ('Female','female')
                                                      ))

    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)

#Create Genres model
class Genre(models.Model):
    name = models.CharField(max_length=100, choices=(('Action','action'),
                                                     ('Horror','horror'),
                                                     ('Drama','drama'),
                                                     ('Comedy','comedy'),
                                                     ('Fantasy','fantasy')
                                                     ))

    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)

#Create Technician model
class Technician(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=(('Director', 'Director'),
                                                     ('Visual Effects (VFX) Artist', 'Visual Effects (VFX) Artist'),
                                                     ('Sound Engineer', 'Sound Engineer'),
                                                     ('Editor', 'Editor')
                                                     ),
                                                     default='Director'
                                                     )

    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)


