import twint#configuration
config = twint.Config()
config.Username = "bostonpolice"
config.Search = "crime"
config.Lang = "en"
config.Limit = 100
config.Since = "2022-10-01"
config.Until = "2022-11-02"
config.Store_json = True
config.Output = "custom_out.json"#running search
twint.run.Search(config)