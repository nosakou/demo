# Demo project

# Installation
virtualenv env --pyrhon=python3.7
source env/bin/activate
pip install -r requirements.txt

# Page Object tests start
pytest page_object/ui_test.py

# Behave tests start
behave @behave_test/test.featureset
behave behave_test/features/onboarding.feature

# Robot tests start
robot robot_test/test.robot
