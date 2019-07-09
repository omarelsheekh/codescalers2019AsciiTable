from asciiTable import AsciiTable
import unittest
import time
class AsciiTableTest(unittest.TestCase):
    def setUp(self):
        self.t=AsciiTable()
        self.t.setTitles(["id", "name", "Date"])
        self.t.addRow(["1", "omar", "15-9-1998"])
        self.t.addRow(["5", "ahmed", "1-1-1990"])
    def test_setAndGetTitles(self):
        titles=["id", "name", "Date"]
        self.assertEqual(titles,self.t.getTitles())
    def test_addAndGetRows(self):
        omar=["1","omar","15-9-1998"]
        ahmed=["5","ahmed","1-1-1990"]
        self.assertEqual(omar,self.t.getRow("1"))
        self.assertEqual(ahmed,self.t.getRow("5"))
    def test_printDashLine(self):
        self.assertEqual("+--+-----+---------+",self.t.printDashLine())
    def test_printTable(self):
        table="""
+--+-----+---------+
|id|name |Date     |
+--+-----+---------+
|1 |omar |15-9-1998|
+--+-----+---------+
|5 |ahmed|1-1-1990 |
+--+-----+---------+
"""
        self.assertEqual(table.strip(),self.t.printTable().strip())
if __name__ == '__main__':
    unittest.main()