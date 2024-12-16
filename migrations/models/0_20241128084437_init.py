from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user_id" BIGINT NOT NULL UNIQUE,
    "full_name" VARCHAR(255) NOT NULL,
    "is_student" BOOL NOT NULL  DEFAULT False,
    "is_teacher" BOOL NOT NULL  DEFAULT False
);
CREATE TABLE IF NOT EXISTS "lesson" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "teacher_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "attendance" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "attended_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "lesson_id" BIGINT NOT NULL REFERENCES "lesson" ("id") ON DELETE CASCADE,
    "student_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
