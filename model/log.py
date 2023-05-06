import csv
from datetime import datetime
cars = []
falseCars = []

def formatCheck(str):
    if len(str)!=7:
        return False
    return True

def formatter(num_plate):
    num_plate = num_plate.split("-")
    num_plate = "".join(num_plate)
    num_plate = num_plate.split()
    num_plate = "".join(num_plate)
    return num_plate

def LogNumber(num_plate):
    num_plate = formatter(num_plate)
    print(num_plate)
    
    if formatCheck(num_plate)   :
        time = datetime.now()
        file = open("log.csv", mode='a+')
        if num_plate not in cars:
            write = csv.writer(file)
            write.writerow([num_plate,time])
            cars.append(num_plate)
        file.close()
