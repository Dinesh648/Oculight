from typing import Union

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from flask import Flask, request, send_file 
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import subprocess
# secrets is a python inbuilt library used to generate hex tokens
import secrets

# from Pillow package

from PIL import Image
import io
import uuid

IMAGEDIR = "images/"

app = FastAPI(debug = True)

# static file setup config
app.mount("/static", StaticFiles(directory="static"), name="static")

GRAY_IMAGE_URL = None

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# main logic 

@app.post("/upload")
async def receiveFile(file: bytes = File(...)):
    # print(file.name)
    image = Image.open(io.BytesIO(file))
    image.show()

    # image.save("images/eye", ".jpg")
    #Trying to convert the image to gray scale

    image = Image.open(io.BytesIO(file))
    gray_image = image.convert('L')

    #Extra line here
    gray_image.show()

    gray_image.save(r"C:\Users\user\OneDrive\Desktop\FastAPI\backend\images/eye.jpg", "png")
    # buffer = io.BytesIO()
    # gray_image.save(buffer, format='PNG')
    # buffer.seek(0)
    # file_bytes = buffer.getvalue()

# trying

    # global GRAY_IMAGE_URL
    # GRAY_IMAGE_URL = "http://localhost:8000/gray_image.png"

    return {"uploadStatus" : "complete"}

@app.get("/image")
async def getImage():
    return {"image_url": GRAY_IMAGE_URL}

    # return FileResponse("gray_image.jpeg")

@app.post("/uploadImage")
async def create_upload_image(file: UploadFile = File(...)):
    # FILEPATH = "./static/images/"
    FILEPATH = r"C:\Users\user\OneDrive\Desktop\final form\oculight\src\static\images/"
    filename = file.filename

    # to get the extension of the image
    # eye.png > ['eye', 'png']

    extension = filename.split(".")[1]

    if extension not in ["png", "jpeg", "jpg"]:
        return {"status": "error", "detail": "File extension not supported!"}
    
    # genertaing a unique file name
    # c1erar233481asjdfjfa.jpg

    token_name = secrets.token_hex(10) + "." + extension 

    # .static/images/c1erar233481asjdfjfa.jpg
    generated_name = FILEPATH + token_name


    file_content = await file.read()

    with open(generated_name, "wb") as file:
        file.write(file_content)

    img = Image.open(generated_name)
    # img = img.convert('L')
    print("saving the image")
    img.save(generated_name)

    print("Starting the model.....")
    # first call the 1st model file
    image_path = generated_name
    # output_path = "C:\Users\user\OneDrive\Desktop\final form\oculight\src\static\images/"
    output_path = r"C:\Users\user\OneDrive\Desktop\final form\oculight\public\static\images/"
    #running the 1st model file
    python_file = r"C:\Users\user\OneDrive\Desktop\final form\oculight\backend\Micro_anurism.py"
    print("Calling the front end")
    result = subprocess.check_output(["python",python_file,image_path, output_path])
    file.close()
    return{"fileName" : token_name}