from winreg import CreateKey,SetValueEx,DeleteValue,CloseKey,HKEY_LOCAL_MACHINE,REG_SZ
def newregkey(name,path):
    key=CreateKey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
    SetValueEx(key, name, 0, REG_SZ, path)
    key.Close()
def deleteregkey(name):
    Key = CreateKey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
    DeleteValue(Key, name)
    Key.Close()