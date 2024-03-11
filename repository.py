from sqlalchemy import select
from database import TaskORM, new_session
from schemas import STask, STaskAdd


class TaskReposittory:
    @classmethod
    async def add_one(cls, task: STaskAdd):
        async with new_session() as session:
            task_dict = task.model_dump()
            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(tasl_model) for tasl_model in task_models]
            return task_schemas