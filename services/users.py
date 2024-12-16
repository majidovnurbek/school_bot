from models.user import User,Lesson


async def add_user(user_id: int, full_name: str,is_student: bool,is_teacher: bool):
    user = User(
        user_id=user_id,
        full_name=full_name,
        is_student=is_student,
        is_teacher=is_teacher,

    )
    await user.save()


async def add_user(user_id: int, full_name: str, is_student: bool = False, is_teacher: bool = False):
    user, created = await User.update_or_create(
        user_id=user_id,  # user_id bo‘yicha tekshiruv
        defaults={
            "full_name": full_name,
            "is_student": is_student,
            "is_teacher": is_teacher,
        }
    )
    if created:
        print(f"Yangi foydalanuvchi yaratildi: {full_name}")
    else:
        print(f"Foydalanuvchi mavjud va yangilandi: {full_name}")


async def create_lesson(title: str, description: str, teacher_id: int):
    lesson = Lesson(
        title=title,
        description=description,
        teacher_id=teacher_id,
    )
    await lesson.save()