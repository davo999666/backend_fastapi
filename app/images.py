from dotenv import load_dotenv
import os
from imagekitio import ImageKit

load_dotenv()


imagekit = ImageKit(
    publicKey=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    privateKey=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    urlEndpoint=os.getenv("IMAGEKIT_URL"),
)
