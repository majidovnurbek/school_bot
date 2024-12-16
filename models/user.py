from tortoise import fields
from tortoise.models import Model
import uuid

class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)  # Telegram User ID
    full_name = fields.CharField(max_length=255)
    is_student = fields.BooleanField(default=False)
    is_teacher = fields.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        table = "users"


class Lesson(Model):
    id = fields.BigIntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    teacher = fields.ForeignKeyField('models.User', related_name='lessons', on_delete=fields.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        table = "lesson"


class Attendance(Model):
    id = fields.IntField(pk=True)
    lesson = fields.ForeignKeyField('models.Lesson', related_name='attendances', on_delete=fields.CASCADE)
    student = fields.ForeignKeyField('models.User', related_name='attendances', on_delete=fields.CASCADE)
    attended_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} attended {self.lesson.title}"

