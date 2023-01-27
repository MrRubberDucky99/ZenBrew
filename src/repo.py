import urllib, json, subprocess, requests
from pathlib import Path
class Repo:
        def __init__(self, url):
                self.url = url
                self.downloaded = False
                file = urllib.urlopen(self.url + "repo.json")
                self.json = json.load(file)
                file.close()
                self.name = self.json["Name"]
                self.format = self.json["Format"]
                self.packageFile = self.json["Packages"]
        
        def downloadPackagesList(self):
                pass

class LocalRepo(Repo):
        def __init__(self, path):
                self.downloaded = True
                file = open(self.path + "repo.json")
                self.json = json.load(file)
                file.close()
                self.name = self.json["Name"]
                self.format = self.json["Format"]
                self.packageFile = self.json["Packages"]
        
        def downloadPackagesList(self):
                pass

class Package:
        def __init__(self, repoURL, jsonFile):
                self.url = repoURL + jsonFile
                self.downloaded = False
                file = urllib.urlopen(self.url)
                self.json = json.load(file)
                file.close()
                self.name = self.json["Name"]
                self.Identifier = self.json["Identifier"]
                self.Description = self.json["Description"]
                self.Author = self.json["Author"]
                self.PackageLocation = self.json["Package Location"]
                self.Type = self.json["Type"]
                self.Script = self.json["Script"]
                self.AllowedInstallTypes = self.json["AllowedInstallTypes"]
                self.FileType = self.json["FileType"]

        def download(self):
                file = urllib.urlopen(self.PackageLocation)
                save = open("Cache/" + self.Identifier + "." + self.FileType, "w")
                save.write(file)
                file.close()
                save.close()

file = requests.get("https://raw.githubusercontent.com/BlackIQ/Hello-World/main/Python/examples/python.py")
save = Path("helloWords.py")
save.write_bytes(file.content)
file.close()