# application.py
from titanium_site.app import create_app  # <-- import from the folder

# AWS Elastic Beanstalk looks for 'application' variable
application = create_app()
