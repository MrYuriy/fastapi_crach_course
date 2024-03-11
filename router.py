from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskReposittory

from schemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskReposittory.add_one(task)
    return{"ok": True, "task_id": task_id}



@router.get("")
async def get_home() -> list[STask]:
    tasks = await TaskReposittory.find_all()
    return {"data": tasks}