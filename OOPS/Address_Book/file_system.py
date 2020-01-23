import json
class FileSystem:

    def readFile(self,file_name):
        with open(file_name,'r') as file_list:
            s = json.load(file_list)
            return s

    def saveFile(self,data,file_name):
        with open(file_name,'w') as file_list:
            json.dump(data,file_list,indent=4)
