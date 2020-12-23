# A symfony message translation plugin for YAZ
TODO: Short description here

# Installing
## From a package
```sh
sudo pip3 install yaz_messaging_plugin
```

## Configure google translate
1. Make a file and store the google credentials,
   see https://cloud.google.com/translate/docs/setup
2. Export the key using
   `export GOOGLE_APPLICATION_CREDENTIALS=/home/user/my-key.json`

# Developing
```bash
# Get the code
git clone git@github.com:boudewijn-zicht/yaz_messaging_plugin.git
cd yaz_messaging_plugin

# Ensure you have python 3.6 or higher and yaz installed
python3 --version

# Setup your virtual environment
virtualenv --python=python3 env
source env/bin/activate
pip install --upgrade yaz pyyml google-cloud-translate
# python setup.py develop

# Run yaz-messaging
./bin/yaz-messaging version --verbose

# Run tests
python test

# Upload a new release to pypi
# Remember to update the version number in ./version.py
python setup.py tag
python setup.py publish

# Once you are done... exit your virtual environment
deactivate
```

# Maintainer
- Boudewijn Schoon <boudewijn@zicht.nl>
