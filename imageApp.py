import os
import json


"""GOAL:
    - Store custom data into the files and able to fetch it with same application
    - Store extra information into the files for sorting purposes   
    - Intended to function with [PNG / GIF / MP4] files
    - Able to re-name the files whatever I want (previous versions relied on storing the URL into the filename)
    - "Graphic Interface would be nice" (drag n' drop images in, buttons, etc)

    FUNCTION(s):
    > SAVING THE FILE >
    - "Drop a file in (either via clipboard [IMAGE ONLY] or drag-and-drop file in)"
    - Input the URL and extra information (for URL only inputs, minimize steps/clicks to "complete the process")
        = The application could suggest already existing tags (would need to track EVERY tag user has assigned before)
    
    < FETCH & MODIFY <
    - Drop a file in (can you input a file if it's currently in the "clipboard???")
    - Display information what file has (click to copy URL OR launch browser with URL?)
        = Ability to edit the fields

    Example tags (What I'd want to include into the image files)
    - URL: where was it found [> very important and sole purpose of the app <]
    - Image_Number: Sometimes the URL contains multiple images
    - Extra URL: for pointing towards an unique URL, let's say "original artist's website or such"
    - (Maybe?) Date the file was added/edited by this app
    - TAGS [imagination is the limit what you could add in, or the hard limit]: 
        What does the image contain that could be useful with sorting? (character count, drawing style, "genre" etc)
    
    SEEKING IMAGES WITH TAGS:
    - "I might want the app to search & show certain images with specific TAGS" 
    - Should I have a some kind of json_datafile, which would contain ALL images?
        - initial is to have some of the data stored INTO the images 
            so I wouldn't need a dedicated file to store the URLs
        - but having a json_datafile containing all used TAGS would help to keep track of "what TAGS exist"
            without having to scan through all of the files just to check what 

"""

""" Useful links, which may provide help with figuring out how to do the metadata part
    - https://stackoverflow.com/questions/12521525/reading-metadata-with-python 
"""


images = {
    "gif": "test_g.gif",
    "jpg": "test_j.jpg",
    "png": "test_p.png",
    "mp4": "test_m.mp4"
}
folder_path = 'testImages'

example_data = {
    'URL': 'https://github.com/', # most important data, WHERE was the image taken from
    'AdditionalURL': 'https://github.com/dashboard', # optional, for an extra site (maybe the artist's own site/profile?)
    'SaveDate': '2024-01-22T23:23:00+0000', # optional, WHEN was the image saved by the application
    'ImageCount': '4', # if the URL contains multiple images. Default is 1
    'TAGS': [
        'Anime',
        'Pokemon',
        'Zoroark',
        'Concept_art',
        'Artist_name'
    ] 
    # Should TAGS be a dictionary or just an array containing tag words? (capitalized?)
        ## Process tags as if they are lowercased and spaces replaced by "_"
    
}

def test_read_XMP(testImageType: str):
    current_directory = os.path.dirname(__file__) # script's own location
    relative_path = f"testImages/{images[testImageType]}"
    abs_file_path = os.path.join(current_directory, relative_path)

    print(abs_file_path)
    
    #xmpfile = XMPFiles(abs_file_path, open_forupdate=True)
    #xmp = xmpfile.get_xmp()

    #print(xmp.get_property(consts.XMP_NS_DC, 'format' ))



def updateTagList():

    pass


def write_json_data(dict_data):
    # temporary alternative way to write json data
    with open("image_data.json", "w") as outfile:
        json.dump(dict_data, outfile)


def read_json_data():
    # temporary alternative way to read json data
    with open("image_data.json", "r") as openfile:
        json_object = json.load(openfile)

    print(json_object)

if __name__ == "__main__":
    test_dictionary = {
        "image_name": "test_p.png",
        "TAGS": ["gray", "test_image", "PNG"]
    }
    write_json_data(test_dictionary)
    read_json_data()
    
    #test_read_XMP("png")


