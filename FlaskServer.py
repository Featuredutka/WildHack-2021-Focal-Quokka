# app.py
import os
import csv
import random
from flask import Flask, render_template

SOURCE_FOLDER = "C:\\Users\\ash\\Desktop\\TEST"
PLOTTING_FOLDER = "C:\\Users\\ash\\Desktop\\seal-counter1\\seal-counter\\src\\components\\chart\\file.js"
DATABASE_FOLDER = "C:\\Users\\ash\\Desktop\\seal-counter1\\seal-counter\\src\\database"

app = Flask(__name__)

def data_processing():
    # Исходная директория
    folder_track = SOURCE_FOLDER
    # Директория для сортировки
    folder_dest = SOURCE_FOLDER

    # Добавление заголовка к БД при отсутствии такого файла в директории
    if not os.path.isfile(DATABASE_FOLDER+"\\"+"data.csv"):
        with open(DATABASE_FOLDER+"\\"+"data.csv", 'w') as f:
            w = csv.DictWriter(f, ["Date", "Amount"])
            w.writeheader()
            print("NewFile")
        f.close

    # Цикл сортировки изображений по дням
    for filename in os.listdir(folder_track):
        extension = filename.split(".")
        if len(extension) > 1 and extension[1].lower() == "jpg":
            file = folder_track + "\\" + filename
            new_path = folder_dest + "\\" + extension[0][:4] + "-" + extension[0][4:6] + "-" + extension[0][6:8]
            # Проверка наличия директории для избежания ошибок
            if not os.path.isdir(new_path):
                os.mkdir(new_path)
            os.rename(file, new_path + "\\" + filename)

    # Цикл отправки изображений в сеть c последующей маркировкой проанализированных данных
    for filename in os.listdir(folder_track):
        extension = filename.split(".")
        if len(extension) < 2 and len(extension[0]) == 10:
            base_folder = folder_track + "\\" + extension[0]
            #value = 10 # Для получения кол-ва тюленей
            table = {}	
		
		    #ЗАГЛУШКА ВМЕСТО НЕЙРОНКИ
            for image in os.listdir(base_folder):
                table[image[9:11] + "-" + image[11:13] + "-" + image[13:15]] = random.randint(10, 30) #TODO Пофиксить value на вывод нейросети
		
		# Запись результатов в БД
            report = {"Date": extension[0] + "-" + max(table), "Amount": max(table.values())}
            with open(DATABASE_FOLDER+"\\"+"data.csv", 'a') as f:  
                w = csv.DictWriter(f, report.keys())
                w.writerow(report)
            f.close()

        # После успешного анализа фотографий добавить метку папке, чтобы больше в нее не залезать
            new_path = folder_track + "\\" + extension[0] + "_p"
            os.rename(base_folder, new_path)

def fetch_data():
    csvfile = open(DATABASE_FOLDER+"\\"+"data.csv", 'r')

    fieldnames = ("Date", "Amount")
    reader = csv.DictReader(csvfile, fieldnames)

    data = [{'DateTime':row["Date"], "Seal Maximum":int(row["Amount"])} for row in reader if row["Date"] != "Date"]
    data = str(data)
    buffer = "".join(
        data[i]
        for i in range(len(data))
        if data[i] != "'" or data[i + 1] != 'D' and data[i - 1] != 'e'
    )

    with open(PLOTTING_FOLDER, 'w') as file:
        file.write("export const newdata =" + buffer)
    file.close()
    csvfile.close()
# Display your index page
@app.route("/")
def index():
    return render_template('index.html')

# A function to add two numbers
@app.route("/add")
def add():
    data_processing()
    fetch_data()
    return ("You can close this tab")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
