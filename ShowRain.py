import pyodbc

from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from climate_ui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# code ----------------------------------------# 

class ClimateForm(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbRain.clicked.connect(self.show_climate_data)
        self.ui.pbRain_2.clicked.connect(self.show_mean_temp)
        self.ui.pbRain_3.clicked.connect(self.show_max_temp)
        self.ui.pbRain_4.clicked.connect(self.show_min_temp)
        self.show()
        self.show_climate_data()
    
    def show_first_row(self):
       
        statementSQL = "SELECT Year, UK_Rain, England_Rain, Northern_Ireland_Rain, Scotland_rain, Wales_Rain FROM tClimate"
        try:
            cs = (
            "Driver={SQL Server};"
            "Server=svr-cmp-01;"
            "Database=22MatsonT636;"
            "Trusted_Connection=yes;"
            "UI=COLLYERS\22MatsonT636;"
            "pwd=SY221636"
            )
            cnxn = pyodbc.connect(cs)
            print("Connected")
            if cs is not None:
                cursor = cnxn.cursor()
                cursor.execute(statementSQL)
                row = cursor.fetchone()
                print(row)
                self.ui.leUk.setText(str(row[1]))
                self.ui.leEngland.setText(str(row[2]))
                self.ui.leNorthernIsland.setText(str(row[3]))
                self.ui.leScotland.setText(str(row[4]))
                self.ui.leWales.setText(str(row[5]))

        except pyodbc.DatabaseError as error:
            print("Error: {}".format(error))
            self.ui.twClimate.clearContents()
            
        finally:
            cnxn.close()
            print("Connection closed")

    def show_climate_data(self):
        self.ui.twClimate.clearContents()
        self.ui.pic_file = "C:\\Users\\22MatsonT636\\OneDrive - The College of Richard Collyer\\Computer Science\\Projects\\Cilmate\\rain_clipart"
        self.ui.lblPic_sun2.setGeometry(QtCore.QRect(550, 150, 200, 200))
        self.ui.lblPic_sun2.setPixmap(QtGui.QPixmap(self.ui.pic_file))
        
        statementSQL = "SELECT Year, UK_Rain, England_Rain, Northern_Ireland_Rain, Scotland_Rain, Wales_Rain FROM tClimate"
        try:
            cs = (
            "Driver={SQL Server};"
            "Server=svr-cmp-01;"
            "Database=22MatsonT636;"
            "Trusted_Connection=yes;"
            "UI=COLLYERS\22MatsonT636;"
            "pwd=SY221636"
            )
            cnxn = pyodbc.connect(cs)
            if cs is not None:
                cursor = cnxn.cursor()
                cursor.execute(statementSQL)
                rows = cursor.fetchall()
                self.ui.twClimate.setRowCount(len(rows))
                self.ui.twClimate.setColumnCount(len(rows[0]))
                col = ["Year", "Uk Rain", "England Rain", "Northen Ireland Rain","Scotland Rain", "Wales Rain", ]
                self.ui.twClimate.setHorizontalHeaderLabels(col)
                self.header = self.ui.twClimate.horizontalHeader()
                
                noRow = 0 
                for tuple in rows:
                    noCol = 0
                    for column in tuple:
                        satuKolum = QTableWidgetItem(str(column))
                        self.ui.leUk.setText(str(rows[0][1]))
                        self.ui.leEngland.setText(str(rows[0][2]))
                        self.ui.leNorthernIsland.setText(str(rows[0][3]))
                        self.ui.leScotland.setText(str(rows[0][4]))
                        self.ui.leWales.setText(str(rows[0][5]))
             
                        self.ui.twClimate.setItem(noRow, noCol, satuKolum)
                        self.header.setSectionResizeMode(noCol, QtWidgets.QHeaderView.Stretch)
                        noCol += 1
                    noRow += 1
    
             
        except pyodbc.DatabaseError as error:
            print("Error: {}".format(error))
            self.ui.twClimate.clearContents()
    def show_mean_temp(self):
        self.ui.twClimate.clearContents()
        self.ui.pic_file = "C:\\Users\\22MatsonT636\\OneDrive - The College of Richard Collyer\\Computer Science\\Projects\\Cilmate\\thermometer_clipart.png"
        self.ui.lblPic_sun2.setGeometry(QtCore.QRect(550, 150, 100, 200))
        self.ui.lblPic_sun2.setPixmap(QtGui.QPixmap(self.ui.pic_file))
        print(self.ui.pic_file)
        statementSQL = "SELECT Year, UK_Mean_Temp, England_Mean_Temp, Norther_Ireland_Mean_Temp, Scotland_Mean_Temp, Wales_Mean_Temp FROM tClimate"
        try:
            cs = (
            "Driver={SQL Server};"
            "Server=svr-cmp-01;"
            "Database=22MatsonT636;"
            "Trusted_Connection=yes;"
            "UI=COLLYERS\22MatsonT636;"
            "pwd=SY221636"
            )
            cnxn = pyodbc.connect(cs)
            if cs is not None:
                cursor = cnxn.cursor()
                cursor.execute(statementSQL)
                rows = cursor.fetchall()
                self.ui.twClimate.setRowCount(len(rows))
                self.ui.twClimate.setColumnCount(len(rows[0]))
                col = ["Year", "Uk Temp", "England Temp", "Northen Ireland Temp","Scotland Temp", "Wales Temp", ]
                self.ui.twClimate.setHorizontalHeaderLabels(col)
                self.header = self.ui.twClimate.horizontalHeader()
                
                noRow = 0 
                for tuple in rows:
                    noCol = 0
                    for column in tuple:
                        satuKolum = QTableWidgetItem(str(column))
                        self.ui.leUk.setText(str(rows[0][1]))
                        self.ui.leEngland.setText(str(rows[0][2]))
                        self.ui.leNorthernIsland.setText(str(rows[0][3]))
                        self.ui.leScotland.setText(str(rows[0][4]))
                        self.ui.leWales.setText(str(rows[0][5]))
             
                        self.ui.twClimate.setItem(noRow, noCol, satuKolum)
                        self.header.setSectionResizeMode(noCol, QtWidgets.QHeaderView.Stretch)
                        noCol += 1
                    noRow += 1
    
             
        except pyodbc.DatabaseError as error:
            print("Error: {}".format(error))
            self.ui.twClimate.clearContents()
    def show_max_temp(self):
        self.ui.twClimate.clearContents()

        self.ui.lblPic_sun2.setGeometry(QtCore.QRect(550,150, 200, 200))
        self.ui.lblPic_sun2.setPixmap(QtGui.QPixmap("C:\\Users\\22MatsonT636\\OneDrive - The College of Richard Collyer\\Computer Science\\Projects\\Cilmate\\sun_clipart.png"))
        statementSQL = "SELECT Year, UK_Max_Temp, England_Max_Temp, Northern_Ireland_Max_Temp, Scotland_Max_Temp, Wales_Max_Temp FROM tClimate"
        try:
            cs = (
            "Driver={SQL Server};"
            "Server=svr-cmp-01;"
            "Database=22MatsonT636;"
            "Trusted_Connection=yes;"
            "UI=COLLYERS\22MatsonT636;"
            "pwd=SY221636"
            )
            cnxn = pyodbc.connect(cs)
            if cs is not None:
                cursor = cnxn.cursor()
                cursor.execute(statementSQL)
                rows = cursor.fetchall()
                self.ui.twClimate.setRowCount(len(rows))
                self.ui.twClimate.setColumnCount(len(rows[0]))
                col = ["Year", "Uk Max Temp", "England Max", "Northen Ireland Max","Scotland Max", "Wales Max Temp", ]
                self.ui.twClimate.setHorizontalHeaderLabels(col)
                self.header = self.ui.twClimate.horizontalHeader()
                
                noRow = 0 
                for tuple in rows:
                    noCol = 0
                    for column in tuple:
                        satuKolum = QTableWidgetItem(str(column))
                        self.ui.leUk.setText(str(rows[0][1]))
                        self.ui.leEngland.setText(str(rows[0][2]))
                        self.ui.leNorthernIsland.setText(str(rows[0][3]))
                        self.ui.leScotland.setText(str(rows[0][4]))
                        self.ui.leWales.setText(str(rows[0][5]))
             
                        self.ui.twClimate.setItem(noRow, noCol, satuKolum)
                        self.header.setSectionResizeMode(noCol, QtWidgets.QHeaderView.Stretch)
                        noCol += 1
                    noRow += 1
    
             
        except pyodbc.DatabaseError as error:
            print("Error: {}".format(error))
            self.ui.twClimate.clearContents()
    def show_min_temp(self):
        self.ui.twClimate.clearContents()
        self.ui.lblPic_sun2.setPixmap(QtGui.QPixmap("C:\\Users\\22MatsonT636\\OneDrive - The College of Richard Collyer\\Computer Science\\Projects\\Cilmate\\snowflake_clipart.png"))
        
        statementSQL = "SELECT Year, UK_Min_Temp, England_Min_Temp, Northern_Ireland_Min_Temp, Scotland_Min_Temp, Wales_Min_Temp FROM tClimate"
        try:
            cs = (
            "Driver={SQL Server};"
            "Server=svr-cmp-01;"
            "Database=22MatsonT636;"
            "Trusted_Connection=yes;"
            "UI=COLLYERS\22MatsonT636;"
            "pwd=SY221636"
            )
            cnxn = pyodbc.connect(cs)
            if cs is not None:
                cursor = cnxn.cursor()
                cursor.execute(statementSQL)
                rows = cursor.fetchall()
                self.ui.twClimate.setRowCount(len(rows))
                self.ui.twClimate.setColumnCount(len(rows[0]))
                col = ["Year", "Uk Min Temp", "England Min", "Northen Ireland Min","Scotland Min", "Wales Min Temp", ]
                self.ui.twClimate.setHorizontalHeaderLabels(col)
                self.header = self.ui.twClimate.horizontalHeader()
                
                noRow = 0 
                for tuple in rows:
                    noCol = 0
                    for column in tuple:
                        satuKolum = QTableWidgetItem(str(column))
                        self.ui.leUk.setText(str(rows[0][1]))
                        self.ui.leEngland.setText(str(rows[0][2]))
                        self.ui.leNorthernIsland.setText(str(rows[0][3]))
                        self.ui.leScotland.setText(str(rows[0][4]))
                        self.ui.leWales.setText(str(rows[0][5]))
             
                        self.ui.twClimate.setItem(noRow, noCol, satuKolum)
                        self.header.setSectionResizeMode(noCol, QtWidgets.QHeaderView.Stretch)
                        noCol += 1
                    noRow += 1
    
             
        except pyodbc.DatabaseError as error:
            print("Error: {}".format(error))
            self.ui.twClimate.clearContents()
    
            

if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    w = ClimateForm()
    w.show()
    sys.exit(app.exec())
