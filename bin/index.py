import sys
import sqlite3
from PyQt5.QtGui import *


    def Handle_Buttons(self):
        ''' Show Data in Table Serves'''


        self.pushButton_35.clicked.connect(self.Clear_All_LineEdits_Of_Family_MArmals)

        self.pushButton_36.clicked.connect(self.Open_Main_Page)
        self.pushButton_36.clicked.connect(self.Clear_All_LineEdits_Of_Family_FArmals)

        self.pushButton_121.clicked.connect(self.Open_Main_Page)
        self.pushButton_4.clicked.connect(self.Open_Main_Page)
        self.pushButton_10.clicked.connect(self.Open_Main_Page)
        self.pushButton_9.clicked.connect(self.Open_Main_Page)
        self.pushButton_23.clicked.connect(self.Open_Main_Page)
        self.pushButton_138.clicked.connect(self.Open_Main_Page)
        self.pushButton_28.clicked.connect(self.Open_Main_Page)
        self.pushButton_29.clicked.connect(self.Open_Main_Page)
        self.pushButton_30.clicked.connect(self.Open_Main_Page)
        self.pushButton_67.clicked.connect(self.Open_Main_Page)
        self.pushButton_86.clicked.connect(self.Open_Main_Page)
        self.pushButton_66.clicked.connect(self.Open_Main_Page)
        self.pushButton_39.clicked.connect(self.Close_program)
        self.pushButton_68.clicked.connect(self.Open_Main_Page)
        self.pushButton_85.clicked.connect(self.Open_Main_Page)
        self.pushButton_46.clicked.connect(self.open_1st_Son_Tab)
        self.pushButton_47.clicked.connect(self.open_2st_Son_Tab)
        self.pushButton_50.clicked.connect(self.open_3st_Son_Tab)
        self.pushButton_51.clicked.connect(self.open_4st_Son_Tab)
        self.pushButton_52.clicked.connect(self.open_5st_Son_Tab)
        self.pushButton_53.clicked.connect(self.open_6st_Son_Tab)
        self.pushButton_54.clicked.connect(self.open_7st_Son_Tab)
        self.pushButton_55.clicked.connect(self.open_8st_Son_Tab)
        self.pushButton_56.clicked.connect(self.open_9st_Son_Tab)
        self.pushButton_40.clicked.connect(self.LOGOUT)
        ''' Family Tab Record and Check '''
        # Check Father Data
        self.pushButton_57.clicked.connect(self.Check_Father_Data)
        # Check Mother Data
        self.pushButton_58.clicked.connect(self.Check_Mother_Data)
        # Sons Tabs
        # 1 st Son
        self.pushButton_11.clicked.connect(self.On_Mouse_Click_in_1st_SoN)
        # 2 st Son
        self.pushButton_13.clicked.connect(self.On_Mouse_Click_in_2st_SoN)
        # Back to 1
        self.pushButton_78.clicked.connect(self.open_1st_Son_Tab)
        # 3 st Son
        self.pushButton_14.clicked.connect(self.On_Mouse_Click_in_3st_SoN)
        # Back to 2
        self.pushButton_80.clicked.connect(self.open_2st_Son_Tab)
        # 4 st Son
        self.pushButton_15.clicked.connect(self.On_Mouse_Click_in_4st_SoN)
        # Back to 3
        self.pushButton_50.clicked.connect(self.open_3st_Son_Tab)
        # 5 st Son
        self.pushButton_16.clicked.connect(self.On_Mouse_Click_in_5st_SoN)
        # Back to 4
        self.pushButton_51.clicked.connect(self.open_4st_Son_Tab)
        # 6 st Son
        self.pushButton_17.clicked.connect(self.On_Mouse_Click_in_6st_SoN)
        # Back to 5
        self.pushButton_52.clicked.connect(self.open_5st_Son_Tab)
        # 7 st Son
        self.pushButton_18.clicked.connect(self.On_Mouse_Click_in_7st_SoN)
        # Back to 6
        self.pushButton_53.clicked.connect(self.open_6st_Son_Tab)
        # 8 st Son
        self.pushButton_19.clicked.connect(self.On_Mouse_Click_in_8st_SoN)
        # Back to 7
        self.pushButton_54.clicked.connect(self.open_7st_Son_Tab)
        # 9 st Son
        self.pushButton_20.clicked.connect(self.On_Mouse_Click_in_9st_SoN)
        # Back to 8
        self.pushButton_55.clicked.connect(self.open_8st_Son_Tab)
        # Back to 9
        self.pushButton_56.clicked.connect(self.open_9st_Son_Tab)
        # Button Enable Record Sons Data
        self.pushButton_102.clicked.connect(self.Check_On_Click_Sons_Tabl)
        # Record Father Data
        self.pushButton_21.clicked.connect(self.Record_Father)
        # Record Mother Data
        self.pushButton_21.clicked.connect(self.Record_Mother)
        # Record Sons Data
        self.pushButton_21.clicked.connect(self.Choice_Recoord_Sons_NumS)
        # Clear Info
        self.pushButton_21.clicked.connect(self.Clear_All_LineEdits_Of_Family)
        self.pushButton_34.clicked.connect(self.Clear_All_LineEdits_Of_Family)
        '''Father Armal Record And Check Data'''
        # Check Father DatalineEd
        self.pushButton_124.clicked.connect(self.Check_Father_Armal)
        # Sons Tabs
        # 1 st Son
        self.pushButton_61.clicked.connect(self.On_Mouse_Click_in_1st_Son_MotherDeadd)
        # 2 st Son
        self.pushButton_77.clicked.connect(self.On_Mouse_Click_in_2st_Son_MotherDeadd)
        # Back to 1
        self.pushButton_78.clicked.connect(self.open_1st_Son_Tab_FArmals)
        # 3 st Son
        self.pushButton_79.clicked.connect(self.On_Mouse_Click_in_3st_Son_MotherDeadd)
        # Back to 2
        self.pushButton_80.clicked.connect(self.open_2st_Son_Tab_FArmals)
        # 4 st Son
        self.pushButton_81.clicked.connect(self.On_Mouse_Click_in_4st_Son_MotherDeadd)
        # Back to 3
        self.pushButton_82.clicked.connect(self.open_3st_Son_Tab_FArmals)
        # 5 st Son
        self.pushButton_83.clicked.connect(self.On_Mouse_Click_in_5st_Son_MotherDeadd)
        # Back to 4
        self.pushButton_84.clicked.connect(self.open_4st_Son_Tab_FArmals)
        # 6 st Son
        self.pushButton_111.clicked.connect(self.On_Mouse_Click_in_6st_Son_MotherDeadd)
        # Back to 5
        self.pushButton_112.clicked.connect(self.open_5st_Son_Tab_FArmals)
        # 7 st Son
        self.pushButton_113.clicked.connect(self.On_Mouse_Click_in_7st_Son_MotherDeadd)
        # Back to 6
        self.pushButton_114.clicked.connect(self.open_6st_Son_Tab_FArmals)
        # 8 st Son
        self.pushButton_115.clicked.connect(self.On_Mouse_Click_in_8st_Son_MotherDeadd)
        # Back to 7
        self.pushButton_116.clicked.connect(self.open_7st_Son_Tab_FArmals)
        # 9 st Son
        self.pushButton_117.clicked.connect(self.On_Mouse_Click_in_9st_Son_MotherDeadd)
        # Back to 8
        self.pushButton_118.clicked.connect(self.open_8st_Son_Tab_FArmals)
        # Back to 9
        self.pushButton_119.clicked.connect(self.open_9st_Son_Tab_FArmals)
        # Button Enable Record Sons Data
        self.pushButton_142.clicked.connect(self.Check_On_Click_Sons_Tabl_FArmals)
        # Record Father Data
        self.pushButton_120.clicked.connect(self.Record_Father_Armal)
        # Record Sons Data
        self.pushButton_120.clicked.connect(self.Choice_Recoord_Sons_NumS_FArmals)
        # Clear Info
        self.pushButton_120.clicked.connect(self.Clear_All_LineEdits_Of_Family_FArmals)
        self.pushButton_36.clicked.connect(self.Clear_All_LineEdits_Of_Family_FArmals)
        '''Mother Armals'''
        # Check Mother Data
        self.pushButton_123.clicked.connect(self.Check_Mother_Armal)
        # Sons Tabs
        # 1 st Son to 2
        self.pushButton_60.clicked.connect(self.On_Mouse_Click_in_1st_Son_FatherDeadd)
        # Back to 1
        self.pushButton_70.clicked.connect(self.open_1st_Son_Tab_MArmals)
        # 2 st Son to 3
        self.pushButton_69.clicked.connect(self.On_Mouse_Click_in_2st_Son_FatherDeadd)
        # Back to 2
        self.pushButton_72.clicked.connect(self.open_2st_Son_Tab_MArmals)
        # 4 st Son
        self.pushButton_71.clicked.connect(self.On_Mouse_Click_in_3st_Son_FatherDeadd)
        # Back to 3
        self.pushButton_74.clicked.connect(self.open_3st_Son_Tab_MArmals)
        # 5 st Son
        self.pushButton_73.clicked.connect(self.On_Mouse_Click_in_4st_Son_FatherDeadd)
        # Back to 4
        self.pushButton_76.clicked.connect(self.open_4st_Son_Tab_MArmals)
        # 6 st Son
        self.pushButton_75.clicked.connect(self.On_Mouse_Click_in_5st_Son_FatherDeadd)
        # Back to 5
        self.pushButton_103.clicked.connect(self.open_5st_Son_Tab_MArmals)
        # 7 st Son
        self.pushButton_101.clicked.connect(self.On_Mouse_Click_in_6st_Son_FatherDeadd)
        # Back to 6
        self.pushButton_105.clicked.connect(self.open_6st_Son_Tab_MArmals)
        # 8 st Son
        self.pushButton_104.clicked.connect(self.On_Mouse_Click_in_7st_Son_FatherDeadd)
        # Back to 7
        self.pushButton_107.clicked.connect(self.open_7st_Son_Tab_MArmals)
        # 9 st Son
        self.pushButton_106.clicked.connect(self.On_Mouse_Click_in_8st_Son_FatherDeadd)
        # Back to 8
        self.pushButton_109.clicked.connect(self.open_8st_Son_Tab_MArmals)
        # Go to 10st  son
        self.pushButton_108.clicked.connect(self.On_Mouse_Click_in_9st_Son_FatherDeadd)

        # Back to 9
        self.pushButton_110.clicked.connect(self.open_9st_Son_Tab_MArmals)
        # Button Enable Record Sons Data
        self.pushButton_141.clicked.connect(self.Check_On_Click_Sons_Tabl_MArmals)
        # Record Mother Data
        self.pushButton_100.clicked.connect(self.Record_Mother_ArmalS)
        # Record Sons Data
        self.pushButton_100.clicked.connect(self.Choice_Recoord_Sons_NumS_MArmals)
        self.pushButton_100.clicked.connect(self.Clear_All_LineEdits_Of_Family_MArmals)

        '''Search Family Tab'''
        # Report Family Data
        self.pushButton_24.clicked.connect(self.Report_Fathers_Data)
        # Report Sons Data
        self.pushButton_27.clicked.connect(self.Report_Sons_Data)
        '''Search Family Special Num'''
        self.pushButton.clicked.connect(self.Search_Num_Family)
        # Clear Form Button Back to MAIN WINDOW
        self.pushButton_4.clicked.connect(self.Clear_SpainBoxes)
        # Report Special Family Num
        self.pushButton_2.clicked.connect(self.Report_Special_Num_FamIly)
        '''Add Sons Akhwet El Rab'''
        # Read Mother From Father ComboBox
        self.comboBox_20.currentTextChanged.connect(self.Read_Mother_Name_From_FComboBox)
        # Check Sons Data
        self.pushButton_122.clicked.connect(self.Check_Add_Sons)
        # Record_Sons Data
        self.pushButton_125.clicked.connect(self.Add_Sons)
        # Clear
        self.pushButton_121.clicked.connect(self.Clear_Sons_LineEdits)
        ''' Add New Serves , Works , Street ,Study'''
        # Add Father Work
        self.pushButton_126.clicked.connect(self.Confirm_Add_FWork)
        # Add Father Work
        self.pushButton_127.clicked.connect(self.Confirm_Add_MWork)
        # Add Sons Work
        self.pushButton_128.clicked.connect(self.Confirm_Add_SWork)
        # Add New Study Sons
        self.pushButton_199.clicked.connect(self.Confirm_Add_SStudy)
        # Add New Street
        self.pushButton_200.clicked.connect(self.Confirm_Add_Streets)
        # Add New Serve
        self.pushButton_201.clicked.connect(self.Confirm_Add_Serves)
        # Delete Father Work
        self.pushButton_202.clicked.connect(self.Confirm_Delete_FWork)
        # Delete Mother Work
        self.pushButton_203.clicked.connect(self.Confirm_Delete_MWork)
        # Delete Sons Work
        self.pushButton_204.clicked.connect(self.Confirm_Delete_SWork)
        # Delete Sons Study
        self.pushButton_205.clicked.connect(self.Confirm_Delete_Study)
        # Delete Street
        self.pushButton_206.clicked.connect(self.Confirm_Delete_Street)
        # Delete Serve
        self.pushButton_207.clicked.connect(self.Confirm_Delete_Serve)
        ''' Add Serves To Family Tabs '''
        # Show Family With Serves
        self.Show_Family_After_Add_Serve()
        # Show Save Button To sAVE Info
        self.pushButton_6.clicked.connect(self.Confirm_Save_Data)
        # Save Info
        self.pushButton_5.clicked.connect(self.Add_Serve_To_Family)
        # Cleaar
        self.pushButton_10.clicked.connect(self.Clear_CLineEdits)
        '''Search Special Serve Tab'''
        # Show Result Search
        self.pushButton_7.clicked.connect(self.Search_Special_Serve)
        # Report Special Serve
        self.pushButton_8.clicked.connect(self.Report_Special_Serve)
        '''Edit Father Data'''
        # Change Selection
        self.tableWidget_6.itemSelectionChanged.connect(self.Selection_Changes_Fathers)
        # Confirm Udate
        self.pushButton_31.clicked.connect(self.Confirmation_Update)
        # Confirm Delete
        self.pushButton_32.clicked.connect(self.Confirm_Delete)
        '''Edit Mother Data '''
        # Change Selection
        self.tableWidget_7.itemSelectionChanged.connect(self.Selection_Changes_Mothers)
        # Confirm Udate
        self.pushButton_62.clicked.connect(self.Confirmation_Mother)
        # Confirm Delete
        self.pushButton_59.clicked.connect(self.Confirm_Delete_MData)
        '''Edit Sons Tab'''
        # Change Selection
        self.tableWidget_8.itemSelectionChanged.connect(self.Selection_Changes_Sons)
        # Confirm Udate Sons Data
        self.pushButton_37.clicked.connect(self.Confirmation_Edit_Sons)
        # Confirm Delete Sons Data
        self.pushButton_38.clicked.connect(self.Confirmation_Deletions)

        '''Edit Regester Tab'''
        # Change Selection
        self.tableWidget_13.itemSelectionChanged.connect(self.Selection_Changes_Regester)
        # Confirm Udate Regester Data
        self.pushButton_96.clicked.connect(self.Confirmation_Edit_Regester)
        # Confirm Delete Regester Data
        self.pushButton_41.clicked.connect(self.Confirmation_Deletions_Regester)

        '''Search Father , Mother , Son , Family Tabs'''
        # Report Special Family of Father Or Mother Or Sons Search
        self.pushButton_90.clicked.connect(self.Report_Specialk_Mom)
        self.pushButton_92.clicked.connect(self.Report_Specialk_SOm)
        self.pushButton_87.clicked.connect(self.Report_Specialk_Fatther)
        # Search Father By Name
        self.comboBox_8.currentTextChanged.connect(self.Search_Father_Data_From_Table)
        # Search Father By Mobile
        # self.pushButton_88.clicked.connect(self.Search_Father_Data_By_Phone)
        # Search Mother By Name
        self.comboBox_9.currentTextChanged.connect(self.Search_Mother_Data_From_Table)
        # Search Mother By Mobile
        # self.pushButton_89.clicked.connect(self.Search_Mother_Data_By_Phone)
        # Search Son By Father
        self.comboBox_10.currentTextChanged.connect(self.Search_Son_Data_From_Table_F)
        '''Search All Family '''
        # Search By Father Name
        self.pushButton_94.clicked.connect(self.Search_All_Family_App)
        # Search By Mother Name
        self.pushButton_95.clicked.connect(self.Search_All_Family_App_ByMother)
        # Report ALL Family Data
        self.pushButton_93.clicked.connect(self.Report_All_Family_Data)
        '''Move Add Tabs'''
        self.comboBox_11.currentTextChanged.connect(self.Cross_To_Added_Tabs)
        '''Move Search Tabs'''
        self.comboBox_14.currentTextChanged.connect(self.Choice_Search_Tabs)
        '''Move Update Tabs'''
        self.comboBox_15.currentTextChanged.connect(self.Choice_Update_Tabs)

        ''' Radio Button For Armals'''
        self.radioButton_140.pressed.connect(self.Father_Dead_RadioButton_A3zeb)
        self.radioButton_61.pressed.connect(self.Father_Dead_RadioButton_Armala)
        self.radioButton_103.pressed.connect(self.Mother_Dead_RadioButton_A3zeb)
        self.radioButton_60.pressed.connect(self.Mother_Dead_RadioButton_Armala)

    def Mother_Dead_RadioButton_A3zeb(self):
        self.lineEdit_35.setEnabled(False)
        self.spinBox_10.setEnabled(False)
        self.lineEdit_35.setText("")
        self.spinBox_10.setValue(0)

    def Mother_Dead_RadioButton_Armala(self):
        self.lineEdit_35.setEnabled(True)
        self.spinBox_10.setEnabled(True)

    def Father_Dead_RadioButton_A3zeb(self):
        self.lineEdit_36.setEnabled(False)
        self.spinBox_11.setEnabled(False)
        self.lineEdit_36.setText("")
        self.spinBox_11.setValue(0)

    def Father_Dead_RadioButton_Armala(self):
        self.lineEdit_36.setEnabled(True)
        self.spinBox_11.setEnabled(True)





    # Combo Box Moving Between Added Tab
    def Cross_To_Added_Tabs(self):
        ComboBox = self.comboBox_11.currentText()
        if ComboBox == 'اضافه بيانات اسرة كامله':
            self.Add_Family_tabs()
        if ComboBox == 'اضافه بيانات اسرة بدون اب':
            self.Armala_Tab()

        if ComboBox == 'اضافه اسرة بدون ام':
            self.Armal_Tab()

        if ComboBox == 'اضافه مواليد':
            self.Sons_Tab()
        if ComboBox == 'اضافه خدمه جديده':
            self.Add_Services_Tab()
        if ComboBox == 'اضافه خدمات جديدة للاسر':
            self.Add_Services_To_Family()

    # Combo Box Moving Between Search Tab
    def Choice_Search_Tabs(self):
        ComboBox = self.comboBox_14.currentText()
        if ComboBox == 'بحث بيانات اسرة كامله':
            self.Search_Family()
        if ComboBox == 'بحث من حهه الاب':
            self.Search_Father()
        if ComboBox == 'بحث من جهه الام':
            self.Search_Mother()
        if ComboBox == 'بحث من جهه الابن':
            self.Search_Sons()
        if ComboBox == 'بحث عن عدد معين من الاسر':
            self.Search_Special_Num()
        if ComboBox == 'بحث عن خدمه':
            self.Search_Services()
        if ComboBox == 'الاسر كامله':
            self.Family_Tabs()

    # Combo Box Moving Between Update Tab
    def Choice_Update_Tabs(self):
        ComboBox = self.comboBox_15.currentText()
        if ComboBox == 'تعديل بيانات اب':
            self.Go_Edit_Father()
            self.Show_Fathers()
        if ComboBox == 'تعديل بيانات ام':
            self.Go_Edit_Mother()
            self.Show_Mothers()
        if ComboBox == 'تعديل بيانات ابن':
            self.Go_Edit_Sons()
            self.Show_All_Sons()
        if ComboBox == 'بيانات التسجيل':
            self.Go_Edit_Regester()
            self.Show_All_Regester()
    '''Program Main Windows Tabs'''

    def Open_Tab_Akwet_El_Rab(self):
        self.tabWidget_2.setCurrentIndex(0)
        # Main Program Tab
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_3.tabBar().setVisible(False)
        # Sons Tab of FArmals
        self.tabWidget_8.tabBar().setVisible(False)
        self.tabWidget_8.setCurrentIndex(0)
        # Sons Tab Of Family
        self.tabWidget_4.tabBar().setVisible(False)
        self.tabWidget_4.setCurrentIndex(0)
        # Sons Tab Of Mother Armal
        self.tabWidget_7.tabBar().setVisible(False)
        self.tabWidget_7.setCurrentIndex(0)

    def Open_Main_Page(self):
        self.tabWidget_2.setCurrentIndex(1)

    def Open_Add_Family_Tab(self):
        self.tabWidget_2.setCurrentIndex(2)

    def Open_Family_Father_Dead(self):
        self.tabWidget_2.setCurrentIndex(3)

    def Open_Family_Mother_Dead(self):
        self.tabWidget_2.setCurrentIndex(4)

    def Add_Children_Tab(self):
        self.tabWidget_2.setCurrentIndex(5)

    def Search_Num_Family_Tab(self):
        self.tabWidget_2.setCurrentIndex(6)

    def Add_Services_Tab(self):
        self.tabWidget_2.setCurrentIndex(7)

    def Search_Services_Tab(self):
        self.tabWidget_2.setCurrentIndex(8)

    def Search_Family_Tab(self):
        self.tabWidget_2.setCurrentIndex(9)

    def Create_New_Services(self):
        self.tabWidget_2.setCurrentIndex(10)

    '''Edit Father ,Mother,Sons Tabs'''

    def Go_Edit_Father(self):
        self.tabWidget_2.setCurrentIndex(11)

    def Go_Edit_Mother(self):
        self.tabWidget_2.setCurrentIndex(12)

    def Go_Edit_Sons(self):
        self.tabWidget_2.setCurrentIndex(13)

    def Go_Edit_Regester(self):
        self.tabWidget_2.setCurrentIndex(18)

    '''Family Sons Tab'''

    # 1st Sons
    def open_1st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(0)

    # 2st Sons
    def open_2st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(1)

    # 3st Sons
    def open_3st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(2)

    # 4st Sons
    def open_4st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(3)

    # 5st Sons
    def open_5st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(4)

    # 6st Sons
    def open_6st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(5)

    # 7st Sons
    def open_7st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(6)

    # 8st Sons
    def open_8st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(7)

    # 9st Sons
    def open_9st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(8)

    # 10st Sons
    def open_10st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(9)

    '''Father Armal Tab'''

    # 1st Sons
    def open_1st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(0)

    # 2st Sons
    def open_2st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(1)

    # 3st Sons
    def open_3st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(2)

    # 4st Sons
    def open_4st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(3)

    # 5st Sons
    def open_5st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(4)

    # 6st Sons
    def open_6st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(5)

    # 7st Sons
    def open_7st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(6)

    # 8st Sons
    def open_8st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(7)

    # 9st Sons
    def open_9st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(8)

    # 10st Sons
    def open_10st_Son_Tab_FArmals(self):
        self.tabWidget_8.setCurrentIndex(9)

    '''Mother Armal Sons Tab '''

    # 1st Sons
    def open_1st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(0)

    # 2st Sons
    def open_2st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(1)

    # 3st Sons
    def open_3st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(2)

    # 4st Sons
    def open_4st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(3)

    # 5st Sons
    def open_5st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(4)

    # 6st Sons
    def open_6st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(5)

    # 7st Sons
    def open_7st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(6)

    # 8st Sons
    def open_8st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(7)

    # 9st Sons
    def open_9st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(8)

    # 10st Sons
    def open_10st_Son_Tab_MArmals(self):
        self.tabWidget_7.setCurrentIndex(9)

    '''Search Family ,Mother,Father,Sons'''

    def Search_Family_Tab(self):
        self.tabWidget_2.setCurrentIndex(17)

    def Search_Father_Tab(self):
        self.tabWidget_2.setCurrentIndex(14)

    def Search_Mother_Tab(self):
        self.tabWidget_2.setCurrentIndex(15)

    def Search_Sons_Tab(self):
        self.tabWidget_2.setCurrentIndex(16)

    ''' Cross To Added Tabs '''

    def Add_Family_tabs(self):
        # Add Famly Tab
        self.Open_Add_Family_Tab()
        self.Add_FF_ComboBox_Work()
        self.Add_FF_ComboBox_Street()
        self.Add_MF_ComboBox_Work()
        self.F1st_Son_Work()
        self.F1st_Son_Study()
        self.F2st_Son_Work()
        self.F2st_Son_Study()
        self.F3st_Son_Work()
        self.F3st_Son_Study()
        self.F4st_Son_Work()
        self.F4st_Son_Study()
        self.F5st_Son_Work()
        self.F5st_Son_Study()
        self.F6st_Son_Work()
        self.F6st_Son_Study()
        self.F7st_Son_Work()
        self.F7st_Son_Study()
        self.F8st_Son_Work()
        self.F8st_Son_Study()
        self.F9st_Son_Work()
        self.F9st_Son_Study()
        self.F10st_Son_Work()
        self.F10st_Son_Study()
        # Add Armala Tab

    #  Add Armala Tab
    def Armala_Tab(self):
        self.Open_Family_Father_Dead()
        self.Add_FArmala_ComboBox_Work()
        self.Add_FArmala_ComboBox_Street()
        self.Armala1st_Son_Work()
        self.Armala1st_Son_Study()
        self.Armala2st_Son_Work()
        self.Armala2st_Son_Study()
        self.Armala3st_Son_Work()
        self.Armala3st_Son_Study()
        self.Armala4st_Son_Work()
        self.Armala4st_Son_Study()
        self.Armala5st_Son_Work()
        self.Armala5st_Son_Study()
        self.Armala6st_Son_Work()
        self.Armala6st_Son_Study()
        self.Armala7st_Son_Work()
        self.Armala7st_Son_Study()
        self.Armala8st_Son_Work()
        self.Armala8st_Son_Study()
        self.Armala9st_Son_Work()
        self.Armala9st_Son_Study()
        self.Armala10st_Son_Work()
        self.Armala10st_Son_Study()

    # Add Armal Tab
    def Armal_Tab(self):
        self.Open_Family_Mother_Dead()
        self.Add_FArmal_ComboBox_Work()
        self.Add_FArmal_ComboBox_Street()
        self.Armal1st_Son_Work()
        self.Armal1st_Son_Study()
        self.Armal2st_Son_Work()
        self.Armal2st_Son_Study()
        self.Armal3st_Son_Work()
        self.Armal3st_Son_Study()
        self.Armal4st_Son_Work()
        self.Armal4st_Son_Study()
        self.Armal5st_Son_Work()
        self.Armal5st_Son_Study()
        self.Armal6st_Son_Work()
        self.Armal6st_Son_Study()
        self.Armal7st_Son_Work()
        self.Armal7st_Son_Study()
        self.Armal8st_Son_Work()
        self.Armal8st_Son_Study()
        self.Armal9st_Son_Work()
        self.Armal9st_Son_Study()
        self.Armal10st_Son_Work()
        self.Armal10st_Son_Study()

    # Add Sons Tab
    def Sons_Tab(self):
        self.Add_Children_Tab()
        self.Read_Father_Name_From_TableDB()

    # Add New Services
    def Add_Services_Tab(self):
        self.Create_New_Services()

    # Add Services To Family
    def Add_Services_To_Family(self):
        self.tabWidget_2.setCurrentIndex(7)
        self.Show_All_Familyu()
        self.Add_Values()

    ''' Cross To Search Tabs '''

    # Search Family
    def Search_Family(self):
        self.Search_Family_Tab()
        self.Show_Family_By_FName_In_ComboBox()
        self.Show_Family_By_MName_In_ComboBox()

    # Search Father
    def Search_Father(self):
        self.Search_Father_Tab()
        self.Show_Father_Name_In_ComboBox()

    # Search Mother
    def Search_Mother(self):
        self.Search_Mother_Tab()
        self.Show_Mother_Name_In_ComboBox()

    # Search Sons
    def Search_Sons(self):
        self.Search_Sons_Tab()
        self.Show_Son_Name_In_ComboBox_F()

    # Search Special Num
    def Search_Special_Num(self):
        self.Search_Num_Family_Tab()

    # Search Searvices
    def Search_Services(self):
        self.Search_Services_Tab()
        self.Add_Values_ComboBoxes()

    # Search Akwet El Rab
    def Family_Tabs(self):
        self.Search_Family_Tab()
        self.Search_Family_Data()
        self.Search_Sons_Data()

    ''' Update Tab'''

    # Update Father Data
    def Update_Father_Tab(self):
        self.Go_Edit_Father()
        self.Show_Fathers()
        self.Show_Work_InComboBoxes()
        self.Show_Streets_ComboBox()

    # Update Mother Data
    def Update_Mother_Tabs(self):
        self.Go_Edit_Mother()
        self.Show_Mothers()
        self.Show_Work_InComboBoxes_Armla()

    # Update Sons Data
    def Update_Sons_Tabs(self):
        self.Go_Edit_Sons()
        self.Show_All_Sons()
        self.Show_Work_InComboBoxes_Sons()
        self.Show_Study_InComboBoxes_Sons()

    ''' ==============================  Family Tab ===================================== '''

    # Record Father Data
    def Record_Father(self):
        Name = self.lineEdit_16.text()
        Ssn = self.lineEdit_14.text()
        Leader = 'لا'
        if self.checkBox_22.isChecked():
            Leader = 'نعم'
        Work = self.comboBox_25.currentText()
        Street = self.comboBox_26.currentText()
        Address = self.lineEdit_15.text()
        Qulified = self.lineEdit_9.text()
        Father = self.lineEdit_13.text()
        DOB = self.dateEdit_25.date()
        DOB = DOB.toPyDate()
        Phone = self.lineEdit_12.text()
        ChildNum = self.spinBox_8.value()
        SpecialCase = 'لا'
        if self.checkBox_19.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_11.text()
        MName = self.lineEdit_99.text()
        MSsn = self.lineEdit_102.text()
        MPhone = self.lineEdit_98.text()
        FamilyNum = int(self.spinBox_8.value()) + int(2)
        Stutus = 'متزوج'
        ProgramNum = self.lineEdit_107.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Father VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (Name, Ssn, Leader, Work, Street, Address, Qulified, Father, DOB, ChildNum, Phone, SpecialCase, Type,
                   MName, MPhone, MSsn, FamilyNum, Stutus, ProgramNum))
        db.commit()
        db.close()
        QMessageBox.information(QWidget(), "جيد", 'تمت حفظ بيانات الاب بنجاح')

    # Check Father Data
    def Check_Father_Data(self):
        Name = self.lineEdit_16.text()
        Ssn = self.lineEdit_14.text()
        Work = self.comboBox_25.currentText()
        Street = self.comboBox_26.currentText()
        Address = self.lineEdit_15.text()
        Qulified = self.lineEdit_9.text()
        ChildNum = self.spinBox_8.value()
        Phone = self.lineEdit_12.text()
        if Phone.isdigit():
            pass
        else:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه رقميه')
        if Ssn.isdigit():
            pass
        else:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال الرقم القومي بطريقه صحيحه رقميه')

        if len(Phone) < 11:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه مكون من 11 رقم')
        if len(Ssn) < 14:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال الرقم القومي مكون من 14 رقم')

        if self.lineEdit_16.text() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم رب الاسرة  ')
        if self.lineEdit_15.text() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال العنوان  ')
        if self.lineEdit_9.text() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال المؤهل   ')
        if self.comboBox_25.currentText() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم العمل  ')
        if self.comboBox_26.currentText() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الشارع  ')
        if Name != '' and Street != '' and Address != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Ssn) == 14 and len(Phone) == 11:
            if ChildNum == 0 and Name != '' and Street != '' and Address != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Ssn) == 14 and len(Phone) == 11:
                Replay = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من عدد الابناء   ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes:
                    X = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من تاريخ الميلاد   ؟!!',
                                                QMessageBox.Yes | QMessageBox.No)
                    if X == QMessageBox.Yes:
                        self.tabWidget_3.setEnabled(True)
            else:
                X = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من تاريخ الميلاد   ؟!!',
                                            QMessageBox.Yes | QMessageBox.No)
                if X == QMessageBox.Yes:
                    self.tabWidget_3.setEnabled(True)
        else:
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال التاكد ان اللاقم القومي 14 رقم والموبيل 11 رقم  ')


    # Record Mother Data
    def Record_Mother(self):
        Name = self.lineEdit_99.text()
        Ssn = self.lineEdit_102.text()
        Leader = 'لا'
        if self.checkBox_21.isChecked():
            Leader = 'نعم'
        Qulified = self.lineEdit_100.text()
        Father = self.lineEdit_101.text()
        Work = self.comboBox_27.currentText()
        Age = self.dateEdit_26.date()
        Age = Age.toPyDate()
        Phone = self.lineEdit_98.text()
        Stutus = 'لا'
        if self.checkBox_20.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_128.text()
        Address = self.lineEdit_15.text()
        Street = self.comboBox_26.currentText()
        Fphone = self.lineEdit_12.text()
        FSsn = self.lineEdit_14.text()
        FName = self.lineEdit_16.text()
        ChildNum = self.spinBox_8.value()
        FamilyNum = int(self.spinBox_8.value()) + 2
        Stutus = 'متزوجه'
        ProgramNum = self.lineEdit_107.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Mother VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (Name, Ssn, Leader, Qulified, Father, Work, Age, Phone, Stutus, Type, Address, Street, FSsn, FName,
                   Fphone, ChildNum, Stutus, FamilyNum, ProgramNum))
        db.commit()
        db.close()
        QMessageBox.information(QWidget(), "جيد", 'تمت حفظ بيانات الام بنجاح')

    # Check Mother Data
    def Check_Mother_Data(self):
        Name = self.lineEdit_99.text()
        Ssn = self.lineEdit_102.text()
        Qulified = self.lineEdit_100.text()
        Work = self.comboBox_27.currentText()
        Phone = self.lineEdit_98.text()
        Age = self.dateEdit_26.date()
        if Phone.isdigit() :
            pass
        else:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه رقميه')
        if Ssn.isdigit():
            pass
        else:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال الرقم القومي بطريقه صحيحه رقميه')

        if len(Phone) < 11:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه مكون من 11 رقم')
        if len(Ssn) < 14:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال الرقم القومي مكون من 14 رقم')

        if self.lineEdit_99.text() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الام  ')
        if self.lineEdit_100.text() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال مؤهل الام   ')
        if self.comboBox_27.currentText() == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم عمل الام   ')
        if Name != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Ssn) == 14 and len(Phone) == 11:
            N = self.spinBox_8.value()
            if Age != '' and Name != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Ssn) == 14 and len(Phone) == 11:
                Replay = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if N == 0 and Name != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Ssn) == 14 and len(Phone) == 11:
                    self.pushButton_21.setEnabled(True)
                elif Replay == QMessageBox.Yes:
                    self.Choice_Son_Num()
                else:
                    pass
        else:
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال التاكد ان اللاقم القومي 14 رقم والموبيل 11 رقم  ')

    # Record Sons
    def Record_1st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_141.text()
        Gender = 'ولد'
        if self.radioButton_86.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_109.text()
        DOB = self.dateEdit_32.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_37.currentText()
        Phone = self.lineEdit_142.text()
        Study = self.comboBox_53.currentText()
        SpecialCase = 'لا'
        if self.checkBox_31.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_140.text()
        NationalID = self.lineEdit_259.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_2st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_144.text()
        Gender = 'ولد'
        if self.radioButton_88.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_111.text()
        DOB = self.dateEdit_33.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_38.currentText()
        Phone = self.lineEdit_145.text()
        Study = self.comboBox_54.currentText()
        SpecialCase = 'لا'
        if self.checkBox_32.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_143.text()
        NationalID = self.lineEdit_260.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_3st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_147.text()
        Gender = 'ولد'
        if self.radioButton_82.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_114.text()
        DOB = self.dateEdit_34.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_39.currentText()
        Phone = self.lineEdit_148.text()
        Study = self.comboBox_55.currentText()
        SpecialCase = 'لا'
        if self.checkBox_24.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_146.text()
        NationalID = self.lineEdit_261.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_4st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_150.text()
        Gender = 'ولد'
        if self.radioButton_90.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_115.text()
        DOB = self.dateEdit_35.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_40.currentText()
        Phone = self.lineEdit_151.text()
        Study = self.comboBox_56.currentText()
        SpecialCase = 'لا'
        if self.checkBox_33.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_149.text()
        NationalID = self.lineEdit_262.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_5st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_138.text()
        Gender = 'ولد'
        if self.radioButton_78.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_122.text()
        DOB = self.dateEdit_31.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_52.currentText()
        Phone = self.lineEdit_139.text()
        Study = self.comboBox_49.currentText()
        SpecialCase = 'لا'
        if self.checkBox_26.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_137.text()
        NationalID = self.lineEdit_263.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_6st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_135.text()
        Gender = 'ولد'
        if self.radioButton_76.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_123.text()
        DOB = self.dateEdit_30.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_41.currentText()
        Phone = self.lineEdit_136.text()
        Study = self.comboBox_51.currentText()
        SpecialCase = 'لا'
        if self.checkBox_30.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_134.text()
        NationalID = self.lineEdit_264.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_7st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_132.text()
        Gender = 'ولد'
        if self.radioButton_74.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_124.text()
        DOB = self.dateEdit_29.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_42.currentText()
        Phone = self.lineEdit_133.text()
        Study = self.comboBox_50.currentText()
        SpecialCase = 'لا'
        if self.checkBox_29.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_131.text()
        NationalID = self.lineEdit_265.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_8st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_125.text()
        Gender = 'ولد'
        if self.radioButton_72.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_106.text()
        DOB = self.dateEdit_28.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_43.currentText()
        Phone = self.lineEdit_126.text()
        Study = self.comboBox_47.currentText()
        SpecialCase = 'لا'
        if self.checkBox_28.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_130.text()
        NationalID = self.lineEdit_266.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_9st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_104.text()
        Gender = 'ولد'
        if self.radioButton_70.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_103.text()
        DOB = self.dateEdit_27.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_44.currentText()
        Phone = self.lineEdit_105.text()
        Study = self.comboBox_46.currentText()
        SpecialCase = 'لا'
        if self.checkBox_27.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_129.text()
        NationalID = self.lineEdit_267.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_10st_Son(self):
        MName = self.lineEdit_99.text()
        FName = self.lineEdit_16.text()
        Name = self.lineEdit_97.text()
        Gender = 'ولد'
        if self.radioButton_66.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_95.text()
        DOB = self.dateEdit_24.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_24.currentText()
        Phone = self.lineEdit_96.text()
        Study = self.comboBox_45.currentText()
        SpecialCase = 'لا'
        if self.checkBox_18.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_127.text()
        NationalID = self.lineEdit_268.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    # Check Sons
    def On_Mouse_Click_in_1st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_141.text()
        Study = self.comboBox_53.currentText()
        Job = self.comboBox_37.currentText()
        NationalID = self.lineEdit_259.text()
        Phone = self.lineEdit_142.text()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_2st_Son_Tab()

    def On_Mouse_Click_in_1st_SoNF(self):
        SName = self.lineEdit_141.text()
        Study = self.comboBox_53.currentText()
        Job = self.comboBox_37.currentText()
        NationalID = self.lineEdit_259.text()
        Phone = self.lineEdit_142.text()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')
        if SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_2st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_144.text()
        Study = self.comboBox_54.currentText()
        Job = self.comboBox_38.currentText()
        Phone = self.lineEdit_148.text()
        NationalID = self.lineEdit_261.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_3st_Son_Tab()

    def On_Mouse_Click_in_2st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_144.text()
        Study = self.comboBox_54.currentText()
        Job = self.comboBox_38.currentText()
        Phone = self.lineEdit_148.text()
        NationalID = self.lineEdit_261.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_3st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_147.text()
        Study = self.comboBox_55.currentText()
        Job = self.comboBox_39.currentText()
        Phone = self.lineEdit_148.text()
        NationalID = self.lineEdit_261.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_4st_Son_Tab()

    def On_Mouse_Click_in_3st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_147.text()
        Study = self.comboBox_55.currentText()
        Job = self.comboBox_39.currentText()
        Phone = self.lineEdit_148.text()
        NationalID = self.lineEdit_261.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_4st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_150.text()
        Study = self.comboBox_56.currentText()
        Job = self.comboBox_40.currentText()
        Phone = self.lineEdit_151.text()
        NationalID = self.lineEdit_262.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_5st_Son_Tab()

    def On_Mouse_Click_in_4st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_150.text()
        Study = self.comboBox_56.currentText()
        Job = self.comboBox_40.currentText()
        Phone = self.lineEdit_151.text()
        NationalID = self.lineEdit_262.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_5st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_138.text()
        Study = self.comboBox_49.currentText()
        Job = self.comboBox_52.currentText()
        Phone = self.lineEdit_139.text()
        NationalID = self.lineEdit_263.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_6st_Son_Tab()

    def On_Mouse_Click_in_5st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_138.text()
        Study = self.comboBox_49.currentText()
        Job = self.comboBox_52.currentText()
        Phone = self.lineEdit_139.text()
        NationalID = self.lineEdit_263.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_6st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_135.text()
        Study = self.comboBox_51.currentText()
        Job = self.comboBox_41.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_7st_Son_Tab()

    def On_Mouse_Click_in_6st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_135.text()
        Study = self.comboBox_51.currentText()
        Job = self.comboBox_41.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_7st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_132.text()
        Study = self.comboBox_50.currentText()
        Job = self.comboBox_42.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_8st_Son_Tab()

    def On_Mouse_Click_in_7st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_132.text()
        Study = self.comboBox_50.currentText()
        Job = self.comboBox_42.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_8st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_125.text()
        Study = self.comboBox_47.currentText()
        Job = self.comboBox_43.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_9st_Son_Tab()

    def On_Mouse_Click_in_8st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_125.text()
        Study = self.comboBox_47.currentText()
        Job = self.comboBox_43.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_9st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_104.text()
        Study = self.comboBox_46.currentText()
        Job = self.comboBox_44.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_10st_Son_Tab()

    def On_Mouse_Click_in_9st_SoNF(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()

        SName = self.lineEdit_104.text()
        Study = self.comboBox_46.currentText()
        Job = self.comboBox_44.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_10st_SoN(self):
        FName = self.lineEdit_16.text()
        MName = self.lineEdit_99.text()
        SName = self.lineEdit_97.text()
        Study = self.comboBox_45.currentText()
        Job = self.comboBox_24.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    # Checkes Sons Num Choices
    def Choice_Son_Num(self):
        try:
            User_Choice = self.spinBox_8.value()
            if User_Choice == 0:
                self.tabWidget_4.setEnabled(False)
            elif User_Choice == 1:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_11.setEnabled(False)
            elif User_Choice == 2:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_13.setEnabled(False)

            elif User_Choice == 3:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_14.setEnabled(False)

            elif User_Choice == 4:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_15.setEnabled(False)

            elif User_Choice == 5:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_16.setEnabled(False)
            elif User_Choice == 6:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_17.setEnabled(False)

            elif User_Choice == 7:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_18.setEnabled(False)

            elif User_Choice == 8:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_19.setEnabled(False)

            elif User_Choice == 9:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_20.setEnabled(False)

            elif User_Choice == 10:
                self.Open_All_Buttons_Sons()
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
            else:
                QMessageBox.information(QWidget(), "للاسف!!", 'عدد الابناء متاح الي 10 ابناء فقط')
        except:
            QMessageBox.information(QWidget(), "للاسف!!", 'عدد الابناء متاح الي 10 ابناء فقط')

    # Checkes Record
    def Choice_Recoord_Sons_NumS(self):
        try:
            User_Choice = self.spinBox_8.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.Record_1st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()

            elif User_Choice == 2:
                self.Record_1st_Son()
                self.Record_2st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 3:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 4:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 5:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                self.Record_5st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 6:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                self.Record_5st_Son()
                self.Record_6st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 7:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                self.Record_5st_Son()
                self.Record_6st_Son()
                self.Record_7st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 8:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                self.Record_5st_Son()
                self.Record_6st_Son()
                self.Record_7st_Son()
                self.Record_8st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 9:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                self.Record_5st_Son()
                self.Record_6st_Son()
                self.Record_7st_Son()
                self.Record_8st_Son()
                self.Record_9st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            elif User_Choice == 10:
                self.Record_1st_Son()
                self.Record_2st_Son()
                self.Record_3st_Son()
                self.Record_4st_Son()
                self.Record_5st_Son()
                self.Record_6st_Son()
                self.Record_7st_Son()
                self.Record_8st_Son()
                self.Record_9st_Son()
                self.Record_10st_Son()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            else:
                QMessageBox.information(QWidget(), "للاسف!!", 'رجاء التاكد من بيانات الاب والاو والابناء        ')
        except:
            pass

    # Checks Sons Tab For Open
    def Check_On_Click_Sons_Tabl(self):
        try:
            User_Choice = self.spinBox_8.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.On_Mouse_Click_in_1st_SoNF()
            elif User_Choice == 2:
                self.On_Mouse_Click_in_2st_SoNF()
            elif User_Choice == 3:
                self.On_Mouse_Click_in_3st_SoNF()
            elif User_Choice == 4:
                self.On_Mouse_Click_in_4st_SoNF()
            elif User_Choice == 5:
                self.On_Mouse_Click_in_5st_SoNF()
            elif User_Choice == 6:
                self.On_Mouse_Click_in_6st_SoNF()
            elif User_Choice == 7:
                self.On_Mouse_Click_in_7st_SoNF()
            elif User_Choice == 8:
                self.On_Mouse_Click_in_8st_SoNF()
            elif User_Choice == 9:
                self.On_Mouse_Click_in_9st_SoNF()
            elif User_Choice == 10:
                self.On_Mouse_Click_in_10st_SoN()
        except:
            pass

    # Make All Button Aviable
    def Open_All_Buttons_Sons(self):
        self.pushButton_20.setEnabled(True)
        self.pushButton_19.setEnabled(True)
        self.pushButton_18.setEnabled(True)
        self.pushButton_17.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_11.setEnabled(True)

    # Clean
    def Clear_All_LineEdits_Of_Family(self):
        self.tabWidget_4.setEnabled(False)
        self.tabWidget_3.setEnabled(False)
        self.tabWidget_4.setCurrentIndex(0)
        self.lineEdit_16.setText('')
        self.lineEdit_107.setText('')


        self.lineEdit_268.setText('')
        self.lineEdit_267.setText('')
        self.lineEdit_266.setText('')
        self.lineEdit_265.setText('')
        self.lineEdit_264.setText('')
        self.lineEdit_263.setText('')
        self.lineEdit_262.setText('')
        self.lineEdit_261.setText('')
        self.lineEdit_260.setText('')
        self.lineEdit_259.setText('')


        self.lineEdit_14.setText('')
        self.comboBox_25.setCurrentIndex(0)
        self.comboBox_26.setCurrentIndex(0)
        self.lineEdit_15.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_12.setText('')
        self.spinBox_8.setValue(0)
        self.lineEdit_11.setText('')
        self.lineEdit_99.setText('')
        self.lineEdit_102.setText('')
        self.lineEdit_100.setText('')
        self.lineEdit_101.setText('')
        self.comboBox_27.setCurrentIndex(0)
        self.lineEdit_98.setText('')
        self.lineEdit_128.setText('')
        # 1 son
        self.lineEdit_141.setText('')
        self.lineEdit_109.setText('')
        self.comboBox_37.setCurrentIndex(0)
        self.lineEdit_142.setText('')
        self.comboBox_53.setCurrentIndex(0)
        self.lineEdit_140.setText('')
        # 2 son
        self.lineEdit_144.setText('')
        self.lineEdit_111.setText('')
        self.comboBox_38.setCurrentIndex(0)
        self.lineEdit_145.setText('')
        self.comboBox_54.setCurrentIndex(0)
        self.lineEdit_143.setText('')
        # 3 son
        self.lineEdit_147.setText('')
        self.lineEdit_114.setText('')
        self.comboBox_39.setCurrentIndex(0)
        self.lineEdit_148.setText('')
        self.comboBox_55.setCurrentIndex(0)
        self.lineEdit_146.setText('')
        # 4 son
        self.lineEdit_150.setText('')
        self.lineEdit_115.setText('')
        self.comboBox_40.setCurrentIndex(0)
        self.lineEdit_151.setText('')
        self.comboBox_56.setCurrentIndex(0)
        self.lineEdit_149.setText('')
        # 5 son
        self.lineEdit_138.setText('')
        self.lineEdit_122.setText('')
        self.comboBox_52.setCurrentIndex(0)
        self.lineEdit_139.setText('')
        self.comboBox_49.setCurrentIndex(0)
        self.lineEdit_137.setText('')
        # 6 son
        self.lineEdit_135.setText('')
        self.lineEdit_123.setText('')
        self.comboBox_41.setCurrentIndex(0)
        self.lineEdit_136.setText('')
        self.comboBox_51.setCurrentIndex(0)
        self.lineEdit_134.setText('')
        # 7 son
        self.lineEdit_132.setText('')
        self.lineEdit_124.setText('')
        self.comboBox_42.setCurrentIndex(0)
        self.lineEdit_133.setText('')
        self.comboBox_50.setCurrentIndex(0)
        self.lineEdit_131.setText('')
        # 8 son
        self.lineEdit_125.setText('')
        self.lineEdit_106.setText('')
        self.comboBox_43.setCurrentIndex(0)
        self.lineEdit_126.setText('')
        self.comboBox_47.setCurrentIndex(0)
        self.lineEdit_130.setText('')
        # 9 son
        self.lineEdit_104.setText('')
        self.lineEdit_103.setText('')
        self.comboBox_44.setCurrentIndex(0)
        self.lineEdit_105.setText('')
        self.comboBox_46.setCurrentIndex(0)
        self.lineEdit_129.setText('')
        # 10 Son
        self.lineEdit_97.setText('')
        self.lineEdit_95.setText('')
        self.comboBox_24.setCurrentIndex(0)
        self.lineEdit_96.setText('')
        self.comboBox_45.setCurrentIndex(0)
        self.lineEdit_127.setText('')

    ''' ============================== Mother Dead Tab ===================================== '''

    # Record Father
    def Record_Father_Armal(self):
        Name = self.lineEdit_164.text()
        MName =  'المرحومة/' + str(self.lineEdit_36.text())
        Ssn = self.lineEdit_166.text()
        Qulified = self.lineEdit_237.text()
        Father = self.lineEdit_236.text()
        Street = self.comboBox_64.currentText()
        Address = self.lineEdit_202.text()
        Work = self.comboBox_65.currentText()
        Phone = self.lineEdit_158.text()
        DOB = self.dateEdit_37.date()
        DOB = DOB.toPyDate()
        ChildNum = self.spinBox_11.value()
        SpecialCase = 'لا'
        if self.checkBox_34.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_159.text()
        Stutus = 'ارمل'

        if self.radioButton_140.isChecked():
            Stutus = 'اعزب'
            self.lineEdit_36.setText("---------")
        ChildNum = self.spinBox_11.value()
        Leader = 'نعم'
        FamilyNum = int(self.spinBox_11.value()) + 1
        MPhone = '----------'
        MSsn = '----------'
        ProgramNum = self.lineEdit_270.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Father VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (Name, Ssn, Leader, Work, Street, Address, Qulified, Father, DOB, ChildNum, Phone, SpecialCase, Type,
                   MName, MPhone, MSsn, FamilyNum, Stutus, ProgramNum))
        db.commit()
        db.close()
        QMessageBox.information(QWidget(), "جيد", 'تمت حفظ بيانات الاب بنجاح')



    # Check Father Armal Data
    def Check_Father_Armal(self):
        Name = self.lineEdit_164.text()
        Qulified = self.lineEdit_237.text()
        Street = self.comboBox_64.currentText()
        Address = self.lineEdit_202.text()
        Work = self.comboBox_65.currentText()
        Ssn = self.lineEdit_166.text()
        Phone = self.lineEdit_158.text()
        if Phone.isdigit():
            pass
        else:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه')
        if Ssn.isdigit():
            pass
        else:
            QMessageBox.warning(self, 'رجاءا', 'تاكد من ادخال الرقم القومي بطريقه صحيحه')
        if Name == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم رب الاسرة  ')
        if Address == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال العنوان  ')
        if Qulified == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال المؤهل   ')
        if Work == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم العمل  ')
        if Street == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الشارع  ')

        if Name != '' and Street != '' and Address != '' and Qulified != '' and Work != '' and Ssn.isdigit() and Phone.isdigit() and len(Phone) == 11 and len(Ssn) == 14:
            if self.spinBox_11.value() == 0 and Name != '' and Street != '' and Address != '' and Qulified != '' and Work != '' and Ssn.isdigit() and Phone.isdigit() and len(Phone) == 11 and len(Ssn) == 14:
                self.tabWidget_8.setEnabled(False)
                Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من عدد الابناء ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes:
                    self.pushButton_120.setEnabled(True)
            else:
                self.Choice_Son_Num_FArmals()
        else:
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال التاكد ان اللاقم القومي 14 رقم والموبيل 11 رقم  ')



    # Record Son
    def Record_1st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_69.text()
        Gender = 'ولد'
        if self.radioButton_40.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_70.text()
        DOB = self.dateEdit_17.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_19.currentText()
        Phone = self.lineEdit_73.text()
        Study = self.comboBox_82.currentText()
        SpecialCase = 'لا'
        if self.checkBox_8.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_160.text()
        NationalID = self.lineEdit_71.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_2st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_163.text()
        Gender = 'ولد'
        if self.radioButton_122.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_203.text()
        DOB = self.dateEdit_48.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_48.currentText()
        Phone = self.lineEdit_162.text()
        Study = self.comboBox_83.currentText()
        SpecialCase = 'لا'
        if self.checkBox_47.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_161.text()
        NationalID = self.lineEdit_241.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_3st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_206.text()
        Gender = 'ولد'
        if self.radioButton_124.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_207.text()
        DOB = self.dateEdit_49.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_59.currentText()
        Phone = self.lineEdit_205.text()
        Study = self.comboBox_84.currentText()
        SpecialCase = 'لا'
        if self.checkBox_48.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_204.text()
        NationalID = self.lineEdit_242.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_4st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_210.text()
        Gender = 'ولد'
        if self.radioButton_126.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_211.text()
        DOB = self.dateEdit_50.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_60.currentText()
        Phone = self.lineEdit_209.text()
        Study = self.comboBox_85.currentText()
        SpecialCase = 'لا'
        if self.checkBox_49.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_208.text()
        NationalID = self.lineEdit_243.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_5st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_214.text()
        Gender = 'ولد'
        if self.radioButton_128.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_215.text()
        DOB = self.dateEdit_51.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_61.currentText()
        Phone = self.lineEdit_213.text()
        Study = self.comboBox_86.currentText()
        SpecialCase = 'لا'
        if self.checkBox_50.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_212.text()
        NationalID = self.lineEdit_244.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_6st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_218.text()
        Gender = 'ولد'
        if self.radioButton_130.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_219.text()
        DOB = self.dateEdit_52.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_62.currentText()
        Phone = self.lineEdit_217.text()
        Study = self.comboBox_87.currentText()
        SpecialCase = 'لا'
        if self.checkBox_51.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_216.text()
        NationalID = self.lineEdit_245.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_7st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_222.text()
        Gender = 'ولد'
        if self.radioButton_132.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_223.text()
        DOB = self.dateEdit_53.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_63.currentText()
        Phone = self.lineEdit_221.text()
        Study = self.comboBox_88.currentText()
        SpecialCase = 'لا'
        if self.checkBox_52.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_220.text()
        NationalID = self.lineEdit_246.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_8st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_226.text()
        Gender = 'ولد'
        if self.radioButton_134.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_227.text()
        DOB = self.dateEdit_54.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_89.currentText()
        Phone = self.lineEdit_225.text()
        Study = self.comboBox_90.currentText()
        SpecialCase = 'لا'
        if self.checkBox_53.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_224.text()
        NationalID = self.lineEdit_247.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_9st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_230.text()
        Gender = 'ولد'
        if self.radioButton_136.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_231.text()
        DOB = self.dateEdit_55.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_91.currentText()
        Phone = self.lineEdit_229.text()
        Study = self.comboBox_92.currentText()
        SpecialCase = 'لا'
        if self.checkBox_54.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_228.text()
        NationalID = self.lineEdit_248.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    def Record_10st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_164.text()
        Name = self.lineEdit_234.text()
        Gender = 'ولد'
        if self.radioButton_138.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_235.text()
        DOB = self.dateEdit_56.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_93.currentText()
        Phone = self.lineEdit_233.text()
        Study = self.comboBox_94.currentText()
        SpecialCase = 'لا'
        if self.checkBox_55.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_232.text()
        NationalID = self.lineEdit_249.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalID))
        db.commit()
        db.close()

    # Check Sons
    def On_Mouse_Click_in_1st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()
        SName = self.lineEdit_69.text()
        Study = self.comboBox_82.currentText()
        Job = self.comboBox_19.currentText()
        Phone = self.lineEdit_73.text()
        NationalID = self.lineEdit_71.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_2st_Son_Tab_FArmals()

    def On_Mouse_Click_in_1st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()
        SName = self.lineEdit_69.text()
        Study = self.comboBox_82.currentText()
        Job = self.comboBox_19.currentText()
        Phone = self.lineEdit_73.text()
        NationalID = self.lineEdit_71.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_2st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_163.text()
        Study = self.comboBox_83.currentText()
        Job = self.comboBox_48.currentText()
        Phone = self.lineEdit_162.text()
        NationalID = self.lineEdit_241.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_3st_Son_Tab_FArmals()

    def On_Mouse_Click_in_2st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_163.text()
        Study = self.comboBox_83.currentText()
        Job = self.comboBox_48.currentText()
        Phone = self.lineEdit_162.text()
        NationalID = self.lineEdit_241.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_3st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_206.text()
        Study = self.comboBox_84.currentText()
        Job = self.comboBox_59.currentText()
        Phone = self.lineEdit_205.text()
        NationalID = self.lineEdit_242.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_4st_Son_Tab_FArmals()

    def On_Mouse_Click_in_3st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_206.text()
        Study = self.comboBox_84.currentText()
        Job = self.comboBox_59.currentText()
        Phone = self.lineEdit_205.text()
        NationalID = self.lineEdit_242.text()


        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_4st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()
        SName = self.lineEdit_210.text()
        Study = self.comboBox_85.currentText()
        Job = self.comboBox_60.currentText()
        Phone = self.lineEdit_209.text()
        NationalID = self.lineEdit_243.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_5st_Son_Tab_FArmals()

    def On_Mouse_Click_in_4st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()
        SName = self.lineEdit_210.text()
        Study = self.comboBox_85.currentText()
        Job = self.comboBox_60.currentText()
        Phone = self.lineEdit_209.text()
        NationalID = self.lineEdit_243.text()

        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_5st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_214.text()
        Study = self.comboBox_86.currentText()
        Job = self.comboBox_61.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_6st_Son_Tab_FArmals()

    def On_Mouse_Click_in_5st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_214.text()
        Study = self.comboBox_86.currentText()
        Job = self.comboBox_61.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_6st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_218.text()
        Study = self.comboBox_87.currentText()
        Job = self.comboBox_62.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_7st_Son_Tab_FArmals()

    def On_Mouse_Click_in_6st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_218.text()
        Study = self.comboBox_87.currentText()
        Job = self.comboBox_62.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_7st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_222.text()
        Study = self.comboBox_88.currentText()
        Job = self.comboBox_63.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_8st_Son_Tab_FArmals()

    def On_Mouse_Click_in_7st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_222.text()
        Study = self.comboBox_88.currentText()
        Job = self.comboBox_63.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_8st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_226.text()
        Study = self.comboBox_90.currentText()
        Job = self.comboBox_89.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_9st_Son_Tab_FArmals()

    def On_Mouse_Click_in_8st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_226.text()
        Study = self.comboBox_90.currentText()
        Job = self.comboBox_89.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_9st_Son_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_230.text()
        Study = self.comboBox_92.currentText()
        Job = self.comboBox_91.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_10st_Son_Tab_FArmals()

    def On_Mouse_Click_in_9st_Sonn_MotherDeaddd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_230.text()
        Study = self.comboBox_92.currentText()
        Job = self.comboBox_91.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    def On_Mouse_Click_in_10st_Sonn_MotherDeadd(self):
        FName = self.lineEdit_164.text()
        MName = self.lineEdit_36.text()

        SName = self.lineEdit_234.text()
        Study = self.comboBox_94.currentText()
        Job = self.comboBox_94.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_120.setEnabled(True)

    # Checkes Sons Num Choices Father Armal
    def Choice_Son_Num_FArmals(self):
        self.Open_All_Buttons_Sons_FArmals()
        try:
            User_Choice = self.spinBox_11.value()
            if User_Choice == 0:
                self.tabWidget_8.setEnabled(False)
            if User_Choice == 1:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_61.setEnabled(False)
            if User_Choice == 2:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_77.setEnabled(False)

            elif User_Choice == 3:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_79.setEnabled(False)

            if User_Choice == 4:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_15.setEnabled(False)

            elif User_Choice == 5:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_16.setEnabled(False)
            if User_Choice == 6:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_17.setEnabled(False)

            if User_Choice == 7:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_18.setEnabled(False)

            if User_Choice == 8:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(False)

            if User_Choice == 9:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
                self.pushButton_20.setEnabled(False)

            if User_Choice == 10:

                self.tabWidget_8.setEnabled(True)
                self.tabWidget_8.setCurrentIndex(0)
            else:

                QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال عدد الابناء')
        except:
            pass
            '''QMessageBox.warning(QWidget(), "Error!!", 'You Should Add Sons Number.')'''

    # Checkes Record
    def Choice_Recoord_Sons_NumS_FArmals(self):
        try:
            User_Choice = self.spinBox_11.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.Record_1st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 2:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 3:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 4:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 5:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                self.Record_5st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 6:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                self.Record_5st_Son_Of_Mother_Dead()
                self.Record_6st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 7:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                self.Record_5st_Son_Of_Mother_Dead()
                self.Record_6st_Son_Of_Mother_Dead()
                self.Record_7st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 8:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                self.Record_5st_Son_Of_Mother_Dead()
                self.Record_6st_Son_Of_Mother_Dead()
                self.Record_7st_Son_Of_Mother_Dead()
                self.Record_8st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 9:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                self.Record_5st_Son_Of_Mother_Dead()
                self.Record_6st_Son_Of_Mother_Dead()
                self.Record_7st_Son_Of_Mother_Dead()
                self.Record_8st_Son_Of_Mother_Dead()
                self.Record_9st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 10:
                self.Record_1st_Son_Of_Mother_Dead()
                self.Record_2st_Son_Of_Mother_Dead()
                self.Record_3st_Son_Of_Mother_Dead()
                self.Record_4st_Son_Of_Mother_Dead()
                self.Record_5st_Son_Of_Mother_Dead()
                self.Record_6st_Son_Of_Mother_Dead()
                self.Record_7st_Son_Of_Mother_Dead()
                self.Record_8st_Son_Of_Mother_Dead()
                self.Record_9st_Son_Of_Mother_Dead()
                self.Record_10st_Son_Of_Mother_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            else:
                QMessageBox.information(QWidget(), "للاسف!!",
                                        'رجاء التاكد من بيانات الاب والاو والابناء        ')
        except:
            pass

    # Checks Sons Tab For Open
    def Check_On_Click_Sons_Tabl_FArmals(self):
        try:
            User_Choice = self.spinBox_11.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.On_Mouse_Click_in_1st_Sonn_MotherDeaddd()
            elif User_Choice == 2:
                self.On_Mouse_Click_in_2st_Sonn_MotherDeaddd()
            elif User_Choice == 3:
                self.On_Mouse_Click_in_3st_Sonn_MotherDeaddd()
            elif User_Choice == 4:
                self.On_Mouse_Click_in_4st_Sonn_MotherDeaddd()
            elif User_Choice == 5:
                self.On_Mouse_Click_in_5st_Sonn_MotherDeaddd()
            elif User_Choice == 6:
                self.On_Mouse_Click_in_6st_Sonn_MotherDeaddd()
            elif User_Choice == 7:
                self.On_Mouse_Click_in_7st_Sonn_MotherDeaddd()
            elif User_Choice == 8:
                self.On_Mouse_Click_in_8st_Sonn_MotherDeaddd()
            elif User_Choice == 9:
                self.On_Mouse_Click_in_9st_Sonn_MotherDeaddd()
            elif User_Choice == 10:
                self.On_Mouse_Click_in_10st_Sonn_MotherDeaddd()
        except:
            pass

    # Make All Button Aviable
    def Open_All_Buttons_Sons_FArmals(self):
        self.pushButton_61.setEnabled(True)
        self.pushButton_77.setEnabled(True)
        self.pushButton_79.setEnabled(True)
        self.pushButton_81.setEnabled(True)
        self.pushButton_83.setEnabled(True)
        self.pushButton_111.setEnabled(True)
        self.pushButton_113.setEnabled(True)
        self.pushButton_115.setEnabled(True)
        self.pushButton_117.setEnabled(True)

    # Clean
    def Clear_All_LineEdits_Of_Family_FArmals(self):
        self.tabWidget_8.setEnabled(False)
        self.tabWidget_8.setCurrentIndex(0)
        self.lineEdit_36.setText('')
        self.lineEdit_164.setText('')
        self.lineEdit_270.setText('')
        self.comboBox_65.setCurrentIndex(0)
        self.comboBox_64.setCurrentIndex(0)
        self.lineEdit_166.setText('')
        self.lineEdit_236.setText('')
        self.lineEdit_202.setText('')
        self.lineEdit_237.setText('')
        self.spinBox_11.setValue(0)
        self.lineEdit_159.setText('')
        self.lineEdit_158.setText('')
        # 1 son
        self.lineEdit_69.setText('')
        self.lineEdit_71.setText('')
        self.lineEdit_70.setText('')
        self.comboBox_82.setCurrentIndex(0)
        self.lineEdit_73.setText('')
        self.comboBox_19.setCurrentIndex(0)
        self.lineEdit_160.setText('')
        # 2 son
        self.lineEdit_163.setText('')
        self.lineEdit_241.setText('')
        self.lineEdit_203.setText('')
        self.comboBox_83.setCurrentIndex(0)
        self.lineEdit_162.setText('')
        self.comboBox_48.setCurrentIndex(0)
        self.lineEdit_161.setText('')
        # 3 son
        self.lineEdit_206.setText('')
        self.lineEdit_242.setText('')
        self.lineEdit_207.setText('')
        self.comboBox_84.setCurrentIndex(0)
        self.lineEdit_205.setText('')
        self.comboBox_59.setCurrentIndex(0)
        self.lineEdit_204.setText('')
        # 4 son
        self.lineEdit_210.setText('')
        self.lineEdit_243.setText('')
        self.lineEdit_211.setText('')
        self.comboBox_85.setCurrentIndex(0)
        self.lineEdit_209.setText('')
        self.comboBox_60.setCurrentIndex(0)
        self.lineEdit_208.setText('')
        # 5 son
        self.lineEdit_214.setText('')
        self.lineEdit_215.setText('')
        self.lineEdit_244.setText('')
        self.comboBox_86.setCurrentIndex(0)
        self.lineEdit_213.setText('')
        self.comboBox_61.setCurrentIndex(0)
        self.lineEdit_212.setText('')
        # 6 son
        self.lineEdit_218.setText('')
        self.lineEdit_245.setText('')
        self.lineEdit_219.setText('')
        self.comboBox_87.setCurrentIndex(0)
        self.lineEdit_217.setText('')
        self.comboBox_62.setCurrentIndex(0)
        self.lineEdit_216.setText('')
        # 7 son
        self.lineEdit_222.setText('')
        self.lineEdit_223.setText('')
        self.lineEdit_246.setText('')
        self.comboBox_88.setCurrentIndex(0)
        self.lineEdit_221.setText('')
        self.comboBox_63.setCurrentIndex(0)
        self.lineEdit_220.setText('')
        # 8 son
        self.lineEdit_226.setText('')
        self.lineEdit_247.setText('')
        self.lineEdit_227.setText('')
        self.comboBox_90.setCurrentIndex(0)
        self.lineEdit_225.setText('')
        self.comboBox_89.setCurrentIndex(0)
        self.lineEdit_224.setText('')
        # 9 son
        self.lineEdit_230.setText('')
        self.lineEdit_248.setText('')
        self.lineEdit_231.setText('')
        self.comboBox_92.setCurrentIndex(0)
        self.lineEdit_229.setText('')
        self.comboBox_91.setCurrentIndex(0)
        self.lineEdit_228.setText('')
        # 10 Son
        self.lineEdit_234.setText('')
        self.lineEdit_235.setText('')
        self.lineEdit_249.setText('')
        self.comboBox_94.setCurrentIndex(0)
        self.lineEdit_233.setText('')
        self.comboBox_93.setCurrentIndex(0)
        self.lineEdit_232.setText('')

    '''============================== Father Dead Tab ====================================='''

    # Mother Armals

    def Close_program(self):
        sys.exit()

    # Record Mother Armal
    def Record_Mother_ArmalS(self):
        Name = self.lineEdit_155.text()
        Ssn = self.lineEdit_154.text()
        Leader = 'نعم'
        Qulified = self.lineEdit_152.text()
        Father = self.lineEdit_200.text()
        Work = self.comboBox_58.currentText()
        Age = self.dateEdit_36.date()
        Age = Age.toPyDate()
        Phone = self.lineEdit_156.text()
        Special = 'لا'
        if self.checkBox_25.isChecked():
            Special = 'نعم'
        Type = self.lineEdit_153.text()
        Address = self.lineEdit_201.text()
        Street = self.comboBox_57.currentText()
        Fphone = '---------'
        FSsn =   '---------'
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        if self.lineEdit_35.text() == '':
            FName='----------'
        else:
            FName = 'المرحوم/' + str(self.lineEdit_35.text())
        ChildNum = self.spinBox_10.value()
        FamilyNum = int(self.spinBox_10.value()) + 1
        Stutus = 'ارمله'
        if self.radioButton_103.isChecked():
            Stutus = 'عزباء'
            self.lineEdit_35.setText('----------')
        ProgramNum = self.lineEdit_269.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Mother VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (Name, Ssn, Leader, Qulified, Father, Work, Age, Phone, Special, Type, Address, Street, FSsn, FName,
                   Fphone, ChildNum, Stutus, FamilyNum, ProgramNum))
        db.commit()
        db.close()
        QMessageBox.information(QWidget(), "جيد", 'تمت حفظ بيانات الام بنجاح')




    # Check Mother Armal Data
    def Check_Mother_Armal(self):
        Name = self.lineEdit_155.text()
        FName = self.lineEdit_35.text()
        Qulified = self.lineEdit_152.text()
        Street = self.comboBox_57.currentText()
        Address = self.lineEdit_201.text()
        Work = self.comboBox_58.currentText()
        Ssn = self.lineEdit_154.text()
        Phone = self.lineEdit_156.text()
        Age = 'x'
        if Name == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم رب الاسرة  ')
        if Address == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال العنوان  ')
        if Qulified == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال المؤهل   ')
        if Work == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم العمل  ')
        if Street == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الشارع  ')
        if Phone.isdigit():
            pass
        else:
            QMessageBox.information(self, 'رجاءا', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه')
        if Ssn.isdigit():
            pass
        else:
            QMessageBox.information(self, 'رجاءا', 'تاكد من ادخال الرقم القومي بطريقه صحيحه')

        if Name != '' and Street != '' and Address != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Phone) == 11 and len(Ssn) == 14 :
            if self.spinBox_10.value() == 0 and Name != '' and Street != '' and Address != '' and Qulified != '' and Work != '' and Phone.isdigit() and Ssn.isdigit() and len(Phone) == 11 and len(Ssn) == 14:
                self.tabWidget_7.setEnabled(False)
                Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من عدد الابناء ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes:
                    Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                                     QMessageBox.Yes | QMessageBox.No)
                    if Replay == QMessageBox.Yes:
                        self.pushButton_100.setEnabled(True)
            else:
                self.Choice_Son_Num_MArmals()
        else:
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال التاكد ان اللاقم القومي 14 رقم والموبيل 11 رقم  ')


    # Record Sons
    def Record_1st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_67.text()
        Gender = 'ولد'
        if self.radioButton_38.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_68.text()
        DOB = self.dateEdit_16.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_18.currentText()
        Phone = self.lineEdit_72.text()
        Study = self.comboBox_69.currentText()
        SpecialCase = 'لا'
        if self.checkBox_7.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_118.text()
        NationalId = self.lineEdit_74.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_2st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_121.text()
        Gender = 'ولد'
        if self.radioButton_104.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_167.text()
        DOB = self.dateEdit_39.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_31.currentText()
        Phone = self.lineEdit_120.text()
        Study = self.comboBox_70.currentText()
        SpecialCase = 'لا'
        if self.checkBox_38.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_119.text()
        NationalId = self.lineEdit_250.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_3st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_170.text()
        Gender = 'ولد'
        if self.radioButton_106.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_171.text()
        DOB = self.dateEdit_40.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_32.currentText()
        Phone = self.lineEdit_169.text()
        Study = self.comboBox_71.currentText()
        SpecialCase = 'لا'
        if self.checkBox_39.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_168.text()
        NationalId = self.lineEdit_251.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_4st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_174.text()
        Gender = 'ولد'
        if self.radioButton_108.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_175.text()
        DOB = self.dateEdit_41.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_33.currentText()
        Phone = self.lineEdit_173.text()
        Study = self.comboBox_72.currentText()
        SpecialCase = 'لا'
        if self.checkBox_40.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_172.text()
        NationalId = self.lineEdit_252.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_5st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_178.text()
        Gender = 'ولد'
        if self.radioButton_110.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_179.text()
        DOB = self.dateEdit_42.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_34.currentText()
        Phone = self.lineEdit_177.text()
        Study = self.comboBox_73.currentText()
        SpecialCase = 'لا'
        if self.checkBox_41.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_176.text()
        NationalId = self.lineEdit_253.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_6st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_182.text()
        Gender = 'ولد'
        if self.radioButton_112.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_183.text()
        DOB = self.dateEdit_43.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_35.currentText()
        Phone = self.lineEdit_181.text()
        Study = self.comboBox_74.currentText()
        SpecialCase = 'لا'
        if self.checkBox_42.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_180.text()
        NationalId = self.lineEdit_254.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_7st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_186.text()
        Gender = 'ولد'
        if self.radioButton_114.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_187.text()
        DOB = self.dateEdit_44.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_36.currentText()
        Phone = self.lineEdit_185.text()
        Study = self.comboBox_75.currentText()
        SpecialCase = 'لا'
        if self.checkBox_43.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_184.text()
        NationalId = self.lineEdit_255.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_8st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_190.text()
        Gender = 'ولد'
        if self.radioButton_116.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_191.text()
        DOB = self.dateEdit_45.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_76.currentText()
        Phone = self.lineEdit_189.text()
        Study = self.comboBox_77.currentText()
        SpecialCase = 'لا'
        if self.checkBox_44.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_188.text()
        NationalId = self.lineEdit_256.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_9st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_194.text()
        Gender = 'ولد'
        if self.radioButton_118.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_195.text()
        DOB = self.dateEdit_46.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_78.currentText()
        Phone = self.lineEdit_193.text()
        Study = self.comboBox_79.currentText()
        SpecialCase = 'لا'
        if self.checkBox_45.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_192.text()
        NationalId = self.lineEdit_257.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    def Record_10st_Son_Of_Father_Dead(self):
        MName = self.lineEdit_155.text()
        FName = 'المرحوم' + '/' + str(self.lineEdit_35.text())
        Name = self.lineEdit_198.text()
        Gender = 'ولد'
        if self.radioButton_120.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_199.text()
        DOB = self.dateEdit_47.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_80.currentText()
        Phone = self.lineEdit_197.text()
        Study = self.comboBox_81.currentText()
        SpecialCase = 'لا'
        if self.checkBox_46.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_196.text()
        NationalId = self.lineEdit_258.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO Sons VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type, NationalId))
        db.commit()
        db.close()

    # Check Sons
    def On_Mouse_Click_in_1st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_67.text()
        Study = self.comboBox_69.currentText()
        Job = self.comboBox_18.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_2st_Son_Tab_MArmals()

    def On_Mouse_Click_in_1st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_67.text()
        Study = self.comboBox_69.currentText()
        Job = self.comboBox_18.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_2st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_121.text()
        Study = self.comboBox_70.currentText()
        Job = self.comboBox_31.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_3st_Son_Tab_MArmals()

    def On_Mouse_Click_in_2st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_121.text()
        Study = self.comboBox_70.currentText()
        Job = self.comboBox_31.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_3st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_170.text()
        Study = self.comboBox_71.currentText()
        Job = self.comboBox_32.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_4st_Son_Tab_MArmals()

    def On_Mouse_Click_in_3st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_170.text()
        Study = self.comboBox_71.currentText()
        Job = self.comboBox_32.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_4st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_174.text()
        Study = self.comboBox_72.currentText()
        Job = self.comboBox_33.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_5st_Son_Tab_MArmals()

    def On_Mouse_Click_in_4st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_174.text()
        Study = self.comboBox_72.currentText()
        Job = self.comboBox_33.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_5st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_178.text()
        Study = self.comboBox_73.currentText()
        Job = self.comboBox_34.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_6st_Son_Tab_MArmals()

    def On_Mouse_Click_in_5st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_178.text()
        Study = self.comboBox_73.currentText()
        Job = self.comboBox_34.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_6st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_182.text()
        Study = self.comboBox_74.currentText()
        Job = self.comboBox_35.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_7st_Son_Tab_MArmals()

    def On_Mouse_Click_in_6st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_182.text()
        Study = self.comboBox_74.currentText()
        Job = self.comboBox_35.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_7st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_186.text()
        Study = self.comboBox_75.currentText()
        Job = self.comboBox_36.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_8st_Son_Tab_MArmals()

    def On_Mouse_Click_in_7st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_186.text()
        Study = self.comboBox_75.currentText()
        Job = self.comboBox_36.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_8st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_190.text()
        Study = self.comboBox_77.currentText()
        Job = self.comboBox_76.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_9st_Son_Tab_MArmals()

    def On_Mouse_Click_in_8st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_190.text()
        Study = self.comboBox_77.currentText()
        Job = self.comboBox_76.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_9st_Son_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_194.text()
        Study = self.comboBox_79.currentText()
        Job = self.comboBox_78.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_10st_Son_Tab_MArmals()

    def On_Mouse_Click_in_9st_Sonn_FatherDeaddd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        SName = self.lineEdit_194.text()
        Study = self.comboBox_79.currentText()
        Job = self.comboBox_78.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    def On_Mouse_Click_in_10st_Sonn_FatherDeadd(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_198.text()
        Study = self.comboBox_81.currentText()
        Job = self.comboBox_80.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)

    # Checkes Sons Num Choices Father Armal
    def Choice_Son_Num_MArmals(self):
        try:
            User_Choice = self.spinBox_10.value()
            if User_Choice == 0:
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(False)
            elif User_Choice == 1:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_60.setEnabled(False)
            elif User_Choice == 2:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_69.setEnabled(False)

            elif User_Choice == 3:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_71.setEnabled(False)

            elif User_Choice == 4:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_73.setEnabled(False)

            elif User_Choice == 5:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_75.setEnabled(False)
            elif User_Choice == 6:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_101.setEnabled(False)

            elif User_Choice == 7:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_104.setEnabled(False)

            elif User_Choice == 8:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_106.setEnabled(False)

            elif User_Choice == 9:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
                self.pushButton_108.setEnabled(False)

            elif User_Choice == 10:
                self.Open_All_Buttons_Sons_MArmals()
                self.tabWidget_7.setEnabled(True)
                self.tabWidget_7.setCurrentIndex(0)
            else:
                QMessageBox.information(QWidget(), "للاسف!!", 'عدد الابناء المتاح فقط 10 ابناء ')
        except:
            pass
            '''QMessageBox.warning(QWidget(), "Error!!", 'You Should Add Sons Number.')'''

    # Checkes Record
    def Choice_Recoord_Sons_NumS_MArmals(self):
        try:
            User_Choice = self.spinBox_10.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.Record_1st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
               # self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 2:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
               # QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 3:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                #self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 4:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
               # self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 5:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
               # self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 6:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
               # self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 7:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                #self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 8:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                self.Record_8st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
                #self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 9:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                self.Record_8st_Son_Of_Father_Dead()
                self.Record_9st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
               # self.Clear_All_LineEdits_Of_Family_MArmals()
            elif User_Choice == 10:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                self.Record_8st_Son_Of_Father_Dead()
                self.Record_9st_Son_Of_Father_Dead()
                self.Record_10st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
              #  self.Clear_All_LineEdits_Of_Family_MArmals()
            else:
                QMessageBox.information(QWidget(), "للاسف!!",
                                        'رجاء التاكد من بيانات الاب والاو والابناء        ')
        except:
            pass

    # Checks Sons Tab For Open
    def Check_On_Click_Sons_Tabl_MArmals(self):
        try:
            User_Choice = self.spinBox_10.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.On_Mouse_Click_in_1st_Sonn_FatherDeaddd()
            elif User_Choice == 2:
                self.On_Mouse_Click_in_2st_Sonn_FatherDeaddd()
            elif User_Choice == 3:
                self.On_Mouse_Click_in_3st_Sonn_FatherDeaddd()
            elif User_Choice == 4:
                self.On_Mouse_Click_in_4st_Sonn_FatherDeaddd()
            elif User_Choice == 5:
                self.On_Mouse_Click_in_5st_Sonn_FatherDeaddd()
            elif User_Choice == 6:
                self.On_Mouse_Click_in_6st_Sonn_FatherDeaddd()
            elif User_Choice == 7:
                self.On_Mouse_Click_in_7st_Sonn_FatherDeaddd()
            elif User_Choice == 8:
                self.On_Mouse_Click_in_8st_Sonn_FatherDeaddd()
            elif User_Choice == 9:
                self.On_Mouse_Click_in_9st_Sonn_FatherDeaddd()
            elif User_Choice == 10:
                self.On_Mouse_Click_in_10st_Sonn_FatherDeaddd()
        except:
            pass

    # Make All Button Aviable
    def Open_All_Buttons_Sons_MArmals(self):
        self.pushButton_60.setEnabled(True)
        self.pushButton_69.setEnabled(True)
        self.pushButton_71.setEnabled(True)
        self.pushButton_73.setEnabled(True)
        self.pushButton_75.setEnabled(True)
        self.pushButton_101.setEnabled(True)
        self.pushButton_104.setEnabled(True)
        self.pushButton_106.setEnabled(True)
        self.pushButton_108.setEnabled(True)

    # Clean
    def Clear_All_LineEdits_Of_Family_MArmals(self):
        self.tabWidget_7.setEnabled(False)
        self.tabWidget_7.setCurrentIndex(0)
        self.pushButton_100.setEnabled(False)
        self.lineEdit_35.setText('')
        self.lineEdit_269.setText('')
        self.lineEdit_155.setText('')
        self.comboBox_57.setCurrentIndex(0)
        self.comboBox_58.setCurrentIndex(0)
        self.lineEdit_154.setText('')
        self.lineEdit_152.setText('')
        self.lineEdit_200.setText('')
        self.lineEdit_201.setText('')
        self.spinBox_10.setValue(0)
        self.lineEdit_156.setText('')
        self.lineEdit_153.setText('')
        # 1 son
        self.lineEdit_67.setText('')
        self.lineEdit_74.setText('')
        self.lineEdit_68.setText('')
        self.comboBox_69.setCurrentIndex(0)
        self.lineEdit_72.setText('')
        self.comboBox_18.setCurrentIndex(0)
        self.lineEdit_118.setText('')
        # 2 son
        self.lineEdit_121.setText('')
        self.lineEdit_250.setText('')
        self.lineEdit_167.setText('')
        self.comboBox_70.setCurrentIndex(0)
        self.lineEdit_120.setText('')
        self.comboBox_31.setCurrentIndex(0)
        self.lineEdit_119.setText('')
        # 3 son
        self.lineEdit_170.setText('')
        self.lineEdit_251.setText('')
        self.lineEdit_171.setText('')
        self.comboBox_71.setCurrentIndex(0)
        self.lineEdit_169.setText('')
        self.comboBox_32.setCurrentIndex(0)
        self.lineEdit_168.setText('')
        # 4 son
        self.lineEdit_174.setText('')
        self.lineEdit_252.setText('')
        self.lineEdit_175.setText('')
        self.comboBox_72.setCurrentIndex(0)
        self.lineEdit_173.setText('')
        self.comboBox_33.setCurrentIndex(0)
        self.lineEdit_172.setText('')
        # 5 son
        self.lineEdit_178.setText('')
        self.lineEdit_253.setText('')
        self.lineEdit_179.setText('')
        self.comboBox_73.setCurrentIndex(0)
        self.lineEdit_177.setText('')
        self.comboBox_34.setCurrentIndex(0)

        # 6 son
        self.lineEdit_182.setText('')
        self.lineEdit_254.setText('')
        self.lineEdit_183.setText('')
        self.comboBox_74.setCurrentIndex(0)
        self.lineEdit_181.setText('')
        self.comboBox_35.setCurrentIndex(0)
        self.lineEdit_180.setText('')
        # 7 son
        self.lineEdit_186.setText('')
        self.lineEdit_255.setText('')
        self.lineEdit_187.setText('')
        self.comboBox_75.setCurrentIndex(0)
        self.lineEdit_185.setText('')
        self.comboBox_36.setCurrentIndex(0)
        self.lineEdit_184.setText('')
        # 8 son
        self.lineEdit_190.setText('')
        self.lineEdit_256.setText('')
        self.lineEdit_191.setText('')
        self.comboBox_77.setCurrentIndex(0)
        self.lineEdit_189.setText('')
        self.comboBox_76.setCurrentIndex(0)
        self.lineEdit_188.setText('')
        # 9 son
        self.lineEdit_194.setText('')
        self.lineEdit_257.setText('')
        self.lineEdit_195.setText('')
        self.comboBox_79.setCurrentIndex(0)
        self.lineEdit_193.setText('')
        self.comboBox_78.setCurrentIndex(0)
        self.lineEdit_192.setText('')
        # 10 Son
        self.lineEdit_198.setText('')
        self.lineEdit_258.setText('')
        self.lineEdit_199.setText('')
        self.comboBox_81.setCurrentIndex(0)
        self.lineEdit_197.setText('')
        self.comboBox_80.setCurrentIndex(0)
        self.lineEdit_196.setText('')


    ''' Search Family Tab '''

    # Show Fathers Data
    def Search_Family_Data(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        Name = ''
        query = '''
        SELECT Name ,MName,Stutus,Work,Phone,Father,Street,Address,Sons,FamilyNum from Father WHERE Stutus=? and Not Name =? order by Name
        '''
        Stutus = 'متزوج'
        Result = conect.execute(query, [(Stutus), (Name)])
        Z = Result.fetchall()
        query = '''
        SELECT Name ,MName,Stutus,Work,Phone,Father,Street,Address,Sons,FamilyNum from Father WHERE Stutus=? order by Name
        '''
        Stutue = 'ارمل'
        Result = conect.execute(query, [(Stutue)])
        X = Result.fetchall()

        query = '''
        SELECT Name ,FName,Stutus,Work,Phone,Father,Street,Address,ChildNum,FamilyNum from Mother WHERE Stutus=? order by Name
        '''
        Stutue = 'ارمله'
        Result = conect.execute(query, [(Stutue)])
        Y = Result.fetchall()

        Result = Z + X + Y
        self.tableWidget_4.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_4.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Show Sons Data
    def Search_Sons_Data(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Name , FName  , Study , DOB , Work  FROM Sons order by FName
        '''
        Result = conect.execute(query)
        Result = Result.fetchall()
        p = len(Result)
        for i in Result:
            d = i[3]
            d1 = list(filter(None, d.split('-')))
            d2 = d1[0]
            named_tuple = time.localtime()
            d3 = time.strftime(d2, named_tuple)
            named_tuple = time.localtime()
            time_string = time.strftime("%Y", named_tuple)
            f = int(time_string)
            g = f - int(d3)
            z = i[1]
            z = g
            y = [((i[0]), (i[1]), (i[2]), (z), (i[4]))]
            Result = Result + y
            self.tableWidget_5.setRowCount(0)
            for row_number, row_data in enumerate(Result[p:]):
                self.tableWidget_5.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_5.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Print Fathers Data
    def Report_Fathers_Data(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_4.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Print Sons Data
    def Report_Sons_Data(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_5.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    '''Search Special Num Of Family Tab'''

    def Search_Num_Family(self):
        From = self.spinBox_2.value()
        To = self.spinBox.value()
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Name ,MName,Phone,Street,Address,Stutus,Sons,FamilyNum from Father WHERE FamilyNum BETWEEN ? and ? 
        '''
        Result = conect.execute(query, [(From), (To)])
        X = Result.fetchall()
        query = '''
        SELECT Name ,FName,Phone,Street,Address,Stutus,ChildNum,FamilyNum from Mother WHERE  FamilyNum BETWEEN ? and ? 
        '''
        Result = conect.execute(query, [(From), (To)])
        Y = Result.fetchall()
        Result = X + Y
        self.tableWidget_23.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_23.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_23.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Clear Spains Boxes
    def Clear_SpainBoxes(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)

    # Report Special Family Num
    def Report_Special_Num_FamIly(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_23.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    '''Add Sons Data'''

    # Add Son Data
    def Add_Sons(self):
        Name = self.lineEdit_7.text()
        Father = self.lineEdit_18.text()
        Phone = self.lineEdit_17.text()
        Type = self.lineEdit_19.text()
        FName = self.comboBox_20.currentText()
        MName = self.lineEdit_10.text()
        Study = self.comboBox_67.currentText()
        Work = self.comboBox_66.currentText()
        Gender = 'ولد'
        NationalId = self.lineEdit_27.text()
        if self.radioButton_3.isChecked():
            Gender = 'بنت'
        DOB = self.dateEdit.date()
        DOB = DOB.toPyDate()
        Stutus = 'لا'
        if self.checkBox_4.isChecked():
            Stutus = 'نعم'
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'insert into Sons VALUES(?,?,?,?,?,?,?,?,?,?,?)'
        x = c.execute(sql,
                      [(MName), (FName), (Name), (Gender), (Father), (Study), (DOB), (Work), (Phone), (Stutus), (Type),
                       (NationalId)])
        db.commit()
        db.close()
        self.Add_Sum_Child_Nums()
        self.Show_Added_Sons()
        self.Clear_Sons_LineEdits()

    # Read Mother Data From Father Combo Box
    def Read_Mother_Name_From_FComboBox(self):
        Name = self.comboBox_20.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Select MName from Father Where Name = ?'
        x = c.execute(Sql, [(Name)])
        Result = x.fetchall()
        MName = str(Result[0][0])
        self.lineEdit_10.setText(MName)
        db.commit()
        db.close()

    # Read Father Data From DB
    def Read_Father_Name_From_TableDB(self):
        Stutus = 'متزوج'
        self.comboBox_20.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Select Name from Father where Stutus = ?'
        x = c.execute(Sql, [(Stutus)])
        Result = x.fetchall()
        db.commit()
        db.close()
        for i in Result:
            self.comboBox_20.addItem(str(i[0]))

    # Check Sons Data
    def Check_Add_Sons(self):
        NameOfFather = self.comboBox_20.currentText()
        NameOfMother = self.lineEdit_10.text()
        Name = self.lineEdit_7.text()
        Age = self.dateEdit.date()
        Age = Age.toPyDate()
        Study = self.comboBox_67.currentText()
        Job = self.comboBox_66.currentText()
        Phone = self.lineEdit_17.text()
        NationalId = self.lineEdit_27.text()
        if Phone.isdigit():
            QMessageBox.information(self, 'success', 'تم ادخال رقم الهاتف بطريقه صحيحه')
        else:
            QMessageBox.warning(self, 'failed', 'تاكد من ادخال رقم الهاتف بطرقه صحيحه')
        if NationalId.isdigit():
            QMessageBox.information(self, 'success', 'تم ادخال الرقم القومي بنجاح')
        else:
            QMessageBox.warning(self, 'failed', 'تاكد من ادخال الرقم القومي بطريقه صحيحه')
        if Name == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من الابن   ')
        if NameOfFather == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من اسم الاب  ')
        # if NameOfMother == '':
        # QMessageBox.information(self, 'برجاء', 'يرجي التاكد من اسم الام  ')
        if Job == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من العمل   ')
        if Study == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من الدراسه   ')
        if Age != '' and Name != '' and NameOfFather != '' and '''NameOfMother !='' ''' and Job != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_125.setEnabled(True)

    # Show Sons Data
    def Show_Added_Sons(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name ,FName , MName from Sons')
        Result = c.fetchall()
        db.commit()
        self.tableWidget_22.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_22.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_22.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Clear Line Eidts
    def Clear_Sons_LineEdits(self):
        self.lineEdit_7.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_18.setText('')
        self.lineEdit_17.setText('')
        self.comboBox_20.setCurrentIndex(0)
        self.lineEdit_19.setText('')
        self.comboBox_67.setCurrentIndex(0)
        self.comboBox_66.setCurrentIndex(0)
        self.pushButton_125.setEnabled(False)

    #  Add Children Num Adding +
    def Add_Sum_Child_Nums(self):
        Name = self.comboBox_20.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Select Sons from Father Where Name = ?'
        x = c.execute(Sql, [(Name)])
        Result = x.fetchall()
        db.commit()
        db.close()
        Num = Result[0][0]
        Sum = Num
        Sum = int(Sum) + int(1)
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'UPDATE Father set Sons = ? Where Name = ?'
        x = c.execute(Sql, [(Sum), (Name)])
        Sum = Sum + int(2)
        Sql = 'UPDATE Father set FamilyNum = ? Where Name = ?'
        d = c.execute(Sql, [(Sum), (Name)])
        db.commit()
        db.close()

    '''Add Work , Serve , Study  Tab'''

    # Show Father Works
    def Show_Father_Works(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Work  FROM WorkF order by Work
        '''
        Result = conect.execute(query)
        self.tableWidget_29.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_29.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_29.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Add Work For Father
    def Add_Father_Work(self):
        Work = self.lineEdit_20.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'insert into WorkF values(?)'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()
        self.Show_Father_Works()

    # Confirm Add Father Work
    def Confirm_Add_FWork(self):
        Work = self.lineEdit_20.text()
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من اسم الوظيفه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and Work != '':
            self.Add_Father_Work()
            QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح')
            self.Clear_FLineEdit()
            self.Show_Father_Works()
        else:
            pass

    # Clear Father Line Edit
    def Clear_FLineEdit(self):
        self.lineEdit_20.setText('')

    # Delete Father Work
    def Delete_Special_FWork(self):
        Work = self.tableWidget_29.item(self.tableWidget_29.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Delete from WorkF Where Work =?'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()

    # Confirm Delete Father Work
    def Confirm_Delete_FWork(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف اسم الوظيفه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Special_FWork()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            self.Show_Father_Works()

    # Show Mother Works
    def Show_Mother_Works(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Work  FROM WorkM order by Work
        '''
        Result = conect.execute(query)
        self.tableWidget_24.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_24.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_24.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Add Work For Mother
    def Add_Mother_Work(self):
        Work = self.lineEdit_21.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'insert into WorkM values(?)'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()

    # Confirm Add Mother Work
    def Confirm_Add_MWork(self):
        Work = self.lineEdit_21.text()
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من اسم الوظيفه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and Work != '':
            self.Add_Mother_Work()
            QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح')
            self.Clear_MLineEdit()
            self.Show_Mother_Works()
        else:
            pass

    # Clear Father Line Edit
    def Clear_MLineEdit(self):
        self.lineEdit_21.setText('')

    # Show Sons Works
    def Show_Sons_Works(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Work FROM WorkS order by Work
        '''
        Result = conect.execute(query)
        self.tableWidget_25.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_25.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_25.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Delete Mother Work
    def Delete_Special_MWork(self):
        Work = self.tableWidget_24.item(self.tableWidget_24.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Delete from WorkM Where Work =?'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()

    # Confirm Delete Mother Work
    def Confirm_Delete_MWork(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف اسم الوظيفه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Special_MWork()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            self.Show_Mother_Works()

    # Add Work Son
    def Add_Sons_Work(self):
        Work = self.lineEdit_22.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'insert into WorkS values(?)'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()

    # Confirm Add Sons Work
    def Confirm_Add_SWork(self):
        Work = self.lineEdit_22.text()
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من اسم الوظيفه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and Work != '':
            self.Add_Sons_Work()
            QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح')
            self.Clear_SLineEdit()
            self.Show_Sons_Works()
        else:
            pass

    # Clear Sons Line Edit
    def Clear_SLineEdit(self):
        self.lineEdit_22.setText('')

    # Delete Son Work
    def Delete_Special_SWork(self):
        Work = self.tableWidget_25.item(self.tableWidget_25.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Delete from WorkS Where Work =?'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()

    # Confirm Delete Son Work
    def Confirm_Delete_SWork(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف اسم الوظيفه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Special_SWork()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            self.Show_Sons_Works()

    # Show Sons Study
    def Show_Sons_Study(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Study  FROM StudyS order by Study
        '''
        Result = conect.execute(query)
        self.tableWidget_30.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_30.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_30.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Add Study
    def Add_Sons_Study(self):
        Work = self.lineEdit_239.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'insert into StudyS values(?)'
        x = c.execute(Sql, [Work])
        db.commit()
        db.close()

    # Confirm Add Sons Study
    def Confirm_Add_SStudy(self):
        Work = self.lineEdit_239.text()
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من اسم الدراسه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and Work != '':
            self.Add_Sons_Study()
            QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح')
            self.Clear_SLineEditStudy()
            self.Show_Sons_Study()
        else:
            pass

    # Clear Sons Line Edit
    def Clear_SLineEditStudy(self):
        self.lineEdit_239.setText('')

    # Delete Study
    def Delete_Special_Study(self):
        Study = self.tableWidget_30.item(self.tableWidget_30.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Delete from StudyS Where Study =?'
        x = c.execute(Sql, [Study])
        db.commit()
        db.close()

    # Confirm Delete Study
    def Confirm_Delete_Study(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف اسم الدراسة ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Special_Study()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            self.Show_Sons_Study()

    # Show All Streets
    def Show_Streets(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Street FROM StreetList
        '''
        Result = conect.execute(query)
        self.tableWidget_31.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_31.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_31.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Add Street
    def Add_Streets(self):
        Street = self.lineEdit_238.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'insert into StreetList values(?)'
        x = c.execute(Sql, [Street])
        db.commit()
        db.close()

    # Confirm Add  Streets
    def Confirm_Add_Streets(self):
        Street = self.lineEdit_238.text()
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من اسم الشارع ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and Street != '':
            self.Add_Streets()
            QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح')
            self.Clear_SLineEditStreets()
            self.Show_Streets()
        else:
            pass

    # Clear Line Edit Streets
    def Clear_SLineEditStreets(self):
        self.lineEdit_238.setText('')

    # Delete Street
    def Delete_Special_Street(self):
        Street = self.tableWidget_31.item(self.tableWidget_31.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Delete from StreetList Where Street =?'
        x = c.execute(Sql, [Street])
        db.commit()
        db.close()

    # Confirm Delete Serve
    def Confirm_Delete_Street(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف اسم الشارع ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Special_Street()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            self.Show_Streets()

    # Show All Serves Added
    def Show_Added_Serves(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Serve FROM Serves order by Serve
        '''
        Result = conect.execute(query)
        self.tableWidget_32.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_32.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_32.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Add Serve
    def Add_Serveses(self):
        Serve = self.lineEdit_240.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'insert into Serves values(?)'
        x = c.execute(Sql, [Serve])
        db.commit()
        db.close()

    # Confirm Add  Serves
    def Confirm_Add_Serves(self):
        Serve = self.lineEdit_240.text()
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف اسم الخدمه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and Serve != '':
            self.Add_Serveses()
            QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح')
            self.Clear_SLineEditServes()
            self.Show_Added_Serves()
        else:
            pass

    # Clear Line Edit Serves
    def Clear_SLineEditServes(self):
        self.lineEdit_240.setText('')

    # Delete Serve
    def Delete_Special_Serve(self):
        Serve = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Delete from Serves Where serve =?'
        x = c.execute(Sql, [Serve])
        db.commit()
        db.close()

    # Confirm Delete Serve
    def Confirm_Delete_Serve(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من اسم الخدمه ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Special_Serve()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            self.Show_Added_Serves()

    '''Add Serve to AKhwet EL RaB Family'''

    # Show Family
    def Show_All_Familyu(self):
        Leader = 'نعم'
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Name,MName,FamilyNum,Stutus,Street,Address FROM Father Where Leader = ? order by Name
        '''
        Result = conect.execute(query, [(Leader)])
        Result = Result.fetchall()
        query = '''
                SELECT Name,FName,FamilyNum,Stutus,Street,Address FROM Mother Where Leader = ? order by Name
                '''
        X = conect.execute(query, [(Leader)])
        X = X.fetchall()
        Result = Result + X
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # Add Family Serves
    def Add_Serve_To_Family(self):
        Serve = self.comboBox.currentText()
        Value = self.lineEdit.text()
        if Value == '':
            Value = 'لا يوجد'
        else:
            self.lineEdit.text()
        Take = 'لا'
        if self.checkBox.isChecked():
            Take = 'نعم'
        try:
            Name =str(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
            Street = str(self.tableWidget.item(self.tableWidget.currentRow(), 4).text())
            FamilyNum = str(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
            Address = str(self.tableWidget.item(self.tableWidget.currentRow(), 5).text())
        except:
            print('Exept Add Serve')

        Date = self.dateEdit_2.date()
        Data = Date.toPyDate()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = '''INSERT INTO AddServices Values(?,?,?,?,?,?,?,?)'''
        Result = c.execute(Sql, [(Name), (FamilyNum), (Street), (Address), (Serve), (Value), (Take), (Data)])
        db.commit()
        db.close()
        self.Clear_CLineEdits()
        self.Show_Family_After_Add_Serve()
        QMessageBox.information(self, 'جيد', 'تمت الاضافه بنجاح ')

    # Add Values To Serves ComboBox
    def Add_Values(self):
        self.comboBox.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Serve from Serves')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox.addItem(str(i[0]))
        self.Clear_CLineEdits()

    # Clear Values
    def Clear_CLineEdits(self):
        self.comboBox.setCurrentIndex(0)
        self.lineEdit.setText('')
        self.pushButton_5.setEnabled(False)
        self.checkBox.setChecked(False)

    # Show Family After Add Serve
    def Show_Family_After_Add_Serve(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT * FROM AddServices order by Father ASC
        '''
        Result = conect.execute(query)
        Result = Result.fetchall()
        self.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Confirm Save Searves With Family
    def Confirm_Save_Data(self):
        Serve = self.comboBox.currentText()
        if Serve == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من اسم الخدمه')
        if Serve.strip(" ") != '':
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من تاريخ الاضافه ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_5.setEnabled(True)
        else:
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من البيانات')

    '''Search Serves Tab'''

    # Search Of Special Serve
    def Search_Special_Serve(self):
        Serve = self.comboBox_2.currentText()
        nummservices = self.lineEdit_24.text()
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
                SELECT Father,FamilyNum,Address,Serve,Value,Take,Date FROM AddServices Where Serve = ? and Date=? order by Father
                '''
        Result = conect.execute(query, [(Serve), (nummservices)])
        Result = Result.fetchall()
        self.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.Clearrrrr()

    # Add Values to ComboBox Serves
    def Add_Values_ComboBoxes(self):
        self.comboBox_2.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Serve from Serves')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_2.addItem(str(i[0]))

    # Clear
    def Clearrrrr(self):
        self.comboBox_2.setCurrentIndex(0)

    # Report
    def Report_Special_Serve(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_3.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)
            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)
            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    '''Edit Father Tab'''

    # Show Values in Work
    def Show_Work_InComboBoxes(self):
        self.comboBox_3.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        c.execute('Select Work from WorkM')
        y = c.fetchall()
        x = x + y
        db.commit()
        db.close()
        for i in x:
            self.comboBox_3.addItem(str(i[0]))

    # Show Streets
    def Show_Streets_ComboBox(self):
        self.comboBox_4.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_4.addItem(str(i[0]))

    # Show All Father
    def Show_Fathers(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        Name = ''
        query = '''
        SELECT Name,Phone,Street,Address,Work,Father,Stutus FROM Father Where Not Name = ? order by Name ASC
        '''
        Result = conect.execute(query, [(Name)])
        Result = Result.fetchall()

        self.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Selection Changes
    def Selection_Changes_Fathers(self):
        try:
            Father = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 5).text()
            Address = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 3).text()
            Phone = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 1).text()
            self.lineEdit_5.setText(Father)
            self.lineEdit_4.setText(Address)
            self.lineEdit_2.setText(Phone)

        except:
            pass

    # Update Data Father Or Armal
    def Update_Data_Father_Armal(self):
        Name = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 0).text()
        Phone = self.lineEdit_2.text()
        Street = self.comboBox_4.currentText()
        Address = self.lineEdit_4.text()
        Work = self.comboBox_3.currentText()
        Father = self.lineEdit_5.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        query = '''
            update Father set Phone= ?,Street = ?,Address = ?,Work = ?,Father =? Where Name = ?
                '''
        Result = c.execute(query, [(Phone), (Street), (Address), (Work), (Father), (Name)])
        Result = Result.fetchall()
        db.commit()
        db.close()
        self.Show_Fathers()
        self.Clear_Our_Inputs()
        QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')

    # Update Mother Armal
    def Update_Data_Mother_Armal(self):
        Name = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 0).text()
        Phone = self.lineEdit_2.text()
        Street = self.comboBox_4.currentText()
        Address = self.lineEdit_4.text()
        Work = self.comboBox_3.currentText()
        Father = self.lineEdit_5.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        query = '''
            update Mother set Phone= ?,Street = ?,Address = ?,Work = ?,Father =? Where Name = ?
                '''
        Result = c.execute(query, [(Phone), (Street), (Address), (Work), (Father), (Name)])
        Result = Result.fetchall()
        db.commit()
        db.close()
        self.Show_Fathers()
        self.Clear_Our_Inputs()
        QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')

    # Confirm Update
    def Confirmation_Update(self):
        try:
            Stutus = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 6).text()
            Name = 'ارمله'
            if Stutus == Name:
                self.Update_Data_Mother_Armal()
            elif Stutus == 'ارمل' or 'متزوج':
                self.Update_Data_Father_Armal()
        except:
            QMessageBox.information(self, 'معذرة', ' تاكد من اختيار رب اسرة من فضلك ')

    # Clear Inputs
    def Clear_Our_Inputs(self):
        self.lineEdit_5.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_2.setText('')
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

    # Delete Father
    def Delete_Father_Data(self):
        Name = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Query = ''' Delete From Father Where Name = ?'''
        Result = c.execute(Query, [(Name)])
        db.commit()
        db.close()

    # Delete Mother Data
    def Delete_Mother_Data(self):
        Name = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Query = ''' Delete From Mother Where Name = ?'''
        Result = c.execute(Query, [(Name)])
        db.commit()
        db.close()

    # Confirm Deletion
    def Confirm_Delete(self):
        try:
            Stutus = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 6).text()
            if Stutus == 'ارمله':
                self.Delete_Mother_Data()
                self.Show_Fathers()
                self.Clear_Our_Inputs()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
            elif Stutus == 'ارمل' or 'متزوج':
                self.Delete_Father_Data()
                self.Clear_Our_Inputs()
                self.Show_Fathers()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
        except:
            QMessageBox.information(self, 'معذرة', ' تاكد من اختيار رب اسرة من فضلك ')

    '''Edit Mother Tab'''

    # Show Values in Work
    def Show_Work_InComboBoxes_Armla(self):
        self.comboBox_5.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_5.addItem(str(i[0]))

    # Show All Mother
    def Show_Mothers(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')

        Name = ''
        query = '''SELECT Name,Phone,Qulified,Father,Work FROM Mother Where Not Name = ? order by Name ASC'''
        Result = conect.execute(query, [(Name)])
        Result = Result.fetchall()
        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Selection Changes
    def Selection_Changes_Mothers(self):
        try:
            Father = self.tableWidget_7.item(self.tableWidget_7.currentRow(), 3).text()
            Qulified = self.tableWidget_7.item(self.tableWidget_7.currentRow(), 2).text()
            Phone = self.tableWidget_7.item(self.tableWidget_7.currentRow(), 1).text()
            self.lineEdit_8.setText(Father)
            self.lineEdit_23.setText(Qulified)
            self.lineEdit_6.setText(Phone)

        except:
            pass

    # Update Mother
    def Update_Data_Mother(self):
        Name = self.tableWidget_7.item(self.tableWidget_7.currentRow(), 0).text()
        Phone = self.lineEdit_6.text()
        Work = self.comboBox_5.currentText()
        Father = self.lineEdit_8.text()
        Qulified = self.lineEdit_23.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        query = '''
            update Mother set Phone= ?,Work = ?,Father =?,Qulified =? Where Name = ?
                '''
        Result = c.execute(query, [(Phone), (Work), (Father), (Qulified), (Name)])
        Result = Result.fetchall()
        db.commit()
        db.close()
        self.Show_Mothers()
        self.Clear_Our_Inputs_Mother()
        QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')

    # Cleeear
    def Clear_Our_Inputs_Mother(self):
        self.lineEdit_6.setText('')
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_8.setText('')
        self.lineEdit_23.setText('')

    # Confirmation Update Mother Data
    def Confirmation_Mother(self):
        try:
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من البيانات ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Update_Data_Mother()
                self.Clear_Our_Inputs_Mother()
                self.Show_Mothers()
            else:
                pass
        except:
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من تحديد بيانات الام')

    # Delete Mother Data
    def Delete_Mother_Datas(self):
        Name = self.tableWidget_7.item(self.tableWidget_7.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Query = ''' Delete From Mother Where Name = ?'''
        Result = c.execute(Query, [(Name)])
        db.commit()
        db.close()

    # Confirm Deletion
    def Confirm_Delete_MData(self):
        try:
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Delete_Mother_Datas()
                self.Show_Mothers()
                self.Clear_Our_Inputs_Mother()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
        except:
            QMessageBox.information(self, 'معذرة', ' تاكد من اختيار رب اسرة من فضلك ')

    '''Edit Sons Tab'''

    # Show Values in Work Sons
    def Show_Work_InComboBoxes_Sons(self):
        self.comboBox_6.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_6.addItem(str(i[0]))

    # Show Values in Study Sons
    def Show_Study_InComboBoxes_Sons(self):
        self.comboBox_7.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_7.addItem(str(i[0]))

    # Selection Changes Sons
    def Selection_Changes_Sons(self):
        try:
            Father = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 3).text()
            Phone = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 1).text()
            self.lineEdit_26.setText(Father)
            self.lineEdit_25.setText(Phone)

        except:
            pass

    # Show All Sons Data
    def Show_All_Sons(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Name,Phone,Study,Work,Father FROM Sons order by Name ASC
        '''
        Result = conect.execute(query)
        Result = Result.fetchall()
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Update Sons
    def Update_Data_Sons(self):
        Name = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 0).text()
        Phone = self.lineEdit_25.text()
        Work = self.comboBox_6.currentText()
        Father = self.lineEdit_26.text()
        Study = self.comboBox_7.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        query = '''
                    update Sons set Phone = ?,Work = ?,Father = ?,Study = ? Where Name = ?
                '''
        Result = c.execute(query, [(Phone), (Work), (Father), (Study), (Name)])
        Result = Result.fetchall()
        db.commit()
        db.close()
        self.Cleear_Sons()
        self.Show_All_Sons()
        QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')

    # Clear Sons Inputus
    def Cleear_Sons(self):
        self.lineEdit_25.setText('')
        self.lineEdit_26.setText('')
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)

    # Confirmation_Edit_Sons
    def Confirmation_Edit_Sons(self):
        try:
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من البيانات ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Update_Data_Sons()
                self.Cleear_Sons()
                self.Show_All_Sons()
            else:
                pass
        except:
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من تحديد بيانات الابن')

    # Delete Sons Data
    def Deletion_Sons(self):
        Name = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Query = ''' Delete From Sons Where Name = ?'''
        Result = c.execute(Query, [(Name)])
        db.commit()
        db.close()

    # Confirmation Delete Sons Data
    def Confirmation_Deletions(self):
        try:
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Deletion_Sons()
                self.Show_All_Sons()
                self.Cleear_Sons()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
        except:
            QMessageBox.information(self, 'معذرة', ' تاكد من اختيار رب اسرة من فضلك ')


    '''Add Values IN ComboBoxes '''

    # Family Tab ======================================================== #
    # Father Family Work
    def Add_FF_ComboBox_Work(self):
        self.comboBox_25.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_25.addItem(str(i[0]))

    # Father Family Street
    def Add_FF_ComboBox_Street(self):
        self.comboBox_26.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_26.addItem(str(i[0]))

    # Mother Family Work
    def Add_MF_ComboBox_Work(self):
        self.comboBox_27.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_27.addItem(str(i[0]))

    # 1st Son Work
    def F1st_Son_Work(self):
        self.comboBox_37.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_37.addItem(str(i[0]))

    # 1st Son Study
    def F1st_Son_Study(self):
        self.comboBox_53.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_53.addItem(str(i[0]))

    # 2st Son Work
    def F2st_Son_Work(self):
        self.comboBox_38.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_38.addItem(str(i[0]))

    # 2st Son Study
    def F2st_Son_Study(self):
        self.comboBox_54.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_54.addItem(str(i[0]))

    # 3st Son Work
    def F3st_Son_Work(self):
        self.comboBox_39.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_39.addItem(str(i[0]))

    # 3st Son Study
    def F3st_Son_Study(self):
        self.comboBox_55.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_55.addItem(str(i[0]))

    # 4st Son Work
    def F4st_Son_Work(self):
        self.comboBox_40.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_40.addItem(str(i[0]))

    # 4st Son Study
    def F4st_Son_Study(self):
        self.comboBox_56.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_56.addItem(str(i[0]))

    # 5st Son Work
    def F5st_Son_Work(self):
        self.comboBox_52.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_52.addItem(str(i[0]))

    # 5st Son Study
    def F5st_Son_Study(self):
        self.comboBox_49.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_49.addItem(str(i[0]))

    # 6st Son Work
    def F6st_Son_Work(self):
        self.comboBox_41.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_41.addItem(str(i[0]))

    # 6st Son Study
    def F6st_Son_Study(self):
        self.comboBox_51.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_51.addItem(str(i[0]))

    # 7st Son Work
    def F7st_Son_Work(self):
        self.comboBox_42.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_42.addItem(str(i[0]))

    # 7st Son Study
    def F7st_Son_Study(self):
        self.comboBox_50.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_50.addItem(str(i[0]))

    # 8st Son Work
    def F8st_Son_Work(self):
        self.comboBox_43.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_43.addItem(str(i[0]))

    # 8st Son Study
    def F8st_Son_Study(self):
        self.comboBox_47.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_47.addItem(str(i[0]))

    # 9st Son Work
    def F9st_Son_Work(self):
        self.comboBox_44.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_44.addItem(str(i[0]))

    # 9st Son Study
    def F9st_Son_Study(self):
        self.comboBox_46.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_46.addItem(str(i[0]))

    # 10st Son Work
    def F10st_Son_Work(self):
        self.comboBox_24.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_24.addItem(str(i[0]))

    # 10st Son Study
    def F10st_Son_Study(self):
        self.comboBox_45.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_45.addItem(str(i[0]))

    # Family Tab Armal ======================================================== #
    # Father Armal Work
    def Add_FArmal_ComboBox_Work(self):
        self.comboBox_65.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_65.addItem(str(i[0]))

    # Father Family Street
    def Add_FArmal_ComboBox_Street(self):
        self.comboBox_64.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_64.addItem(str(i[0]))

    # 1st Son Work
    def Armal1st_Son_Work(self):
        self.comboBox_19.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_19.addItem(str(i[0]))

    # 1st Son Study
    def Armal1st_Son_Study(self):
        self.comboBox_82.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_82.addItem(str(i[0]))

    # 2st Son Work
    def Armal2st_Son_Work(self):
        self.comboBox_83.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_83.addItem(str(i[0]))

    # 2st Son Study
    def Armal2st_Son_Study(self):
        self.comboBox_48.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_48.addItem(str(i[0]))

    # 3st Son Work
    def Armal3st_Son_Work(self):
        self.comboBox_84.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_84.addItem(str(i[0]))

    # 3st Son Study
    def Armal3st_Son_Study(self):
        self.comboBox_59.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_59.addItem(str(i[0]))

    # 4st Son Work
    def Armal4st_Son_Work(self):
        self.comboBox_85.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_85.addItem(str(i[0]))

    # 4st Son Study
    def Armal4st_Son_Study(self):
        self.comboBox_60.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_60.addItem(str(i[0]))

    # 5st Son Work
    def Armal5st_Son_Work(self):
        self.comboBox_86.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_86.addItem(str(i[0]))

    # 5st Son Study
    def Armal5st_Son_Study(self):
        self.comboBox_61.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_61.addItem(str(i[0]))

    # 6st Son Work
    def Armal6st_Son_Work(self):
        self.comboBox_87.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_87.addItem(str(i[0]))

    # 6st Son Study
    def Armal6st_Son_Study(self):
        self.comboBox_62.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_62.addItem(str(i[0]))

    # 7st Son Work
    def Armal7st_Son_Work(self):
        self.comboBox_88.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_88.addItem(str(i[0]))

    # 7st Son Study
    def Armal7st_Son_Study(self):
        self.comboBox_63.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_63.addItem(str(i[0]))

    # 8st Son Work
    def Armal8st_Son_Work(self):
        self.comboBox_90.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_90.addItem(str(i[0]))

    # 8st Son Study
    def Armal8st_Son_Study(self):
        self.comboBox_89.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_89.addItem(str(i[0]))

    # 9st Son Work
    def Armal9st_Son_Work(self):
        self.comboBox_92.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_92.addItem(str(i[0]))

    # 9st Son Study
    def Armal9st_Son_Study(self):
        self.comboBox_91.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_91.addItem(str(i[0]))

    # 10st Son Work
    def Armal10st_Son_Work(self):
        self.comboBox_94.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_94.addItem(str(i[0]))

    # 10st Son Study
    def Armal10st_Son_Study(self):
        self.comboBox_92.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_92.addItem(str(i[0]))

    # Family Tab Armal ======================================================== #
    # Father Armal Work
    def Add_FArmala_ComboBox_Work(self):
        self.comboBox_58.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_58.addItem(str(i[0]))

    # Father Family Street
    def Add_FArmala_ComboBox_Street(self):
        self.comboBox_57.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_57.addItem(str(i[0]))

    # 1st Son Work
    def Armala1st_Son_Work(self):
        self.comboBox_18.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_18.addItem(str(i[0]))

    # 1st Son Study
    def Armala1st_Son_Study(self):
        self.comboBox_69.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_69.addItem(str(i[0]))

    # 2st Son Work
    def Armala2st_Son_Work(self):
        self.comboBox_31.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_31.addItem(str(i[0]))

    # 2st Son Study
    def Armala2st_Son_Study(self):
        self.comboBox_70.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_70.addItem(str(i[0]))

    # 3st Son Work
    def Armala3st_Son_Work(self):
        self.comboBox_32.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_32.addItem(str(i[0]))

    # 3st Son Study
    def Armala3st_Son_Study(self):
        self.comboBox_71.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_71.addItem(str(i[0]))


    # 4st Son Work
    def Armala4st_Son_Work(self):
        self.comboBox_33.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_33.addItem(str(i[0]))

    # 4st Son Study
    def Armala4st_Son_Study(self):
        self.comboBox_72.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_72.addItem(str(i[0]))

    # 5st Son Work
    def Armala5st_Son_Work(self):
        self.comboBox_34.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_34.addItem(str(i[0]))

    # 5st Son Study
    def Armala5st_Son_Study(self):
        self.comboBox_73.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_73.addItem(str(i[0]))

    # 6st Son Work
    def Armala6st_Son_Work(self):
        self.comboBox_35.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_35.addItem(str(i[0]))

    # 6st Son Study
    def Armala6st_Son_Study(self):
        self.comboBox_74.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_74.addItem(str(i[0]))

    # 7st Son Work
    def Armala7st_Son_Work(self):
        self.comboBox_36.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_36.addItem(str(i[0]))

    # 7st Son Study
    def Armala7st_Son_Study(self):
        self.comboBox_75.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_75.addItem(str(i[0]))

    # 8st Son Work
    def Armala8st_Son_Work(self):
        self.comboBox_76.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_76.addItem(str(i[0]))

    # 8st Son Study
    def Armala8st_Son_Study(self):
        self.comboBox_77.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_77.addItem(str(i[0]))

    # 9st Son Work
    def Armala9st_Son_Work(self):
        self.comboBox_78.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_78.addItem(str(i[0]))

    # 9st Son Study
    def Armala9st_Son_Study(self):
        self.comboBox_79.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_79.addItem(str(i[0]))

    # 10st Son Work
    def Armala10st_Son_Work(self):
        self.comboBox_80.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_80.addItem(str(i[0]))

    # 10st Son Study
    def Armala10st_Son_Study(self):
        self.comboBox_81.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_81.addItem(str(i[0]))

    '''Search Father Data'''

    def Show_Father_Name_In_ComboBox(self):
        self.comboBox_8.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from Father')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_8.addItem(str(i[0]))

    def Search_Father_Data_From_Table(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,MName,MPhone,Sons,Phone,Street,Address FROM Father Where Name =? and Not Name = ? '''
        Name = self.comboBox_8.currentText()
        N = ''
        x = c.execute(sql, [(Name), (N)])
        Result = x.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    #####

    def Report_Specialk_Fatther(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            x = self.tableWidget_9.model()
            model = x
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    '''Search Mother Data'''

    def Show_Mother_Name_In_ComboBox(self):
        self.comboBox_9.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from Mother')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_9.addItem(str(i[0]))

    def Search_Mother_Data_From_Table(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,FName,FPhone,ChildNum,Stutus,Street,Address FROM Mother Where Name =? and Not Name = ? '''
        Name = self.comboBox_9.currentText()
        N = ''
        x = c.execute(sql, [(Name), (N)])
        Result = x.fetchall()
        self.tableWidget_10.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def Report_Specialk_Mom(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            x = self.tableWidget_10.model()
            model = x
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    '''Search Sons Data'''

    def Show_Son_Name_In_ComboBox_F(self):
        self.comboBox_10.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Distinct FName from Sons ')
        x = c.fetchall()
        c.execute('Select Distinct MName from Sons')
        Y = c.fetchall()
        x = x + Y
        db.commit()
        db.close()
        for i in x:
            self.comboBox_10.addItem(str(i[0]))

    def Search_Son_Data_From_Table_F(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Distinct Name,MName,FName,Work,Study,Phone FROM Sons Where Not Name =? and FName =? or Not Name =? and MName = ?   '''
        Name = self.comboBox_10.currentText()
        N = ''
        x = c.execute(sql, [(N), (Name), (N), (Name)])
        Result = x.fetchall()
        self.tableWidget_11.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_11.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def Report_Specialk_SOm(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            x = self.tableWidget_11.model()
            model = x
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    '''Search All Family'''

    # Search Family BY Father Name
    def Show_Family_By_FName_In_ComboBox(self):
        self.comboBox_12.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from Father')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_12.addItem(str(i[0]))

    # Search Family By Father
    def Search_All_Family_App(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,MName,Phone,Sons,Street,Address FROM Father Where Not Name =? and Name =?   '''
        Name = self.comboBox_12.currentText()
        N = ''
        x = c.execute(sql, [(N), (Name)])
        Result = x.fetchall()
        s = [('----------------------', '----------------------', '----------------------', '----------------------',
              '----------------------', '----------------------', '----------------------')]
        Title = [('اسم الابن', 'اب الاعتراف', 'الجنس', 'الموبيل', 'الدراسه', 'الوظيفه', 'العمر')]

        sql = '''SELECT Name,Father,Gender,Phone,Study,Work,DOB FROM Sons Where Not Name =? and FName =?'''
        t = c.execute(sql, [(N), (Name)])
        X = t.fetchall()
        Result = Result + s + Title + s + X
        self.tableWidget_12.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_12.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.Cierir()

    # Search Family BY Mother Name
    def Show_Family_By_MName_In_ComboBox(self):
        self.comboBox_13.clear()

        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from Mother')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_13.addItem(str(i[0]))

    # By Mother Data
    def Search_All_Family_App_ByMother(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Stutus,Phone,ChildNum,Street,Address FROM Mother Where Not Name =? and Name =?   '''
        Name = self.comboBox_13.currentText()
        N = ''
        x = c.execute(sql, [(N), (Name)])
        Result = x.fetchall()
        s = [('----------------------', '----------------------', '----------------------', '----------------------',
              '----------------------', '----------------------', '----------------------')]
        Title = [('اسم الابن', 'اب الاعتراف', 'الجنس', 'الموبيل', 'الدراسه', 'الوظيفه', 'العمر')]

        sql = '''SELECT Name,Father,Gender,Phone,Study,Work,DOB FROM Sons Where Not Name =? and MName =?'''
        t = c.execute(sql, [(N), (Name)])
        X = t.fetchall()
        Result = Result + s + Title + s + X
        self.tableWidget_12.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_12.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.Cilear()

    # Mother ComboBox Claer
    def Cilear(self):
        self.comboBox_13.setCurrentIndex(0)

    # Father ComboBox Clear
    def Cierir(self):
        self.comboBox_12.setCurrentIndex(0)

    # Report Family Data
    def Report_All_Family_Data(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            x = self.tableWidget_12.model()
            model = x
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass


    # Selection Changes Regester
    def Selection_Changes_Regester(self):
        try:
            pword = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 1).text()
            work = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 3).text()
            charch = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 4).text()
            father = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 5).text()
            qualify = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 7).text()
            self.lineEdit_29.setText(pword)
            self.lineEdit_32.setText(work)
            self.lineEdit_30.setText(charch)
            self.lineEdit_28.setText(father)
            self.lineEdit_31.setText(qualify)

        except:
            pass
    # Show All Regester Data
    def Show_All_Regester(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''SELECT Name,password,Ssn,work,church,fregonize,gender,Qulified FROM RecordEmpData order by Name ASC'''
        print(23423)
        Result = conect.execute(query)
        Result = Result.fetchall()
        self.tableWidget_13.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_13.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_13.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # Update Regester
    def Update_Data_Regester(self):
        Name = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 0).text()
        Psword = self.lineEdit_28.text()
        wrk = self.lineEdit_32.text()
        charchname = self.lineEdit_30.text()
        father = self.lineEdit_28.text()
        qualify=self.lineEdit_31.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        query = '''update RecordEmpData set password = ?,work = ?,church = ?,fregonize = ?,Qulified =? Where Name = ?'''
        Result = c.execute(query, [(Psword), (wrk), (charchname), (father),(qualify), (Name)])
        Result = Result.fetchall()
        db.commit()
        db.close()
        self.Cleear_Sons()
        self.Show_All_Sons()
        QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')

    # Clear Regester Inputus
    def Cleear_Regester(self):
        self.lineEdit_28.setText('')
        self.lineEdit_29.setText('')
        self.lineEdit_30.setText('')
        self.lineEdit_31.setText('')
        self.lineEdit_32.setText('')

    # Confirmation_Edit_Regester
    def Confirmation_Edit_Regester(self):
        try:
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من البيانات ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Update_Data_Regester()
                self.Cleear_Regester()
                self.Show_All_Regester()
            else:
                pass
        except:
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من تحديد البيانات')

    # Delete Regester Data
    def Deletion_Regester(self):
        Name = self.tableWidget_13.item(self.tableWidget_13.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Query = ''' Delete From RecordEmpData Where Name = ?'''
        Result = c.execute(Query, [(Name)])
        db.commit()
        db.close()

    # Confirmation Delete Regester Data
    def Confirmation_Deletions_Regester(self):
        try:
            Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                             , QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Deletion_Regester()
                self.Show_All_Regester()
                self.Cleear_Regester()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح')
        except:
            QMessageBox.information(self, 'معذرة', ' تاكد من اختيار رب اسرة من فضلك ')


    def LOGOUT(self):
        self.window2 = login()
        self.close()
        self.window2.show()


class Aftkad(QMainWindow, MainUI2):
    def __init__(self, parent=None):
        super(Aftkad, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Method For Handle All Buttons
        self.Handle_Buttons()
        # Show Family Data IN Table For Edit
        self.Show_Father_Data_For_Edit()
        self.Show_Mother_Data_For_Edit()
        self.Show_Sons_Data_For_Edit()


        self.Show_Aftkad_Data_Before_Add_Date()
        self.Show_Aftkad_Data()
        self.Show_Fathers_Not_Have_FatherReconize()
        self.Show_Mothers_Not_Have_FatherReconize()


        self.Select_Special_Age_From_Mans()


        self.Show_Work_Father_List()
        self.Show_Work_Mother_List()
        self.Show_Work_Son_List()

        self.Show_Work_Study_List()
        self.Show_Work_Street_List()


        self.Show_All_Male_Armals()
        self.Show_All_FeMale_Armals()

        self.Show_all_A3zab_Data()

        self.Show_All_FeMale_Armals()



        self.radioButton_62.pressed.connect(self.Father_Dead_RadioButton_A3zeb)
        self.radioButton_59.pressed.connect(self.Father_Dead_RadioButton_Armala)
        self.radioButton_126.pressed.connect(self.Mother_Dead_RadioButton_A3zeb)
        self.radioButton_125.pressed.connect(self.Mother_Dead_RadioButton_Armala)

    def Mother_Dead_RadioButton_A3zeb(self):
        self.lineEdit_36.setEnabled(False)
        self.spinBox_11.setEnabled(False)
        self.lineEdit_36.setText("")
        self.spinBox_11.setValue(0)

    def Mother_Dead_RadioButton_Armala(self):
        self.lineEdit_36.setEnabled(True)
        self.spinBox_11.setEnabled(True)

    def Father_Dead_RadioButton_A3zeb(self):
        self.lineEdit_35.setEnabled(False)
        self.spinBox_10.setEnabled(False)
        self.lineEdit_35.setText("")
        self.spinBox_10.setValue(0)

    def Father_Dead_RadioButton_Armala(self):
        self.lineEdit_35.setEnabled(True)
        self.spinBox_10.setEnabled(True)



    def Handle_Buttons(self):
        self.lineEdit_40.textChanged.connect(self.Search_A3zab_Male_Tab_By_Name)
        self.lineEdit_58.textChanged.connect(self.Search_A3zab_Male_Tab_By_Phone)
        self.lineEdit_168.textChanged.connect(self.Search_MotherDead_By_Name_Filter)
        self.lineEdit_169.textChanged.connect(self.Search_MotherDead_By_Phone_Filter)
        self.lineEdit_171.textChanged.connect(self.Search_FatherDead_By_Name_Filter)
        self.lineEdit_170.textChanged.connect(self.Search_FatherDead_By_Phone_Filter)

        self.lineEdit_173.textChanged.connect(self.Make_Filter_Fathers_Special_Cases)
        self.lineEdit_172.textChanged.connect(self.Make_Filter_Fathers_Special_Cases_Phones)

        self.lineEdit_175.textChanged.connect(self.Special_Case_Females_filter_Name)
        self.lineEdit_174.textChanged.connect(self.Special_Case_Females_filter_Phone)

        self.lineEdit_176.textChanged.connect(self.Son_Filter_Sepcial_Cases)
        self.lineEdit_178.textChanged.connect(self.Son_Filter_Sepcial_Cases_FName)
        self.lineEdit_179.textChanged.connect(self.Son_Filter_Sepcial_Cases_MName)
        self.lineEdit_177.textChanged.connect(self.Son_Filter_Sepcial_Cases_Phone)

        self.lineEdit_180.textChanged.connect(self.Make_Filter_For_FName_Table_Update)
        self.lineEdit_181.textChanged.connect(self.Make_Filter_For_FPhone_Table_Update)
        self.lineEdit_185.textChanged.connect(self.Make_Filter_By_Mother_Namee)
        self.lineEdit_184.textChanged.connect(self.Make_Filter_By_Mother_Phonee)

        self.lineEdit_187.textChanged.connect(self.Sons_Filter_Update_BY_Name)
        self.lineEdit_189.textChanged.connect(self.Sons_Filter_Update_BY_FName)
        self.lineEdit_188.textChanged.connect(self.Sons_Filter_Update_BY_MName)
        self.lineEdit_190.textChanged.connect(self.Sons_Filter_Update_BY_Phone)

        self.lineEdit_747.textChanged.connect(self.Make_Filter_Armal_Data_BY_Name)
        self.lineEdit_748.textChanged.connect(self.Make_Filter_Armal_Data_BY_Phone)


        self.lineEdit_749.textChanged.connect(self.Make_Mother_Filter_By_Name)
        self.lineEdit_750.textChanged.connect(self.Make_Mother_Filter_By_Phone)

        self.lineEdit_191.textChanged.connect(self.Filter_Family_Aftkad_By_Phone)

        self.lineEdit_192.textChanged.connect(self.Filter_DateAftkad_By_FName)
        self.lineEdit_193.textChanged.connect(self.Filter_DateAftkad_By_MName)
        self.lineEdit_194.textChanged.connect(self.Filter_DateAftkad_By_Phone)


        self.lineEdit_195.textChanged.connect(self.Filter_Father_Without_FatherReconize_By_Name)
        self.lineEdit_196.textChanged.connect(self.Filter_Mother_Without_FatherReconize_By_Name)
        self.lineEdit_197.textChanged.connect(self.Filter_Father_Without_FatherReconize_By_Phone)
        self.lineEdit_198.textChanged.connect(self.Filter_Mother_Without_FatherReconize_By_Phone)


        # Exit Program
        self.pushButton_13.clicked.connect(self.Exit)
        # Back To Login
        self.pushButton_14.clicked.connect(self.Go_To_Login)
        # Father Dead Tab ==================================
        # Button Check Father Dead Tab
        self.pushButton_123.clicked.connect(self.Check_Data_Of_Father_Dead)
        self.pushButton_141.clicked.connect(self.Check_On_Click_Sons_Tab_Of_Father_Dead)
        # Record Sons Data of Father Dead
        self.pushButton_100.clicked.connect(self.Choice_Record_Sons_Num_Data_FatherDead)
        # Record Father Data of Father Dead
        self.pushButton_100.clicked.connect(self.Add_Family_Which_Father_Dead)

        # Mother Dead ================
        # Button Check Father Dead Tab
        self.pushButton_142.clicked.connect(self.Check_Data_Of_Mother_Dead)
        self.pushButton_143.clicked.connect(self.Check_On_Click_Sons_Tab_Of_Mother_Dead)
        # Record Sons Data of Mother Dead
        self.pushButton_101.clicked.connect(self.Choice_Record_Sons_Num_Data_MotherDead)
        # Record Sons Data of Mother Dead
        self.pushButton_101.clicked.connect(self.Add_Family_Which_Mother_Dead)
        self.pushButton_101.clicked.connect(self.Clear_Data_Of_Father_Dead)

        # =====================================================

        # Show Mans In Speacial Age
        self.pushButton_80.clicked.connect(self.Select_Special_Age_From_Mans)
        # Show Females In Speacial Age
        self.pushButton_81.clicked.connect(self.Select_Special_Age_From_Femals)
        # Show Special Age for Father Armals
        self.pushButton_675.clicked.connect(self.Select_Special_Age_From_Mans_Armals)
        # Show Special Age for Mother Armals
        self.pushButton_678.clicked.connect(self.Select_Special_Age_From_Femals_Armals)

        # Moving Between Sons of Father Dead Tabs
        # Move To 2st Son Tab
        self.pushButton_58.clicked.connect(self.On_Mouse_Click_in_2st_Son_Of_FatherDead)
        # Back To 1st Son Tab
        self.pushButton_62.clicked.connect(self.Open_Son_1st_OF_FatherDead_Tab)
        # Move To 3st Son Tab
        self.pushButton_61.clicked.connect(self.On_Mouse_Click_in_3st_Son_Of_FatherDead)
        # Back To 2st Son Tab
        self.pushButton_64.clicked.connect(self.Open_Son_2st_OF_FatherDead_Tab)
        # Move To 4st Son Tab
        self.pushButton_63.clicked.connect(self.On_Mouse_Click_in_4st_Son_Of_FatherDead)
        # Back To 3st Son Tab
        self.pushButton_66.clicked.connect(self.Open_Son_3st_OF_FatherDead_Tab)
        # Move To 5st Son Tab
        self.pushButton_65.clicked.connect(self.On_Mouse_Click_in_5st_Son_Of_FatherDead)
        # Back To 4st Son Tab
        self.pushButton_68.clicked.connect(self.Open_Son_4st_OF_FatherDead_Tab)
        # Move To 6st Son Tab
        self.pushButton_67.clicked.connect(self.On_Mouse_Click_in_6st_Son_Of_FatherDead)
        # Back To 5st Son Tab
        self.pushButton_92.clicked.connect(self.Open_Son_5st_OF_FatherDead_Tab)
        # Move To 7st Son Tab
        self.pushButton_91.clicked.connect(self.On_Mouse_Click_in_7st_Son_Of_FatherDead)
        # Back To 6st Son Tab
        self.pushButton_94.clicked.connect(self.Open_Son_6st_OF_FatherDead_Tab)
        # Move To 8st Son Tab
        self.pushButton_93.clicked.connect(self.On_Mouse_Click_in_8st_Son_Of_FatherDead)
        # Back To 7st Son Tab
        self.pushButton_96.clicked.connect(self.Open_Son_7st_OF_FatherDead_Tab)
        # Move To 9st Son Tab
        self.pushButton_95.clicked.connect(self.On_Mouse_Click_in_9st_Son_Of_FatherDead)
        # Back To 8st Son Tab
        self.pushButton_98.clicked.connect(self.Open_Son_8st_OF_FatherDead_Tab)
        # Move To 10st Son Tab
        self.pushButton_97.clicked.connect(self.On_Mouse_Click_in_10st_Son_Of_FatherDead)
        # Back To 9st Son Tab
        self.pushButton_99.clicked.connect(self.Open_Son_9st_OF_FatherDead_Tab)
        # Moving Between Sons of Mother Dead Tabs
        # Move To 2st Son Tab
        self.pushButton_171.clicked.connect(self.On_Mouse_Click_in_2st_Son_Of_MotherDead)
        # Back To 1st Son Tab
        self.pushButton_173.clicked.connect(self.Open_Son_1st_OF_MotherDead_Tab)
        # Move To 3st Son Tab
        self.pushButton_172.clicked.connect(self.On_Mouse_Click_in_3st_Son_Of_MotherDead)
        # Back To 2st Son Tab
        self.pushButton_175.clicked.connect(self.Open_Son_2st_OF_MotherDead_Tab)
        # Move To 4st Son Tab
        self.pushButton_174.clicked.connect(self.On_Mouse_Click_in_4st_Son_Of_MotherDead)
        # Back To 3st Son Tab
        self.pushButton_177.clicked.connect(self.Open_Son_3st_OF_MotherDead_Tab)
        # Move To 5st Son Tab
        self.pushButton_176.clicked.connect(self.On_Mouse_Click_in_5st_Son_Of_MotherDead)
        # Back To 4st Son Tab
        self.pushButton_179.clicked.connect(self.Open_Son_4st_OF_MotherDead_Tab)
        # Move To 6st Son Tab
        self.pushButton_178.clicked.connect(self.On_Mouse_Click_in_6st_Son_Of_MotherDead)
        # Back To 5st Son Tab
        self.pushButton_181.clicked.connect(self.Open_Son_5st_OF_MotherDead_Tab)
        # Move To 7st Son Tab
        self.pushButton_180.clicked.connect(self.On_Mouse_Click_in_7st_Son_Of_MotherDead)
        # Back To 6st Son Tab
        self.pushButton_183.clicked.connect(self.Open_Son_6st_OF_MotherDead_Tab)
        # Move To 8st Son Tab
        self.pushButton_182.clicked.connect(self.On_Mouse_Click_in_8st_Son_Of_MotherDead)
        # Back To 7st Son Tab
        self.pushButton_185.clicked.connect(self.Open_Son_7st_OF_MotherDead_Tab)
        # Move To 9st Son Tab
        self.pushButton_184.clicked.connect(self.On_Mouse_Click_in_9st_Son_Of_MotherDead)
        # Back To 8st Son Tab
        self.pushButton_187.clicked.connect(self.Open_Son_8st_OF_MotherDead_Tab)
        # Move To 10st Son Tab
        self.pushButton_186.clicked.connect(self.On_Mouse_Click_in_10st_Son_Of_MotherDead)
        # Back To 9st Son Tab
        self.pushButton_188.clicked.connect(self.Open_Son_9st_OF_MotherDead_Tab)
        # Button Search Speacial Street
        self.pushButton_52.clicked.connect(self.Search_Family_In_Speacial_Street)

        # Selection Father Data From Table
        self.tableWidget_16.itemSelectionChanged.connect(self.Selection_Father_Data_From_Table)

        # Selection Mother Data From Table
        self.tableWidget_17.itemSelectionChanged.connect(self.Selection_Mother_Data_From_Table)
        # Selection A3zaab Data

        self.tableWidget_32.itemSelectionChanged.connect(self.Selection_A3zab)
        # Selection Sons Data From Table
        self.tableWidget_8.itemSelectionChanged.connect(self.Selection_Sons_Data_From_Table)
        # Selection Family Aftkad Data From Table
        self.tableWidget_7.itemSelectionChanged.connect(self.Selection_Family_Data_Aftkad_Tablee)
        # Selection Armal Males Data From Table
        self.tableWidget_131.itemSelectionChanged.connect(self.Selection_From_Armal_Male_Data)
        # Selection Armal FeMales Data From Table
        self.tableWidget_132.itemSelectionChanged.connect(self.Selection_From_Armal_FeMale_Data)

        # ============= Udate & Delete Data
        # Button ConFirm Update Father Data
        self.pushButton_163.clicked.connect(self.Confirm_Update_Father_Data)
        # Button Confirm Delete Father Data
        self.pushButton_164.clicked.connect(self.Confirm_Delete)

        # Button ConFirm Update Mother Data
        self.pushButton_161.clicked.connect(self.Confirm_Update_Mother_Data)
        # Button Confirm Delete Mother Data
        self.pushButton_162.clicked.connect(self.Confirm_Delete_MotherData)

        # Button ConFirm Update Sons Data
        self.pushButton_159.clicked.connect(self.Confirm_Update_Sons_Data)
        # Button Confirm Delete Son Data
        self.pushButton_160.clicked.connect(self.Comfirm_Delete_Son)

        # Button Search Aftkad Date
        self.pushButton_51.clicked.connect(self.Show_Aftkad_Data_ForSEARCH_Datee)

        # Udate Male Armal
        self.pushButton_689.clicked.connect(self.Confirm_Update_Data)
        # Update Female Armal
        self.pushButton_682.clicked.connect(self.Confirm_Update_Dataa)

        # Button Add date Aftkad  Data
        self.pushButton_11.clicked.connect(self.Confirm_Add_Aftkad_Date)

        # Button Search date Aftkad  Data
        self.pushButton_51.clicked.connect(self.Show_Aftkad_Data_Before_Add_Date)

        # Button Delete A3zab
        self.pushButton_113.clicked.connect(self.Confirm_Delete_A3zab_Data)
        # Clear Line Edits A3zab Tab
        self.pushButton_110.clicked.connect(self.Cleaaar)
        self.pushButton_110.clicked.connect(self.Clear_Updates)

        # Button For Search Special Work for father
        self.pushButton_33.clicked.connect(self.Search_From_Father_Work)
        # Button For Search Special Work for Mother
        self.pushButton_131.clicked.connect(self.Search_From_Mother_Work)
        # Button For Search Special Work for Sons
        self.pushButton_132.clicked.connect(self.Search_From_Sons_Work)
        # Button For Search Special Study for Sons
        self.pushButton_69.clicked.connect(self.Search_Sons_Study)
        # Button Update A3zab Data
        self.pushButton_114.clicked.connect(self.Confirm_Update_A3zab_Data)
        # =================== Show All fAMILY Data ======================================= #
        self.Show_All_Family_Data()
        self.Show_All_Sons_Family_Data()
        self.Mans_Armals()
        self.Females_Armals()
        self.Special_Case_Mans()
        self.Special_Case_Females()
        self.Special_Case_Sons()
        # ================================= Record Sons Data ============================================= #
        # Record Family Father and Mother and Sons Data
        self.pushButton_21.clicked.connect(self.Record_Father_Data)
        self.pushButton_21.clicked.connect(self.Record_Mother_Data)
        self.pushButton_21.clicked.connect(self.Choice_Record_Sons_Num_Data)
        self.pushButton_21.clicked.connect(self.Clear_Data_Of_Family_Of_Aftkad)

        # ============================ Move And Back Through Sons Tabs Of Father Dead================================= #
        # Move To 2st Son Tab
        self.pushButton.clicked.connect(self.On_Mouse_Click_in_1st_Son)
        # Back To 1st Son Tab
        self.pushButton_29.clicked.connect(self.open_1st_Son_Tab)
        # Move To 3st Son Tab
        self.pushButton_2.clicked.connect(self.On_Mouse_Click_in_2st_Son)
        # Back To 2st Son Tab
        self.pushButton_28.clicked.connect(self.open_2st_Son_Tab)
        # Move To 4st Son Tab
        self.pushButton_4.clicked.connect(self.On_Mouse_Click_in_3st_Son)
        # Back To 3st Son Tab
        self.pushButton_27.clicked.connect(self.open_3st_Son_Tab)
        # Move To 5st Son Tab
        self.pushButton_5.clicked.connect(self.On_Mouse_Click_in_4st_Son)
        # Back To 4st Son Tab
        self.pushButton_26.clicked.connect(self.open_4st_Son_Tab)
        # Move To 6st Son Tab
        self.pushButton_6.clicked.connect(self.On_Mouse_Click_in_5st_Son)
        # Back To 5st Son Tab
        self.pushButton_25.clicked.connect(self.open_5st_Son_Tab)
        # Move To 7st Son Tab
        self.pushButton_7.clicked.connect(self.On_Mouse_Click_in_6st_Son)
        # Back To 6st Son Tab
        self.pushButton_24.clicked.connect(self.open_6st_Son_Tab)
        # Move To 8st Son Tab
        self.pushButton_8.clicked.connect(self.On_Mouse_Click_in_7st_Son)
        # Back To 7st Son Tab
        self.pushButton_23.clicked.connect(self.open_7st_Son_Tab)
        # Move To 9st Son Tab
        self.pushButton_9.clicked.connect(self.On_Mouse_Click_in_8st_Son)
        # Back To 8st Son Tab
        self.pushButton_22.clicked.connect(self.open_8st_Son_Tab)
        # Move To 10st Son Tab
        self.pushButton_10.clicked.connect(self.On_Mouse_Click_in_9st_Son)
        # Back To 9st Son Tab
        self.pushButton_12.clicked.connect(self.open_9st_Son_Tab)
        # ===================================== Record Data ============================================ #
        # Check Father Data
        self.pushButton_49.clicked.connect(self.Check_Father_Data)
        # Check Mother Data
        self.pushButton_48.clicked.connect(self.Check_Mother_Data)
        # ====================================== Start Open Tabs ======================================= #
        # Report Student Data
        self.pushButton_70.clicked.connect(self.savefileStudent)
        # Report Female Age
        self.pushButton_47.clicked.connect(self.savefileFemaleByAge)
        # Report Man Age
        self.pushButton_45.clicked.connect(self.savefileManByAge)
        # Report Work Data
        self.pushButton_34.clicked.connect(self.savefileWorks)
        # Report Special Case Data
        self.pushButton_32.clicked.connect(self.savefileSpecialCase)
        # Report Female Data
        self.pushButton_16.clicked.connect(self.savefileFemaleArmals)
        # Report Male Data
        self.pushButton_15.clicked.connect(self.savefileMaleArmals)
        # Report All Family Data
        self.pushButton_37.clicked.connect(self.savefileOffAallFamilyData)
        # Report All Sons Data
        self.pushButton_50.clicked.connect(self.savefileSons)
        # Report All Sons Data Special Caase
        self.pushButton_128.clicked.connect(self.savefileSons_SpecialCase)
        # Report All Femlaes Data Special Case
        self.pushButton_126.clicked.connect(self.savefileFemales_SpecialCase)
        # Report Mother Work
        self.pushButton_133.clicked.connect(self.savefileMother_Work)
        # Report Sons Work
        self.pushButton_134.clicked.connect(self.savefileSons_Work)
        # Report Street Special Data
        self.pushButton_53.clicked.connect(self.savefileReport_StreetData)
        # Report Mans Without Father
        self.pushButton_55.clicked.connect(self.savefileReport_ManWithoutFather)
        # Report Females Without Father
        self.pushButton_56.clicked.connect(self.savefileReport_FemaleWithoutFather)
        # Report All Family Aftkad
        self.pushButton_673.clicked.connect(self.savefileReport_Family_Aftkad)
        # Report All A3zab Data
        self.pushButton_111.clicked.connect(self.savefileReport_A3zabs_Data)
        # Report Only One Family Has Searched
        self.pushButton_71.clicked.connect(self.savefileReport_OnlyOneFamilySearched)

        # =================================================================== #
        # Tab Open 1st Tab
        self.open_Start_Program()
        # Tab Open 1st Tab
        self.pushButton_3.clicked.connect(self.open_Main_Prgram_Component)
        # Return To 1st Tab
        self.pushButton_35.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_36.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_38.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_39.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_40.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_41.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_42.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_43.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_44.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_46.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_125.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_135.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_136.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_137.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_138.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_125.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_127.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_139.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_140.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_54.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_57.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_59.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_60.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_105.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_110.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_35.clicked.connect(self.Clear_Data_Of_Family_Of_Aftkad)
        self.pushButton_676.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_677.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_685.clicked.connect(self.open_Main_Prgram_Component)
        self.pushButton_683.clicked.connect(self.open_Main_Prgram_Component)

        '''Search Family Aftkad'''

        self.pushButton_112.clicked.connect(self.Search_Family_Aftkad)
        self.pushButton_116.clicked.connect(self.Search_Family_Mother_Name)
        # Make Refresh For All Tables
        # Check Sons In Family Aftkad Data
        self.pushButton_102.clicked.connect(self.Check_On_Click_Sons_Tab_Of_Family_Aftkad)

        # Buttons Add Sons Record Data
        # Get Mother Name Form DB To Show In Combo Box
        self.comboBox_18.currentTextChanged.connect(self.Read_Mother_Name_From_Table)
        # Check Sons Data
        self.pushButton_106.clicked.connect(self.Check_Add_Sons_Data)
        # Add Sons Data
        self.pushButton_104.clicked.connect(self.Add_Sons_Data)

        # Buttons Save Iteam Date of Add in List ======================
        # Button Add FWork
        self.pushButton_107.clicked.connect(self.Confirm_Add_Work_To_List_Father)

        # Button Add MWork
        self.pushButton_108.clicked.connect(self.Confirm_Add_Work_To_List_Mother)

        # Button Add Son
        self.pushButton_109.clicked.connect(self.Confirm_Add_Work_To_List_Son)

        # Button Add Study
        self.pushButton_199.clicked.connect(self.Confirm_Add_Study)

        # Button Add Street
        self.pushButton_200.clicked.connect(self.Confirm_Add_Street)

        # Button Delete Male Armal
        self.pushButton_690.clicked.connect(self.Confirm_Delete_Armal)

        # Button Delete FeMale Armal
        self.pushButton_688.clicked.connect(self.Confirm_Delete_Female_Armal)

        # Button Delete Father Job From Table
        self.pushButton_202.clicked.connect(self.Confirm_Delete_From_Father_List)
        self.pushButton_203.clicked.connect(self.Confirm_Delete_From_Mother_List)
        self.pushButton_204.clicked.connect(self.Confirm_Delete_From_Son_List)
        self.pushButton_205.clicked.connect(self.Confirm_Delete_From_Study_List)
        self.pushButton_206.clicked.connect(self.Confirm_Delete_From_Street_List)

        # Edit Son Tab ==============
        # Clear LineEdit on click back to MAIN WINDOW FATHER AND MOTHER DEAD TAB
        self.pushButton_59.clicked.connect(self.Clear_Data_Of_Father_Dead)
        self.pushButton_60.clicked.connect(self.Clear_Data_Of_Mother_Dead)
        # ====================================== End Open Tabs By Buttons ======================================= #

        # Call ComboBoxes Tabs
        self.comboBox_66.currentTextChanged.connect(self.Choice_Added_Tabs)
        self.comboBox_68.currentTextChanged.connect(self.Choice_Search_Tabs)
        self.comboBox_67.currentTextChanged.connect(self.Choice_Update_Tabs)
        self.comboBox_69.currentTextChanged.connect(self.Choice_Report_Tabs)

    # ComboBox Added Tabs
    def Choice_Added_Tabs(self):
        combo = self.comboBox_66.currentText()
        if combo == "اضافه اسرة جديده":
            self.Added_Family_Tab()
            self.comboBox_66.setCurrentIndex(0)
        if combo == "اضافه تاريخ افتقاد و طباعه اسر الافتقاد":
            self.Added_Family_Aftkad_Date_Tab()
            self.comboBox_66.setCurrentIndex(0)
        if combo == "اضافه اسرة بدون ام":
            self.Added_Armla_Tab()
            self.comboBox_66.setCurrentIndex(0)
        if combo == "اضافه اسرة بدون اب":

            self.Added_Armal_Tab()
            self.comboBox_66.setCurrentIndex(0)
        if combo == "اضافه مواليد":
            self.Added_Sons_Tab()
            self.comboBox_66.setCurrentIndex(0)

    # ComboBox Search Tabs
    def Choice_Search_Tabs(self):
        Combo = self.comboBox_68.currentText()

        if Combo == "البحث عن الاسر":
            self.Search_Family_Tab()
            self.comboBox_68.setCurrentIndex(0)
        if Combo == "بحث عن تاريخ زيارة الاسر":
            self.Search_Date_Aftkad_Tab()
            self.comboBox_68.setCurrentIndex(0)
        if Combo == "بحث ليس لديهم اب اعتراف":
            self.Search_Withot_Father_Tabs()
            self.comboBox_68.setCurrentIndex(0)
        if Combo == "بحث اسر عند شارع معين":
            self.Search_Special_Street_Tabs()
            self.comboBox_68.setCurrentIndex(0)

    # Add Father Work
    def Read_Father_Work_In_List_Armal(self):
        self.comboBox_336.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_336.addItem(str(i[0]))


    # Add Father Street
    def Read_Father_Street_In_List_Armal(self):
        self.comboBox_337.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_337.addItem(str(i[0]))
    # ComboBox Update Tabs
    def Choice_Update_Tabs(self):
        Combo = self.comboBox_67.currentText()
        if (Combo == "تعديل بيانات رب الاسرة"):
            self.Update_Father_Tabs()
            self.comboBox_67.setCurrentIndex(0)
        if (Combo == "تعديل بيانات الابناء"):
            self.Update_Sons_Tabs()
            self.Show_Sons_Data_For_Edit()
            self.comboBox_67.setCurrentIndex(0)
        if (Combo == "تعديل بيانات الامهات"):
            self.Update_Mother_Tabs()
            self.comboBox_67.setCurrentIndex(0)
        if (Combo == "تعديل او اضافه ليست"):
            self.Update_EditList_Tabs()
            self.comboBox_67.setCurrentIndex(0)
        if (Combo == "تعديل بيانات ارمل"):
            self.Update_ArmlaData_Tabs()
            self.Show_All_FeMale_Armals()
            self.comboBox_67.setCurrentIndex(0)
        if (Combo == "تعديل بيانات ارملة"):
            self.Update_ArmalData_Tabs()
            self.comboBox_67.setCurrentIndex(0)

    # ComboBox Report Tabs
    def Choice_Report_Tabs(self):
        Combo = self.comboBox_69.currentText()
        if (Combo == "السيدات الارامل"):
            self.Report_Armala_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "حالات خاصة  الابناء "):
            self.Report_Sons_SpecialCase_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "حالات خاصة السيدات"):
            self.Report_Female_SpecialCase_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "حالات خاصة رب الاسرة"):
            self.Report_Male_SpecialCase_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "الرجال الارامل"):
            self.Report_Armal_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "اسر الافتقاد"):
            self.Report_Family_Aftkad_Tab()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "كل ما يخص العزاب"):
            self.Report_A3zabs_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "الوظائف"):
            self.Report_Jobs_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "الابناء المتسربين/المتعلمين"):
            self.Report_Study_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "سن الرجال"):
            self.Report_Mage_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "سن النساء"):
            self.Report_Fage_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "سن الرجال الارامل"):
            self.Report_Armalage_Tabs()
            self.comboBox_69.setCurrentIndex(0)
        if (Combo == "سن النساء الارامل"):
            self.Report_ArmalaAge_()
            self.comboBox_69.setCurrentIndex(0)

    # ====================================== Open Tabs By Current Index ======================================= #
    def open_Start_Program(self):
        self.tabWidget.setCurrentIndex(0)
        # Main Program Tab
        self.tabWidget.tabBar().setVisible(False)

        # Sons Tab
        self.tabWidget_4.tabBar().setVisible(False)
        self.tabWidget_4.setCurrentIndex(0)

        # Sons Tab Mother Dead
        self.tabWidget_7.tabBar().setVisible(False)
        self.tabWidget_7.setCurrentIndex(0)
        # Sons Tab Father Dead
        self.tabWidget_8.tabBar().setVisible(False)
        self.tabWidget_8.setCurrentIndex(0)

    # ============================================================================= Main Tabs =============================================================== #
    def open_Main_Prgram_Component(self):
        self.tabWidget.setCurrentIndex(1)

    def Add_Family(self):
        self.tabWidget.setCurrentIndex(2)

    def open_To_Show__All_Family(self):
        self.tabWidget.setCurrentIndex(3)

    def open_Search_Family(self):
        self.tabWidget.setCurrentIndex(4)

    def open_Man_Armal(self):
        self.tabWidget.setCurrentIndex(5)

    def open_Female_Armal(self):
        self.tabWidget.setCurrentIndex(6)

    def open_Secial_Case(self):
        self.tabWidget.setCurrentIndex(7)

    def open_Work_Tab(self):
        self.tabWidget.setCurrentIndex(8)

    def open_Student_Tab(self):
        self.tabWidget.setCurrentIndex(9)

    def open_Man_Search_Age(self):
        self.tabWidget.setCurrentIndex(10)

    def open_Female_Search_Age(self):
        self.tabWidget.setCurrentIndex(11)

    def open_Secial_Case_Females(self):
        self.tabWidget.setCurrentIndex(13)

    def open_Secial_Case_Sons(self):
        self.tabWidget.setCurrentIndex(14)

    def open_Edit_Father_Data(self):
        self.tabWidget.setCurrentIndex(15)

    def open_Edit_Mother_Data(self):
        self.tabWidget.setCurrentIndex(16)

    def open_Edit_Sons_Data(self):
        self.tabWidget.setCurrentIndex(17)

    def open_Edit_Lists(self):
        self.tabWidget.setCurrentIndex(18)

    def Open_Add_AftkadDate(self):
        self.tabWidget.setCurrentIndex(19)

    def Open_Search_AftkadDate(self):
        self.tabWidget.setCurrentIndex(20)

    def Open_Search_SpecialStreet(self):
        self.tabWidget.setCurrentIndex(21)

    def Open_Search_NotHaveFather(self):
        self.tabWidget.setCurrentIndex(12)

    def Open_Family_Without_Father(self):
        self.tabWidget.setCurrentIndex(22)

    def Open_Family_Without_Mother(self):
        self.tabWidget.setCurrentIndex(23)

    def Open_Add_Son_Data(self):
        self.tabWidget.setCurrentIndex(24)

    def Open_Azab_Data(self):
        self.tabWidget.setCurrentIndex(25)

    def Open_Armal_Male_Tab(self):
        self.tabWidget.setCurrentIndex(27)

    def Open_Armal_Female_Tab(self):
        self.tabWidget.setCurrentIndex(26)

    def Open_Armal_Male_Tab_Edit(self):
        self.tabWidget.setCurrentIndex(29)

    def Open_Armal_Female_Tab_Edit(self):
        self.tabWidget.setCurrentIndex(28)

    # ------------------------------------------------------------------- #

    # ComboBox Moving Between Added Tabs Aftkad
    def Added_Family_Aftkad_Date_Tab(self):
        self.Open_Add_AftkadDate()
        self.Show_Aftkad_Data_Before_Add_Date()

    def Added_Armla_Tab(self):
        self.Open_Family_Without_Mother()
        self.Read_mMother_Work_In_List()
        self.Read_Street_In_List()
        self.Read_mSon1_Work_In_List()
        self.Read_mSon1_Study_In_List()
        self.Read_mSon2_Work_In_List()
        self.Read_mSon2_Study_In_List()
        self.Read_mSon3_Work_In_List()
        self.Read_mSon3_Study_In_List()
        self.Read_mSon4_Work_In_List()
        self.Read_mSon4_Study_In_List()
        self.Read_mSon5_Work_In_List()
        self.Read_mSon5_Study_In_List()
        self.Read_mSon6_Work_In_List()
        self.Read_mSon6_Study_In_List()
        self.Read_mSon7_Work_In_List()
        self.Read_mSon7_Study_In_List()
        self.Read_mSon8_Work_In_List()
        self.Read_mSon8_Study_In_List()
        self.Read_mSon9_Work_In_List()
        self.Read_mSon9_Study_In_List()
        self.Read_mSon10_Work_In_List()
        self.Read_mSon10_Study_In_List()

    def Added_Armal_Tab(self):
        self.Open_Family_Without_Father()
        self.Read_fFather_Work_In_List()
        self.Read_fFather_Street_In_List()
        self.Read_fSon1_Work_In_List()
        self.Read_fSon1_Study_In_List()
        self.Read_fSon2_Work_In_List()
        self.Read_fSon2_Study_In_List()
        self.Read_fSon3_Work_In_List()
        self.Read_fSon3_Study_In_List()
        self.Read_fSon4_Work_In_List()
        self.Read_fSon4_Study_In_List()
        self.Read_fSon5_Work_In_List()
        self.Read_fSon5_Study_In_List()
        self.Read_fSon6_Work_In_List()
        self.Read_fSon6_Study_In_List()
        self.Read_fSon7_Work_In_List()
        self.Read_fSon7_Study_In_List()
        self.Read_fSon8_Work_In_List()
        self.Read_fSon8_Study_In_List()
        self.Read_fSon9_Work_In_List()
        self.Read_fSon9_Study_In_List()
        self.Read_fSon10_Work_In_List()
        self.Read_fSon10_Study_In_List()

    def Added_Sons_Tab(self):
        self.Open_Add_Son_Data()
        self.Read_Father_Name_From_Table()
        self.Read_Son_sStudy_In_List()
        self.Read_Son_wWork_In_List()

    def Added_Family_Tab(self):
        self.Add_Family()
        self.Read_Father_Street_In_List()
        self.Read_Father_Work_In_List()
        self.Read_Mother_Work_In_List()
        self.Read_Son1_Work_In_List()
        self.Read_Son1_Study_In_List()
        self.Read_Son2_Work_In_List()
        self.Read_Son2_Study_In_List()
        self.Read_Son3_Work_In_List()
        self.Read_Son3_Study_In_List()
        self.Read_Son4_Work_In_List()
        self.Read_Son4_Study_In_List()
        self.Read_Son5_Work_In_List()
        self.Read_Son5_Study_In_List()
        self.Read_Son6_Work_In_List()
        self.Read_Son6_Study_In_List()
        self.Read_Son7_Work_In_List()
        self.Read_Son7_Study_In_List()
        self.Read_Son8_Work_In_List()
        self.Read_Son8_Study_In_List()
        self.Read_Son9_Work_In_List()
        self.Read_Son9_Study_In_List()
        self.Read_Son10_Work_In_List()
        self.Read_Son10_Study_In_List()

    # ComboBox Moving Between Search Tabs Aftkad
    def Search_Family_Tab(self):
        self.open_Search_Family()
        self.Show_FatherAftkad_Name()
        self.Show_MotherAftkad_Name()

    def Search_Date_Aftkad_Tab(self):
        self.Open_Search_AftkadDate()
        self.Show_Aftkad_Data()
        self.Show_Aftkad_Data()

    def Search_Withot_Father_Tabs(self):
        self.Open_Search_NotHaveFather()
        self.Show_Fathers_Not_Have_FatherReconize()
        self.Show_Mothers_Not_Have_FatherReconize()

    def Search_Special_Street_Tabs(self):
        self.Open_Search_SpecialStreet()
        self.Read_Street_Data()

    # ComboBox Moving Between Update Tabs Aftkad
    def Update_Father_Tabs(self):
        self.open_Edit_Father_Data()
        self.Show_Father_Data_For_Edit()
        self.Read_Fatheer_Work_In_List()
        self.Read_Fatheer_Street_In_List()

    def Update_Mother_Tabs(self):
        self.open_Edit_Mother_Data()
        self.Show_Mother_Data_For_Edit()
        self.Read_Motheer_Work_In_List()
        self.Show_Mother_Street()

    def Update_Sons_Tabs(self):
        self.open_Edit_Sons_Data()
        self.Show_Sons_Data_For_Edit()
        self.Read_Sonn_Work_In_List()
        self.Read_Sonn_Study_In_List()

    def Update_EditList_Tabs(self):
        self.open_Edit_Lists()

    def Update_ArmalData_Tabs(self):
        self.Open_Armal_Female_Tab_Edit()
        self.Read_Street_FArmal_Data()
        self.Read_FArmal_Work_In_List()

    def Update_ArmlaData_Tabs(self):
        self.Open_Armal_Male_Tab_Edit()
        self.Read_Street_Data_FemaleArmal()
        self.Read_Mom_Work_In_List_FemaleArmal()

    # ComboBox Moving Between Reports Tabs Aftkad
    def Report_Armala_Tabs(self):
        self.open_Female_Armal()
        self.Females_Armals()

    def Report_Sons_SpecialCase_Tabs(self):
        self.open_Secial_Case_Sons()
        self.Special_Case_Sons()

    def Report_Female_SpecialCase_Tabs(self):
        self.open_Secial_Case_Females()
        self.Special_Case_Females()

    def Report_Male_SpecialCase_Tabs(self):
        self.open_Secial_Case()
        self.Special_Case_Mans()

    def Report_Armal_Tabs(self):
        self.open_Man_Armal()
        self.Mans_Armals()

    def Report_Family_Aftkad_Tab(self):
        self.open_To_Show__All_Family()
        self.Show_All_Family_Data()
        self.Show_All_Sons_Family_Data()

    def Report_A3zabs_Tabs(self):
        self.Open_Azab_Data()
        self.Street_Combo_Male_and_Female_A3zab()
        self.Work_Combo_Male_and_Female_A3zab()

    def Report_Jobs_Tabs(self):
        self.open_Work_Tab()
        self.Read_Fatherr_Work_In_List()
        self.Read_Motherr_Work_In_List()
        self.Read_Son_Work_In_List()

    def Report_Study_Tabs(self):
        self.open_Student_Tab()
        self.Read_Son_Study_In_List()

    def Report_Mage_Tabs(self):
        self.open_Man_Search_Age()

    def Report_Fage_Tabs(self):
        self.open_Female_Search_Age()

    def Report_Armalage_Tabs(self):
        self.Open_Armal_Male_Tab()

    def Report_ArmalaAge_(self):
        self.Open_Armal_Female_Tab()

    # ===============================================================================================
    # ============================== Record Family Aftkad ===========================================
    # ===============================================================================================
    # Father

    def Record_Father_Data(self):
        Name = self.lineEdit.text()
        Ssn = self.lineEdit_2.text()
        Street = self.comboBox_15.currentText()
        Address = self.lineEdit_3.text()
        Qulified = self.lineEdit_4.text()
        Work = self.comboBox.currentText()
        Phone = self.lineEdit_8.text()
        Father = self.lineEdit_5.text()
        Age = self.dateEdit_16.date()
        Age = Age.toPyDate()
        ChildNum = self.spinBox_7.value()
        State = 'متزوج'


        Stutus = 'لا'
        if self.checkBox.isChecked():
            Stutus = 'نعم'
            

        if self.lineEdit_10.text() == '':
            Type = 'سليم'
        else:
            Type = self.lineEdit_10.text()

        MName = self.lineEdit_68.text()
        MPhone = self.lineEdit_70.text()
        MSsn = self.lineEdit_67.text()

        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO FatherAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (
        Name, Ssn, Work, Street, Address, Qulified, Father, ChildNum, Age, Phone, State, Stutus, Type, MName, MPhone,
        MSsn))
        db.commit()
        db.close()
        QMessageBox.information(QWidget(), "جيد", 'تمت حفظ بيانات الاب بنجاح')

    # ===============================================================================================
    # ============================== Check Family Aftkad ============================================
    # ===============================================================================================

    def Check_Father_Data(self):
        Name = self.lineEdit.text()
        Street = self.comboBox_15.currentText()
        Address = self.lineEdit_3.text()
        Qulified = self.lineEdit_4.text()
        Work = self.comboBox.currentText()
        ChildNum = self.spinBox_7.value()
        Age = self.dateEdit_16.date()
        Age = Age.toPyDate()
        Ssn = self.lineEdit_2.text()
        Phone = self.lineEdit_8.text()

        if Name == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم رب الاسرة  ')

        if Address == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال العنوان  ')

        if Qulified == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال المؤهل   ')

        if Work == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم العمل  ')

        if Street == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الشارع  ')

        if Name.strip(" ") != '' and Street.strip(" ") != '' and Address.strip(" ") != '' and Qulified.strip(
                " ") != '' and Work != ''and  Phone != '' and len(Phone) == 11 and int(Phone) != str(Phone) and len(Ssn) == 14 and int(Ssn) != str(Ssn) or Ssn == "" :

            if ChildNum == 0 and Name.strip(" ") != '' and Street.strip(" ") != '' and Address.strip(" ") != '':
                Replay = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من عدد الابناء   ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes and Name != '' and Street != '' and Address != '':
                    X = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من تاريخ الميلاد   ؟!!',
                                                QMessageBox.Yes | QMessageBox.No)
                    if X == QMessageBox.Yes:
                            self.tabWidget_2.setEnabled(True)
            else:
                X = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من تاريخ الميلاد   ؟!!',
                                            QMessageBox.Yes | QMessageBox.No)
                if X == QMessageBox.Yes and Name != '' and Street != '' and Address != '':
                        self.tabWidget_2.setEnabled(True)
        else:
            QMessageBox.information(self, 'معذرة', 'يرجي التاكد من رقميه العدد القومي او الهاتف')

    # ===============================================================================================
    # ============================= Record Family Aftkad ============================================
    # ===============================================================================================
    # Mother

    def Record_Mother_Data(self):
        Name = self.lineEdit_68.text()
        Ssn = self.lineEdit_67.text()
        Qulified = self.lineEdit_6.text()
        Father = self.lineEdit_69.text()
        Work = self.comboBox_2.currentText()
        Phone = self.lineEdit_70.text()
        Age = self.dateEdit_13.date()
        Age = Age.toPyDate()
        Stutus = 'لا'
        if self.checkBox_12.isChecked():
            Stutus = 'نعم'

        Type = self.lineEdit_107.text()
        if Type != '':
            Type = self.lineEdit_107.text()
        else:
            Type = 'سليمه'
        Address = self.lineEdit_3.text()
        Street = self.comboBox_15.currentText()
        Fphone = self.lineEdit_8.text()
        FSsn = self.lineEdit_2.text()
        FName = self.lineEdit.text()

        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO MotherAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (Name, Ssn, Qulified, Father, Work, Phone, Age, Stutus, Type, FSsn, FName, Fphone, Address, Street))
        db.commit()
        db.close()
        QMessageBox.information(QWidget(), "جيد", 'تمت حفظ بيانات الام بنجاح')

    # ===============================================================================================
    # ============================== Check Family Aftkad ============================================
    # ===============================================================================================
    # Mother

    def Check_Mother_Data(self):
        Name = self.lineEdit_68.text()
        Qulified = self.lineEdit_6.text()
        Work = self.comboBox_2.currentText()
        DOB = self.dateEdit_13.date()
        DOB = DOB.toPyDate()
        value = self.spinBox_7.value()
        Ssn = self.lineEdit_67.text()
        Phone = self.lineEdit_70.text()

        if Name == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الام  ')

        if Qulified == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال مؤهل الام   ')

        if Work == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم عمل الام   ')

        if Name.strip(" ") != '' and Qulified.strip(" ") != '' and Work.strip(" ") != '' and Phone != '' and len(Phone) == 11 and int(Phone) != str(Phone) and len(Ssn) == 14 and int(Ssn) != str(Ssn) or Ssn == "":
            if value == 0 and Name != '' and Qulified != '' and Work != '':
                Replay = QMessageBox.information(QWidget(), 'رجاءا ', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes:
                    self.pushButton_21.setEnabled(True)

            elif value != 0:
                self.Make_All_Button_Next_Visible_True()
                self.Choice_Son_Num()

        else:
            QMessageBox.information(self, 'معذرة', 'يرجي التاكد من رقميه العدد القومي او الهاتف')

    # ===============================================================================================
    # =========================== Printing in Family Aftkad Program =================================
    # ===============================================================================================

    # Report All Family Data

    def savefileOffAallFamilyData(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            x = self.tableWidget.model()

            model = x
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass


    # Report For Female Armal Data

    def savefileFemaleArmals(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_10.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Male Armal Data

    def savefileMaleArmals(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_9.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Work Data

    def savefileWorks(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_12.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For SpecialCase Data

    def savefileSpecialCase(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_11.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Man By Age Data

    def savefileManByAge(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_14.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Female By Age Data

    def savefileFemaleByAge(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_15.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Female By Age Data

    def savefileStudent(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_13.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Female By Age Data

    def savefileSons(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_2.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report For Female By Age Data

    def savefileFemales_SpecialCase(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_25.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report All Sons Data Special Cases

    def savefileSons_SpecialCase(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_26.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report Mother Work

    def savefileMother_Work(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_27.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report Sons Work

    def savefileSons_Work(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_28.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report Street Special Data

    def savefileReport_StreetData(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_19.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report Females Without Father

    def savefileReport_FemaleWithoutFather(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_21.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report Mans Without Father

    def savefileReport_ManWithoutFather(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_20.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report All Family Aftkad

    def savefileReport_Family_Aftkad(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_6.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report All A3zab Data

    def savefileReport_A3zabs_Data(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_32.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass

    # Report Only One Family Has Searched

    def savefileReport_OnlyOneFamilySearched(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.tableWidget_33.model()
            for c in range(model.columnCount()):
                text = model.headerData(c, QtCore.Qt.Horizontal)
                sheet.write(0, c + 1, text, style=style)

            for r in range(model.rowCount()):
                text = model.headerData(r, QtCore.Qt.Vertical)
                sheet.write(r + 1, 0, text, style=style)

            for c in range(model.columnCount()):
                for r in range(model.rowCount()):
                    text = model.data(model.index(r, c))
                    sheet.write(r + 1, c + 1, text)
            wbk.save(filename)
        except:
            pass
    # ===============================================================================================
    # =================================== Sons Tabs =================================================
    # ===============================================================================================

    def open_1st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(0)

    def open_2st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(1)

    def open_3st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(2)

    def open_4st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(3)

    def open_5st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(4)

    def open_6st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(5)

    def open_7st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(6)

    def open_8st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(7)

    def open_9st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(8)

    def open_10st_Son_Tab(self):
        self.tabWidget_4.setCurrentIndex(9)
    # ===============================================================================================
    # =================================== Constrains Sons Tabs Data =================================
    # ===============================================================================================

    # 1- Validate To Go Next Son

    # 2- Set Button Save Visability True

    def On_Mouse_Click_in_1st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()
        SName = self.lineEdit_17.text()
        Study = self.comboBox_28.currentText()
        Job = self.comboBox_3.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_2st_Son_Tab()

    def On_Mouse_Click_in_1st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_17.text()
        Study = self.comboBox_28.currentText()
        Job = self.comboBox_3.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_2st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_23.text()
        Study = self.comboBox_29.currentText()
        Job = self.comboBox_4.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_3st_Son_Tab()

    def On_Mouse_Click_in_2st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_23.text()
        Study = self.comboBox_29.currentText()
        Job = self.comboBox_4.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_3st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_27.text()
        Study = self.comboBox_30.currentText()
        Job = self.comboBox_5.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_4st_Son_Tab()

    def On_Mouse_Click_in_3st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_27.text()
        Study = self.comboBox_30.currentText()
        Job = self.comboBox_5.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_4st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()
        SName = self.lineEdit_32.text()
        Study = self.comboBox_31.currentText()
        Job = self.comboBox_6.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_5st_Son_Tab()

    def On_Mouse_Click_in_4st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()
        SName = self.lineEdit_32.text()
        Study = self.comboBox_31.currentText()
        Job = self.comboBox_6.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_5st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_37.text()
        Study = self.comboBox_48.currentText()
        Job = self.comboBox_7.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_6st_Son_Tab()

    def On_Mouse_Click_in_5st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_37.text()
        Study = self.comboBox_48.currentText()
        Job = self.comboBox_7.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_6st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_41.text()
        Study = self.comboBox_32.currentText()
        Job = self.comboBox_8.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_7st_Son_Tab()

    def On_Mouse_Click_in_6st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_41.text()
        Study = self.comboBox_32.currentText()
        Job = self.comboBox_8.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_7st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_44.text()
        Study = self.comboBox_33.currentText()
        Job = self.comboBox_9.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_8st_Son_Tab()

    def On_Mouse_Click_in_7st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_44.text()
        Study = self.comboBox_33.currentText()
        Job = self.comboBox_9.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_8st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_48.text()
        Study = self.comboBox_34.currentText()
        Job = self.comboBox_10.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_9st_Son_Tab()

    def On_Mouse_Click_in_8st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_48.text()
        Study = self.comboBox_34.currentText()
        Job = self.comboBox_10.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_9st_Son(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_52.text()
        Study = self.comboBox_35.currentText()
        Job = self.comboBox_11.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.open_10st_Son_Tab()

    def On_Mouse_Click_in_9st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_52.text()
        Study = self.comboBox_35.currentText()
        Job = self.comboBox_11.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    def On_Mouse_Click_in_10st_Sonn(self):
        FName = self.lineEdit.text()
        MName = self.lineEdit_68.text()

        SName = self.lineEdit_56.text()
        Study = self.comboBox_36.currentText()
        Job = self.comboBox_12.currentText()
        if SName == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم الابن   ')
        if Study == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال دراسة الابن   ')
        if Job == '':
            QMessageBox.information(self, 'رجاءا', 'يرجي ادخال اسم وظيفه الابن   ')

        if FName.strip(" ") != "" and MName.strip(" ") != "" and SName.strip(" ") != "" and Study != '' and Job != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_21.setEnabled(True)

    # ==============================================================================
    def Enable_Mother_Tab(self):
        self.tabWidget_2.setEnabled(True)

    # ===============================================================================================
    # ===================================Choice Sons Tabs Num Of Sons ===============================
    # ===============================================================================================

    def Choice_Son_Num(self):
        try:
            User_Choice = self.spinBox_7.value()
            if User_Choice == 0:
                self.tabWidget_4.setEnabled(False)
            elif User_Choice == 1:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton.setEnabled(False)
            elif User_Choice == 2:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_2.setEnabled(False)
            elif User_Choice == 3:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_4.setEnabled(False)
            elif User_Choice == 4:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_5.setEnabled(False)
            elif User_Choice == 5:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_6.setEnabled(False)
            elif User_Choice == 6:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_7.setEnabled(False)
            elif User_Choice == 7:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_8.setEnabled(False)
            elif User_Choice == 8:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_9.setEnabled(False)
            elif User_Choice == 9:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
                self.pushButton_10.setEnabled(False)
            elif User_Choice == 10:
                self.tabWidget_4.setEnabled(True)
                self.tabWidget_4.setCurrentIndex(0)
            else:
                QMessageBox.information(QWidget(), "للاسف!!", 'عدد الابناء متاح الي 10 ابناء فقط')
        except:
            QMessageBox.information(QWidget(), "للاسف!!", 'عدد الابناء متاح الي 10 ابناء فقط')

    # ===============================================================================================
    # ============================== Choice Sons Tabs Num Of Sons Records ===========================
    # ===============================================================================================

    def Choice_Record_Sons_Num_Data(self):
        try:
            User_Choice = self.spinBox_7.value()
            if User_Choice == 0:
                pass
            if User_Choice == 1:
                self.Record_1st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابن بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 2:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 3:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 4:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 5:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                self.Record_5st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 6:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                self.Record_5st_Son_Data()
                self.Record_6st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 7:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                self.Record_5st_Son_Data()
                self.Record_6st_Son_Data()
                self.Record_7st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 8:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                self.Record_5st_Son_Data()
                self.Record_6st_Son_Data()
                self.Record_7st_Son_Data()
                self.Record_8st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 9:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                self.Record_5st_Son_Data()
                self.Record_6st_Son_Data()
                self.Record_7st_Son_Data()
                self.Record_8st_Son_Data()
                self.Record_9st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            if User_Choice == 10:
                self.Record_1st_Son_Data()
                self.Record_2st_Son_Data()
                self.Record_3st_Son_Data()
                self.Record_4st_Son_Data()
                self.Record_5st_Son_Data()
                self.Record_6st_Son_Data()
                self.Record_7st_Son_Data()
                self.Record_8st_Son_Data()
                self.Record_9st_Son_Data()
                self.Record_10st_Son_Data()
                QMessageBox.information(self, 'جيد', 'تم حفظ بيانات الابناء بنجاح  ')
                self.Clear_Data_Of_Family_Of_Aftkad()
            else:
               pass
        except:
            pass

    # ===============================================================================================
    # ============================== Choice Sons Tabs Num Of Sons Records ===========================
    # ===============================================================================================

    def Check_On_Click_Sons_Tab_Of_Family_Aftkad(self):
        try:
            User_Choice = self.spinBox_7.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.On_Mouse_Click_in_1st_Sonn()
            elif User_Choice == 2:
                self.On_Mouse_Click_in_2st_Sonn()
            elif User_Choice == 3:
                self.On_Mouse_Click_in_3st_Sonn()
            elif User_Choice == 4:
                self.On_Mouse_Click_in_4st_Sonn()
            elif User_Choice == 5:
                self.On_Mouse_Click_in_5st_Sonn()
            elif User_Choice == 6:
                self.On_Mouse_Click_in_6st_Sonn()
            elif User_Choice == 7:
                self.On_Mouse_Click_in_7st_Sonn()
            elif User_Choice == 8:
                self.On_Mouse_Click_in_8st_Sonn()
            elif User_Choice == 9:
                self.On_Mouse_Click_in_9st_Sonn()
            elif User_Choice == 10:
                self.On_Mouse_Click_in_10st_Sonn()
        except:
            pass

    # ===============================================================================================
    # ============================== Choice Sons Num Of Sons Records ================================
    # ===============================================================================================

    def Record_1st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()

        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()
        SSsn = self.lineEdit_46.text()
        SName = self.lineEdit_17.text()
        SFather = self.lineEdit_19.text()
        SPhone = self.lineEdit_20.text()
        Gender = 'ولد'
        if self.radioButton_32.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_28.currentText()
        Job = self.comboBox_3.currentText()
        Stutus = 'لا'
        if self.checkBox_2.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_108.text()
        Age = self.dateEdit_3.date()
        Age = Age.toPyDate()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (
                  SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName, Gender,
                  Type,SSsn))
        db.commit()
        db.close()

    def Record_2st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()

        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()
        SSsn = self.lineEdit_60.text()
        SName = self.lineEdit_23.text()
        SFather = self.lineEdit_24.text()
        SPhone = self.lineEdit_25.text()
        Gender = 'ولد'
        if self.radioButton_34.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_29.currentText()
        Job = self.comboBox_4.currentText()
        Stutus = 'لا'
        if self.checkBox_3.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_110.text()
        Age = self.dateEdit_4.date()
        Age = Age.toPyDate()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_3st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SSsn =self.lineEdit_61.text()
        SName = self.lineEdit_27.text()
        SFather = self.lineEdit_28.text()
        SPhone = self.lineEdit_29.text()
        Gender = 'ولد'
        if self.radioButton_80.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_30.currentText()
        Job = self.comboBox_5.currentText()
        Stutus = 'لا'
        if self.checkBox_23.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_112.text()
        Age = self.dateEdit_5.date()
        Age = Age.toPyDate()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_4st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_32.text()
        SFather = self.lineEdit_33.text()
        SPhone = self.lineEdit_34.text()
        Gender = 'ولد'
        if self.radioButton_42.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_31.currentText()
        Job = self.comboBox_6.currentText()
        Stutus = 'لا'
        if self.checkBox_5.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_113.text()
        Age = self.dateEdit_6.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_62.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_5st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_37.text()
        SFather = self.lineEdit_38.text()
        SPhone = self.lineEdit_39.text()
        Gender = 'ولد'
        if self.radioButton_84.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_48.currentText()
        Job = self.comboBox_7.currentText()
        Stutus = 'لا'
        if self.checkBox_25.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_116.text()
        Age = self.dateEdit_7.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_63.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_6st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_41.text()
        SFather = self.lineEdit_42.text()
        SPhone = self.lineEdit_43.text()
        Gender = 'ولد'
        if self.radioButton_46.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_32.currentText()
        Job = self.comboBox_8.currentText()
        Stutus = 'لا'
        if self.checkBox_7.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_117.text()
        Age = self.dateEdit_8.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_64.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_7st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_44.text()
        SFather = self.lineEdit_45.text()
        SPhone = self.lineEdit_47.text()
        Gender = 'ولد'
        if self.radioButton_48.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_33.currentText()
        Job = self.comboBox_9.currentText()
        Stutus = 'لا'
        if self.checkBox_8.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_118.text()
        Age = self.dateEdit_9.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_72.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_8st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_48.text()
        SFather = self.lineEdit_49.text()
        SPhone = self.lineEdit_51.text()
        Gender = 'ولد'
        if self.radioButton_50.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_34.currentText()
        Job = self.comboBox_10.currentText()
        Stutus = 'لا'
        if self.checkBox_9.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_119.text()
        Age = self.dateEdit_10.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_73.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_9st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_52.text()
        SFather = self.lineEdit_53.text()
        SPhone = self.lineEdit_55.text()
        Gender = 'ولد'
        if self.radioButton_52.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_35.currentText()
        Job = self.comboBox_11.currentText()
        Stutus = 'لا'
        if self.checkBox_10.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_120.text()
        Age = self.dateEdit_11.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_74.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    def Record_10st_Son_Data(self):
        FName = self.lineEdit.text()
        FSsn = self.lineEdit_2.text()
        FPhone = self.lineEdit_8.text()
        if self.lineEdit_68.text() == '':
            MName = '--------'
        else:
            MName = self.lineEdit_68.text()
        if self.lineEdit_67.text() == '':
            MSsn = '--------'
        else:
            MSsn = self.lineEdit_67.text()
        if self.lineEdit_70.text() == '':
            MPhone = '--------'
        else:
            MPhone = self.lineEdit_70.text()

        SName = self.lineEdit_56.text()
        SFather = self.lineEdit_57.text()
        SPhone = self.lineEdit_59.text()
        Gender = 'ولد'
        if self.radioButton_54.isChecked():
            Gender = 'بنت'
        Study = self.comboBox_36.currentText()
        Job = self.comboBox_12.currentText()
        Stutus = 'لا'
        if self.checkBox_11.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_121.text()
        Age = self.dateEdit_12.date()
        Age = Age.toPyDate()
        SSsn = self.lineEdit_111.text()
        if FName.strip(" ") != "" and MName.strip(" ") != "" and FSsn.strip(" ") != "" and FPhone.strip(
                " ") != "" and MSsn.strip(" ") != "" and MPhone.strip(" ") != "" and SName.strip(" ") != "":
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (
                          SName, SFather, Age, SPhone, Job, Study, Stutus, MSsn, FSsn, MPhone, FPhone, MName, FName,
                          Gender,Type,SSsn))
            db.commit()
            db.close()

    # ===============================================================================================
    # ====================================  Clear Sons Line Edits ===================================
    # ===============================================================================================

    def Clear_Data_Of_Family_Of_Aftkad(self):
        self.tabWidget_4.setEnabled(False)
        self.tabWidget_2.setEnabled(False)
        self.tabWidget_4.setCurrentIndex(0)
        # Family Data LineEdits
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_68.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_67.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_69.setText('')
        self.lineEdit_70.setText('')
        self.lineEdit_107.setText('')
        self.comboBox.setCurrentIndex(0)
        self.comboBox_15.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.spinBox_7.setValue(0)
        # 1st Sons
        self.lineEdit_17.setText('')
        self.lineEdit_20.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_108.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_28.setCurrentIndex(0)
        # 2st Sons
        self.lineEdit_23.setText('')
        self.lineEdit_25.setText('')
        self.lineEdit_24.setText('')
        self.lineEdit_110.setText('')
        self.comboBox_29.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        # 3st Sons
        self.lineEdit_27.setText('')
        self.lineEdit_29.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_112.setText('')
        self.comboBox_30.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        # 4st Sons
        self.lineEdit_32.setText('')
        self.lineEdit_34.setText('')
        self.lineEdit_33.setText('')
        self.lineEdit_113.setText('')
        self.comboBox_31.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        # 5st Sons
        self.lineEdit_37.setText('')
        self.lineEdit_39.setText('')
        self.lineEdit_38.setText('')
        self.lineEdit_116.setText('')
        self.comboBox_48.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        # 6st Sons
        self.lineEdit_41.setText('')
        self.lineEdit_43.setText('')
        self.lineEdit_42.setText('')
        self.lineEdit_117.setText('')
        self.comboBox_32.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        # 7st Sons
        self.lineEdit_44.setText('')
        self.lineEdit_45.setText('')
        self.lineEdit_47.setText('')
        self.lineEdit_118.setText('')
        self.comboBox_33.setCurrentIndex(0)
        self.comboBox_9.setCurrentIndex(0)
        # 8st Sons
        self.lineEdit_48.setText('')
        self.lineEdit_51.setText('')
        self.lineEdit_49.setText('')
        self.lineEdit_119.setText('')
        self.comboBox_34.setCurrentIndex(0)
        self.comboBox_10.setCurrentIndex(0)
        # 9st Sons
        self.lineEdit_52.setText('')
        self.lineEdit_55.setText('')
        self.lineEdit_53.setText('')
        self.lineEdit_120.setText('')
        self.comboBox_35.setCurrentIndex(0)
        self.comboBox_11.setCurrentIndex(0)
        # 10st Sons
        self.lineEdit_56.setText('')
        self.lineEdit_59.setText('')
        self.lineEdit_57.setText('')
        self.lineEdit_121.setText('')
        self.comboBox_36.setCurrentIndex(0)
        self.comboBox_12.setCurrentIndex(0)

        self.lineEdit_46.setText('')
        self.lineEdit_60.setText('')
        self.lineEdit_61.setText('')
        self.lineEdit_62.setText('')
        self.lineEdit_63.setText('')
        self.lineEdit_64.setText('')
        self.lineEdit_72.setText('')
        self.lineEdit_73.setText('')
        self.lineEdit_74.setText('')
        self.lineEdit_111.setText('')
        self.pushButton_21.setEnabled(False)
        self.Make_All_Button_Next_Visible_True()
    def Make_All_Button_Next_Visible_True(self):
        self.pushButton_10.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)

    # ===============================================================================================
    # =============================== Tab Of Show All Family Data ===================================
    # ===============================================================================================

    def Show_All_Family_Data(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT F.Name, M.Name , F.Street, F.Address, F.Work, F.DOF, M.Work , M.DOF , F.Phone, M.Phone,F.ChildNum  
        FROM FatherAftkad as F JOIN MotherAftkad as M where F.Name = M.FName 
        '''
        Result = conect.execute(query)
        Result = Result.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    def Show_All_Sons_Family_Data(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        query = '''
        SELECT Name , FName  , Study , DOF , Phone  FROM SonsAftkad order by FName
        '''

        Result = conect.execute(query)
        self.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conect.close()

    # ===============================================================================================
    # ======================= Searching Family By Father Name or MotherName =========================
    # ===============================================================================================

    # Show Father Name in ComboBox For Searching

    def Show_FatherAftkad_Name(self):
        self.comboBox_64.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from FatherAftkad order by Name ')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_64.addItem(str(i[0]))

    # Show Mother Name in ComboBox For Searching

    def Show_MotherAftkad_Name(self):
        self.comboBox_65.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from MotherAftkad order by Name')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_65.addItem(str(i[0]))

    # Search Family Across Father Name

    def Search_Family_Aftkad(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        Name = self.comboBox_64.currentText()
        query = '''
        SELECT Name,Street,Address,Ssn,Work,Qulified,Phone,ChildNum,SpecialCase from FatherAftkad WHERE Name=? and Not Name =? order by Name
        '''
        Names = ''
        Result = conect.execute(query, [(Name), (Names)])
        Z = Result.fetchall()
        query = '''
        SELECT Name,FName,Ssn,Father,Phone,Work,Qulified,SpecialCase,Type FROM MotherAftkad WHERE FName=? and Not Name =? 
        '''
        Result = conect.execute(query, [(Name), (Names)])
        X = Result.fetchall()

        query = '''
        SELECT Name,FName,Gender,Study,Work,Father,Phone,Stutus,TypeInjurd from SonsAftkad WHERE FName=? and Not Name =? order by Name
        '''

        Result = conect.execute(query, [(Name), (Names)])
        Y = Result.fetchall()
        s = [(
             '--------------', '--------------', '--------------', '--------------', '--------------', '--------------',
             '--------------', '--------------', '--------------')]
        TitleM = [('اسم الام', 'الزوج ', 'الرقم القومي', 'اب الاعتراف', 'الموبيل', 'الوظيفه', 'المؤهل', 'حاله خاصه ؟',
                   'نوع الاعاقه')]
        TitleS = [('اسم الابن', 'الاب ', 'الجنس', ' الدراسه', 'الوظيفه', 'اب الاعتراف', 'الموبيل', 'حاله خاصه ؟',
                   'نوع الاعاقه')]
        Result = Z + s + TitleM + s + X + s + TitleS + s + Y

        self.tableWidget_33.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_33.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_33.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.Cleara()

    # Search Family Across Mother Name

    def Search_Family_Mother_Name(self):
        conect = sqlite3.connect('Akhwet_El_Rab.db')
        Name = self.comboBox_65.currentText()
        query = '''
        SELECT Name,Street,Address,Ssn,Work,Qulified,Phone,ChildNum,SpecialCase from FatherAftkad WHERE MName=? and Not Name =? order by Name
        '''
        Names = ''
        Result = conect.execute(query, [(Name), (Names)])
        Z = Result.fetchall()
        query = '''
        SELECT Name,FName,Ssn,Father,Phone,Work,Qulified,SpecialCase,Type FROM MotherAftkad WHERE Name=? and Not Name =? 
        '''
        Result = conect.execute(query, [(Name), (Names)])
        X = Result.fetchall()

        query = '''
        SELECT Name,FName,Gender,Study,Work,Father,Phone,Stutus,TypeInjurd from SonsAftkad WHERE MName=? and Not Name =? order by Name
        '''

        Result = conect.execute(query, [(Name), (Names)])
        Y = Result.fetchall()
        s = [(
             '--------------', '--------------', '--------------', '--------------', '--------------', '--------------',
             '--------------', '--------------', '--------------')]
        TitleM = [('اسم الام', 'الزوج ', 'الرقم القومي', 'اب الاعتراف', 'الموبيل', 'الوظيفه', 'المؤهل', 'حاله خاصه ؟',
                   'نوع الاعاقه')]
        TitleS = [('اسم الابن', 'الاب ', 'الجنس', ' الدراسه', 'الوظيفه', 'اب الاعتراف', 'الموبيل', 'حاله خاصه ؟',
                   'نوع الاعاقه')]
        Result = Z + s + TitleM + s + X + s + TitleS + s + Y

        self.tableWidget_33.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_33.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_33.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.Clearas()

    # Clearing

    def Cleara(self):
        self.comboBox_64.setCurrentIndex(0)

    def Clearas(self):
        self.comboBox_65.setCurrentIndex(0)

    # ===============================================================================================
    # ======================= Clear Data Father And Mother After Recorded ===========================
    # ===============================================================================================

    def Clear_Data_From_Record_Data(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_68.setText('')
        self.lineEdit_67.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_69.setText('')
        self.lineEdit_70.setText('')
        self.lineEdit_107.setText('')
        self.lineEdit_17.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_20.setText('')
        self.lineEdit_108.setText('')
        self.lineEdit_23.setText('')
        self.lineEdit_24.setText('')
        self.lineEdit_25.setText('')
        self.lineEdit_110.setText('')
        self.lineEdit_27.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_29.setText('')
        self.lineEdit_112.setText('')
        self.lineEdit_32.setText('')
        self.lineEdit_33.setText('')
        self.lineEdit_34.setText('')
        self.lineEdit_113.setText('')
        self.lineEdit_37.setText('')
        self.lineEdit_38.setText('')
        self.lineEdit_39.setText('')
        self.lineEdit_116.setText('')
        self.lineEdit_41.setText('')
        self.lineEdit_42.setText('')
        self.lineEdit_43.setText('')
        self.lineEdit_117.setText('')
        self.lineEdit_44.setText('')
        self.lineEdit_45.setText('')
        self.lineEdit_47.setText('')
        self.lineEdit_118.setText('')
        self.lineEdit_48.setText('')
        self.lineEdit_49.setText('')
        self.lineEdit_51.setText('')
        self.lineEdit_119.setText('')
        self.lineEdit_52.setText('')
        self.lineEdit_53.setText('')
        self.lineEdit_55.setText('')
        self.lineEdit_120.setText('')
        self.lineEdit_56.setText('')
        self.lineEdit_57.setText('')
        self.lineEdit_59.setText('')
        self.lineEdit_121.setText('')
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_28.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_29.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_30.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_31.setCurrentIndex(0)
        self.spinBox_7.setValue(0)
        self.tabWidget_4.setEnabled(False)
        self.tabWidget_4.setCurrentIndex(0)

    # STOP IN COMBO SON NUM 5
    def Clear_After_Choice_Work(self):
        self.comboBox_13.setCurrentIndex(0)
        self.comboBox_27.setCurrentIndex(0)
        self.comboBox_50.setCurrentIndex(0)

    def Clear_After_Choice_Study(self):
        self.comboBox_37.setCurrentIndex(0)

    # ===============================================================================================
    # =================================== Run The 18 Function of Search =============================
    # ===============================================================================================

    def Search_Family_bY_FatherName(self):
        Name = self.lineEdit_46.text()
        if Name == '':
            QMessageBox.warning(self, 'معذرة', 'برجاء التامد من الحقل  !!! ')
        else:
            self.Seaarch_Family_Father_By_Name()
            self.Search_Mothr_Data_By_Name()
            self.Search_Sons_Data_By_Name()
            self.Clear_After_Search_Father_Name_and_All_Search()

    def Search_Family_By_FPhone(self):
        Phone = self.lineEdit_61.text()
        if Phone == '':
            QMessageBox.warning(self, 'معذرة', 'برجاء التامد من الحقل  !!! ')
        else:
            self.Seaarch_Family_Father_By_Phone()
            self.Search_Mothr_Data_By_Phone()
            self.Search_Sons_Data_By_Phone()
            self.Clear_After_Search_Father_Name_and_All_Search()

    def Search_Family_By_FSsn(self):
        Ssn = self.lineEdit_63.text()
        if Ssn == '':
            QMessageBox.warning(self, 'معذرة', 'برجاء التامد من الحقل  !!! ')
        else:
            self.Seaarch_Family_Father_By_Ssn()
            self.Search_Mothr_Data_By_Ssn()
            self.Search_Sons_Data_By_Ssn()
            self.Clear_After_Search_Father_Name_and_All_Search()

    def Search_Family_By_MotherName(self):
        Name = self.lineEdit_60.text()
        if Name == '':
            QMessageBox.warning(self, 'معذرة', 'برجاء التامد من الحقل  !!! ')
        else:
            self.Seaarch_Family_Mother_By_Name_From_Motherr()
            self.Search_FROM_MOTHER_Sons_Data_By_Name()
            self.Seaarch_Family_From_MotherTo_Father_By_Name()
            self.Clear_After_Search_Father_Name_and_All_Search()

    def Search_Family_By_MPhone(self):
        Phone = self.lineEdit_62.text()
        if Phone == '':
            QMessageBox.warning(self, 'معذرة', 'برجاء التامد من الحقل  !!! ')
        else:
            self.Seaarch_Family_Mother_By_Phone_From_Mother()
            self.Search_FROM_MOTHER_Sons_Data_By_Phone()
            self.Seaarch_Family_From_MotherTo_Father_By_Phone()
            self.Clear_After_Search_Father_Name_and_All_Search()

    def Search_Family_By_MSsn(self):
        Ssn = self.lineEdit_64.text()
        if Ssn == '':
            QMessageBox.warning(self, 'معذرة', 'برجاء التامد من الحقل  !!! ')
        else:
            self.Search_Mothr_Data_By_Ssn()
            self.Search_FROM_MOTHER_Sons_Data_By_Ssn()
            self.Seaarch_Family_From_MotherTo_Father_By_Ssn()
            self.Clear_After_Search_Father_Name_and_All_Search()

    def Clear_After_Search_Father_Name_and_All_Search(self):
        self.lineEdit_46.setText('')
        self.lineEdit_61.setText('')
        self.lineEdit_63.setText('')
        self.lineEdit_60.setText('')
        self.lineEdit_62.setText('')
        self.lineEdit_64.setText('')

    # ===============================================================================================
    # =================================== Show All Armals Data ======================================
    # ===============================================================================================
    # Fathers Armals

    def Mans_Armals(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Street,Address,Phone,Work,Qulified,Father,DOB,ChildNum,Name FROM MotherDead Where Relation=? and NOT FName = ? '''
        Name = 'ارمل'
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        db.close()
    # ===============================================================================================
    # =================================== Show All Armls Data By  Filter Them ======================
    # ===============================================================================================

    # Filter By Name
    def Search_MotherDead_By_Name_Filter(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Street,Address,Phone,Work,Qulified,Father,DOB,ChildNum,Name FROM MotherDead Where FName LIKE ('%' || ? || '%') and NOT FName = ?'''
        Name = self.lineEdit_168.text()
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    # Filter BY Phone
    def Search_MotherDead_By_Phone_Filter(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Street,Address,Phone,Work,Qulified,Father,DOB,ChildNum,Name FROM MotherDead Where Phone LIKE ('%' || ? || '%') and NOT FName = ?'''
        Name = self.lineEdit_169.text()
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_9.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # ===============================================================================================
    # =================================== Show All Armalas Data ======================================
    # ===============================================================================================

    # Mother Armals
    def Females_Armals(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT MName,Street,Address,Phone,Work,Qulified,Father,DOF,ChildNum,Name FROM FatherDead Where Relation=? and NOT MName=?'''
        Name = 'ارمله'
        S=""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_10.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # =================================== Show All Armals Data By  Filter Them ======================
    # ===============================================================================================
    # Filter By Name
    def Search_FatherDead_By_Name_Filter(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT MName,Street,Address,Phone,Work,Qulified,Father,DOF,ChildNum,Name FROM FatherDead Where MName LIKE ('%' || ? || '%') and NOT MName = ?'''
        Name = self.lineEdit_171.text()
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_10.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    # Filter BY Phone
    def Search_FatherDead_By_Phone_Filter(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT MName,Street,Address,Phone,Work,Qulified,Father,DOF,ChildNum,Name FROM FatherDead Where Phone LIKE ('%' || ? || '%') and NOT MName = ?'''
        Name = self.lineEdit_170.text()
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_10.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # ===============================================================================================
    # =================================== Show All Mans Of Special Cases ============================
    # ===============================================================================================

    def Special_Case_Mans(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone,DOF,State,TypeInjured,MName FROM FatherAftkad Where SpecialCase=? and NOT Name = ? '''
        Name = 'نعم'
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        sql = '''SELECT FName,Street,Address,Work,Phone,DOB,Relation,Type,Name FROM MotherDead Where SpecialCase=? and NOT FName = ? '''
        Name = 'نعم'
        S = ""
        x = c.execute(sql, [(Name),(S)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_11.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_11.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # ============================== Show All Fathers Special Cases  Filter Them ====================
    # ===============================================================================================

    # Filter By Name
    def Make_Filter_Fathers_Special_Cases(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone,DOF,State,TypeInjured,MName FROM FatherAftkad Where Name LIKE ('%' || ? || '%') and NOT Name = ? and SpecialCase=? '''
        Name = self.lineEdit_173.text()
        Names = 'نعم'
        S = ""
        x = c.execute(sql, [(Name),(S),(Names)])
        Result = x.fetchall()
        sql = '''SELECT FName,Street,Address,Work,Phone,DOB,Relation,Type,Name FROM MotherDead Where FName LIKE ('%' || ? || '%') and NOT FName = ? and SpecialCase=? '''
        Name = self.lineEdit_173.text()
        S = ""
        Names = 'نعم'
        x = c.execute(sql, [(Name),(S),(Names)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_11.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_11.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter By Phone
    def Make_Filter_Fathers_Special_Cases_Phones(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone,DOF,State,TypeInjured,MName FROM FatherAftkad Where Phone LIKE ('%' || ? || '%') and NOT Name = ? and SpecialCase=? '''
        Name = self.lineEdit_172.text()
        Names = 'نعم'
        S = ""
        x = c.execute(sql, [(Name),(S),(Names)])
        Result = x.fetchall()
        sql = '''SELECT FName,Street,Address,Work,Phone,DOB,Relation,Type,Name FROM MotherDead Where Phone LIKE ('%' || ? || '%') and NOT FName = ? and SpecialCase=? '''
        Name = self.lineEdit_172.text()
        S = ""
        Names = 'نعم'
        x = c.execute(sql, [(Name),(S),(Names)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_11.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_11.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # =================================== Show All Females Of Special Cases =========================
    # ===============================================================================================

    def Special_Case_Females(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone,DOF,?,FName,Type FROM MotherAftkad Where SpecialCase=? '''
        Name = 'نعم'
        State = 'متزوجه'
        x = c.execute(sql, [(State), (Name)])
        Result = x.fetchall()
        sql = '''SELECT MName,Street,Address,Work,Phone,DOF,Relation,Name,Type FROM FatherDead Where SpecialCase=? '''
        Name = 'نعم'
        x = c.execute(sql, [(Name)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_25.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_25.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_25.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # =============================== Show All Females Of Special Cases Make Filter =================
    # ===============================================================================================

    # Filter BY Name
    def Special_Case_Females_filter_Name(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone,DOF,?,FName,Type FROM MotherAftkad Where Name LIKE ('%' || ? || '%') and NOT Name = ? and SpecialCase=? '''
        State = 'متزوجه'
        Name = self.lineEdit_175.text()
        SS = 'نعم'
        S = ""
        x = c.execute(sql, [(State),(Name) ,(S),(SS)])
        Result = x.fetchall()
        sql = '''SELECT MName,Street,Address,Work,Phone,DOF,Relation,Name,Type FROM FatherDead Where MName LIKE ('%' || ? || '%') and NOT MName = ? and SpecialCase=? '''
        Name = self.lineEdit_175.text()
        S = ""
        SS="نعم"
        x = c.execute(sql, [(Name),(S),(SS)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_25.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_25.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_25.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter BY Phone
    def Special_Case_Females_filter_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone,DOF,?,FName,Type FROM MotherAftkad Where Phone LIKE ('%' || ? || '%') and NOT Name = ? and SpecialCase=? '''
        State = 'متزوجه'
        Name = self.lineEdit_174.text()
        SS = 'نعم'
        S = ""
        x = c.execute(sql, [(State),(Name) ,(S),(SS)])
        Result = x.fetchall()
        sql = '''SELECT MName,Street,Address,Work,Phone,DOF,Relation,Name,Type FROM FatherDead Where Phone LIKE ('%' || ? || '%') and NOT MName = ? and SpecialCase=? '''
        Name = self.lineEdit_174.text()
        S = ""
        SS="نعم"
        x = c.execute(sql, [(Name),(S),(SS)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_25.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_25.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_25.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # =================================== Show All Sons Of Special Cases ============================
    # ===============================================================================================

    def Special_Case_Sons(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Study,Work,DOF,Phone,TypeInjurd FROM SonsAftkad Where Stutus= ? '''
        Name = 'نعم'
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsFDead Where SpecialCase=? '''
        Name = 'نعم'
        x = c.execute(sql, [(Name)])
        X = x.fetchall()

        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsMDead Where SpecialCase=? '''
        Name = 'نعم'
        x = c.execute(sql, [(Name)])
        Y = x.fetchall()

        Result = Result + X + Y
        self.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_26.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # =============================== Show All Sons Of Special Cases Make Filter ====================
    # ===============================================================================================

    # Filter By Son Name
    def Son_Filter_Sepcial_Cases(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Study,Work,DOF,Phone,TypeInjurd FROM SonsAftkad Where Stutus= ? and NOT Name = ? and Name LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_176.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS),(S),(Name)])
        Result = x.fetchall()
        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsFDead Where SpecialCase=?  and NOT Name = ? and Name LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_176.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS),(S),(Name)])
        X = x.fetchall()

        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsMDead Where SpecialCase=?  and NOT Name = ? and Name LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_176.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS),(S),(Name)])
        Y = x.fetchall()

        Result = Result + X + Y
        self.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_26.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter By Father Name
    def Son_Filter_Sepcial_Cases_FName(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Study,Work,DOF,Phone,TypeInjurd FROM SonsAftkad Where Stutus= ? and NOT Name = ? and FName LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_178.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        Result = x.fetchall()
        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsFDead Where SpecialCase=?  and NOT Name = ? and FName LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_178.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        X = x.fetchall()

        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsMDead Where SpecialCase=?  and NOT Name = ? and FName LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_178.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        Y = x.fetchall()

        Result = Result + X + Y
        self.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_26.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter By Mother Name
    def Son_Filter_Sepcial_Cases_MName(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Study,Work,DOF,Phone,TypeInjurd FROM SonsAftkad Where Stutus= ? and NOT Name = ? and MName LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_179.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        Result = x.fetchall()
        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsFDead Where SpecialCase=?  and NOT Name = ? and MName LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_179.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        X = x.fetchall()

        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsMDead Where SpecialCase=?  and NOT Name = ? and MName LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_179.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        Y = x.fetchall()

        Result = Result + X + Y
        self.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_26.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter By Phone
    def Son_Filter_Sepcial_Cases_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Study,Work,DOF,Phone,TypeInjurd FROM SonsAftkad Where Stutus= ? and NOT Name = ? and Phone LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_177.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        Result = x.fetchall()
        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsFDead Where SpecialCase=?  and NOT Name = ? and Phone LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_177.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        X = x.fetchall()

        sql = '''SELECT Name, FName ,MName,Study,Job,DOB,Phone,Type FROM SonsMDead Where SpecialCase=?  and NOT Name = ? and Phone LIKE ('%' || ? || '%')'''
        Name = self.lineEdit_177.text()
        S = ""
        SS = "نعم"
        x = c.execute(sql, [(SS), (S), (Name)])
        Y = x.fetchall()

        Result = Result + X + Y
        self.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_26.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # ================ Searching Work For Father and Mother and Sons Work and Stufy =================
    # ===============================================================================================

    # Father Work
    def Search_From_Father_Work(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Work,Phone,? FROM FatherAftkad Where Work=? and Not Name= ?'''
        work = self.comboBox_13.currentText()
        s = ''
        M = 'متزوج'
        x = c.execute(sql, [(M), (work), (s)])
        Result = x.fetchall()
        sql = '''SELECT FName,Work,Phone,Relation FROM MotherDead Where Work=? and Not FName = ?'''
        Name = self.comboBox_13.currentText()
        m = ''
        x = c.execute(sql, [(Name), (m)])
        X = x.fetchall()
        Result = Result + X
        self.tableWidget_12.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_12.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        self.Clear_After_Choice_Work()

    # Mother Work
    def Search_From_Mother_Work(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Work,Phone,? FROM MotherAftkad Where Work=? and Not Name = ?'''
        Work = self.comboBox_27.currentText()
        Relation = 'متزوجه'
        n = ''
        x = c.execute(sql, [(Relation), (Work), (n)])
        Result = x.fetchall()

        sql = '''SELECT MName,Work,Phone,Relation FROM FatherDead Where Work=? and Not MName = ? '''
        Workk = self.comboBox_27.currentText()
        Name = ''
        x = c.execute(sql, [(Workk), (Name)])
        X = x.fetchall()

        Result = Result + X
        self.tableWidget_27.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_27.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_27.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        self.Clear_After_Choice_Work()

    # Sons Work
    def Search_From_Sons_Work(self):
        Work = self.comboBox_50.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,Work,Phone FROM SonsAftkad Where Work=? and Not Name = ? '''

        Name = ''
        x = c.execute(sql, [(Work), (Name)])
        Result = x.fetchall()
        sql = '''SELECT Name,FName,Job,Phone FROM SonsFDead Where Job=? and Not Name = ?'''

        Name = ''
        x = c.execute(sql, [(Work), (Name)])
        X = x.fetchall()
        sql = '''SELECT Name,FName,Job,Phone FROM SonsMDead Where Job=? and Not Name = ?'''

        Name = ''
        x = c.execute(sql, [(Work), (Name)])
        Y = x.fetchall()
        Result = Result + Y + X
        self.tableWidget_28.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_28.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_28.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        self.Clear_After_Choice_Work()

    # Sons Study or No Have Study
    def Search_Sons_Study(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Study FROM SonsAftkad Where Study=? '''
        Name = self.comboBox_37.currentText()
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        sql = '''SELECT Name,FName,MName,Study FROM SonsFDead Where Study=? '''
        Name = self.comboBox_37.currentText()
        x = c.execute(sql, [(Name)])
        X = x.fetchall()
        sql = '''SELECT Name,FName,MName,Study FROM SonsMDead Where Study=? '''
        Name = self.comboBox_37.currentText()
        x = c.execute(sql, [(Name)])
        Y = x.fetchall()
        Result = Result + X + Y
        self.tableWidget_13.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_13.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_13.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        self.Clear_After_Choice_Study()

    # ===============================================================================================
    # ======================================== Update Father Data ===================================
    # ===============================================================================================

    # 1 Update Father Data
    def Show_Father_Data_For_Edit(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Street,Address,Work,Father FROM FatherAftkad Where Not Name = ?'''
        Name = ""
        x = c.execute(sql,[(Name)])
        Result = x.fetchall()
        self.tableWidget_16.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_16.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_16.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ===============================================================================================
    # ======================================== Update Father Data MAKE Filter =======================
    # ===============================================================================================

    # Make Filter For Father Table For Update By Name
    def Make_Filter_For_FName_Table_Update(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Street,Address,Work,Father FROM FatherAftkad WHERE Name LIKE ('%' || ? || '%') and NOT Name = ?'''
        Name = self.lineEdit_180.text()
        S = ""
        x = c.execute(sql,[(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_16.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_16.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_16.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Make Filter For Update By Phone
    def Make_Filter_For_FPhone_Table_Update(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Street,Address,Work,Father FROM FatherAftkad WHERE Phone LIKE ('%' || ? || '%') and NOT Name = ?'''
        Name = self.lineEdit_181.text()
        S = ""
        x = c.execute(sql,[(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_16.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_16.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_16.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Selection Values From Table In Line Edits
    def Selection_Father_Data_From_Table(self):
        try:
            Address = self.tableWidget_16.item(self.tableWidget_16.currentRow(), 3).text()
            Phone = self.tableWidget_16.item(self.tableWidget_16.currentRow(), 1).text()
            Father = self.tableWidget_16.item(self.tableWidget_16.currentRow(), 5).text()
            self.lineEdit_18.setText(Address)
            self.lineEdit_21.setText(Phone)
            self.lineEdit_22.setText(Father)
        except:
            pass
    # Update Function Of Father Data
    def Update_Father_Data(self):
        try:
            Name = self.tableWidget_16.item(self.tableWidget_16.currentRow(), 0).text()
            Address = self.lineEdit_18.text()
            Phone = self.lineEdit_21.text()
            Work = self.comboBox_58.currentText()
            Street = self.comboBox_14.currentText()
            Father = self.lineEdit_22.text()
            Qulified = self.lineEdit_22.text()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute(
                '''UPDATE FatherAftkad set Phone = ?,Address = ?, Work = ?, Father = ?,Street = ? Where Name = ?''',
                (Phone, Address, Work, Father, Street, Name))
            db.commit()
            db.close()
        except:
            pass
    # Make Clear Line Edites After Update
    def Clear_After_Edit(self):
        self.lineEdit_18.setText('')
        self.lineEdit_21.setText('')
        self.lineEdit_22.setText('')
        self.comboBox_58.setCurrentIndex(0)
        self.comboBox_14.setCurrentIndex(0)
    # Confirmation Update
    def Confirm_Update_Father_Data(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من تعديل البيانات ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Update_Father_Data()
            QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح ')
            self.Show_Father_Data_For_Edit()
            self.Clear_After_Edit()
        else:
            pass

    # 2 Delete Father Data
    def Delete_Father_Data(self):
        try:
            Name = self.tableWidget_16.item(self.tableWidget_16.currentRow(), 0).text()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            sql = '''DELETE FROM FatherAftkad Where Name= ?'''
            c.execute(sql, [(Name)])
            db.commit()
            db.close()
        except:
            pass
    # Confirmation Delete Father
    def Confirm_Delete(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Father_Data()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح ')
            self.Show_Father_Data_For_Edit()
            self.Clear_After_Edit()
        else:
            pass

    # ===============================================================================================
    # ======================================== Update Mother Data ===================================
    # ===============================================================================================
    # 1 Update
    
    # Show Mother Data On Table
    def Show_Mother_Data_For_Edit(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Street,Address,Work,Father FROM MotherAftkad Where Name != ? and NOT Name = ?'''
        Name = 'None'
        S = ""
        x = c.execute(sql, [(Name),(S)])
        Result = x.fetchall()
        self.tableWidget_17.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_17.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_17.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Selection Data
    def Selection_Mother_Data_From_Table(self):
        try:
            Address = self.tableWidget_17.item(self.tableWidget_17.currentRow(), 3).text()
            Father = self.tableWidget_17.item(self.tableWidget_17.currentRow(), 5).text()
            Phone = self.tableWidget_17.item(self.tableWidget_17.currentRow(), 1).text()
            self.lineEdit_30.setText(Address)
            self.lineEdit_26.setText(Phone)
            self.comboBox_737.setCurrentText(Father)
        except:
            pass

    # Update Mother Data
    def Update_Mother_Data(self):
        Name = self.tableWidget_17.item(self.tableWidget_17.currentRow(), 0).text()
        Phone = self.lineEdit_26.text()
        Father = self.lineEdit_737.text()
        Work = self.comboBox_57.currentText()
        Street = self.comboBox_63.currentText()
        Address = self.lineEdit_30.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute(
            '''UPDATE MotherAftkad set Phone = ? , Address = ?, Work = ?, Father = ? ,Street = ? Where Name = ?''',
            (Phone, Address, Work, Father, Street, Name))
        db.commit()
        db.close()

    # Confirmation Update Mother Data
    def Confirm_Update_Mother_Data(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من تعديل البيانات  ؟!!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Update_Mother_Data()
            QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح ')
            self.Show_Mother_Data_For_Edit()
            self.Clear_Line_EEdits()
        else:
            pass

    # Clearing Data After Update Or Delete
    def Clear_Line_EEdits(self):
        self.lineEdit_737.setText('')
        self.lineEdit_26.setText('')
        self.lineEdit_30.setText('')
        self.comboBox_57.setCurrentIndex(0)
        self.comboBox_63.setCurrentIndex(0)

    # 2 Delete

    # Delete Mother Data
    def Delete_Mother_Data(self):
        try:
            Name = self.tableWidget_17.item(self.tableWidget_17.currentRow(), 0).text()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            sql = '''DELETE FROM MotherAftkad Where Name= ?'''
            c.execute(sql, [(Name)])
            db.commit()
            db.close()
        except:
            pass

    # Confirmation Delete Mother Data
    def Confirm_Delete_MotherData(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Mother_Data()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح ')
            self.Show_Mother_Data_For_Edit()
            self.Clear_Line_EEdits()
        else:
            pass

    # ===============================================================================================
    # ======================================== Filter Mother Data ===================================
    # ===============================================================================================
    # Filter By Name
    def Make_Filter_By_Mother_Namee(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Street,Address,Work,Father FROM MotherAftkad Where Name != ? and NOT Name = ? and Name LIKE ('%' || ? || '%') '''
        Name = 'None'
        S = ""
        MName = self.lineEdit_185.text()
        x = c.execute(sql, [(Name),(S),(MName)])
        Result = x.fetchall()
        self.tableWidget_17.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_17.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_17.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter BY Phone
    def Make_Filter_By_Mother_Phonee(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,Street,Address,Work,Father FROM MotherAftkad Where Name != ? and NOT Name = ? and Phone LIKE ('%' || ? || '%') '''
        Name = 'None'
        S = ""
        MPhone = self.lineEdit_184.text()
        x = c.execute(sql, [(Name),(S),(MPhone)])
        Result = x.fetchall()
        self.tableWidget_17.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_17.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_17.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()


    # ===============================================================================================
    # ======================================== Update Sons Data =====================================
    # ===============================================================================================

    # 1 Update Son
    def Show_Sons_Data_For_Edit(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Work,Study FROM SonsAftkad Where NOT Name = ?'''
        S = ""
        x = c.execute(sql,[(S)])
        Result = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsFDead Where NOT Name = ?'''
        S = ""
        y = c.execute(sql,[(S)])
        y = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsMDead Where NOT Name = ?'''
        W = ""
        S= c.execute(sql,[(W)])
        S = x.fetchall()

        Result = Result + y + S
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Selection_Sons_Data_From_Table(self):
        try:
            Phone = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 4).text()
            Father = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 5).text()
            Ssn = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 3).text()
            self.lineEdit_146.setText(Phone)
            self.lineEdit_186.setText(Ssn)
            self.lineEdit_739.setText(Father)
        except:
            pass

    def Update_Sons_Data(self):
        Name = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 0).text()
        FName = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 1).text()
        Phone = self.lineEdit_146.text()
        Ssn = self.lineEdit_186.text()
        Father = self.lineEdit_739.text()
        Work = self.comboBox_60.currentText()
        Study = self.comboBox_61.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('''UPDATE SonsAftkad set Phone = ?,Ssn = ? , Study = ?, Work = ?, Father = ? Where Name = ? and FName = ?''',
                  (Phone,Ssn ,Study, Work, Father, Name,FName))

        c.execute('''UPDATE SonsFDead set Phone = ? ,Ssn = ? ,Study = ?, Job = ?, Father = ? Where Name = ? and FName = ?''',
                  (Phone,Ssn ,Study, Work, Father, Name,FName))

        c.execute('''UPDATE SonsMDead set Phone = ? ,Ssn = ? , Study = ?, Job = ?, Father = ? Where Name = ? and FName = ?''',
                  (Phone,Ssn , Study, Work, Father, Name, FName))

        db.commit()
        db.close()

    def Confirm_Update_Sons_Data(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من تعديل البيانات   ؟!!!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Update_Sons_Data()
            QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')
            self.Show_Sons_Data_For_Edit()
            self.Clear_Son_LineEdits()
        else:
            pass
    # ===============================================================================================
    # ======================================== Filter Sons Data =====================================
    # ===============================================================================================
    # Filter Sons By Name
    def Sons_Filter_Update_BY_Name(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Name = self.lineEdit_187.text()
        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Work,Study FROM SonsAftkad Where NOT Name = ? and Name LIKE ('%' || ? || '%')'''
        S = ""

        x = c.execute(sql,[(S),(Name)])
        Result = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsFDead Where NOT Name = ? and Name LIKE ('%' || ? || '%')'''
        S = ""
        y = c.execute(sql,[(S),(Name)])
        y = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsMDead Where NOT Name = ? and Name LIKE ('%' || ? || '%')'''
        W = ""
        S= c.execute(sql,[(W),(Name)])
        S = x.fetchall()

        Result = Result + y + S
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter Sons By FName
    def Sons_Filter_Update_BY_FName(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Name = self.lineEdit_189.text()
        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Work,Study FROM SonsAftkad Where NOT Name = ? and FName LIKE ('%' || ? || '%')'''
        S = ""

        x = c.execute(sql, [(S), (Name)])
        Result = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsFDead Where NOT Name = ? and FName LIKE ('%' || ? || '%')'''
        S = ""
        y = c.execute(sql, [(S), (Name)])
        y = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsMDead Where NOT Name = ? and FName LIKE ('%' || ? || '%')'''
        W = ""
        S = c.execute(sql, [(W), (Name)])
        S = x.fetchall()

        Result = Result + y + S
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter Sons By MName
    def Sons_Filter_Update_BY_MName(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Name = self.lineEdit_188.text()
        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Work,Study FROM SonsAftkad Where NOT Name = ? and MName LIKE ('%' || ? || '%')'''
        S = ""

        x = c.execute(sql, [(S), (Name)])
        Result = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsFDead Where NOT Name = ? and MName LIKE ('%' || ? || '%')'''
        S = ""
        y = c.execute(sql, [(S), (Name)])
        y = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsMDead Where NOT Name = ? and MName LIKE ('%' || ? || '%')'''
        W = ""
        S = c.execute(sql, [(W), (Name)])
        S = x.fetchall()

        Result = Result + y + S
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter Sons By Phone
    def Sons_Filter_Update_BY_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Name = self.lineEdit_190.text()
        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Work,Study FROM SonsAftkad Where NOT Name = ? and Phone LIKE ('%' || ? || '%')'''
        S = ""

        x = c.execute(sql, [(S), (Name)])
        Result = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsFDead Where NOT Name = ? and Phone LIKE ('%' || ? || '%')'''
        S = ""
        y = c.execute(sql, [(S), (Name)])
        y = x.fetchall()

        sql = '''SELECT Name,FName,MName,Ssn,Phone,Father,Job,Study FROM SonsMDead Where NOT Name = ? and Phone LIKE ('%' || ? || '%')'''
        W = ""
        S = c.execute(sql, [(W), (Name)])
        S = x.fetchall()

        Result = Result + y + S
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()


    # ========================================================================================
    # ======================================== Delete Sons Data ==============================
    # ========================================================================================

    # 2 Delete
    def Delete_Son_Data(self):
        try:
            Name = self.tableWidget_8.item(self.tableWidget_8.currentRow(), 0).text()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            sql = '''DELETE FROM SonsAftkad Where Name= ?'''
            c.execute(sql, [(Name)])
            db.commit()
            db.close()
        except:
            pass
    # Confirmation Delete
    def Comfirm_Delete_Son(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Son_Data()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح ')
            self.Show_Sons_Data_For_Edit()
            self.Clear_Son_LineEdits()
        else:
            pass
    # Clearing LineEdits
    def Clear_Son_LineEdits(self):
        self.lineEdit_146.setText('')
        self.lineEdit_739.setText('')
        self.comboBox_60.setCurrentIndex(0)
        self.comboBox_61.setCurrentIndex(0)

    # ========================================================================================
    # ======================================== Update Father Armals ==========================
    # ========================================================================================
    # Father Armal
    def Show_All_Male_Armals(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Name,Street,Address,Work,Phone,Qulified,Father FROM MotherDead WHERE Not FName=? '''
        Name = ''
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        self.tableWidget_131.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_131.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_131.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # ========================================================================================
    # ======================================== Make Father Armals Filter =====================
    # ========================================================================================
    # Make Filter BY NAME
    def Make_Filter_Armal_Data_BY_Name(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Name,Street,Address,Work,Phone,Qulified,Father FROM MotherDead WHERE Not FName=? and FName LIKE ('%' || ? || '%')'''
        S = ''
        Name = self.lineEdit_747.text()
        x = c.execute(sql, [(S),(Name)])
        Result = x.fetchall()
        self.tableWidget_131.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_131.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_131.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Make Filter BY Phone
    def Make_Filter_Armal_Data_BY_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Name,Street,Address,Work,Phone,Qulified,Father FROM MotherDead WHERE Not FName=? and Phone LIKE ('%' || ? || '%')'''
        S = ''
        Name = self.lineEdit_748.text()
        x = c.execute(sql, [(S), (Name)])
        Result = x.fetchall()
        self.tableWidget_131.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_131.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_131.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()


    def Selection_From_Armal_Male_Data(self):
        try:
            Phone = self.tableWidget_131.item(self.tableWidget_131.currentRow(), 5).text()
            Father = self.tableWidget_131.item(self.tableWidget_131.currentRow(), 7).text()
            Address = self.tableWidget_131.item(self.tableWidget_131.currentRow(), 3).text()
            Qulified = self.tableWidget_131.item(self.tableWidget_131.currentRow(), 6).text()
            self.lineEdit_745.setText(Phone)
            self.lineEdit_744.setText(Father)
            self.lineEdit_743.setText(Address)
            self.lineEdit_746.setText(Qulified)
        except:
            pass
    # Father Update Method
    def Update_Father_Armal(self):
        Name = self.tableWidget_131.item(self.tableWidget_131.currentRow(), 0).text()
        Phone = self.lineEdit_745.text()
        Father = self.lineEdit_744.text()
        Address = self.lineEdit_743.text()
        Qulified = self.lineEdit_746.text()
        Street = self.comboBox_337.currentText()
        Work = self.comboBox_336.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''UPDATE MotherDead set Phone = ? , Father = ?, Address = ?, Qulified = ?,Street =? ,Work = ? Where FName = ?'''
        x = c.execute(sql, [(Phone), (Father), (Address), (Qulified), (Street), (Work), (Name)])
        Result = x.fetchall()
        print(Result)
        db.commit()
        db.close()

    def Clear_lIne_Edits(self):
        self.lineEdit_745.setText('')
        self.lineEdit_744.setText('')
        self.lineEdit_743.setText('')
        self.lineEdit_746.setText('')
        self.comboBox_337.setCurrentIndex(0)
        self.comboBox_336.setCurrentIndex(0)

    def Confirm_Update_Data(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من تعديل البيانات   ؟!!!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Update_Father_Armal()
            QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')
            self.Show_All_Male_Armals()
            self.Clear_lIne_Edits()
        else:
            pass

    def Delete_Armal(self):
        try:
            Name = self.tableWidget_131.item(self.tableWidget_131.currentRow(), 0).text()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            sql = '''DELETE FROM MotherDead Where FName= ?'''
            c.execute(sql, [(Name)])
            db.commit()
            db.close()
        except:
            pass

    def Confirm_Delete_Armal(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Armal()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح ')
            self.Show_All_Male_Armals()
            self.Clear_lIne_Edits()
        else:
            pass
    # ========================================================================================
    # ======================================== Update Mother Armala ==========================
    # ========================================================================================
    # Mother Armala

    def Show_All_FeMale_Armals(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT MName,Name,Street,Address,Work,Phone,Qulified,Father,ChildNum FROM FatherDead WHERE Not MName=? '''
        Name = ''
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        self.tableWidget_132.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_132.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_132.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # ========================================================================================
    # =================================== Make Mother Armala Filter ==========================
    # ========================================================================================

    # Make Filter By Mother Name
    def Make_Mother_Filter_By_Name(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT MName,Name,Street,Address,Work,Phone,Qulified,Father,ChildNum FROM FatherDead WHERE Not MName=? and MName LIKE ('%' || ? || '%')'''
        S = ''
        Name = self.lineEdit_749.text()
        x = c.execute(sql, [(S),(Name)])
        Result = x.fetchall()
        self.tableWidget_132.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_132.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_132.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Make Filter By Mother Phone
    def Make_Mother_Filter_By_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT MName,Name,Street,Address,Work,Phone,Qulified,Father,ChildNum FROM FatherDead WHERE Not MName=? and Phone LIKE ('%' || ? || '%')'''
        S = ''
        Phone = self.lineEdit_750.text()
        x = c.execute(sql, [(S), (Phone)])
        Result = x.fetchall()
        self.tableWidget_132.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_132.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_132.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()



    def Selection_From_Armal_FeMale_Data(self):
        try:
            Phone = self.tableWidget_132.item(self.tableWidget_132.currentRow(), 5).text()
            Father = self.tableWidget_132.item(self.tableWidget_132.currentRow(), 7).text()
            Address = self.tableWidget_132.item(self.tableWidget_132.currentRow(), 3).text()
            Qulified = self.tableWidget_132.item(self.tableWidget_132.currentRow(), 6).text()
            self.lineEdit_740.setText(Phone)
            self.lineEdit_742.setText(Father)
            self.lineEdit_738.setText(Address)
            self.lineEdit_741.setText(Qulified)
        except:
            pass

    def Update_Mother_Armal(self):
        Name = self.tableWidget_132.item(self.tableWidget_132.currentRow(), 0).text()
        Phone = self.lineEdit_740.text()
        Father = self.lineEdit_742.text()
        Address = self.lineEdit_738.text()
        Qulified = self.lineEdit_741.text()
        Street = self.comboBox_333.currentText()
        Work = self.comboBox_335.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''UPDATE FatherDead set Phone = ? , Father = ?, Address = ?, Qulified = ?,Street =? ,Work = ? Where MName = ?'''
        x = c.execute(sql, [(Phone), (Father), (Address), (Qulified), (Street), (Work), (Name)])
        Result = x.fetchall()
        db.commit()
        db.close()

    def Clear_lIne_Editss(self):
        self.lineEdit_740.setText('')
        self.lineEdit_742.setText('')
        self.lineEdit_738.setText('')
        self.lineEdit_741.setText('')
        self.comboBox_333.setCurrentIndex(0)
        self.comboBox_335.setCurrentIndex(0)

    def Confirm_Update_Dataa(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من تعديل البيانات   ؟!!!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Update_Mother_Armal()
            self.Show_All_FeMale_Armals()
            QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح')
            self.Show_All_FeMale_Armals()
            self.Clear_lIne_Editss()
        else:
            pass

    def Delete_Female_Armal(self):
        try:
            Name = self.tableWidget_132.item(self.tableWidget_132.currentRow(), 0).text()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            sql = '''DELETE FROM FatherDead Where MName= ?'''
            c.execute(sql, [(Name)])
            db.commit()
            db.close()
        except:
            pass

    def Confirm_Delete_Female_Armal(self):
        Replay = QMessageBox.information(QWidget(), "معذرة", 'هل انت متاكد من حذف البيانات ؟!!!'
                                         , QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Female_Armal()
            QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح ')
            self.Show_All_FeMale_Armals()
            self.Clear_lIne_Editss()
        else:
            pass

    # ========================================================================================
    # =================================== Add Aftkad Date For Families =======================
    # ========================================================================================

    # Add Aftkad Date
    def Show_Aftkad_Data_Before_Add_Date(self):
        State = 'متزوج'
        Name = ''
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,MName,MPhone,Street,Address,ChildNum,? FROM FatherAftkad where Not Name = ?'''
        x = c.execute(sql, [(State), (Name)])
        Result = x.fetchall()
        Phone = '---------'
        FName = ''
        sql = '''SELECT FName,Phone,Name,?,Street,Address,ChildNum,Relation FROM MotherDead where Not FName = ?'''
        x = c.execute(sql, [(Phone), (FName)])
        X = x.fetchall()
        Phone = '---------'
        MName = ''
        sql = '''SELECT Name,?,MName,Phone,Street,Address,ChildNum,Relation FROM FatherDead where Not MName = ?'''
        x = c.execute(sql, [(Phone), (MName)])
        Y = x.fetchall()
        Result = Result + X + Y
        self.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # ========================================================================================
    # ================================ Add Aftkad Date Filter Families =======================
    # ========================================================================================

    # Filter By Mobile Phone
    def Filter_Family_Aftkad_By_Phone(self):
        State = 'متزوج'
        Name = ''
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Phone,MName,MPhone,Street,Address,ChildNum,? FROM FatherAftkad where Not Name = ? and Phone LIKE ('%' || ? || '%') or MPhone  LIKE ('%' || ? || '%') and Not Name = ?  '''
        P=self.lineEdit_191.text()
        x = c.execute(sql, [(State), (Name),(P),(P),(Name)])
        Result = x.fetchall()
        Phone = '---------'
        FName = ''
        sql = '''SELECT FName,Phone,Name,?,Street,Address,ChildNum,Relation FROM MotherDead where Not FName = ? and Phone LIKE ('%' || ? || '%') '''
        x = c.execute(sql, [(Phone), (FName),(P)])
        X = x.fetchall()
        Phone = '---------'
        MName = ''
        sql = '''SELECT Name,?,MName,Phone,Street,Address,ChildNum,Relation FROM FatherDead where Not MName = ? and Phone LIKE ('%' || ? || '%')'''
        x = c.execute(sql, [(Phone), (MName),(P)])
        Y = x.fetchall()
        Result = Result + X + Y
        self.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Commit_Store_Data(self):
        try:
            Husband = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 0).text()
            Phone = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 1).text()
            Wife = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 2).text()
            Phone2 = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 3).text()
            Street = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 4).text()
            Address = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 5).text()
            ChildNum = self.tableWidget_6.item(self.tableWidget_6.currentRow(), 6).text()
            Date = self.dateEdit_14.date()
            Date = Date.toPyDate()
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO AftkadDate VALUES(?,?,?,?,?,?,?,?)',
                      (Husband, Wife, Street, Address, ChildNum, Phone, Phone2, Date))
            db.commit()
            db.close()
        except:
            pass

    def Confirm_Add_Aftkad_Date(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Commit_Store_Data()
            QMessageBox.information(self, 'جيد', 'تم حفظ التاريخ')
        else:
            QMessageBox.information(self, 'انتبه', 'يرجي التاكد من التاريخ')

    # ========================================================================================
    # ================================== Search Aftkad Filter Families =======================
    # ========================================================================================

    # Search Aftkad
    def Show_Aftkad_Data(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Name,FPhone,MName,MPhone,Street,Address,ChildNum FROM AftkadDate '''
        x = c.execute(sql)
        Result = x.fetchall()
        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter By FName
    def Filter_DateAftkad_By_FName(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Name,FPhone,MName,MPhone,Street,Address,ChildNum FROM AftkadDate Where Not Name = ? and Name LIKE ('%' || ? || '%') '''
        S = ''
        Name = self.lineEdit_192.text()
        x = c.execute(sql,[(S),(Name)])
        Result = x.fetchall()
        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter By MName
    def Filter_DateAftkad_By_MName(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Name,FPhone,MName,MPhone,Street,Address,ChildNum FROM AftkadDate Where Not MName = ? and MName LIKE ('%' || ? || '%') '''
        S = ''
        Name = self.lineEdit_193.text()
        x = c.execute(sql,[(S), (Name)])
        Result = x.fetchall()
        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter By Phone
    def Filter_DateAftkad_By_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Name,FPhone,MName,MPhone,Street,Address,ChildNum FROM AftkadDate Where Not MName = ? and FPhone LIKE ('%' || ? || '%') or MPhone LIKE ('%' || ? || '%')  '''
        S = ''
        Name = self.lineEdit_194.text()
        Names = self.lineEdit_194.text()
        x = c.execute(sql, [(S), (Name),(Names)])
        Result = x.fetchall()
        self.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Selection_Family_Data_Aftkad_Tablee(self):
        try:
            Husband = self.tableWidget_7.item(self.tableWidget_7.currentRow(), 0).text()
            S = self.lineEdit_31.setText(Husband)
        except:
            pass

    def Show_Aftkad_Data_ForSEARCH_Datee(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT DateAftkad FROM AftkadDate Where Name = ?'
        Name = self.lineEdit_31.text()
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        self.tableWidget_18.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_18.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_18.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        self.Clear()

    def Clear(self):
        self.lineEdit_31.setText('')

    # ========================================================================================
    # =========================== Show Fathers Not Have FatherReconize =======================
    # ========================================================================================

    def Show_Fathers_Not_Have_FatherReconize(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT Name,Street,Address,Work,Phone FROM FatherAftkad Where Father = ? and Not Name = ?'
        Name = ''
        x = c.execute(sql, [(Name), (Name)])
        Result = x.fetchall()

        sql = 'SELECT FName,Street,Address,Work,Phone FROM MotherDead Where Father = ? and Not FName = ?'
        Name = ''
        x = c.execute(sql, [(Name), (Name)])
        X = x.fetchall()



        Result = Result + X
        self.tableWidget_20.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_20.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_20.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Show_Mothers_Not_Have_FatherReconize(self):
        Name = ''
        NName = 'None'
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT Name,Street,Address,Work,Phone FROM MotherAftkad Where Father = ? and Not Name = ?'
        x = c.execute(sql, [(Name), (Name)])
        Result = x.fetchall()

        sql = 'SELECT MName,Street,Address,Work,Phone FROM FatherDead Where Father = ? and Not Name = ?'
        Name = ''
        x = c.execute(sql, [(Name), (Name)])
        Y = x.fetchall()
        Result = Result + Y
        self.tableWidget_21.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_21.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_21.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Filter Father Without FatherReconize
    def Filter_Father_Without_FatherReconize_By_Name(self):
        FName = self.lineEdit_195.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone FROM FatherAftkad Where Father = ? and Not Name = ? and Name  LIKE ('%' || ? || '%')'''
        Name = ''
        x = c.execute(sql, [(Name), (Name),(FName)])
        Result = x.fetchall()

        sql = '''SELECT FName,Street,Address,Work,Phone FROM MotherDead Where Father = ? and Not FName = ? and FName LIKE ('%' || ? || '%')'''
        Name = ''
        x = c.execute(sql, [(Name), (Name),(FName)])
        X = x.fetchall()

        Result = Result + X
        self.tableWidget_20.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_20.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_20.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter Mother Without FatherReconize
    def Filter_Mother_Without_FatherReconize_By_Name(self):
        Name = ''
        NName = self.lineEdit_196.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone FROM MotherAftkad Where Father = ? and Not Name = ? and Name LIKE ('%' || ? || '%')'''
        x = c.execute(sql, [(Name), (Name),(NName)])
        Result = x.fetchall()

        sql = '''SELECT MName,Street,Address,Work,Phone FROM FatherDead Where Father = ? and Not Name = ? and MName LIKE ('%' || ? || '%')'''
        Name = ''
        x = c.execute(sql, [(Name), (Name),(NName)])
        Y = x.fetchall()
        Result = Result + Y
        self.tableWidget_21.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_21.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_21.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Filter_Father_Without_FatherReconize_By_Phone(self):
        FPhone = self.lineEdit_197.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone FROM FatherAftkad Where Father = ? and Not Name = ? and Phone  LIKE ('%' || ? || '%')'''
        Name = ''
        x = c.execute(sql, [(Name), (Name), (FPhone)])
        Result = x.fetchall()

        sql = '''SELECT FName,Street,Address,Work,Phone FROM MotherDead Where Father = ? and Not FName = ? and Phone LIKE ('%' || ? || '%')'''
        Name = ''
        x = c.execute(sql, [(Name), (Name), (FPhone)])
        X = x.fetchall()

        Result = Result + X
        self.tableWidget_20.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_20.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_20.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # Filter Mother Without FatherReconize
    def Filter_Mother_Without_FatherReconize_By_Phone(self):
        Name = ''
        MPhone= self.lineEdit_198.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT Name,Street,Address,Work,Phone FROM MotherAftkad Where Father = ? and Not Name = ? and Phone LIKE ('%' || ? || '%')'''
        x = c.execute(sql, [(Name), (Name), (MPhone)])
        Result = x.fetchall()

        sql = '''SELECT MName,Street,Address,Work,Phone FROM FatherDead Where Father = ? and Not Name = ? and Phone LIKE ('%' || ? || '%')'''
        Name = ''
        x = c.execute(sql, [(Name), (Name), (MPhone)])
        Y = x.fetchall()
        Result = Result + Y
        self.tableWidget_21.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_21.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_21.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
    # ========================================================================================
    # =========================== Show Fathers Not Have FatherReconize =======================
    # ========================================================================================

    def Search_Family_In_Speacial_Street(self):
        Name = self.comboBox_16.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT Name,MName,ChildNum,Street,Address FROM FatherAftkad Where Street = ?'
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()

        sql = 'SELECT FName,Name,ChildNum,Street,Address FROM MotherDead Where Street = ?'
        x = c.execute(sql, [(Name)])
        X = x.fetchall()

        sql = 'SELECT Name,MName,ChildNum,Street,Address FROM FatherDead Where Street = ?'
        x = c.execute(sql, [(Name)])
        Y = x.fetchall()

        Result = Result + X + Y
        self.tableWidget_19.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_19.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_19.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()
        self.Reset_Combo_Of_Search_Street()

    def Reset_Combo_Of_Search_Street(self):
        self.comboBox_16.setCurrentIndex(0)
    # ========================================================================================
    # =========================== Select Special Age From Mans ===============================
    # ========================================================================================

    def Select_Special_Age_From_Mans(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT Name,DOF,Work,Father,Phone FROM FatherAftkad'
        x = c.execute(sql)
        Result = x.fetchall()
        fromm = self.spinBox_2.value()
        too = self.spinBox.value()
        p = len(Result)
        for i in Result:
            d = i[1]
            d1 = list(filter(None, d.split('-')))
            d2 = d1[0]
            named_tuple = time.localtime()
            d3 = time.strftime(d2, named_tuple)
            named_tuple = time.localtime()
            time_string = time.strftime("%Y", named_tuple)
            f = int(time_string)
            g = f - int(d3)
            if g <= too and g >= fromm:
                z = i[1]
                z = g
                y = [((i[0]), (z), (i[2]), (i[3]), (i[4]))]
                Result = Result + y

                self.tableWidget_14.setRowCount(0)
                for row_number, row_data in enumerate(Result[p:]):
                    self.tableWidget_14.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_14.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # ========================================================================================
    # =========================== Select Special Age From Femals =============================
    # ========================================================================================

    def Select_Special_Age_From_Femals(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT Name,DOF,Work,Father,Phone FROM MotherAftkad'
        x = c.execute(sql)
        Result = x.fetchall()
        fromm = self.spinBox_5.value()
        too = self.spinBox_6.value()
        p = len(Result)
        for i in Result:
            d = i[1]
            d1 = list(filter(None, d.split('-')))
            d2 = d1[0]
            named_tuple = time.localtime()
            d3 = time.strftime(d2, named_tuple)
            named_tuple = time.localtime()
            time_string = time.strftime("%Y", named_tuple)
            f = int(time_string)
            g = f - int(d3)
            if g <= too and g >= fromm:
                z = i[1]
                z = g
                y = [((i[0]), (z), (i[2]), (i[3]), (i[4]))]
                Result = Result + y
                self.tableWidget_15.setRowCount(0)
                for row_number, row_data in enumerate(Result[p:]):
                    self.tableWidget_15.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_15.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # ========================================================================================
    # ============================ Select Special Age From Mans Armals =======================
    # ========================================================================================

    def Select_Special_Age_From_Mans_Armals(self):
        Name = ''
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT FName,DOB,Work,Father,Phone FROM MotherDead Where Not FName = ?'
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        fromm = self.spinBox_29.value()
        too = self.spinBox_30.value()
        p = len(Result)
        for i in Result:
            d = i[1]
            d1 = list(filter(None, d.split('-')))
            d2 = d1[0]
            named_tuple = time.localtime()
            d3 = time.strftime(d2, named_tuple)
            named_tuple = time.localtime()
            time_string = time.strftime("%Y", named_tuple)
            f = int(time_string)
            g = f - int(d3)
            if g <= too and g >= fromm:
                z = i[1]
                z = g
                y = [((i[0]), (z), (i[2]), (i[3]), (i[4]))]
                Result = Result + y
                self.tableWidget_129.setRowCount(0)
                for row_number, row_data in enumerate(Result[p:]):
                    self.tableWidget_129.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_129.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    # ========================================================================================
    # ========================== Select Special Age From Femals Armals =======================
    # ========================================================================================

    def Select_Special_Age_From_Femals_Armals(self):
        Name = ''
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT MName,DOF,Work,Father,Phone FROM FatherDead Where Not MName = ?'
        x = c.execute(sql, [(Name)])
        Result = x.fetchall()
        fromm = self.spinBox_31.value()
        too = self.spinBox_32.value()
        p = len(Result)
        for i in Result:
            d = i[1]
            d1 = list(filter(None, d.split('-')))
            d2 = d1[0]
            named_tuple = time.localtime()
            d3 = time.strftime(d2, named_tuple)
            named_tuple = time.localtime()
            time_string = time.strftime("%Y", named_tuple)
            f = int(time_string)
            g = f - int(d3)
            if g <= too and g >= fromm:
                z = i[1]
                z = g
                y = [((i[0]), (z), (i[2]), (i[3]), (i[4]))]
                Result = Result + y
                self.tableWidget_130.setRowCount(0)
                for row_number, row_data in enumerate(Result[p:]):
                    self.tableWidget_130.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_130.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    # ========================================================================================
    # ========================== Record Data if Father Dead  =================================
    # ========================================================================================

    def Add_Family_Which_Father_Dead(self):
        Name = ' المرحوم/ ' + self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Ssn = self.lineEdit_154.text()
        Qulified = self.lineEdit_143.text()
        Father = self.lineEdit_142.text()
        Street = self.comboBox_55.currentText()
        Address = self.lineEdit_152.text()
        Work = self.comboBox_54.currentText()
        DOB = self.dateEdit_28.date()
        DOB = DOB.toPyDate()
        Phone = self.lineEdit_144.text()
        SpecialCase = 'لا'
        if self.checkBox_24.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_153.text()
        ChildNum = self.spinBox_10.value()
        Relation = 'ارمله'
        if self.radioButton_62.isChecked():
            Relation = 'عزباء'
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO FatherDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (
            Name, MName, Ssn, Qulified, Father, Street, Address, Work, DOB, Phone, SpecialCase, Type, ChildNum,
            Relation))
        db.commit()
        db.close()
        QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الاسرة بنجاح  ')
        self.Clear_Data_Of_Father_Dead()
        self.Show_all_A3zab_Data()

    # ========================================================================================
    # ========================== Record Data if Mother Dead  =================================
    # ========================================================================================

    def Add_Family_Which_Mother_Dead(self):
        Name = ' المرحومة/ ' + self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Ssn = self.lineEdit_162.text()
        Qulified = self.lineEdit_161.text()
        Father = self.lineEdit_160.text()
        Street = self.comboBox_56.currentText()
        Address = self.lineEdit_158.text()
        Work = self.comboBox_59.currentText()
        DOB = self.dateEdit_29.date()
        DOB = DOB.toPyDate()
        Phone = self.lineEdit_156.text()
        SpecialCase = 'لا'
        if self.checkBox_27.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_157.text()
        ChildNum = self.spinBox_11.value()
        Relation = 'ارمل'
        if self.radioButton_126.isChecked():
            Relation = 'اعزب'
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO MotherDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (
            Name, FName, Ssn, Qulified, Father, Street, Address, Work, DOB, Phone, SpecialCase, Type, ChildNum,
            Relation))
        db.commit()
        db.close()
        QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الاسرة بنجاح  ')
        self.Clear_Data_Of_Mother_Dead()
        self.Show_all_A3zab_Data()
    # ========================================================================================
    # ========================== Check Data of Father Dead Tab  ==============================
    # ========================================================================================

    def Check_Data_Of_Father_Dead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Qulified = self.lineEdit_143.text()
        Father = self.lineEdit_142.text()
        Street = self.comboBox_55.currentText()
        Address = self.lineEdit_152.text()
        Work = self.comboBox_54.currentText()
        DOB = self.dateEdit_28.date()
        FSssn = self.lineEdit_154.text()
        FPhone = self.lineEdit_144.text()
        if Name == '' and self.radioButton_59.isChecked():
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم رب الاسرة ')
        if MName == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم الام ')
        if Qulified == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم المؤهل ')
        if Address == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم العنوان ')
        if Street == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم الشارع ')
        if Work == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم العمل ')
        if MName != '' and Qulified != '' and Address != '' and self.comboBox_55.currentText() != '' and self.comboBox_54.currentText() != '' and FPhone != '' and len(FPhone) == 11 and int(FPhone) != str(FPhone) and len(FSssn) == 14 and int(FSssn) != str(FSssn) or FSssn == "":

            if self.spinBox_10.value() == 0 and MName != '' and Qulified != '' and Address != '' and self.comboBox_55.currentText() != '' and self.comboBox_54.currentText() != '' and FPhone != '' and len(FPhone) == 11 and int(FPhone) != str(FPhone) and len(FSssn) == 14 and int(FSssn) != str(FSssn) or FSssn == "":
                Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من عدد الابناء ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes:
                    self.pushButton_100.setEnabled(True)
                else:
                    pass
            else:
                self.Choice_Son_Num_Of_SonsFatherDead()
        else:
            QMessageBox.information(self, 'معذرة', 'يرجي التاكد من رقميه العدد القومي او الهاتف')


    # ========================================================================================
    # ========================== Check Data of Mother Dead Tab  ==============================
    # ========================================================================================

    def Check_Data_Of_Mother_Dead(self):
        Name =self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Qulified = self.lineEdit_161.text()
        Street = self.comboBox_56.currentText()
        Address = self.lineEdit_158.text()
        Work = self.comboBox_59.currentText()
        if self.radioButton_125.isChecked() and Name == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم رب الاسرة ')
        if FName == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم الام ')
        if Qulified == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم المؤهل ')
        if Address == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم العنوان ')
        if Street == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم الشارع ')
        if Work == '':
            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال اسم العمل ')
        Phone = self.lineEdit_156.text()
        MsSn = self.lineEdit_162.text()
        if FName != '' and Qulified != '' and Address != '' and self.comboBox_56.currentText() != '' and self.comboBox_59.currentText() != '' and Phone != '' and len(Phone) == 11 and int(Phone) != str(Phone) and len(MsSn) == 14 and int(MsSn) != str(MsSn) or MsSn == "":
            if self.spinBox_11.value() == 0 and FName != '' and Qulified != '' and Address != '' and self.comboBox_56.currentText() != '' and self.comboBox_59.currentText() != '' and Phone != '' and len(Phone) == 11 and int(Phone) != str(Phone) and len(MsSn) == 14 and int(MsSn) != str(MsSn) or MsSn == "":
                Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من عدد الابناء ؟!!',
                                                 QMessageBox.Yes | QMessageBox.No)
                if Replay == QMessageBox.Yes:
                    self.pushButton_101.setEnabled(True)
            else:
                self.Choice_Son_Num_Of_SonsMotherDead()
        else:
            QMessageBox.information(self, 'معذرة', 'يرجي التاكد من رقميه العدد القومي او الهاتف')

    # ========================================================================================
    # ========================== Check Data of Sons in Father Dead Tab  ======================
    # ========================================================================================

    def Enable_Sons_Buttons_Of_Father_Dead_Tabs(self):
        # 1
        self.pushButton_58.setEnabled(True)
        # 2
        self.pushButton_61.setEnabled(True)
        # 3
        self.pushButton_63.setEnabled(True)
        # 4
        self.pushButton_65.setEnabled(True)
        # 5
        self.pushButton_67.setEnabled(True)
        # 6
        self.pushButton_91.setEnabled(True)
        # 7
        self.pushButton_93.setEnabled(True)
        # 8
        self.pushButton_95.setEnabled(True)
        # 9
        self.pushButton_97.setEnabled(True)

    def Choice_Son_Num_Of_SonsFatherDead(self):
        try:
            User_Choice = self.spinBox_10.value()
            if User_Choice == 0:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(False)
            elif User_Choice == 1:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_58.setEnabled(False)
            elif User_Choice == 2:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_61.setEnabled(False)
            elif User_Choice == 3:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_63.setEnabled(False)
            elif User_Choice == 4:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_65.setEnabled(False)
            elif User_Choice == 5:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_67.setEnabled(False)
            elif User_Choice == 6:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_91.setEnabled(False)
            elif User_Choice == 7:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_93.setEnabled(False)
            elif User_Choice == 8:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_95.setEnabled(False)
            elif User_Choice == 9:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
                self.pushButton_97.setEnabled(False)
            elif User_Choice == 10:
                self.Enable_Sons_Buttons_Of_Father_Dead_Tabs()
                self.tabWidget_7.setCurrentIndex(0)
                self.tabWidget_7.setEnabled(True)
            else:
                QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال عدد الابناء لايزيد عن 10 اطفال')
        except:
            pass
            '''QMessageBox.warning(QWidget(), "Error!!", 'You Should Add Sons Number.')'''

    def Enable_Sons_Buttons_Of_Mother_Dead_Tabs(self):
        # 1
        self.pushButton_171.setEnabled(True)
        # 2
        self.pushButton_172.setEnabled(True)
        # 3
        self.pushButton_174.setEnabled(True)
        # 4
        self.pushButton_176.setEnabled(True)
        # 5
        self.pushButton_178.setEnabled(True)
        # 6
        self.pushButton_180.setEnabled(True)
        # 7
        self.pushButton_182.setEnabled(True)
        # 8
        self.pushButton_184.setEnabled(True)
        # 9
        self.pushButton_186.setEnabled(True)

    def Choice_Son_Num_Of_SonsMotherDead(self):
        try:
            User_Choice = self.spinBox_11.value()
            if User_Choice == 0:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(False)
            elif User_Choice == 1:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_171.setEnabled(False)
            elif User_Choice == 2:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_172.setEnabled(False)
            elif User_Choice == 3:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_174.setEnabled(False)
            elif User_Choice == 4:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_176.setEnabled(False)
            elif User_Choice == 5:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_178.setEnabled(False)
            elif User_Choice == 6:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_180.setEnabled(False)
            elif User_Choice == 7:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_182.setEnabled(False)
            elif User_Choice == 8:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_184.setEnabled(False)
            elif User_Choice == 9:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
                self.pushButton_186.setEnabled(False)
            elif User_Choice == 10:
                self.Enable_Sons_Buttons_Of_Mother_Dead_Tabs()
                self.tabWidget_8.setCurrentIndex(0)
                self.tabWidget_8.setEnabled(True)
            else:
                QMessageBox.information(QWidget(), "للاسف!!", 'رجاء ادخال عدد الابناء لايزيد عن 10 اطفال')
        except:
            pass
            '''QMessageBox.warning(QWidget(), "Error!!", 'You Should Add Sons Number.')'''

    # ========================================================================================
    # ========================== Moving Between Sons of Father and Mother Dead Tabs ==========
    # ========================================================================================

    def Open_Son_1st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(0)

    def Open_Son_1st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(0)

    def Open_Son_2st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(1)

    def Open_Son_2st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(1)

    def Open_Son_3st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(2)

    def Open_Son_3st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(2)

    def Open_Son_4st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(3)

    def Open_Son_4st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(3)

    def Open_Son_5st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(4)

    def Open_Son_5st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(4)

    def Open_Son_6st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(5)

    def Open_Son_6st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(5)

    def Open_Son_7st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(6)

    def Open_Son_7st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(6)

    def Open_Son_8st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(7)

    def Open_Son_8st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(7)

    def Open_Son_9st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(8)

    def Open_Son_9st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(8)

    def Open_Son_10st_OF_FatherDead_Tab(self):
        self.tabWidget_7.setCurrentIndex(9)

    def Open_Son_10st_OF_MotherDead_Tab(self):
        self.tabWidget_8.setCurrentIndex(9)

    # ========================================================================================
    # ============== Constrain Moving Between Sons Of Father Dead Tabs  ======================
    # ========================================================================================

    def On_Mouse_Click_in_2st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_65.text()
        Study = self.comboBox_38.currentText()
        DOB = self.dateEdit_15.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_2st_OF_FatherDead_Tab()

    def On_Mouse_Click_in_2st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_65.text()
        Study = self.comboBox_38.currentText()
        DOB = self.dateEdit_15.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_3st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_76.text()
        Study = self.comboBox_40.currentText()
        DOB = self.dateEdit_17.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_3st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_3st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_76.text()
        Study = self.comboBox_40.currentText()
        DOB = self.dateEdit_17.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_4st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_79.text()
        Study = self.comboBox_41.currentText()
        DOB = self.dateEdit_18.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_4st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_4st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_79.text()
        Study = self.comboBox_41.currentText()
        DOB = self.dateEdit_18.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_5st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_82.text()
        Study = self.comboBox_42.currentText()
        DOB = self.dateEdit_19.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_5st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_5st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_82.text()
        Study = self.comboBox_42.currentText()
        DOB = self.dateEdit_19.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_6st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_85.text()
        Study = self.comboBox_43.currentText()
        DOB = self.dateEdit_20.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_6st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_6st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_85.text()
        Study = self.comboBox_43.currentText()
        DOB = self.dateEdit_20.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_7st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_88.text()
        Study = self.comboBox_44.currentText()
        DOB = self.dateEdit_21.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_7st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_7st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_88.text()
        Study = self.comboBox_44.currentText()
        DOB = self.dateEdit_21.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_8st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_91.text()
        Study = self.comboBox_45.currentText()
        DOB = self.dateEdit_22.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_8st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_8st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_91.text()
        Study = self.comboBox_45.currentText()
        DOB = self.dateEdit_22.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_9st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_94.text()
        Study = self.comboBox_46.currentText()
        DOB = self.dateEdit_23.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_9st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_9st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_94.text()
        Study = self.comboBox_46.currentText()
        DOB = self.dateEdit_23.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_10st_Son_Of_FatherDead(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_97.text()
        Study = self.comboBox_47.currentText()
        DOB = self.dateEdit_24.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_10st_OF_FatherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_10st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_97.text()
        Study = self.comboBox_47.currentText()
        DOB = self.dateEdit_24.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    # ========================================================================================
    # ============== Constrain Moving Between Sons Of Mother Dead Tabs =======================
    # ========================================================================================

    def On_Mouse_Click_in_2st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_229.text()
        Study = self.comboBox_99.currentText()
        DOB = self.dateEdit_48.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_2st_OF_MotherDead_Tab()

    def On_Mouse_Click_in_2st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_229.text()
        Study = self.comboBox_99.currentText()
        DOB = self.dateEdit_48.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_3st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_235.text()
        Study = self.comboBox_101.currentText()
        DOB = self.dateEdit_49.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_3st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_3st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_235.text()
        Study = self.comboBox_101.currentText()
        DOB = self.dateEdit_49.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_4st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_239.text()
        Study = self.comboBox_103.currentText()
        DOB = self.dateEdit_50.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_4st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_4st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_239.text()
        Study = self.comboBox_103.currentText()
        DOB = self.dateEdit_50.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_5st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_243.text()
        Study = self.comboBox_105.currentText()
        DOB = self.dateEdit_51.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_5st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_5st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_243.text()
        Study = self.comboBox_105.currentText()
        DOB = self.dateEdit_51.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_6st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_247.text()
        Study = self.comboBox_107.currentText()
        DOB = self.dateEdit_52.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_6st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_6st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_247.text()
        Study = self.comboBox_107.currentText()
        DOB = self.dateEdit_52.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_7st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_251.text()
        Study = self.comboBox_109.currentText()
        DOB = self.dateEdit_53.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_7st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_7st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_251.text()
        Study = self.comboBox_109.currentText()
        DOB = self.dateEdit_53.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_8st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_255.text()
        Study = self.comboBox_111.currentText()
        DOB = self.dateEdit_54.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_8st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_8st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_255.text()
        Study = self.comboBox_111.currentText()
        DOB = self.dateEdit_54.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_9st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_259.text()
        Study = self.comboBox_113.currentText()
        DOB = self.dateEdit_55.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_9st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_9st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_259.text()
        Study = self.comboBox_113.currentText()
        DOB = self.dateEdit_55.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def On_Mouse_Click_in_10st_Son_Of_MotherDead(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_263.text()
        Study = self.comboBox_115.currentText()
        DOB = self.dateEdit_56.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Open_Son_10st_OF_MotherDead_Tab()
            else:
                pass

    def On_Mouse_Click_in_10st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_263.text()
        Study = self.comboBox_115.currentText()
        DOB = self.dateEdit_56.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass
    # ========================================================================================
    # ============== First and last Sons Of Father Dead Tab ==================================
    # ========================================================================================

    def On_Mouse_Check_10st_Son_Of_FatherDeadd(self):
        Name = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        SName = self.lineEdit_130.text()
        Study = self.comboBox_51.currentText()
        DOB = self.dateEdit_26.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and MName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_100.setEnabled(True)
            else:
                pass

    def Check_On_Click_Sons_Tab_Of_Father_Dead(self):
        try:
            User_Choice = self.spinBox_10.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.On_Mouse_Click_in_2st_Son_Of_FatherDeadd()
            elif User_Choice == 2:
                self.On_Mouse_Click_in_3st_Son_Of_FatherDeadd()
            elif User_Choice == 3:
                self.On_Mouse_Click_in_4st_Son_Of_FatherDeadd()
            elif User_Choice == 4:
                self.On_Mouse_Click_in_5st_Son_Of_FatherDeadd()
            elif User_Choice == 5:
                self.On_Mouse_Click_in_6st_Son_Of_FatherDeadd()
            elif User_Choice == 6:
                self.On_Mouse_Click_in_7st_Son_Of_FatherDeadd()
            elif User_Choice == 7:
                self.On_Mouse_Click_in_8st_Son_Of_FatherDeadd()
            elif User_Choice == 8:
                self.On_Mouse_Click_in_9st_Son_Of_FatherDeadd()
            elif User_Choice == 9:
                self.On_Mouse_Click_in_10st_Son_Of_FatherDeadd()
            elif User_Choice == 10:
                self.On_Mouse_Check_10st_Son_Of_FatherDeadd()
        except:
            pass
    # ========================================================================================
    # ========================= First and last Sons Of Mother Dead Tab =======================
    # ========================================================================================

    def On_Mouse_Check_10st_Son_Of_MotherDeadd(self):
        Name = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        SName = self.lineEdit_267.text()
        Study = self.comboBox_117.currentText()
        DOB = self.dateEdit_57.date()
        DOB = DOB.toPyDate()
        if SName == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال اسم الابن ')
        if Study == '':
            QMessageBox.information(QWidget(), "رجاء!!", 'رجاء ادخال دراسه الابن ')
        if DOB != '' and Name.strip(" ") != "" and FName.strip(" ") != "" and SName != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_101.setEnabled(True)
            else:
                pass

    def Check_On_Click_Sons_Tab_Of_Mother_Dead(self):
        try:
            User_Choice = self.spinBox_11.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.On_Mouse_Click_in_2st_Son_Of_MotherDeadd()
            elif User_Choice == 2:
                self.On_Mouse_Click_in_3st_Son_Of_MotherDeadd()
            elif User_Choice == 3:
                self.On_Mouse_Click_in_4st_Son_Of_MotherDeadd()
            elif User_Choice == 4:
                self.On_Mouse_Click_in_5st_Son_Of_MotherDeadd()
            elif User_Choice == 5:
                self.On_Mouse_Click_in_6st_Son_Of_MotherDeadd()
            elif User_Choice == 6:
                self.On_Mouse_Click_in_7st_Son_Of_MotherDeadd()
            elif User_Choice == 7:
                self.On_Mouse_Click_in_8st_Son_Of_MotherDeadd()
            elif User_Choice == 8:
                self.On_Mouse_Click_in_9st_Son_Of_MotherDeadd()
            elif User_Choice == 9:
                self.On_Mouse_Click_in_10st_Son_Of_MotherDeadd()
            elif User_Choice == 10:
                self.On_Mouse_Check_10st_Son_Of_MotherDeadd()
        except:
            pass

    # ========================================================================================
    # ========================= Record Sons Data of Motehr Dead Tabs =========================
    # ========================================================================================

    def Record_1st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_229.text()
        Gender = 'ولد'
        if self.radioButton_44.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_230.text()
        DOB = self.dateEdit_48.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_98.currentText()
        Phone = self.lineEdit_231.text()
        Study = self.comboBox_99.currentText()
        Sssn = self.lineEdit_145.text()
        SpecialCase = 'لا'
        if self.checkBox_46.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_232.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_2st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_235.text()
        Gender = 'ولد'
        if self.radioButton_127.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_236.text()
        DOB = self.dateEdit_49.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_100.currentText()
        Phone = self.lineEdit_234.text()
        Study = self.comboBox_101.currentText()
        Sssn = self.lineEdit_147.text()
        SpecialCase = 'لا'
        if self.checkBox_47.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_233.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_3st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_239.text()
        Gender = 'ولد'
        if self.radioButton_129.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_240.text()
        DOB = self.dateEdit_50.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_102.currentText()
        Phone = self.lineEdit_238.text()
        Study = self.comboBox_103.currentText()
        Sssn = self.lineEdit_148.text()
        SpecialCase = 'لا'
        if self.checkBox_48.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_237.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_4st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_243.text()
        Gender = 'ولد'
        if self.radioButton_131.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_230.text()
        DOB = self.dateEdit_51.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_104.currentText()
        Phone = self.lineEdit_242.text()
        Study = self.comboBox_105.currentText()
        Sssn = self.lineEdit_149.text()
        SpecialCase = 'لا'
        if self.checkBox_49.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_241.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_5st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_247.text()
        Gender = 'ولد'
        if self.radioButton_133.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_248.text()
        DOB = self.dateEdit_52.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_106.currentText()
        Phone = self.lineEdit_246.text()
        Study = self.comboBox_107.currentText()
        Sssn = self.lineEdit_150.text()
        SpecialCase = 'لا'
        if self.checkBox_50.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_245.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_6st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_251.text()
        Gender = 'ولد'
        if self.radioButton_135.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_252.text()
        DOB = self.dateEdit_53.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_108.currentText()
        Phone = self.lineEdit_250.text()
        Study = self.comboBox_109.currentText()
        Sssn = self.lineEdit_151.text()
        SpecialCase = 'لا'
        if self.checkBox_51.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_249.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_7st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_255.text()
        Gender = 'ولد'
        if self.radioButton_137.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_256.text()
        DOB = self.dateEdit_54.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_110.currentText()
        Phone = self.lineEdit_254.text()
        Study = self.comboBox_111.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_163.text()
        if self.checkBox_52.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_253.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_8st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_259.text()
        Gender = 'ولد'
        if self.radioButton_139.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_260.text()
        DOB = self.dateEdit_55.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_112.currentText()
        Phone = self.lineEdit_258.text()
        Study = self.comboBox_113.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_164.text()
        if self.checkBox_53.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_257.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_9st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_263.text()
        Gender = 'ولد'
        if self.radioButton_141.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_264.text()
        DOB = self.dateEdit_56.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_114.currentText()
        Phone = self.lineEdit_262.text()
        Study = self.comboBox_115.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_165.text()
        if self.checkBox_54.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_261.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_10st_Son_Of_Mother_Dead(self):
        MName = self.lineEdit_36.text()
        FName = self.lineEdit_159.text()
        Name = self.lineEdit_267.text()
        Gender = 'ولد'
        if self.radioButton_143.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_268.text()
        DOB = self.dateEdit_57.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_116.currentText()
        Phone = self.lineEdit_266.text()
        Study = self.comboBox_117.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_166.text()
        if self.checkBox_55.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_265.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsMDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            MName, FName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Choice_Record_Sons_Num_Data_MotherDead(self):
        User_Choice = self.spinBox_11.value()
        if User_Choice == 0:
            pass
        elif User_Choice == 1:
            self.Record_1st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 2:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 3:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 4:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 5:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            self.Record_5st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 6:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            self.Record_5st_Son_Of_Mother_Dead()
            self.Record_6st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 7:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            self.Record_5st_Son_Of_Mother_Dead()
            self.Record_6st_Son_Of_Mother_Dead()
            self.Record_7st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 8:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            self.Record_5st_Son_Of_Mother_Dead()
            self.Record_6st_Son_Of_Mother_Dead()
            self.Record_7st_Son_Of_Mother_Dead()
            self.Record_8st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 9:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            self.Record_5st_Son_Of_Mother_Dead()
            self.Record_6st_Son_Of_Mother_Dead()
            self.Record_7st_Son_Of_Mother_Dead()
            self.Record_8st_Son_Of_Mother_Dead()
            self.Record_9st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()
        elif User_Choice == 10:
            self.Record_1st_Son_Of_Mother_Dead()
            self.Record_2st_Son_Of_Mother_Dead()
            self.Record_3st_Son_Of_Mother_Dead()
            self.Record_4st_Son_Of_Mother_Dead()
            self.Record_5st_Son_Of_Mother_Dead()
            self.Record_6st_Son_Of_Mother_Dead()
            self.Record_7st_Son_Of_Mother_Dead()
            self.Record_8st_Son_Of_Mother_Dead()
            self.Record_9st_Son_Of_Mother_Dead()
            self.Record_10st_Son_Of_Mother_Dead()
            QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            self.Clear_Data_Of_Mother_Dead()

        else:

            QMessageBox.information(QWidget(), "للاسف!!", 'رجاء التاكد من بيانات الاب والاو والابناء        ')

    # ========================================================================================
    # ========================= Record Sons Data of Motehr Dead Tabs =========================
    # ========================================================================================

    def Record_1st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Name = self.lineEdit_65.text()
        Gender = 'ولد'
        if self.radioButton_36.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_66.text()
        DOB = self.dateEdit_15.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_17.currentText()
        Phone = self.lineEdit_71.text()
        Study = self.comboBox_38.currentText()
        Sssn = self.lineEdit_132.text()
        SpecialCase = 'لا'
        if self.checkBox_6.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_109.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_2st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Name = self.lineEdit_76.text()
        Gender = 'ولد'
        if self.radioButton_63.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_77.text()
        DOB = self.dateEdit_17.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_19.currentText()
        Phone = self.lineEdit_75.text()
        Study = self.comboBox_40.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_133.text()
        if self.checkBox_14.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_144.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_3st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        Name = self.lineEdit_79.text()
        Gender = 'ولد'
        if self.radioButton_65.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_80.text()
        DOB = self.dateEdit_18.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_20.currentText()
        Phone = self.lineEdit_78.text()
        Study = self.comboBox_41.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_134.text()
        if self.checkBox_15.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_115.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_4st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        Name = self.lineEdit_82.text()
        Gender = 'ولد'
        if self.radioButton_67.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_83.text()
        DOB = self.dateEdit_19.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_21.currentText()
        Phone = self.lineEdit_81.text()
        Study = self.comboBox_42.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_135.text()
        if self.checkBox_16.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_122.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_5st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        Name = self.lineEdit_85.text()
        Gender = 'ولد'
        if self.radioButton_69.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_86.text()
        DOB = self.dateEdit_20.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_22.currentText()
        Phone = self.lineEdit_84.text()
        Study = self.comboBox_43.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_136.text()
        if self.checkBox_17.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_123.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_6st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Name = self.lineEdit_88.text()
        Gender = 'ولد'
        if self.radioButton_71.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_89.text()
        DOB = self.dateEdit_18.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_23.currentText()
        Phone = self.lineEdit_87.text()
        Study = self.comboBox_44.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_137.text()
        if self.checkBox_18.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_124.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_7st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()

        Name = self.lineEdit_91.text()
        Gender = 'ولد'
        if self.radioButton_73.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_92.text()
        DOB = self.dateEdit_22.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_24.currentText()
        Phone = self.lineEdit_90.text()
        Study = self.comboBox_45.currentText()
        SpecialCase = 'لا'
        Sssn = self.lineEdit_138.text()
        if self.checkBox_19.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_125.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_8st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Sssn = self.lineEdit_139.text()
        Name = self.lineEdit_94.text()
        Gender = 'ولد'
        if self.radioButton_75.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_95.text()
        DOB = self.dateEdit_23.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_25.currentText()
        Phone = self.lineEdit_93.text()
        Study = self.comboBox_46.currentText()
        SpecialCase = 'لا'
        if self.checkBox_20.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_126.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_9st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Sssn = self.lineEdit_140.text()
        Name = self.lineEdit_97.text()
        Gender = 'ولد'
        if self.radioButton_77.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_98.text()
        DOB = self.dateEdit_24.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_26.currentText()
        Phone = self.lineEdit_96.text()
        Study = self.comboBox_47.currentText()
        SpecialCase = 'لا'
        if self.checkBox_21.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_127.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Record_10st_Son_Of_Father_Dead(self):
        FName = self.lineEdit_35.text()
        MName = self.lineEdit_155.text()
        Sssn = self.lineEdit_141.text()
        Name = self.lineEdit_130.text()
        Gender = 'ولد'
        if self.radioButton_79.isChecked():
            Gender = 'بنت'
        Father = self.lineEdit_131.text()
        DOB = self.dateEdit_26.date()
        DOB = DOB.toPyDate()
        Job = self.comboBox_49.currentText()
        Phone = self.lineEdit_129.text()
        Study = self.comboBox_51.currentText()
        SpecialCase = 'لا'
        if self.checkBox_26.isChecked():
            SpecialCase = 'نعم'
        Type = self.lineEdit_128.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('INSERT INTO SonsFDead VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (
            FName, MName, Name, Gender, Father, Study, DOB, Job, Phone, SpecialCase, Type,Sssn))
        db.commit()
        db.close()

    def Choice_Record_Sons_Num_Data_FatherDead(self):
        try:
            User_Choice = self.spinBox_10.value()
            if User_Choice == 0:
                pass
            elif User_Choice == 1:
                self.Record_1st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 2:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 3:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 4:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 5:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 6:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 7:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 8:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                self.Record_8st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 9:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                self.Record_8st_Son_Of_Father_Dead()
                self.Record_9st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')
            elif User_Choice == 10:
                self.Record_1st_Son_Of_Father_Dead()
                self.Record_2st_Son_Of_Father_Dead()
                self.Record_3st_Son_Of_Father_Dead()
                self.Record_4st_Son_Of_Father_Dead()
                self.Record_5st_Son_Of_Father_Dead()
                self.Record_6st_Son_Of_Father_Dead()
                self.Record_7st_Son_Of_Father_Dead()
                self.Record_8st_Son_Of_Father_Dead()
                self.Record_9st_Son_Of_Father_Dead()
                self.Record_10st_Son_Of_Father_Dead()
                QMessageBox.information(self, 'جيد', 'تم حفظ البيانات الابناء بنجاح  ')

            else:

                QMessageBox.information(QWidget(), "للاسف!!", 'رجاء التاكد من بيانات الاب والاو والابناء        ')
        except:
            pass

    # ========================================================================================
    # ========================= Clear Data OF Family Of Father Dead ==========================
    # ========================================================================================

    def Clear_Data_Of_Father_Dead(self):
        self.tabWidget_7.setEnabled(False)
        self.tabWidget_7.setCurrentIndex(0)
        # Family Data LineEdits
        self.lineEdit_35.setText('')
        self.lineEdit_155.setText('')
        self.lineEdit_154.setText('')
        self.lineEdit_143.setText('')
        self.lineEdit_142.setText('')
        self.lineEdit_152.setText('')
        self.lineEdit_153.setText('')
        self.lineEdit_144.setText('')
        self.comboBox_55.setCurrentIndex(0)
        self.comboBox_54.setCurrentIndex(0)
        self.spinBox_10.setValue(0)
        # 1st Sons
        self.lineEdit_65.setText('')
        self.lineEdit_66.setText('')
        self.lineEdit_71.setText('')
        self.lineEdit_109.setText('')
        self.lineEdit_35.setText('')
        self.comboBox_38.setCurrentIndex(0)
        self.comboBox_17.setCurrentIndex(0)
        # 2st Sons
        self.lineEdit_76.setText('')
        self.lineEdit_133.setText('')
        self.lineEdit_77.setText('')
        self.lineEdit_75.setText('')
        self.lineEdit_114.setText('')
        self.comboBox_40.setCurrentIndex(0)
        self.comboBox_19.setCurrentIndex(0)
        # 3st Sons
        self.lineEdit_79.setText('')
        self.lineEdit_80.setText('')
        self.lineEdit_78.setText('')
        self.lineEdit_115.setText('')
        self.lineEdit_134.setText('')
        self.comboBox_41.setCurrentIndex(0)
        self.comboBox_20.setCurrentIndex(0)
        # 4st Sons
        self.lineEdit_82.setText('')
        self.lineEdit_135.setText('')
        self.lineEdit_83.setText('')
        self.lineEdit_81.setText('')
        self.lineEdit_122.setText('')
        self.comboBox_42.setCurrentIndex(0)
        self.comboBox_21.setCurrentIndex(0)
        # 5st Sons
        self.lineEdit_85.setText('')
        self.lineEdit_86.setText('')
        self.lineEdit_136.setText('')
        self.lineEdit_84.setText('')
        self.lineEdit_123.setText('')
        self.comboBox_43.setCurrentIndex(0)
        self.comboBox_22.setCurrentIndex(0)
        # 6st Sons
        self.lineEdit_88.setText('')
        self.lineEdit_89.setText('')
        self.lineEdit_137.setText('')
        self.lineEdit_87.setText('')
        self.lineEdit_124.setText('')
        self.comboBox_44.setCurrentIndex(0)
        self.comboBox_23.setCurrentIndex(0)
        # 7st Sons
        self.lineEdit_138.setText('')
        self.lineEdit_91.setText('')
        self.lineEdit_92.setText('')
        self.lineEdit_90.setText('')
        self.lineEdit_125.setText('')
        self.comboBox_45.setCurrentIndex(0)
        self.comboBox_24.setCurrentIndex(0)
        # 8st Sons
        self.lineEdit_139.setText('')
        self.lineEdit_94.setText('')
        self.lineEdit_95.setText('')
        self.lineEdit_93.setText('')
        self.lineEdit_126.setText('')
        self.comboBox_46.setCurrentIndex(0)
        self.comboBox_25.setCurrentIndex(0)
        # 9st Sons
        self.lineEdit_140.setText('')
        self.lineEdit_97.setText('')
        self.lineEdit_98.setText('')
        self.lineEdit_96.setText('')
        self.lineEdit_127.setText('')
        self.comboBox_47.setCurrentIndex(0)
        self.comboBox_26.setCurrentIndex(0)
        # 10st Sons
        self.lineEdit_141.setText('')
        self.lineEdit_130.setText('')
        self.lineEdit_131.setText('')
        self.lineEdit_129.setText('')
        self.lineEdit_128.setText('')
        self.comboBox_51.setCurrentIndex(0)
        self.comboBox_49.setCurrentIndex(0)
        self.pushButton_100.setEnabled(False)

    def Clear_Data_Of_Mother_Dead(self):
        self.tabWidget_8.setEnabled(False)
        self.tabWidget_8.setCurrentIndex(0)
        # Family Data LineEdits

        self.lineEdit_36.setText('')
        self.lineEdit_159.setText('')
        self.lineEdit_162.setText('')
        self.lineEdit_161.setText('')
        self.lineEdit_160.setText('')
        self.lineEdit_158.setText('')
        self.lineEdit_156.setText('')
        self.lineEdit_157.setText('')
        self.comboBox_56.setCurrentIndex(0)
        self.comboBox_59.setCurrentIndex(0)
        self.spinBox_11.setValue(0)
        # 1st Sons
        self.lineEdit_145.setText('')
        self.lineEdit_229.setText('')
        self.lineEdit_230.setText('')
        self.lineEdit_231.setText('')
        self.lineEdit_232.setText('')
        self.comboBox_99.setCurrentIndex(0)
        self.comboBox_98.setCurrentIndex(0)
        # 2st Sons
        self.lineEdit_147.setText('')
        self.lineEdit_235.setText('')
        self.lineEdit_236.setText('')
        self.lineEdit_234.setText('')
        self.lineEdit_233.setText('')
        self.comboBox_101.setCurrentIndex(0)
        self.comboBox_49.setCurrentIndex(0)
        # 3st Sons
        self.lineEdit_148.setText('')
        self.lineEdit_239.setText('')
        self.lineEdit_240.setText('')
        self.lineEdit_238.setText('')
        self.lineEdit_237.setText('')
        self.comboBox_103.setCurrentIndex(0)
        self.comboBox_50.setCurrentIndex(0)
        # 4st Sons
        self.lineEdit_149.setText('')
        self.lineEdit_243.setText('')
        self.lineEdit_244.setText('')
        self.lineEdit_242.setText('')
        self.lineEdit_241.setText('')
        self.comboBox_105.setCurrentIndex(0)
        self.comboBox_51.setCurrentIndex(0)
        # 5st Sons
        self.lineEdit_150.setText('')
        self.lineEdit_247.setText('')
        self.lineEdit_248.setText('')
        self.lineEdit_246.setText('')
        self.lineEdit_245.setText('')
        self.comboBox_107.setCurrentIndex(0)
        self.comboBox_106.setCurrentIndex(0)
        # 6st Sons
        self.lineEdit_151.setText('')
        self.lineEdit_251.setText('')
        self.lineEdit_252.setText('')
        self.lineEdit_250.setText('')
        self.lineEdit_249.setText('')
        self.comboBox_109.setCurrentIndex(0)
        self.comboBox_108.setCurrentIndex(0)
        # 7st Sons
        self.lineEdit_163.setText('')
        self.lineEdit_255.setText('')
        self.lineEdit_256.setText('')
        self.lineEdit_254.setText('')
        self.lineEdit_253.setText('')
        self.comboBox_111.setCurrentIndex(0)
        self.comboBox_110.setCurrentIndex(0)
        # 8st Sons
        self.lineEdit_164.setText('')
        self.lineEdit_259.setText('')
        self.lineEdit_260.setText('')
        self.lineEdit_258.setText('')
        self.lineEdit_257.setText('')
        self.comboBox_113.setCurrentIndex(0)
        self.comboBox_112.setCurrentIndex(0)
        # 9st Sons
        self.lineEdit_165.setText('')
        self.lineEdit_263.setText('')
        self.lineEdit_264.setText('')
        self.lineEdit_262.setText('')
        self.lineEdit_261.setText('')
        self.comboBox_115.setCurrentIndex(0)
        self.comboBox_114.setCurrentIndex(0)
        # 10st Sons
        self.lineEdit_166.setText('')
        self.lineEdit_267.setText('')
        self.lineEdit_268.setText('')
        self.lineEdit_266.setText('')
        self.lineEdit_265.setText('')
        self.comboBox_117.setCurrentIndex(0)
        self.comboBox_116.setCurrentIndex(0)
        self.pushButton_101.setEnabled(False)

    # ========================================================================================
    # ====================================== Add Sons Data ===================================
    # ========================================================================================

    def Add_Sons_Data(self):
        NameOfFather = self.comboBox_18.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Select Ssn , Phone from FatherAftkad where Name = ?'
        x = c.execute(sql, [(NameOfFather)])
        db.commit()
        db.close()
        NameOfMother = self.lineEdit_9.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Select Ssn , Phone from MotherAftkad where Name = ?'
        x = c.execute(sql, [(NameOfMother)])
        Result = x.fetchall()
        db.commit()
        db.close()
        MSsn = Result[0][0]
        MPhone = Result[0][1]
        FSsn = Result[0][0]
        FPhone = Result[0][1]
        Name = self.lineEdit_7.text()
        Father = self.lineEdit_11.text()
        Phone = self.lineEdit_13.text()
        Age = self.dateEdit.date()
        Age = Age.toPyDate()
        Study = self.comboBox_52.currentText()
        Job = self.comboBox_53.currentText()
        Gender = 'ولد'
        Sssn = self.lineEdit_167.text()
        if self.radioButton_3.isChecked():
            Gender = 'بنت'
        Stutus = 'لا'
        if self.checkBox_4.isChecked():
            Stutus = 'نعم'
        Type = self.lineEdit_12.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'insert into SonsAftkad VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        x = c.execute(sql,
                      [(Name), (Father), (Age), (Phone), (Job), (Study), (Stutus), (MSsn), (FSsn), (MPhone), (FPhone),
                       (NameOfMother), (NameOfFather), (Gender), (Type),(Sssn)])
        db.commit()
        db.close()
        self.Add_Sum_Child_Num()
        self.Show_Added_Son()
        self.Clear_Sons_LineEdits()

    def Check_Add_Sons_Data(self):
        NameOfFather = self.comboBox_18.currentText()
        NameOfMother = self.lineEdit_9.text()
        Name = self.lineEdit_7.text()
        Age = self.dateEdit.date()
        Age = Age.toPyDate()
        Study = self.comboBox_52.currentText()
        Job = self.comboBox_53.currentText()
        if Name == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من الابن   ')
        if NameOfFather == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من اسم الاب  ')
        # if NameOfMother == '':
        # QMessageBox.information(self, 'برجاء', 'يرجي التاكد من اسم الام  ')
        if Job == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من العمل   ')
        if Study == '':
            QMessageBox.information(self, 'برجاء', 'يرجي التاكد من الدراسه   ')
        if Age != '' and Name != '' and NameOfFather != '' and '''NameOfMother !='' ''' and Job != '' and Study != '':
            Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تاريخ الميلاد ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.pushButton_104.setEnabled(True)

    def Clear_Sons_LineEdits(self):
        self.lineEdit_7.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_12.setText('')
        self.comboBox_18.setCurrentIndex(0)
        self.lineEdit_11.setText('')
        self.comboBox_52.setCurrentIndex(0)
        self.comboBox_53.setCurrentIndex(0)
        self.pushButton_104.setEnabled(False)

    def Show_Added_Son(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name ,FName , MName from SonsAftkad')
        Result = c.fetchall()
        db.commit()
        self.tableWidget_22.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_22.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_22.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Read_Father_Name_From_Table(self):
        self.comboBox_18.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Name from FatherAftkad')
        x = c.fetchall()

        db.commit()
        db.close()
        for i in x:
            self.comboBox_18.addItem(str(i[0]))

    def Read_Mother_Name_From_Table(self):
        Name = self.comboBox_18.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Select MName from FatherAftkad Where Name = ?'
        x = c.execute(Sql, [(Name)])
        Result = x.fetchall()
        MName = Result[0][0]
        self.lineEdit_9.setText(MName)
        db.commit()
        db.close()

    def Add_Sum_Child_Num(self):
        Name = self.comboBox_18.currentText()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'Select ChildNum from FatherAftkad Where Name = ?'
        x = c.execute(Sql, [(Name)])
        Result = x.fetchall()
        db.commit()
        db.close()
        Num = Result[0][0]
        Sum = Num
        Sum = int(Sum) + int(1)
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'UPDATE FatherAftkad set ChildNum = ? Where Name = ?'
        x = c.execute(Sql, [(Sum), (Name)])
        db.commit()
        db.close()

    # ========================================================================================
    # ====================================== Add Item im New Lists ===========================
    # ========================================================================================

    # List Add Work For Father List
    def Add_Work_in_List_For_Father(self):
        Work = self.lineEdit_14.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'INSERT INTO WorkF VALUES(?)'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Father_List()

    def Confirm_Add_Work_To_List_Father(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من اسم الوظيفة ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and self.lineEdit_14.text() != '':
            self.Add_Work_in_List_For_Father()
            self.Clear_LineEdit_List_Father()
        else:
            QMessageBox.warning(self, 'معذرة', 'تاكد من اسم وظيفه الاب     !!!')

    def Clear_LineEdit_List_Father(self):
        self.lineEdit_14.setText('')

    # List Add Work For Mother List
    def Add_Work_in_List_For_Mother(self):
        Work = self.lineEdit_15.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'INSERT INTO WorkM VALUES(?)'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Mother_List()

    def Confirm_Add_Work_To_List_Mother(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من اسم الوظيفة ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and self.lineEdit_15.text() != '':
            self.Add_Work_in_List_For_Mother()
            self.Clear_LineEdit_List_Mother()
        else:
            QMessageBox.warning(self, 'معذرة', 'تاكد من اسم وظيفه الام     !!!')

    def Clear_LineEdit_List_Mother(self):
        self.lineEdit_15.setText('')

    # List Add Work For Son List
    def Add_Work_in_List_For_Son(self):
        Work = self.lineEdit_16.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'INSERT INTO WorkS VALUES(?)'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Son_List()

    def Confirm_Add_Work_To_List_Son(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من اسم الوظيفة ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and self.lineEdit_16.text() != '':
            self.Add_Work_in_List_For_Son()
            self.Clear_LineEdit_List_Son()
        else:
            QMessageBox.warning(self, 'معذرة', 'تاكد من اسم وظيفه الابن     !!!')

    def Clear_LineEdit_List_Son(self):
        self.lineEdit_16.setText('')

    # List Add Study
    def Add_Study_in_List(self):
        Study = self.lineEdit_182.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'INSERT INTO StudyS VALUES(?)'
        x = c.execute(sql, [(Study)])
        db.commit()
        db.close()
        self.Show_Work_Study_List()

    def Confirm_Add_Study(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من اسم الدراسة ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and self.lineEdit_182.text() != '':
            self.Add_Study_in_List()
            self.Clear_LineEdit_List_Study()
        else:
            QMessageBox.warning(self, 'معذرة', 'تاكد من اسم السنه الدراسيه    !!!')

    def Clear_LineEdit_List_Study(self):
        self.lineEdit_182.setText('')

    # List Add Street
    def Add_Street_in_List(self):
        Street = self.lineEdit_183.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'INSERT INTO StreetList VALUES(?)'
        x = c.execute(sql, [(Street)])
        db.commit()
        db.close()
        self.Show_Work_Street_List()

    def Confirm_Add_Street(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من اسم الشارع ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes and self.lineEdit_183.text() != '':
            self.Add_Street_in_List()
            self.Clear_LineEdit_List_Street()
        else:
            QMessageBox.warning(self, 'معذرة', 'تاكد من اسم الشارع    !!!')

    def Clear_LineEdit_List_Street(self):
        self.lineEdit_183.setText('')

    # Methods Show Data From Tables
    def Show_Work_Father_List(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Work FROM WorkF '''
        x = c.execute(sql)
        Result = x.fetchall()
        self.tableWidget_29.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_29.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_29.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Show_Work_Mother_List(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Work FROM WorkM '''
        x = c.execute(sql)
        Result = x.fetchall()
        self.tableWidget_24.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_24.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_24.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Show_Work_Son_List(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Work FROM WorkS '''
        x = c.execute(sql)
        Result = x.fetchall()
        self.tableWidget_23.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_23.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_23.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Show_Work_Study_List(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Study FROM StudyS '''
        x = c.execute(sql)
        Result = x.fetchall()
        self.tableWidget_30.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_30.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_30.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Show_Work_Street_List(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT DISTINCT Street FROM StreetList '''
        x = c.execute(sql)
        Result = x.fetchall()
        self.tableWidget_31.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_31.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_31.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    # Defs Delete From Tables
    # List Delete Father Work From List
    def Delete_Job_From_Father_List(self):
        Work = self.tableWidget_29.item(self.tableWidget_29.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Delete From WorkF Where Work = ?'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Father_List()

    def Confirm_Delete_From_Father_List(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تريد حذف الوظيفه ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Job_From_Father_List()
        else:
            pass

    # List Delete Mother Work From List
    def Delete_Job_From_Mother_List(self):
        Work = self.tableWidget_24.item(self.tableWidget_24.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Delete From WorkM Where Work = ?'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Mother_List()

    def Confirm_Delete_From_Mother_List(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تريد حذف الوظيفه ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Job_From_Mother_List()
        else:
            pass

    # List Delete Son Work From List
    def Delete_Job_From_Son_List(self):
        Work = self.tableWidget_23.item(self.tableWidget_23.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Delete From WorkS Where Work = ?'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Son_List()

    def Confirm_Delete_From_Son_List(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تريد حذف الوظيفه ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_Job_From_Son_List()
        else:
            pass

    # List Delete Study From List
    def Delete_From_Study_List(self):
        Study = self.tableWidget_30.item(self.tableWidget_30.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Delete From StudyS Where Study = ?'
        x = c.execute(sql, [(Study)])
        db.commit()
        db.close()
        self.Show_Work_Study_List()

    def Confirm_Delete_From_Study_List(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تريد حذف السنه الدراسيه ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_From_Study_List()
        else:
            pass

    # List Delete Street From List
    def Delete_From_Street_List(self):
        Work = self.tableWidget_31.item(self.tableWidget_31.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'Delete From StreetList Where Street = ?'
        x = c.execute(sql, [(Work)])
        db.commit()
        db.close()
        self.Show_Work_Street_List()

    def Confirm_Delete_From_Street_List(self):
        Replay = QMessageBox.information(QWidget(), 'رجاء', 'هل انت متاكد من تريد حذف الوظيفه ؟!!',
                                         QMessageBox.Yes | QMessageBox.No)
        if Replay == QMessageBox.Yes:
            self.Delete_From_Street_List()
        else:
            pass

    # ==== Add Auto Values To Combo Boxes ====== #
    # Add Family Tab =============================
    # Add Father Work
    def Read_Father_Work_In_List(self):
        self.comboBox.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox.addItem(str(i[0]))

    # Add Father Street
    def Read_Father_Street_In_List(self):
        self.comboBox_15.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_15.addItem(str(i[0]))

    # Add Mother Work
    def Read_Mother_Work_In_List(self):
        self.comboBox_2.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_2.addItem(str(i[0]))

    # Sons
    # 1st
    def Read_Son1_Work_In_List(self):
        self.comboBox_3.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_3.addItem(str(i[0]))

    def Read_Son1_Study_In_List(self):
        self.comboBox_28.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_28.addItem(str(i[0]))

    # 2st
    def Read_Son2_Work_In_List(self):
        self.comboBox_4.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_4.addItem(str(i[0]))

    def Read_Son2_Study_In_List(self):
        self.comboBox_29.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_29.addItem(str(i[0]))

    # 3st
    def Read_Son3_Work_In_List(self):
        self.comboBox_5.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_5.addItem(str(i[0]))

    def Read_Son3_Study_In_List(self):
        self.comboBox_30.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_30.addItem(str(i[0]))

    # 4st
    def Read_Son4_Work_In_List(self):
        self.comboBox_6.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_6.addItem(str(i[0]))

    def Read_Son4_Study_In_List(self):
        self.comboBox_31.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_31.addItem(str(i[0]))

    # 5st
    def Read_Son5_Work_In_List(self):
        self.comboBox_7.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_7.addItem(str(i[0]))

    def Read_Son5_Study_In_List(self):
        self.comboBox_48.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_48.addItem(str(i[0]))

    # 6st
    def Read_Son6_Work_In_List(self):
        self.comboBox_8.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_8.addItem(str(i[0]))

    def Read_Son6_Study_In_List(self):
        self.comboBox_32.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_32.addItem(str(i[0]))

    # 7st
    def Read_Son7_Work_In_List(self):
        self.comboBox_9.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_9.addItem(str(i[0]))

    def Read_Son7_Study_In_List(self):
        self.comboBox_33.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_33.addItem(str(i[0]))

    # 8st
    def Read_Son8_Work_In_List(self):
        self.comboBox_10.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_10.addItem(str(i[0]))

    def Read_Son8_Study_In_List(self):
        self.comboBox_34.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_34.addItem(str(i[0]))

    # 9st
    def Read_Son9_Work_In_List(self):
        self.comboBox_11.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_11.addItem(str(i[0]))

    def Read_Son9_Study_In_List(self):
        self.comboBox_35.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_35.addItem(str(i[0]))

    # 10st
    def Read_Son10_Work_In_List(self):
        self.comboBox_12.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_12.addItem(str(i[0]))

    def Read_Son10_Study_In_List(self):
        self.comboBox_36.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_36.addItem(str(i[0]))

    # Add In Search Job Tab ====================
    # Father Job
    def Read_Fatherr_Work_In_List(self):
        self.comboBox_13.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_13.addItem(str(i[0]))

    # Mother Job
    def Read_Motherr_Work_In_List(self):
        self.comboBox_27.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_27.addItem(str(i[0]))

    # Son Job
    def Read_Son_Work_In_List(self):
        self.comboBox_50.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_50.addItem(str(i[0]))

    # Add In Search Study Tab
    # Sons Study
    def Read_Son_Study_In_List(self):
        self.comboBox_37.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_37.addItem(str(i[0]))

    # Edit Father Data Tab =============================
    # Father Work
    def Read_Fatheer_Work_In_List(self):
        self.comboBox_58.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_58.addItem(str(i[0]))

    # Father Street
    def Read_Fatheer_Street_In_List(self):
        self.comboBox_14.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_14.addItem(str(i[0]))

    # Edit Mother Tab =================================
    # Mother Job
    def Read_Motheer_Work_In_List(self):
        self.comboBox_57.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_57.addItem(str(i[0]))

    # Mother Street
    def Show_Mother_Street(self):
        self.comboBox_63.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_63.addItem(str(i[0]))

    # Edit Sons Tab ===================
    # Sons Work
    def Read_Sonn_Study_In_List(self):
        self.comboBox_61.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_61.addItem(str(i[0]))

    # Sons Job
    def Read_Sonn_Work_In_List(self):
        self.comboBox_60.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_60.addItem(str(i[0]))

    # Search Street Tab ============================
    # Street Data
    def Read_Street_Data(self):
        self.comboBox_16.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_16.addItem(str(i[0]))

    # Add Sons Tab
    # Study
    def Read_Son_sStudy_In_List(self):
        self.comboBox_52.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_52.addItem(str(i[0]))
    # Job
    def Read_Son_wWork_In_List(self):
        self.comboBox_53.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_53.addItem(str(i[0]))




    # Record Family Without Father ================================
    # Add Father Work
    def Read_fFather_Work_In_List(self):
        self.comboBox_54.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_54.addItem(str(i[0]))

    # Add Father Street
    def Read_fFather_Street_In_List(self):
        self.comboBox_55.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_55.addItem(str(i[0]))

    # Sons
    # 1st
    def Read_fSon1_Work_In_List(self):
        self.comboBox_17.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_17.addItem(str(i[0]))

    def Read_fSon1_Study_In_List(self):
        self.comboBox_38.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_38.addItem(str(i[0]))

    # 2st
    def Read_fSon2_Work_In_List(self):
        self.comboBox_19.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_19.addItem(str(i[0]))

    def Read_fSon2_Study_In_List(self):
        self.comboBox_40.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_40.addItem(str(i[0]))

    # 3st
    def Read_fSon3_Work_In_List(self):
        self.comboBox_20.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_20.addItem(str(i[0]))

    def Read_fSon3_Study_In_List(self):
        self.comboBox_41.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_41.addItem(str(i[0]))

    # 4st
    def Read_fSon4_Work_In_List(self):
        self.comboBox_21.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_21.addItem(str(i[0]))

    def Read_fSon4_Study_In_List(self):
        self.comboBox_42.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_42.addItem(str(i[0]))

    # 5st
    def Read_fSon5_Work_In_List(self):
        self.comboBox_22.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_22.addItem(str(i[0]))

    def Read_fSon5_Study_In_List(self):
        self.comboBox_43.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_43.addItem(str(i[0]))

    # 6st
    def Read_fSon6_Work_In_List(self):
        self.comboBox_23.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_23.addItem(str(i[0]))

    def Read_fSon6_Study_In_List(self):
        self.comboBox_44.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_44.addItem(str(i[0]))

    # 7st
    def Read_fSon7_Work_In_List(self):
        self.comboBox_24.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_24.addItem(str(i[0]))

    def Read_fSon7_Study_In_List(self):
        self.comboBox_45.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_45.addItem(str(i[0]))

    # 8st
    def Read_fSon8_Work_In_List(self):
        self.comboBox_25.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_25.addItem(str(i[0]))

    def Read_fSon8_Study_In_List(self):
        self.comboBox_46.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_46.addItem(str(i[0]))

    # 9st
    def Read_fSon9_Work_In_List(self):
        self.comboBox_26.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_26.addItem(str(i[0]))

    def Read_fSon9_Study_In_List(self):
        self.comboBox_35.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_35.addItem(str(i[0]))

    # 10st
    def Read_fSon10_Work_In_List(self):
        self.comboBox_49.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_49.addItem(str(i[0]))

    def Read_fSon10_Study_In_List(self):
        self.comboBox_51.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_51.addItem(str(i[0]))

    # Record Family Without Mother ================================
    # Add Mother Work
    def Read_mMother_Work_In_List(self):
        self.comboBox_59.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_59.addItem(str(i[0]))

    # Add Father Street
    def Read_Street_In_List(self):
        self.comboBox_56.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_56.addItem(str(i[0]))

    # Sons
    # 1st
    def Read_mSon1_Work_In_List(self):
        self.comboBox_98.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_98.addItem(str(i[0]))

    def Read_mSon1_Study_In_List(self):
        self.comboBox_99.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_99.addItem(str(i[0]))

    # 2st
    def Read_mSon2_Work_In_List(self):
        self.comboBox_100.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_100.addItem(str(i[0]))

    def Read_mSon2_Study_In_List(self):
        self.comboBox_101.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_101.addItem(str(i[0]))

    # 3st
    def Read_mSon3_Work_In_List(self):
        self.comboBox_102.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_102.addItem(str(i[0]))

    def Read_mSon3_Study_In_List(self):
        self.comboBox_103.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_103.addItem(str(i[0]))

    # 4st
    def Read_mSon4_Work_In_List(self):
        self.comboBox_104.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_104.addItem(str(i[0]))

    def Read_mSon4_Study_In_List(self):
        self.comboBox_105.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_105.addItem(str(i[0]))

    # 5st
    def Read_mSon5_Work_In_List(self):
        self.comboBox_106.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_106.addItem(str(i[0]))

    def Read_mSon5_Study_In_List(self):
        self.comboBox_107.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_107.addItem(str(i[0]))

    # 6st
    def Read_mSon6_Work_In_List(self):
        self.comboBox_108.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_108.addItem(str(i[0]))

    def Read_mSon6_Study_In_List(self):
        self.comboBox_109.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_109.addItem(str(i[0]))

    # 7st
    def Read_mSon7_Work_In_List(self):
        self.comboBox_110.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_110.addItem(str(i[0]))

    def Read_mSon7_Study_In_List(self):
        self.comboBox_111.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_111.addItem(str(i[0]))

    # 8st
    def Read_mSon8_Work_In_List(self):
        self.comboBox_112.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_112.addItem(str(i[0]))

    def Read_mSon8_Study_In_List(self):
        self.comboBox_113.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_113.addItem(str(i[0]))

    # 9st
    def Read_mSon9_Work_In_List(self):
        self.comboBox_114.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_114.addItem(str(i[0]))

    def Read_mSon9_Study_In_List(self):
        self.comboBox_115.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_115.addItem(str(i[0]))

    # 10st
    def Read_mSon10_Work_In_List(self):
        self.comboBox_116.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_116.addItem(str(i[0]))

    def Read_mSon10_Study_In_List(self):
        self.comboBox_117.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Study from StudyS')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_117.addItem(str(i[0]))

    # Edit Male Armal Tab ==============================
    # Street
    def Read_Street_FArmal_Data(self):
        self.comboBox_333.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_333.addItem(str(i[0]))

    # Work
    def Read_FArmal_Work_In_List(self):
        self.comboBox_335.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkM')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_335.addItem(str(i[0]))

    # Edit FeMale Armal Tab ==============================
    # Street
    def Read_Street_Data_FemaleArmal(self):
        self.comboBox_337.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_337.addItem(str(i[0]))

    # Work
    def Read_Mom_Work_In_List_FemaleArmal(self):
        self.comboBox_336.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_336.addItem(str(i[0]))

    # ================== A3zab Data
    # Work
    def Work_Combo_Male_and_Female_A3zab(self):
        self.comboBox_62.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Work from WorkF')
        x = c.fetchall()
        c.execute('Select Work from WorkM')
        xx = c.fetchall()
        xxx = x + xx
        db.commit()
        db.close()
        for i in xxx:
            self.comboBox_62.addItem(str(i[0]))

    # Street
    def Street_Combo_Male_and_Female_A3zab(self):
        self.comboBox_39.clear()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('Select Street from StreetList')
        x = c.fetchall()
        db.commit()
        db.close()
        for i in x:
            self.comboBox_39.addItem(str(i[0]))

    # ======================================= A33333333zaB Tab ==========================
    # Show All Data for A3zab
    def Show_all_A3zab_Data(self):
        try:
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            sql = '''SELECT MName,Street,Address,Work,DOF,Phone,Relation FROM FatherDead WHERE Relation =?'''
            xs = 'عزباء'
            x = c.execute(sql, [(xs)])
            X = x.fetchall()
            sql = '''SELECT FName,Street,Address,Work,DOB,Phone,Relation FROM MotherDead WHERE Relation =?'''
            ss = 'اعزب'
            x = c.execute(sql, [(ss)])
            Result = x.fetchall()
            Result = Result + X

            p = len(Result)
            for i in Result:
                d = i[4]
                d1 = list(filter(None, d.split('-')))
                d2 = d1[0]
                named_tuple = time.localtime()
                d3 = time.strftime(d2, named_tuple)
                named_tuple = time.localtime()
                time_string = time.strftime("%Y", named_tuple)
                f = int(time_string)
                g = f - int(d3)
                z = i[1]
                z = g
                y = [((i[0]), (i[1]), (i[2]), (i[3]), (z), (i[5]), i[6])]
                Result = Result + y
                self.tableWidget_32.setRowCount(0)
                for row_number, row_data in enumerate(Result[p:]):
                    self.tableWidget_32.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_32.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except:
            pass

    def Selection_A3zab(self):
        try:
            Address = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 2).text()
            Phone = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 5).text()
            self.lineEdit_54.setText(Address)
            self.lineEdit_50.setText(Phone)
        except:
            pass

    # Update
    def Update_Male_A3zab(self):
        Name = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 0).text()
        Street = self.comboBox_39.currentText()
        Address = self.lineEdit_54.text()
        Work = self.comboBox_62.currentText()
        Phone = self.lineEdit_50.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'UPDATE MotherDead set Street = ?,Address = ?,Work = ?,Phone =? Where FName = ?'
        x = c.execute(Sql, [(Street), (Address), (Work), (Phone), (Name)])
        db.commit()
        db.close()
        self.Clear_Updates()

    def Update_FeMale_A3zab(self):
        Name = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 0).text()
        Street = self.comboBox_39.currentText()
        Address = self.lineEdit_54.text()
        Work = self.comboBox_62.currentText()
        Phone = self.lineEdit_50.text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        Sql = 'UPDATE FatherDead set Street = ?,Address = ?,Work = ?,Phone =? Where MName = ?'
        x = c.execute(Sql, [(Street), (Address), (Work), (Phone), (Name)])
        db.commit()
        db.close()
        self.Clear_Updates()

    def Clear_Updates(self):
        Street = self.comboBox_39.setCurrentIndex(0)
        Address = self.lineEdit_54.setText('')
        Work = self.comboBox_62.setCurrentIndex(0)
        Phone = self.lineEdit_50.setText('')

    def Confirm_Update_A3zab_Data(self):
        Relation = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 6).text()
        if Relation == 'اعزب':
            Replay = QMessageBox.information(QWidget(), 'معذرة', 'هل انت متاكد من تعديل البيانات    ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Update_Male_A3zab()
                self.Show_all_A3zab_Data()
                self.Clear_Updates()
                QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح   ')
        elif Relation == 'عزباء':
            Replay = QMessageBox.information(QWidget(), 'معذرة', 'هل انت متاكد من تعديل البيانات    ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Update_FeMale_A3zab()
                self.Show_all_A3zab_Data()
                self.Clear_Updates()
                QMessageBox.information(self, 'جيد', 'تم التعديل بنجاح   ')

    # Delete
    def Delete_A3zab_FeMale(self):
        Name = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''DELETE FROM FatherDead Where MName= ?'''
        c.execute(sql, [(Name)])
        db.commit()
        db.close()

    def Delete_A3zab_Male(self):
        Name = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 0).text()
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''DELETE FROM MotherDead Where FName= ?'''
        c.execute(sql, [(Name)])
        db.commit()
        db.close()

    def Confirm_Delete_A3zab_Data(self):
        Relation = self.tableWidget_32.item(self.tableWidget_32.currentRow(), 6).text()
        print(Relation)
        if Relation == 'اعزب':
            Replay = QMessageBox.information(QWidget(), 'معذرة', 'هل انت متاكد من حذف البيانات    ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Delete_A3zab_Male()
                self.Show_all_A3zab_Data()
                self.Clear_Updates()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح   ')
                self.Show_all_A3zab_Data()
        elif Relation == 'عزباء':
            Replay = QMessageBox.information(QWidget(), 'معذرة', 'هل انت متاكد من حذف البيانات    ؟!!',
                                             QMessageBox.Yes | QMessageBox.No)
            if Replay == QMessageBox.Yes:
                self.Delete_A3zab_FeMale()
                self.Show_all_A3zab_Data()
                self.Clear_Updates()
                QMessageBox.information(self, 'جيد', 'تم الحذف بنجاح   ')
                self.Show_all_A3zab_Data()

    # Search A3zab Tab
    def Search_A3zab_Male_Tab_By_Name(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Street,Address,Work,DOB,Phone,Relation FROM MotherDead Where Relation =? and FName LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_40.text()
        Relation = 'اعزب'
        x = c.execute(sql, [(Relation),(Name)])
        Result = x.fetchall()

        sql = '''SELECT MName,Street,Address,Work,DOF,Phone,Relation FROM FatherDead Where Relation =? and MName LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_40.text()
        Relation = 'عزباء'
        x = c.execute(sql, [(Relation),(Name)])
        X = x.fetchall()
        Result = X + Result
        self.tableWidget_32.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_32.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_32.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Search_A3zab_Male_Tab_By_Phone(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = '''SELECT FName,Street,Address,Work,DOB,Phone,Relation FROM MotherDead Where Relation = ? and Phone LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_58.text()
        Relation = 'اعزب'
        x = c.execute(sql, [(Relation),(Name)])
        Result = x.fetchall()
        sql = '''SELECT MName,Street,Address,Work,DOF,Phone,Relation FROM FatherDead Where Relation = ? and Phone LIKE ('%' || ? || '%') '''
        Name = self.lineEdit_58.text()
        Relation = 'عزباء'
        x = c.execute(sql, [(Relation),(Name)])
        X = x.fetchall()

        Result = Result + X
        self.tableWidget_32.setRowCount(0)
        for row_number, row_data in enumerate(Result):
            self.tableWidget_32.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_32.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def Cleaaar(self):
        self.lineEdit_40.setText('')
        self.lineEdit_58.setText('')

    def Exit(self):
        sys.exit()

    def Go_To_Login(self):
        self.window2 = login()
        self.close()
        self.window2.show()

''' 
    def sfakjdsokfg(self):

        d = []
        for row in rrt: # نعمل فور للقراءة
            d.append(row)
            n = []
            for i in d:
                for u in i:
                    n.append(u)
                    if len(n) >= 5 :
                        x1 = n[-5]
                        x2 = n[-4]
                        x3 = n[-3]
                        x4 = n[-2]
                        x5 = n[-1]
                    if len(n) >= 10:
                        x6 = n[-10]
                        x7 = n[-9]
                        x8 = n[-8]
                        x9 = n[-7]
                        x10 = n[-6]
                    if len(n) >= 15:
                        x11 = n[-15]
                        x12 = n[-14]
                        x13 = n[-13]
                        x14 = n[-12]
                        x15 = n[-11]
                    if len(n) >= 20:
                        x16 = n[-20]
                        x17 = n[-19]
                        x18 = n[-18]
                        x19 = n[-17]
                        x20 = n[-16]
                    if len(n) >= 25:
                        x21 = n[-25]
                        x22 = n[-24]
                        x23 = n[-23]
                        x24 = n[-22]
                        x25 = n[-21]
                    if len(n) > 26:
                        with open('nm1_cli.csv', 'w') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow(sn1) # المراد طبعه
                        if len(n) >= 5:
                            self.tableWidget_4.setItem(0, 0, QTableWidgetItem(str(x1)))
                            self.tableWidget_4.setItem(0, 1, QTableWidgetItem(str(x2)))
                            self.tableWidget_4.setItem(0, 2, QTableWidgetItem(str(x3)))
                            self.tableWidget_4.setItem(0, 3, QTableWidgetItem(str(x4)))
                            self.tableWidget_4.setItem(0, 4, QTableWidgetItem(str(x5)))
                        if len(n) >= 10:
                            self.tableWidget_4.setItem(1, 0, QTableWidgetItem(str(x6)))
                            self.tableWidget_4.setItem(1, 1, QTableWidgetItem(str(x7)))
                            self.tableWidget_4.setItem(1, 2, QTableWidgetItem(str(x8)))
                            self.tableWidget_4.setItem(1, 3, QTableWidgetItem(str(x9)))
                            self.tableWidget_4.setItem(1, 4, QTableWidgetItem(str(x10)))
                        if len(n) >= 15:
                            self.tableWidget_4.setItem(2, 0, QTableWidgetItem(str(x11)))
                            self.tableWidget_4.setItem(2, 1, QTableWidgetItem(str(x12)))
                            self.tableWidget_4.setItem(2, 2, QTableWidgetItem(str(x13)))
                            self.tableWidget_4.setItem(2, 3, QTableWidgetItem(str(x14)))
                            self.tableWidget_4.setItem(2, 4, QTableWidgetItem(str(x15)))
                        if len(n) >= 20:
                            self.tableWidget_4.setItem(3, 0, QTableWidgetItem(str(x16)))
                            self.tableWidget_4.setItem(3, 1, QTableWidgetItem(str(x17)))
                            self.tableWidget_4.setItem(3, 2, QTableWidgetItem(str(x18)))
                            self.tableWidget_4.setItem(3, 3, QTableWidgetItem(str(x19)))
                            self.tableWidget_4.setItem(3, 4, QTableWidgetItem(str(x20)))
                        if len(n) >= 25:
                            self.tableWidget_4.setItem(4, 0, QTableWidgetItem(str(x21)))
                            self.tableWidget_4.setItem(4, 1, QTableWidgetItem(str(x22)))
                            self.tableWidget_4.setItem(4, 2, QTableWidgetItem(str(x23)))
                            self.tableWidget_4.setItem(4, 3, QTableWidgetItem(str(x24)))
                            self.tableWidget_4.setItem(4, 4, QTableWidgetItem(str(x25)))

'''
'''
    def Date_To_Age(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        sql = 'SELECT * FROM FatherAftkad Where Name=?'
        Name ='مينا شحاته'
        x = c.execute(sql, [(Name)])
        evx = x.fetchall()
        print(evx)
        ###############
        # A اخراج ميلاد المستخدم
        d = str(evx[0][6])
        d1 = list(filter(None, d.split('/')))  #
        d2 = d1[2]
        named_tuple = time.localtime()  # get struct_time
        d3 = time.strftime(d2, named_tuple)
        ###########
        # A اخراج العام الحالي
        named_tuple = time.localtime()
        time_string = time.strftime("%Y", named_tuple)
        f = int(time_string)  # الوقت الحالي
        g = f - int(d3)
        print(g)
        print('gooood')
'''
class login(QMainWindow, MainUI3):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Method for handle all Buttons
        self.Handle_Buttons()

    def Handle_Buttons(self):
        # Button to login employee
        self.pushButton.clicked.connect(self.register)
        # Button from get pass by ssn to main registration
        self.pushButton_12.clicked.connect(self.open_Registration)
        # Button to creat employee
        self.pushButton_3.clicked.connect(self.create_account_Emp)
        # Button Go to forget password
        self.pushButton_10.clicked.connect(self.open_Forget_password)
        # button back to register
        self.pushButton_4.clicked.connect(self.open_Registration)
        # button to return to new registration
        self.pushButton_2.clicked.connect(self.open_tab_New_Registration)
        # button to confirm changing password
        self.pushButton_7.clicked.connect(self.Chage_Password)
        # for clearing line edits after confirmation
        self.pushButton_7.clicked.connect(self.Clear_Changing_password_Lineedit)
        # Button to open main program registration
        self.pushButton_5.clicked.connect(self.Pass_To_Program)
        # Button to go to change password
        self.pushButton_9.clicked.connect(self.Go_To_Change_pass)
        # Button Back to Register with new password
        self.pushButton_8.clicked.connect(self.Back_To_Register)
        # Call Method of Hidden Tabs Bar (main)
        self.Hidden_Tab_Bar()
        # Execute Current Tab
        self.Current_Tabs()
        # Button for Close The Program\
        self.pushButton_6.clicked.connect(self.Close_Login_page)
        # Button for Searching Password
        self.pushButton_11.clicked.connect(self.get_password_By_Ssn)

    def Hidden_Tab_Bar(self):
        # Which Hidden Admin TabWidgets
        self.tabWidget.tabBar().setVisible(False)

    def Current_Tabs(self):
        # current tab in main window
        self.tabWidget.setCurrentIndex(0)

    def Close_Login_page(self):
        sys.exit()

    def Go_To_Change_pass(self):
        self.tabWidget.setCurrentIndex(1)

    def Back_To_Register(self):
        self.tabWidget.setCurrentIndex(0)

    def open_Registration(self):
        self.tabWidget.setCurrentIndex(2)

    def Pass_To_Program(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            self.c = db.cursor()
        self.c.execute('SELECT * FROM Registration')
        data = self.c.fetchall()
        Password = str(self.lineEdit_6.text())
        for row in data:
            if (Password == str(row[0])):
                self.open_Registration()
                db.close()

            else:
                QMessageBox.warning(QWidget(), "Error", 'Error!!!Check Password Aagin')

    def Clear_Changing_password_Lineedit(self):
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')

    def Chage_Password(self):
        x = str(self.lineEdit_7.text())
        y = str(self.lineEdit_8.text())
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        c.execute('SELECT * FROM Registration')
        data = c.fetchall()
        for row in data:
            if (str(row[0]) == x and x.strip(" ") != "" and y.strip(" ") != ""):
                c.execute('UPDATE Registration set password = ' + y)
                db.commit()
                QMessageBox.information(QWidget(), "Welcome", 'Password has Changed')
                db.close()
            else:
                QMessageBox.warning(QWidget(), "Error", 'Error!!!Check Password Aagin')

    def open_tab_New_Registration(self):
        self.tabWidget.setCurrentIndex(3)

    def open_Forget_password(self):
        self.tabWidget.setCurrentIndex(4)

    def clear_creat_Emp(self):
        self.lineEdit_3.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_10.setText('')

    def create_account_Emp(self):

        gender = None
        name = str(self.lineEdit_3.text())
        Ssn = self.lineEdit_9.text()
        password = str(self.lineEdit_5.text())
        church = str(self.lineEdit_12.text())
        freconize = str(self.lineEdit_13.text())
        Qulified = str(self.lineEdit_11.text())
        work = str(self.lineEdit_10.text())

        gender = 'Male'
        if self.radioButton_2.isChecked():
            gender = str('Female')
        if name == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من الاسم من فضلك !!')
        if password == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من كلمه المرور من فضلك !!')
        if Ssn == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من الرقم القومي من فضلك !!')
        if work == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من العمل من فضلك !!')
        if Qulified == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من المؤهل من فضلك !!')
        if church == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من اسم الكنيسه من فضلك !!')
        if freconize == '':
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من اب الاعتراف من فضلك !!')
        try:

            if name != '' and password != '' and Ssn != '' and church != '' and freconize != '' and Qulified != '' and work != '' and len(
                    Ssn) >= 14 and int(Ssn) != str(Ssn):
                with sqlite3.connect('Akhwet_El_Rab.db') as db:
                    c = db.cursor()
                c.execute('INSERT INTO RecordEmpData VALUES(?,?,?,?,?,?,?,?)',
                          (name, password, Ssn, work, church, freconize, gender, Qulified))
                db.commit()
                db.close()
                self.clear_creat_Emp()
                QMessageBox.information(QWidget(), "Success!!", 'Account Created Successfully .')
            else:
                QMessageBox.information(self, 'معذرة', 'برجاء التاكد من الرقم القومي من انه 14 رقم !!')
        except:
            QMessageBox.information(self, 'معذرة', 'برجاء التاكد من الرقم القومي من انه 14 رقم !!')

    def register(self):
        with sqlite3.connect('Akhwet_El_Rab.db') as db:
            c = db.cursor()
        username = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())
        c.execute('SELECT * FROM RecordEmpData')
        data = c.fetchall()
        db.commit()
        db.close()
        for row in data:
            if (username == 'مينا' and password == '0000'):
                self.window2 = Main()
                self.close()
                self.window2.show()
                break
            elif row[0] == str(username) and row[1] == str(password):
                self.window2 = Aftkad()
                self.close()
                self.window2.show()
                break
        else:
            QMessageBox.warning(QWidget(), "Error", 'Error !!! Check Username & Password.')
            pass

    ''' or username == 'مينا' and password == '0000' '''

    def get_password_By_Ssn(self):
        try:
            with sqlite3.connect('Akhwet_El_Rab.db') as db:
                c = db.cursor()
            Ssn = str(self.lineEdit_15.text())
            c.execute('SELECT password FROM RecordEmpData where Ssn = ' + Ssn)
            data = c.fetchall()
            db.close()
            for index in data:
                self.lineEdit_16.setText(str(index[0]))
        except:
            QMessageBox.warning(QWidget(), "Error", 'Error !!! Check Ssn again.')
            pass


def main():
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
