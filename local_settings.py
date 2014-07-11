'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC3f9c151e755b346897d9e25fd10039f8" 
AUTH_TOKEN = "4a27e11696c3e2eff934bbefecc8af9f"
BSSSPAM_APP_SID = "AP57e921d1cb322b4a1de0226f4cec36b8"
BSS_SPAM_ID = "+15084362463"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
