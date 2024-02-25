from django.contrib import admin
from .models import DayExercise, Repeat, MuscleTypes, Exercise


class RepeatInline(admin.TabularInline):
    model = Repeat
    extra = 0


class DayExerciseAdmin(admin.ModelAdmin):
    inlines = [RepeatInline]
    list_display = ("formatted_date", "exercise", "exercise_muscle_type", "total_approaches")
    list_filter = ("date", "exercise__muscle_type")
    search_fields = ("date", "exercise", "exercise__muscle_type__name")

    def formatted_date(self, obj):
        return obj.date.strftime("%d-%m-%Y")
    formatted_date.short_description = 'Date'

    def exercise_muscle_type(self, obj):
        return obj.exercise.muscle_type
    exercise_muscle_type.short_description = 'Exercise Muscle Type'
    
    def total_approaches(self, obj):
        return obj.repeat_set.count()


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "muscle_type")
    list_filter = ("muscle_type",)
    search_fields = ("name", "muscle_type")


admin.site.register(MuscleTypes)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(DayExercise, DayExerciseAdmin)
