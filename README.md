# Automatic-License-Plate-Recognition
Welcome to my Automatic License Plate Recognition model!

I have designed this model in such a way that it can be used in parking lots and other situations where the flow of vehicle traffic is from the same entry/exit point. This lets us calibrate the video frame which helps improve accuracy though we must provide the regions initially.

This project uses the conventional method of License Plate detection by first detecting the vehicle and then the actual License Plate.

I have used two different **YOLOv8n models** custom trained on separate datasets for vehicle and License Plate detection.

Initially I tried a different method of License Plate detection wherein the regions to detect the license plate where already defined alongwith the video input. These regions have to be specified only once during calibration. This method, though it removed the need for vehicle detection and increased efficiency, required the need for hard coded values within the input frame. Thus I went back to the conventional method.

The model first takes each frame of the video as input and the vehicle detection model is run on it. The detected vehicles are cropped out and sent to the License Plate detection model. The input frame with a bounding box is also saved to denote the region of the license plate. 

The next custom-trained YOLOv8 model then runs on this cropped frame and searches for license plates. The input frame is again cropped to the license plate and is then sent for License Plate Recognition.

License Plate Recognition involves reading the license plate accurately. In this project, I have used a **pre trained PaddleOCR pipeline** to read the license plates due to its high accuracy in reading such data. 

The input license plate image is first preprocessed before OCR is performed on it. The license plate is converted ito grayscale, normalised and then scaled to a DPI of 300 before performing OCR.

Once the PaddleOCR pipeline returns the read number, a basic check (which can be modified later) is done to check if the number fits the form of a license plate number. If yes, the number is written into **"log.csv"** alongwith the time of detection.

The vehicle and license plate detection models were trained on datasets from Kaggle (linked provided below).

**Vehicle Detection:**
https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset

**License Plate Detection:**
https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset

**VD-results** and **LPD-results** contain graphs obtained while training the Vehicle Detection and License Plate detection models respectively

## Using the model
- Clone the repository and add the input video file.
- Run the start.py file.
- The path of the video file must be given as input initially.
- Check the log.csv file for the results.




Thank You!!!
