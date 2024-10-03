import unittest

import CrimeDataSolution as cds


class CrimeDataTesting(unittest.TestCase):

    def test_read_in_file(self):
        """ read_in_file function returns correct values """
        filename = "CrimeDataSmall.csv"

        lst = cds.read_in_file(filename)

        self.assertIsInstance(lst, list, "Returned datatype should be a list")
        self.assertEqual(len(lst), 4, "There should be 4 rows returned from CrimeDataSmall 1 header and 3 data rows")
        self.assertEqual(len(lst[0]), 23, "Each row should have 23 columns")
        self.assertEqual(lst[0][1], "Reported_Date", "Column 1 was incorrect header")
        self.assertEqual(lst[0][7], "Offense", "Column 7 was incorrect header")
        self.assertEqual(lst[0][13], "Zip Code", "Column 13 header was incorrect")
        self.assertEqual(lst[1][1], "03/19/2019", "Column 1 was incorrect in first data row")
        self.assertEqual(lst[1][7], "Vehicular – Non-Injury", "Column 7 was incorrect in first data row")
        self.assertEqual(lst[1][13], "64161", "Column 13 in first data row was incorrect")
        self.assertEqual(lst[3][1], "03/27/2019", "Column 1 was incorrect in 3rd data row")
        self.assertEqual(lst[3][7], "Embezzlement", "Column 7 was incorrect 3rd data row")
        self.assertEqual(lst[3][13], "64112", "Column 13 3rd data row was incorrect")
        self.assertEqual(lst[3][11], "4600,  S WORNALL RD", "Column 11 3rd data row was incorrect.  Use csv module to read ")
        
    def test_month_from_number(self):
        """ month_from_number returns string representation of integer month """
        self.assertEqual(cds.month_from_number(1).lower(), "january")
        self.assertEqual(cds.month_from_number(2).lower(), "february")
        self.assertEqual(cds.month_from_number(3).lower(), "march")
        self.assertEqual(cds.month_from_number(4).lower(), "april")
        self.assertEqual(cds.month_from_number(5).lower(), "may")
        self.assertEqual(cds.month_from_number(6).lower(), "june")
        self.assertEqual(cds.month_from_number(7).lower(), "july")
        self.assertEqual(cds.month_from_number(8).lower(), "august")
        self.assertEqual(cds.month_from_number(9).lower(), "september")
        self.assertEqual(cds.month_from_number(10).lower(), "october")
        self.assertEqual(cds.month_from_number(11).lower(), "november")
        self.assertEqual(cds.month_from_number(12).lower(), "december")

    def test_month_from_number_raises_error_if_not_1_to_12(self):
        """ month_from_number raises valueerror if not a valid month"""

        with self.assertRaises(ValueError, msg="Should raise a value error if month is 0") as ctx:
            cds.month_from_number(0)
        with self.assertRaises(ValueError, msg="Should raise a value error if month is 13") as ctx:
            cds.month_from_number(13)
        with self.assertRaises(ValueError, msg="Should raise a value error if month is 110") as ctx:
            cds.month_from_number(110)


    def test_create_reported_date_dict(self):
        """ create_reported_date_dict returns a valid dictionary """

        data = [
                ['Report_No', 'Reported_Date', 'Reported_Time', 'From_Date', 'From_Time', 'To_Date', 'To_Time', 'Offense', 'IBRS', 'Description', 'Beat', 'Address', 'City', 'Zip Code', 'Rep_Dist', 'Area', 'DVFlag', 'Involvement', 'Race', 'Sex', 'Age', 'Firearm Used Flag', 'Location'],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '04/21/2019', '', '', '', '', '', 'Arson', '', '', '', '', '', '64125', '', '', '', '', '', '', '', '', '']
                ]
        result = cds.create_reported_date_dict(data)
        self.assertIsInstance(result, dict, "function should return a dictionary")
        self.assertEqual(len(result), 2, "There should be 2 items in the dictionary")
        self.assertEqual(result["03/19/2019"], 2, "value incorrect for key '03/19/2019'")
        self.assertEqual(result["04/21/2019"], 1, "value incorrect for key '04/21/2019'")


    def test_create_reported_month_dict(self):
        """ create_reported_month_dict returns a valid dictionary """

        data = [
                ['Report_No', 'Reported_Date', 'Reported_Time', 'From_Date', 'From_Time', 'To_Date', 'To_Time', 'Offense', 'IBRS', 'Description', 'Beat', 'Address', 'City', 'Zip Code', 'Rep_Dist', 'Area', 'DVFlag', 'Involvement', 'Race', 'Sex', 'Age', 'Firearm Used Flag', 'Location'],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '04/21/2019', '', '', '', '', '', 'Arson', '', '', '', '', '', '64125', '', '', '', '', '', '', '', '', '']
                ]
        result = cds.create_reported_month_dict(data)
        self.assertIsInstance(result, dict, "function should return a dictionary")
        self.assertEqual(len(result), 2, "There should be 2 items in the dictionary")
        self.assertEqual(result[3], 2, "value incorrect for key 3")
        self.assertEqual(result[4], 1, "value incorrect for key 4")


    def test_create_offense_dict(self):
        """ create_offense_dict returns a valid dictionary """

        data = [
                ['Report_No', 'Reported_Date', 'Reported_Time', 'From_Date', 'From_Time', 'To_Date', 'To_Time', 'Offense', 'IBRS', 'Description', 'Beat', 'Address', 'City', 'Zip Code', 'Rep_Dist', 'Area', 'DVFlag', 'Involvement', 'Race', 'Sex', 'Age', 'Firearm Used Flag', 'Location'],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '04/21/2019', '', '', '', '', '', 'Arson', '', '', '', '', '', '64125', '', '', '', '', '', '', '', '', '']
                ]
        result = cds.create_offense_dict(data)
        self.assertIsInstance(result, dict, "function should return a dictionary")
        self.assertEqual(len(result), 2, "There should be 2 items in the dictionary")
        self.assertEqual(result["Vehicular"], 2, "value incorrect for key 'Vehicular'")
        self.assertEqual(result["Arson"], 1, "value incorrect for key 'Arson'")


    def test_create_offense_by_zip_dict(self):
        """ create_offense_dict returns a valid dictionary """

        data = [
                ['Report_No', 'Reported_Date', 'Reported_Time', 'From_Date', 'From_Time', 'To_Date', 'To_Time', 'Offense', 'IBRS', 'Description', 'Beat', 'Address', 'City', 'Zip Code', 'Rep_Dist', 'Area', 'DVFlag', 'Involvement', 'Race', 'Sex', 'Age', 'Firearm Used Flag', 'Location'],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', ''],
                ['', '03/19/2019', '', '', '', '', '', 'Vehicular', '', '', '', '', '', '64125', '', '', '', '', '', '', '', '', ''],
                ['', '04/21/2019', '', '', '', '', '', 'Arson', '', '', '', '', '', '64161', '', '', '', '', '', '', '', '', '']
                ]
        result = cds.create_offense_by_zip(data)
        self.assertIsInstance(result, dict, "function should return a dictionary")
        self.assertEqual(len(result), 2, "There should be 2 items in the dictionary")
        self.assertIsInstance(result["Vehicular"], dict, "value for key Vehicular should be a dicationary")
        self.assertIsInstance(result["Arson"], dict, "value for key Arson should be a dicationary")

        self.assertEqual(len(result["Vehicular"]), 2, "dictionary for key Vehicular should have 2 items in it")
        self.assertEqual(result["Vehicular"], {'64161':1,'64125':1}, "value for dictionary key Vehicular incorrect")
        self.assertEqual(result["Arson"], {'64161':1}, "value for dictionary key Vehicular incorrect")

        
if __name__ == "__main__":

    unittest.main()
