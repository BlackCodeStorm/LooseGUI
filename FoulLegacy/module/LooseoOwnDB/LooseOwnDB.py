class LooseOwnDB:
    def __init__(self,_DataBaseFilePath):
        try:
            self._SystemDataBaseFile = open(_DataBaseFilePath,"r+")
        except:
            return "LIWB.MODULES.SDB.NOFOUNDFILE"
        return "LIWB.MOULES.SDB.RUNFINISH"

    def setDoPlace(self):
        pass