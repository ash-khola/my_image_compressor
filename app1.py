# from re import I
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QInputDialog 
from PyQt5.QtGui import QIcon
from PIL import Image
from PyQt5.QtCore import Qt
import PIL
import os


class App(QMainWindow):    # we are inheriting our App class from predefined class QMainWindow which already has methods like window, title 

    def __init__(self):
        super().__init__()          # this statement is used to initialize parent class constructor
        self.title = "Ashish's Image Compressor"
        self.left = 400
        self.top = 50
        self.width = 1200
        self.height = 1000
        self.statusBar().showMessage("Message:")
        self.statusBar().setObjectName("status")
        self.setFixedSize(self.width, self.height)
        self.setObjectName("main_window")
        stylesheet = ""
        with open("my_gui\design1.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)    # stylesheet, setFixedSize, setobjectName etc. are methods of the parent class QMainWindow
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #_____________________________________________________ 

        # ******************************************** main window ********************************************

        # ---- making the window of file bubble -----
        self.file_bubble = QFrame(self)                      # here it is an attribute which is dynamically allocated the type by the return value from QFrame(self) which is a small window
        self.file_bubble.setObjectName("bubble")             # to add qss properties we need to assign some name to it so that we can change it's properties in qss file
        self.file_bubble.move(200, 100)                      # to set the bubble position in the window
        self.file_bubble.mousePressEvent = self.file_bubble_clicked  # a mouse press event has been added to the attribute file_bubble and this event will be automatically passed along with the attribute when we call file_bubble_clicked function for it


        # ---- making the heading of file bubble -----
        self.file_bubble_heading = QLabel(self.file_bubble)      # this is the heading attribute for file bubble 
        self.file_bubble_heading.setObjectName("bubble_heading") # object namae given to this attribte to use it in the qss file
        self.file_bubble_heading.setText("Compress Image")       # giving text to the heading
        self.file_bubble_heading.move(320, 10)                   # setting the position of the heading with respect to file bubble


        # ---- making the paragraph of file bubble -----
        self.file_bubble_para = QLabel(self.file_bubble)        # this is the paragraph attribute for file bubble 
        self.file_bubble_para.setObjectName("bubble_para")      # object namae given to this attribte to use it in the qss file
        self.file_bubble_para.setText("Click here to compress image")   # giving text to the paragraph
        self.file_bubble_para.move(300, 60)                     # setting the position of the heading with respect to file bubble



        # ------------------------------------same things below for the dir bubble

        # ---- making the window of dir bubble -----
        self.dir_bubble = QFrame(self)
        self.dir_bubble.setObjectName("bubble")
        self.dir_bubble.move(200, 500)
        self.dir_bubble.mousePressEvent = self.dir_bubble_clicked


        # ---- making the heading of dir bubble -----
        self.dir_bubble_heading = QLabel(self.dir_bubble)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.setText("Compress Folder")
        self.dir_bubble_heading.move(320, 10)


        # ---- making the paragraph of dir bubble -----
        self.dir_bubble_para = QLabel(self.dir_bubble)
        self.dir_bubble_para.setObjectName("bubble_para")
        self.dir_bubble_para.setText("Click here to compress complete folder of images")
        # self.dir_bubble_para.setWordWrap(True)  # to avoid the text going out of boundary
        self.dir_bubble_para.move(220, 60)

        # ******************************************** main window ********************************************


        #_____________________________________________________ 



        # ******************************************** File bubble expanded  ********************************************

        # ---- making the window of the expanded file bubble -----
        self.file_bubble_expanded = QFrame(self)
        self.file_bubble_expanded.setObjectName("bubble_expanded")
        self.file_bubble_expanded.move(200, 100)
        self.file_bubble_expanded.setVisible(False) # initailly hiding the file and dir compression functionality bubbles otherwise they will overlap with the file and dir bubble


        # ---- giving heading to expanded file bubble -----
        self.file_bubble_heading = QLabel(self.file_bubble_expanded)      # this was used for the main window but we can reuse the same attribute to give heading to expanded file window
        self.file_bubble_heading.setObjectName("bubble_heading")          # object name given to this attribte to use it in the qss file
        self.file_bubble_heading.setText("Compress Image")                # giving text to the heading
        self.file_bubble_heading.move(320, 10)


        # ---- making back arrow of the expanded file bubble -----
        self.back_arrow_file_bubble_expanded = QLabel(self.file_bubble_expanded)    # back arrow attribute created
        self.back_arrow_file_bubble_expanded.setObjectName("back_arrow")            # object name given to beautify it in qss file
        self.back_arrow_file_bubble_expanded.move(30, 10)                           # aligned with respect to the file_bubble
        self.back_arrow_file_bubble_expanded.setTextFormat(Qt.RichText)             # added to use html special symbol codes in pyqt5
        self.back_arrow_file_bubble_expanded.setText("&#8592;")                     # hex value for writing arrow
        self.back_arrow_file_bubble_expanded.mousePressEvent = self.back_arrow_clicked   # adding mouse Press Event to back arrow attribute


        # ---- adding text, asking to upload image -----
        self.select_image_label_compressor = QLabel(self.file_bubble_expanded)
        self.select_image_label_compressor.setObjectName("bubble_para")
        self.select_image_label_compressor.setText("Choose Image")
        self.select_image_label_compressor.move(150, 100)


        # ---- adding text box to add path of the image to be compressed -----
        self.image_path = QLineEdit(self.file_bubble_expanded)
        self.image_path.setObjectName("path_text")
        self.image_path.move(300, 100)


        # ---- adding browse button to select the image directly from the explorer -----
        self.browse_button = QPushButton(self.file_bubble_expanded)
        self.browse_button.setObjectName("browse_button")
        self.browse_button.setText("...")
        self.browse_button.clicked.connect(self.select_file)   # function call to open the operating system file explorer on clicking the button
        self.browse_button.move(510, 100)


        # ---- adding text, asking to choose compression quality -----
        self.select_image_quality = QLabel(self.file_bubble_expanded)
        self.select_image_quality.setObjectName("bubble_para")
        self.select_image_quality.setText("Choose image quality")
        self.select_image_quality.move(150, 130)


        # ---- adding text box to enter quality of compression -----
        self.image_quality = QLineEdit(self.file_bubble_expanded)
        self.image_quality.setObjectName("quality_path_text")
        self.image_quality.move(350, 130)


        # ---- adding dropbox to choose quality of compression -----
        self.quality_combo = QComboBox(self.file_bubble_expanded)
        self.quality_combo.setObjectName("quality_combo")
        self.quality_combo.addItem("High")
        self.quality_combo.addItem("Medium")
        self.quality_combo.addItem("Low")
        self.quality_combo.move(510, 130)
        self.quality_combo.currentIndexChanged.connect(self.quality_current_value_img)

        
        # ---- making the compress button at the end -----
        self.compress_image = QPushButton(self.file_bubble_expanded)
        self.compress_image.setObjectName("compress_button")
        self.compress_image.setText("Compress")
        self.compress_image.clicked.connect(self.resize_pic)  # on clicking the button the resize_pic function will be called which will further call compress_code inside it to finally compress the image
        self.compress_image.move(350, 190)


        # ******************************************** End File bubble expanded  ********************************************

        #_____________________________________________________ 





        # ******************************************** Dir bubble expanded  ********************************************

        # ---- making the window of the expanded dir bubble -----
        self.dir_bubble_expanded = QFrame(self)
        self.dir_bubble_expanded.setObjectName("bubble_expanded")
        self.dir_bubble_expanded.move(200, 100)
        self.dir_bubble_expanded.setVisible(False)


        # ---- making back arrow of the expanded dir bubble -----
        self.back_arrow_dir_bubble_expanded = QLabel(self.dir_bubble_expanded)
        self.back_arrow_dir_bubble_expanded.setObjectName("back_arrow")
        self.back_arrow_dir_bubble_expanded.move(30, 10)
        self.back_arrow_dir_bubble_expanded.setTextFormat(Qt.RichText)
        self.back_arrow_dir_bubble_expanded.setText("&#8592;")
        self.back_arrow_dir_bubble_expanded.mousePressEvent = self.back_arrow_clicked


        # ---- giving heading to expanded dir bubble expanded -----
        self.file_bubble_heading = QLabel(self.dir_bubble_expanded)      # this was used for the main window but we can reuse the same attribute to give heading to expanded file window
        self.file_bubble_heading.setObjectName("bubble_heading")          # object name given to this attribte to use it in the qss file
        self.file_bubble_heading.setText("Compress Folder")                # giving text to the heading
        self.file_bubble_heading.move(320, 10)


        # ---- adding text, asking to upload folder -----
        self.select_image_label_compressor = QLabel(self.dir_bubble_expanded)
        self.select_image_label_compressor.setObjectName("bubble_para")
        self.select_image_label_compressor.setText("Choose source folder")
        self.select_image_label_compressor.move(150, 100)


        # ---- adding text box to add path of the folder to be compressed -----
        self.source_path = QLineEdit(self.dir_bubble_expanded)
        self.source_path.setObjectName("path_text")
        self.source_path.move(320, 100)


        # ---- adding browse button to select the folder directly from the explorer -----
        self.browse_source_button = QPushButton(self.dir_bubble_expanded)
        self.browse_source_button.setObjectName("browse_button")
        self.browse_source_button.setText("...")
        self.browse_source_button.clicked.connect(self.select_source_folder)
        self.browse_source_button.move(520, 100)


        # ---- adding text, asking to enter destination folder path -----
        self.select_dest_label_compressor = QLabel(self.dir_bubble_expanded)
        self.select_dest_label_compressor.setObjectName("bubble_para")
        self.select_dest_label_compressor.setText("Choose destination folder")
        self.select_dest_label_compressor.move(150, 130)


        # ---- adding text box to add path of the folder where the folder image will be saved -----
        self.destination_path = QLineEdit(self.dir_bubble_expanded)
        self.destination_path.setObjectName("path_text")
        self.destination_path.move(360, 130)


        # ---- adding browse button to add path of the folder where the folder image will be saved -----
        self.browse_destination_button = QPushButton(self.dir_bubble_expanded)
        self.browse_destination_button.setObjectName("browse_button")
        self.browse_destination_button.setText("...")
        self.browse_destination_button.clicked.connect(self.select_dest_folder)   # on clicking it function called
        self.browse_destination_button.move(560, 130)


        # ---- adding text, asking to choose compression quality of folder -----
        self.select_image_quality_dir = QLabel(self.dir_bubble_expanded)
        self.select_image_quality_dir.setObjectName("bubble_para")
        self.select_image_quality_dir.setText("Choose image quality")
        self.select_image_quality_dir.move(150, 160)


        # ---- adding text box to enter quality of compression of folder -----
        self.image_quality_dir = QLineEdit(self.dir_bubble_expanded)
        self.image_quality_dir.setObjectName("quality_path_text")
        self.image_quality_dir.move(350, 160)


        # ---- adding dropbox to choose quality of compression -----
        self.quality_combo_dir = QComboBox(self.dir_bubble_expanded)
        self.quality_combo_dir.setObjectName("quality_combo")
        self.quality_combo_dir.addItem("High")
        self.quality_combo_dir.addItem("Medium")
        self.quality_combo_dir.addItem("Low")
        self.quality_combo_dir.currentIndexChanged.connect(self.quality_current_value_dir)    # calling the function to change the quality of in the quality text box as we select Low/Medium/High, by default it is High
        self.quality_combo_dir.move(510, 160)

        
        # ---- making the compress button at the end of dir expanded-----
        self.compress_dir = QPushButton(self.dir_bubble_expanded)
        self.compress_dir.setObjectName("compress_button")
        self.compress_dir.clicked.connect(self.resize_directory)
        self.compress_dir.setText("Compress")
        self.compress_dir.move(350, 220)
        
        # ******************************************** End Dir bubble expanded  ********************************************
        #_____________________________________________________ 



        self.show()  # it is a method to dislplay the window

    # ******************************************** functions ********************************************

    # ---- functionality on clicking file bubble -----
    def file_bubble_clicked(self, event):
        print("File_bubble clicked")
        self.file_bubble.setVisible(False) # we are hiding the file and dir bubble once we click on any of the button
        self.dir_bubble.setVisible(False)
        self.file_bubble_expanded.setVisible(True)  # we are making the hidden file compression fuctionality bubble visible
        self.dir_bubble_expanded.setVisible(False)  # this will be useful when we make the back button
    
    # ---- functionality on clicking dir bubble -----
    def dir_bubble_clicked(self, event):
        print("Dir bubble clicked")
        self.file_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.dir_bubble_expanded.setVisible(True)
        self.file_bubble_expanded.setVisible(False)


    # ---- functionality on clicking back button of any of the bubble -----    
    def back_arrow_clicked(self, event):
        self.file_bubble.setVisible(True)   # making visible the bubbles of the main window only and hiding expanded ones
        self.dir_bubble.setVisible(True)  
        self.file_bubble_expanded.setVisible(False)
        self.dir_bubble_expanded.setVisible(False)

    
    # ---- functionality of opening the file explorer on clicking the ... button to select image -----    
    def select_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files(*);; JPEG (*.jpeg)")
        if(fileName):
            print(fileName, _)
        self.image_path.setText(fileName)
        img = Image.open(fileName)   # to get the properties of the image
        self.image_width = img.width   # image_width attribute made because it will also be useful in resizing the image
        self.image_quality.setText(str(self.image_width))    # filling the quality_path text box with the width of the selected image

    
    # ---- functionality of opening the file explorer on clicking the ... button to select folder -----
    def select_source_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")    # to fetch the address of the source folder
        print(folder)  # to check which folder was selected
        # filling the box with the path of the chosen destination
        self.source_path.setText(folder)
        # print(self.sender().objectName())            # to check which button was clicked
        files = os.listdir(folder)     # geeting all the images in an array
        print(files)

        first_pic = folder + "/" + files[0]

        img = Image.open(first_pic)    # we are getting the first image because we will set the initial quality as per the quality of the first pic
        self.folder_image_width = img.width
        self.image_quality_dir.setText(str(self.folder_image_width))
        

    def select_dest_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        print(folder)
        self.destination_path.setText(folder)
    

    # ----- functionality to change the text inside the quality text box of image when we change the quality in the quality drop box -----
    def quality_current_value_img(self):
        if self.quality_combo.currentText() == "High":
            self.image_quality.setText(str(int(self.image_width)))

        if self.quality_combo.currentText() == "Medium":
            self.image_quality.setText(str(int(self.image_width/2)))
            # self.compress_width =  int(self.image_width / 2) 
 
        if self.quality_combo.currentText() == "Low":
            self.image_quality.setText(str(int(self.image_width/4)))
            # self.compress_width =  int(self.image_width / 4) 

    # ----- functionality to change the text inside the quality text box of folder when we change the quality in the quality drop box -----        

    def quality_current_value_dir(self):
        if self.quality_combo_dir.currentText() == "High":
            self.image_quality_dir.setText(str(int(self.folder_image_width)))
            # self.compress_width =  int(self.image_width)

        if self.quality_combo_dir.currentText() == "Medium":
            self.image_quality_dir.setText(str(int(self.folder_image_width / 2)))
            # self.compress_width =  int(self.image_width / 2)
            
        if self.quality_combo_dir.currentText() == "Low":
            self.image_quality_dir.setText(str(int(self.folder_image_width / 4)))
            # self.compress_width =  int(self.image_width / 4)



    # ----- functionality for compressing image -----        
    def resize_pic(self):
        old_pic = self.image_path.text()    # getting the path of the image to be compressed 
        print(old_pic)
        directories = self.image_path.text().split('/')   # spliting the path of the so that we can mosify it to get the saving destination path
        print(directories)

        new_pic = ""
        new_pic_name, okPressed = QInputDialog.getText(self, "Save Image as", "Image name", QLineEdit.Normal, "")
        if okPressed and new_pic_name != '':
            print(new_pic_name)
            
            if old_pic[-5:] == ".jpeg":
                new_pic_name += ".jpeg"

            if old_pic[-4:] == ".png":
                new_pic_name += ".png"

            if old_pic[-4:] == ".jpg":
                new_pic_name += ".jpg"
            
            else:
                new_pic_name += ".jpeg"
            
            for directory in directories[:-1]:
                new_pic = new_pic + directory + "/"      
            
            new_pic += new_pic_name    # here is the major modification in the path, our path is ready here
            print(new_pic)

        self.compression_code(old_pic, new_pic, int(self.image_quality.text()))  # calling the compression code to finally compress image
        self.statusBar().showMessage("Message: Compressed")



    # ----- functionality for compressing directory ----- 
    def resize_directory(self):
        source_directory = self.source_path.text()      # getting the the path of the source directory
        files = os.listdir(source_directory)            # getting all the files as a list files

        dest_directory = self.destination_path.text()

        i = 0

        for file in files:
            i += 1

            if file[-4:] == '.jpg' or file[-4:] == '.png' or file[-5:] == '.jpeg' or file[-4:] == '.JPG' or file[-4:] == '.PNG' or file[-5:] == 'JPEG':
                old_pic = source_directory + '/' + file
                new_pic = dest_directory + '/' + file
                
                img = Image.open(old_pic)
                self.folder_image_width = img.width

                # will fill the quality text box for each image as per the quality chosen before compression

                if self.quality_combo_dir.currentText() == "High":   
                    self.image_quality_dir.setText(str(int(self.folder_image_width)))
                    # self.compress_width =  int(self.image_width)

                if self.quality_combo_dir.currentText() == "Medium":
                    self.image_quality_dir.setText(str(int(self.folder_image_width / 2)))
                    # self.compress_width =  int(self.image_width / 2)
                    
                if self.quality_combo_dir.currentText() == "Low":
                    self.image_quality_dir.setText(str(int(self.folder_image_width / 4)))
                    # self.compress_width =  int(self.image_width / 4)
                
                self.compression_code(old_pic, new_pic, int(self.image_quality_dir.text()))

                total_images = len(files)
                images_done = i
                percentage = int(images_done / total_images * 100)

                self.statusBar().showMessage("Message: Compressed" + str(percentage) + "%")     # showing percentage of the compressed files
        
            else:
                print("ingnored " + file)
                continue
        
        self.statusBar().showMessage("Message: Compressed All")    # finally when all files are compressed



    # ----- compression code used for resizing the images of both single image and folder images -----      
    def compression_code(self, old_pic, new_pic, mywidth):

        try:
            img = Image.open(old_pic)       # extracting image from the path
            wpercent = (mywidth / float(img.size[0]))      # getting the width of the image to be compressed
            hsize = int((float(img.size[1])*float(wpercent)))     # getting the width of the image to be compressed
            img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)   # finally resizing the image
            img.save(new_pic)     # saving the compressed image
            
        except Exception as e:
            self.statusBar().showMessage("Message: " + e)



if __name__ == '__main__':  # broadly it is used to directly run our code
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())