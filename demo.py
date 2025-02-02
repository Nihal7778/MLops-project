import os
from us_visa.constants import MONGODB_URL_KEY
mongo_db_url = os.getenv(MONGODB_URL_KEY)
print(mongo_db_url)


