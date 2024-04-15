import datetime
import json
import os
import time
import cv2
import requests


def get_dog_image_url(url: str) -> str:
    try:
        response = requests.get(url)
        if str(response.status_code).startswith("2"):

            response_dict = json.loads(response.text)
            return response_dict['message']
        else:
            raise Exception("Error on getting the image\n Status"
                            f"code {response.status_code}\n"
                            f"{response.text}")

    except Exception as e:
        print(f"Error on GET {e}")


def save_image(url: str, path: str = "images"):
    try:

        response = requests.get(url)
        timestamp = int(time.time())

        breed_name = url.split("/")[4]
        breed_name = breed_name.replace("-", "_")

        os.makedirs(path, exist_ok=True)

        with open(f"{path}\\image_{breed_name}.png", "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to save image {e}")


def show_images(path: str = "images"):
    images_list = os.listdir(path)

    for image_name in images_list:
        relative_path = os.path.join(path, image_name)
        image_content = cv2.imread(relative_path)
        cv2.imshow(f"{image_name.replace('png', '')}", image_content)
        cv2.waitKey(0)


def show_specific_image(path: str = "images"):
    images_list = os.listdir(path)

    for image_name in images_list:
        breed_name = input("Introduceti imaginea dorita in functie de rasa animalului: ")
        breed_image = image_name.split("_")[1]
        if breed_name.lower() in breed_image.lower():
            relative_path = os.path.join(path, image_name)
            image_content = cv2.imread(relative_path)
            cv2.imshow(f"{image_name.replace('png', '')}", image_content)
            cv2.waitKey(0)
        else:
            print("Rasa cainelui a fost introdusa incorect")

