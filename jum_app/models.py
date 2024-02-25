from django.db import models


class MuscleTypes(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "День груп м'язів"
        verbose_name_plural = "Дні груп м'язів"
        indexes = [
            models.Index(
                fields=["id", "name"],
            ),
            models.Index(fields=["id"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class Exercise(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=255)
    video = models.URLField(null=True, blank=True)
    muscle_type = models.ForeignKey(
        MuscleTypes, on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Вправа"
        verbose_name_plural = "Вправи"
        indexes = [
            models.Index(
                fields=["id", "name", "muscle_type"],
            ),
            models.Index(fields=["id"]),
            models.Index(fields=["name"]),
            models.Index(fields=["muscle_type"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} | Muscle type: {self.muscle_type.name}"


class DayExercise(models.Model):
    date = models.DateField(auto_now_add=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        ordering = [
            "date",
            "exercise"
        ]
        verbose_name = "Впава на день"
        verbose_name_plural = "Вправи на день"
        indexes = [
            models.Index(
                fields=["id", "date", "exercise"],
            ),
            models.Index(fields=["id"]),
            models.Index(fields=["date"]),
            models.Index(fields=["exercise"]),
        ]

    def __str__(self) -> str:
        return f"{self.date} | {self.exercise.name}"


IS_HURD = [
    ("Отказ", "Отказ"),
    ("Дуже складно", "Дуже складно"),
    ("Ідеально", "Ідеально"),
    ("Задегко", "Задегко"),
]



class Repeat(models.Model):
    day_exercise = models.ForeignKey(DayExercise, on_delete=models.CASCADE, null=False, blank=False)
    repeats = models.PositiveIntegerField(null=False, blank=False)
    weight = models.FloatField(null=False, blank=False)
    hurd_type = models.CharField(max_length=255, choices=IS_HURD, null=False, blank=False)
    
    class Meta:
        ordering = [
            "day_exercise",
            "repeats",
        ]
        verbose_name = "Підхід"
        verbose_name_plural = "Підходи"
        indexes = [
            models.Index(
                fields=["id", "day_exercise", "repeats"],
            ),
            models.Index(fields=["id"]),
            models.Index(fields=["day_exercise"]),
            models.Index(fields=["repeats"]),
        ]
    
    def __str__(self) -> str:
        return f"{self.day_exercise.exercise.name} | Повторів: {self.repeats} | Вага: {self.weight} кг"
