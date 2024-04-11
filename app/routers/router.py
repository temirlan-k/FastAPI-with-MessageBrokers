from celery import group
from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api import universities
from app.celery_tasks.tasks import get_all_universities_task,get_university_task
from app.config.celery_conf.create_celery import get_task_info

from app.schemas.schema import Country

router = APIRouter(prefix='/universities', tags=['University'], responses={404: {"description": "Not found"}})


@router.post("/")
def get_universities(country: Country) -> dict:
    """
    Return the List of universities for the countries for e.g ["turkey","india","australia"] provided
    in input in a sync way
    """
    data: dict = {}
    for cnt in country:
        data.update(universities.get_all_universities_for_country(cnt))
    return data


@router.post("/async")
async def get_universities_async(country: Country):
    """
    Return the List of universities for the countries for e.g ["turkey","india","australia"] provided
    in input in an async way. It just returns the task id, which can later be used to get the result.
    """
    task = get_all_universities_task.apply_async(args=[country.country])
    return JSONResponse({"task_id": task.id})
