import sys

import cv2  # Image proc.
import numpy as np

import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
import pytesseract  # OCR
import argparse
from PIL import Image
from PyQt5.QtWidgets import QFileDialog

from test import *

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        ui = Ui_MainWindow()
        ui.setupUi(self)

        self.text = ui.textEdit
        self.inputImg = ui.input
        self.inputIcon = ui.AddPic
        self.TextIcon = ui.label_2
        self.radioLAT = ui.radioButton
        self.radioENG = ui.radioButton_2
        self.fontSize = ui.spinBox

        # extract text with pytesseract (OCR)
        open_btn = ui.pushButton
        open_btn.clicked.connect(self.extract_text)

        #import opened picture into the edited (working on it)
        open_btn = ui.pushButton_2
        open_btn.clicked.connect(self.edit)

        # import picture button
        open_btn = ui.pushButton_3
        open_btn.clicked.connect(self.openImage)

        # save text button
        save_text_btn = ui.pushButton_5
        save_text_btn.clicked.connect(self.saveText_test)
        # clear the text window
        clear_text_btn = ui.pushButton_6
        clear_text_btn.clicked.connect(self.clearText)
        # save text to new file
        clear_text_btn = ui.pushButton_7
        clear_text_btn.clicked.connect(self.saveText)

        ########################################
        #########  Image Processing   ##########
        ########################################

        # blurring the image (works well for edge detect and segmentation)
        clear_text_btn = ui.pushButton_8
        clear_text_btn.clicked.connect(self.blur)
        # sharpening the image
        clear_text_btn = ui.pushButton_9
        clear_text_btn.clicked.connect(self.sharpen)
        # grayscaling the img
        clear_text_btn = ui.pushButton_11
        clear_text_btn.clicked.connect(self.grayscale)
        # segmentation
        clear_text_btn = ui.pushButton_12
        clear_text_btn.clicked.connect(self.segmentation)
        # contrast test
        clear_text_btn = ui.pushButton_4
        clear_text_btn.clicked.connect(self.automatic_brightness_and_contrast)

        #tool tip information
        ui.input.setToolTip('Select an image to convert')
        ui.textEdit.setToolTip('Image output')
        ui.pushButton.setToolTip('Button to adjust the image')
        ui.pushButton_2.setToolTip('Button to convert the image to text')


    #pagriez attelu korekti
    def autorotate(self):  # pagriez ieladeto attelu

        image = cv2.imread('res/temp_edit.png')
        self.inputIcon.setVisible(0)  # hides the addpic icon

        # convert the image to grayscale and flip the foreground
        # and background to ensure foreground is now "white" and
        # the background is "black"
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)

        # threshold the image, setting all foreground pixels to
        # 255 and all background pixels to 0
        thresh = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # grab the (x, y) coordinates of all pixel values that
        # are greater than zero, then use these coordinates to
        # compute a rotated bounding box that contains all
        # coordinates
        coords = np.column_stack(np.where(thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]

        # the `cv2.minAreaRect` function returns values in the
        # range [-90, 0); as the rectangle rotates clockwise the
        # returned angle trends to 0 -- in this special case we
        # need to add 90 degrees to the angle
        if angle < -45:
            angle = -(90 + angle)

        # otherwise, just take the inverse of the angle to make
        # it positive
        else:
            angle = -angle

        # rotate the image to deskew it
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h),
                                 flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        # draw the correction angle on the image so we can validate it
        # cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
        #           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # show the output image
        print("[INFO] angle: {:.3f}".format(angle))
        cv2.imwrite('res/temp_edit.png', rotated)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

    # atvert attelu
    def openImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                      "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  # hides the addpic icon

        image = cv2.imread(fileName)
        cv2.imwrite('res/temp_edit.png', image)
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)
        self.autorotate()

        # izveido histogrammu un parada
        img = cv2.imread('res/temp_edit.png', 0)
        plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
        hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
        plt.xlabel('RGB Channel Values')
        plt.ylabel('values')
        plt.legend(handles=[hist_data])
        plt.show()

    def clearText(self): #clear the output window
        self.text.clear()

    def biggerText(self): #the concept needs a lot of work
        self.text.setFontPointSize(self.fontSize.value())

        #if self.fontSize.valueChanged:
        #    self.text.setFontPointSize(self.fontSize.value())

    def blur(self): #currently in testing mode
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  # hides the addpic icon
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        # Reading our image and displaying it
        image = cv2.imread(fileName)
        # Creating our 3 x 3 kernel that would look like this:
        #         # [[ 0.11111111  0.11111111  0.11111111]
        #         #  [ 0.11111111  0.11111111  0.11111111]
        #         #  [ 0.11111111  0.11111111  0.11111111]]

        kernel_3x3 = np.ones((3, 3), np.float32) / 9
        # We apply the filter and display the image
        blurred = cv2.filter2D(image, -1, kernel_3x3)
        cv2.imwrite('res/temp_edit.png', blurred)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)
        self.autorotate()

        '''
        Hello World
        
     # Let's try with 7 x 7 kernel to get a more blurred image
        kernel_7x7 = np.ones((7, 7), np.float32) / 49
        blurred2 = cv2.filter2D(image, -1, kernel_7x7)
        cv2.imshow('7x7 Kernel Blurring', blurred2)
        cv2.waitKey(0)

        '''

        # izveido histogrammu un parada
        img = cv2.imread('res/temp_edit.png', 0)
        plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
        hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
        plt.xlabel('RGB Channel Values')
        plt.ylabel('values')
        plt.legend(handles=[hist_data])
        plt.show()

    def grayscale(self): #currently in testing mode
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  # hides the addpic icon
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        image = cv2.imread(fileName)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('res/temp_edit.png', gray)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)
        self.autorotate()

        # izveido histogrammu un parada
        img = cv2.imread('res/temp_edit.png', 0)
        plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
        hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
        plt.xlabel('RGB Channel Values')
        plt.ylabel('values')
        plt.legend(handles=[hist_data])
        plt.show()

    def segmentation(self): #currently in testing mode
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")

        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  # hides the addpic icon
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        #obligati jabut ieprieks deginetam objektam
        image = cv2.imread(fileName)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #making it grayscale at first
        _,mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)  #segmentation ##izveidot adaptīvo

        cv2.imwrite('res/temp_edit.png', mask)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)
        self.autorotate()

        # izveido histogrammu un parada
        img = cv2.imread('res/temp_edit.png', 0)
        plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
        hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
        plt.xlabel('RGB Channel Values')
        plt.ylabel('values')
        plt.legend(handles=[hist_data])
        plt.show()

    # Automatic brightness and contrast optimization with optional histogram clipping
    def automatic_brightness_and_contrast(self, clip_hist_percent=1):

        #Opens and inserts file
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  #hides the addpic icon
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        #Object definition
        image = cv2.imread(fileName)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #Calculates grayscale histogram from picture (blue)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])  #image, channels, mask, hist size, ranges
        hist_size = len(hist)

        #Calculate cumulative distribution from the histogram ->
        #Lai noteiktu kur krāsas frekvence ir mazāka par sliekšņa vērtību un nogrieztu labo un kreiso pusi, dodot min un max diapazonu.
        accumulator = []
        accumulator.append(float(hist[0])) #append -> adds an item to the end of the list (self, object)
        for index in range(1, hist_size):
            accumulator.append(accumulator[index - 1] + float(hist[index])) #finds the given element in a list and returns its position

        #Izgriešanas metode noņem visattālākās detaļas un palielina kontrastu/spilgtumu
        #Locate points to clip
        maximum = accumulator[-1]
        clip_hist_percent *= (maximum / 100.0)
        clip_hist_percent /= 2.0

        #Locate left cut
        minimum_gray = 0
        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray += 1

        #Locate right cut
        maximum_gray = hist_size - 1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1

        #Calculate alpha and beta values
        #alpha=2 #Contrast
        #beta=1 #Brightness

        #Alpha = min and max grayscale range (diapazons) after clipping and divide it from output range of 255
        alpha = 255 / maximum_gray - minimum_gray
        beta = -minimum_gray * alpha
        #ConvertScaleAbs -> scales (mērogo), calculates absolute values and converts the result to 8-bit
        auto_result = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

        cv2.imwrite('res/temp_edit.png', auto_result)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        #New histogram - visualisation after clipping (orange)
        new_hist = cv2.calcHist([gray], [0], None, [256],
                                [minimum_gray, maximum_gray])  # image, channels, mask, hist size, ranges
        plt.plot(hist)
        plt.plot(new_hist)
        plt.xlim([0, 256])
        plt.show()

    def sharpen(self): #currently in testing mode
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  # hides the addpic icon
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        # Reading in and displaying our image
        image = cv2.imread(fileName)
        # Create our shapening kernel, it must equal to one eventually
        kernel_sharpening = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])

        # something = cv2.fastNlMeansDenoisingColored(kernel_sharpening, None, 10, 10, 7, 21)
        #cv2.imshow("something", something)

        # applying the sharpening kernel to the input image & displaying it.
        sharpened = cv2.filter2D(image, -1, kernel_sharpening)

        cv2.imwrite('res/temp_edit.png', sharpened)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)
        self.autorotate()

        # izveido histogrammu un parada
        img = cv2.imread('res/temp_edit.png', 0)
        plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
        hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
        plt.xlabel('RGB Channel Values')
        plt.ylabel('values')
        plt.legend(handles=[hist_data])
        plt.show()

    def edit(self): #here is where all the image processing things will happen
        # edge detect test
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
        f = open(fileName, "r")
        label = self.inputImg
        self.inputIcon.setVisible(0)  # hides the addpic icon
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        label = self.inputImg
        # self.inputImg.setPixmap(QPixmap(fileName))
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        self.inputIcon.setVisible(0)  # hides the addpic icon
        img = cv2.imread(fileName)
        new_img = cv2.Canny(img, 0, 200)
        cv2.imwrite('res/temp_edit.png', new_img)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        # izveido histogrammu un parada
        img = cv2.imread('res/temp_edit.png', 0)
        plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
        hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
        plt.xlabel('RGB Channel Values')
        plt.ylabel('values')
        plt.legend(handles=[hist_data])
        plt.show()

    def saveText_test(self): #save output text test
        with open('output_save_test.txt', 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def saveText(self): #save output text
        filename = QFileDialog.getSaveFileName(self, "Save Text", "",
                                            "All Files (*);;TEXT Files (*.txt)")
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def extract_text(self):
        # img to text
        self.inputIcon.setVisible(0)  # hides the addpic icon
        fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                  "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")

        #make sure the directory points to the place where tesseract is
        pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR-Mac/tesseract' #'/usr/local/bin/tesseract'

        label = self.inputImg
        pixmap = QtGui.QPixmap(fileName)
        pixmap_resized = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)

        img = Image.open(fileName)
        if self.radioENG.isChecked():
            text = pytesseract.image_to_string(img, lang="eng") #izmanto anglu valodu
        else:
            text = pytesseract.image_to_string(img, lang="lav")  # izmanto latviesu valodu
        self.TextIcon.setVisible(0)
        self.text.setText(text)
        self.biggerText()

def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

 #opens and shows the main app window
if __name__ == "__main__":
     main()
