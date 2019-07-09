class AsciiTable:
    """This class is responsible for creating AsciiTable and fill it with data
    in the constructor we create table with empty row
    """
    def __init__(self):
        self.table=["empty row"]
    def addRow(self,r):
        """Add row of data in the table.
        Arguments:
            r {list} -- the values in the cells
        """
        self.table.append(r)
    def setTitles(self,r):
        """Set the titles of the table columns.
        Arguments:
            r {list} -- the titles of the table
        """
        self.table[0]=r
    def getTitles(self):
        """Get the Titles of the table columns .
        Returns:
            list -- the titles of the table columns
        """
        return self.table[0]
    def getRow(self,id):
        """Get the a row of Data by an id .
        Arguments:
            id {int} -- the id of the row needed
        Returns:
            list -- the row of data
        """
        for i in self.table:
            if i[0]==id:
                return i
        return None
    def maxWidth(self):
        """Get the max width of table columns .
        Returns:
            list -- the max width of the table columns
        """
        colNum=len(self.table[0])
        colWidth=[]
        while colNum>0:
            colWidth.append(0)
            colNum-=1

        for r in self.table:
            colNum = len(colWidth) - 1
            while colNum>=0:
                if len(r[colNum]) > colWidth[colNum]:
                    colWidth[colNum]=len(r[colNum])
                colNum-=1
        return colWidth
    def printDashLine(self):
        """Print a dash line at first and end of the table and between rows .
        Returns:
            line {str} -- the dash line ready to be printed
        """
        line = "+"
        mWidth = self.maxWidth()
        for i in mWidth:
            for j in range(0,i):
                line += "-"
            line+="+"
        return line
    def printTable(self):
        """Print the whole f*cking table .
        Returns:
            table {str} -- the table ready to be printed
        """
        table=self.printDashLine()+"\n"
        mWidth=self.maxWidth()
        for r in self.table:
            cNum=0
            for c in r:
                table+="|"+c
                for s in range(0,mWidth[cNum]-len(c)):
                    table+=" "
                cNum+=1
            table+="|\n"+self.printDashLine()+"\n"
        return table

if __name__ == '__main__':
    ta=AsciiTable()
    ta.setTitles(["id","name","Date"])
    ta.addRow(["1", "ffffffff", "15-9-1998"])
    ta.addRow(["5684556", "ggggggggggg", "1-1-1990"])
    print(ta.maxWidth())
    print(ta.printTable())


