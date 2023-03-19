import openai
from fastapi import APIRouter, BackgroundTasks, File, UploadFile
from fastapi_cache.decorator import cache

from internal.config import settings

router = APIRouter(tags=["AI"])
openai.api_key = settings.SECRET_OPENAI_KEY


@router.post("/generate-nigger-image")
@cache(expire=60)
async def generate_fucking_slaves(prompt: str):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1920x1080",
    )

    return response["data"][0]["url"]


@router.post("/handly-photoshop")
@cache(expire=60)
async def tiny_dick(
    prompt: str,
    background_tasks: BackgroundTasks,
    photo: UploadFile = File(...),
    mask: UploadFile = File(...),
):
    def mega_dick():
        response = openai.Image.create_edit(
            image=open(photo, "rb"),
            mask=open(mask, "rb"),
            prompt=prompt,
            n=1,
            size="1024x1024",
        )
        image_url = response["data"][0]["url"]
        return image_url

    background_tasks.add_task(mega_dick())
    return {"message": "background task hasbeen started. Please wait a minute"}


@router.post("/generate-image")
async def generate_image_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(tiny_dick(prompt, image, mask, size, number))
    return {"message": "Generating image in the background"}
