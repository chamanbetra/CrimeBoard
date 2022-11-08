#Twitter bot to scrape tweets and insert it into a json file


import twint
import os
config = twint.Config()

config.Username = "bostonpolice"

#Search parameters
config.Search = "killed OR shot OR crime"
config.Lang = "en"
config.Limit = 100
config.Since = "2021-02-01"
config.Until = "2022-11-02"
# check if file exists
if os.path.exists("custom_out.json"):
    os.remove("custom_out.json")
    print("File deleted !")
else:
    print("File doesnot exist !")
config.Store_json = True
config.Output = "custom_out.json"#running search
twint.run.Search(config)