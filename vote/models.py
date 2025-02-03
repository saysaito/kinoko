from django.db import models

# Create your models here.

class Vote(models.Model):
    KINOKO = 'kinoko'
    TAKENOKO = 'takenoko'
    CHOICE_TYPES = [
        (KINOKO, 'きのこの山'),
        (TAKENOKO, 'タケノコの里'),
    ]
    
    choice = models.CharField(
        max_length=10,
        choices=CHOICE_TYPES,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_choice_display()} - {self.created_at}"
