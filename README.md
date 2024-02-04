# imageMetadataApp
Personal app, which can be used to store URL and various data into an image files for sorting/storing purposes.
This is also a coding practice for myself.

# Purpose of this App

Store URL data and possible extra data into an image file itself, while avoiding utilizing "database" for storing the image information. 
#### Additional features:
- Utilize the application to perform quick edits of the metadata
- Fetch image data from the clipboard to speed up saving process
- Both "Drag and drop" file into the application and filebrowser
- Graphical User Interface for ease of use
- Support for the legacy "imageMetadataApp" applications, where the URL was stored in the "file name" (and possibly convert old files into new ones automatically when detected?)

#### Potential features, if possible:
- Test URLs found from the images (does the URL work anymore and such, example: twitter "tweet containing the image deleted")

# Functionalities

[TBA]

## Version 1 - File_name_converter.py
<img src="https://github.com/veldoodles/imageMetadataApp/blob/main/images/First%20version%20-%20Python.png" width="720">


### Pros:
- Made with Python
- Solved the issue
- Able to convert the filenames back into URL 

### Cons:
- Manual copy-pasting was slow and tedious
- Didn't support all URLs as the original code swapped incompatable characters with other ones and may had missed few characters
- Graphic User Interface wasn't well designed
- Relied copy-pasting the new filename into the image itself
  
## Version 2 - Godot Link-To-Filename Converter
<img src="https://github.com/veldoodles/imageMetadataApp/blob/main/images/Second%20version%20-%20GODOT.png" width="720">


### Pros:
- Better User Interface (implemented buttons for shortcuts)
- More features, supports multi-image URLs, reading "clipboard" for ease of access
- Better URL-to-flename conversion method
- Supported legacy conversion method (and back)

### Cons:
- Saving process was still tedious, though less tedious
- Multi-image processing still tedious
- User Interface gets cluttered when processing many images during the same session
- Still relied on copy-pasting the new filename into the image itself
