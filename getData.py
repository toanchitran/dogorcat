# this script is used to download the images using the provided url
import requests
import ntpath

# the file which contain the images
image_urls_file_name = 'dog_link.txt'
# the destination of the images inside the images folder
destination_folder = 'image/dog/'

# save image data
def save_image_data(image_data,file_name):
    with open(destination_folder+file_name,'wb') as file_object:
        file_object.write(image_data)

# read the images_url file
with open(image_urls_file_name) as file_object:

    print("------DOWNLOADING AND SAVING THE IMAGES---------")
    for line in file_object:
        file_name = ntpath.basename(line.strip())
        try:
            image_data = requests.get(line).content
        except:
            print("error download an image")
        # save the image
        print(file_name)
        save_image_data(image_data,file_name)