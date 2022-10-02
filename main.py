from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import image
import os


directory = r"C:\Users\kbbudak\PycharmProjects\pytho\pics"

directory_sablon = r"C:\Users\kbbudak\PycharmProjects\pytho\sablon.jpeg"


def finalize_card(loc_photofolder=directory,loc_sablon=directory_sablon,loc_card=None):
    for filename in os.listdir(loc_photofolder):
        f = os.path.join(loc_photofolder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(os.path.basename(filename).split('.',2)[0])
            namesurname = os.path.basename(filename).split('.',2)[0]
            c_of_letter  = namesurname.count(" ")
#            print(c_of_letter)
            name2 = ''
            surname = ''
            if c_of_letter == 0:
                name = namesurname.split(" ", 2)
            elif c_of_letter == 1:
                name,surname = namesurname.split(" ",2)
            else:
                name, name2, surname = namesurname.split(" ",2)
                name = name + " " + name2
#            print(name)
#            print(surname)

            class_name = loc_photofolder.split(os.sep)[-1]

            fig = Image.open(f)
            fig = fig.resize((57,69))
#            fig.show()
            img = open_image(loc_sablon)
#           print(name)
            if type(name) == str:
                draw_text(img=img,text=name)
            if type(surname) == str:
                draw_text(img,surname,99,143)
            if type(class_name) == str:
                draw_text(img,class_name,99,162)

            paste_image(img,fig)
#            img.show()
            if type(name) == str:
                name = name + '.jpg'
            else:
                name = ' '.join(name)
            print(name)
            loc_card_final = os.path.join(loc_card, name)
            print("loc_card = " + loc_card)
            print(loc_card)
            img.save(loc_card_final,"JPEG")
            loc_card_final = ''

def open_image(location):
    img = Image.open(location)
    img = img.resize((321,208))
    return img

def draw_text(img,text="Hello World",cor_x=99,cor_y=124):
#   img = Image.new('RGB', (3508 ,4961 ), color = 'red')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 12)
    # draw.text((x, y),"Sample Text",(r,g,b))JJ
    draw.text((cor_x, cor_y),text,(0,0,0),font=font)
#    img.save(r"C:\Users\kbbudak\PycharmProjects\pytho\pil_red.png")
#    print(img)

def paste_image(pic1,pic2):
    pic1.paste(pic2,(240,113))


for folder in os.listdir(directory):
    path_to_save = r"C:\Users\kbbudak\PycharmProjects\pytho\NewRecs"
    path_to_save = os.path.join(path_to_save, folder)
    if not os.path.isdir(path_to_save):
        os.mkdir(path_to_save)
    print(path_to_save)
    path_of_source = os.path.join(directory, folder)

    finalize_card(loc_photofolder=path_of_source, loc_card=path_to_save)
    path_of_source = ''