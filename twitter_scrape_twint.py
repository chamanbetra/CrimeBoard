import twint

# Configure
c = twint.Config()
c.Profile_full = True
c.Username = "realDonaldTrump"
c.Search = "great"

# Run
twint.run.Search(c)