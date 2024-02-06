from module.LooseLogs import LooseLogs
log = LooseLogs.LooseLogs("./debug/test.log","MainThread")
log.initializeLogs()
log.writeLog("INFO","Start the main thread!")
log.writeLogs("INFO",["aaaaaaaaaaaa","aaaaaaaaaaaa","aaaaaaaaaaaa","aaaaaaaaaaaa","aaaaaaaaaaaa",])