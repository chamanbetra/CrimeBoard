import twint

# Configure
# c = twint.Config()
# c.Limit = 1
# c.Username = "bostonpolice"
#
# # Run
# twint.run.Search(c)

# Configure
c = twint.Config()
c.Lang = "en"
c.Hide_output = True
c.Username = "bostonpolice"
c.Search = ['investigation']
c.Limit = 1
# Run
twint.run.Search(c)

