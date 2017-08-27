Installation
==================

Requirements

1. Python 2.7x
2. MongoDB
3. Redis

## For Linux, PIP an Virtual Environment Setup

    sudo apt-get install python-pip python-dev build-essential
    sudo apt-get install python-pip
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

## For MacOSX, PIP and Virtual Environment Setup

For MacOSX users, `Homrbrew` and `XCode command line tools` are needed.

HomeBrew setup:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

XCode command line tools setup:

    xcode-select --install

And Then:

    sudo easy_install pip
    sudo apt-get install python-pip
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

For Virtual Environment:

    virtualenv argumanorg
    source argumanorg/bin/active

And you need to clone project and install requirements

    git clone git@github.com:arguman/arguman.org.git
    cd arguman.org
    pip install -r requirements.txt

Start MongoDB (http://docs.mongodb.org/manual/installation/)

    mongod

For MacOSX, setup Redis

    brew install redis-server

For Linux setup Redis (For latest version of Redis https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)

    sudo apt-get install redis-server

Start Redis:

    redis-server

Start the application of arguman:

    cd web
    python manage.py migrate
    python manage.pr runserver


The End
:tada:

# Setting up Arguman on its own domain

If you want to create independent domain name and branding for arguman in your country 
then configure following variables in `settings_local.py` config file.

1. Set current language:
    ```python
    LANGUAGE_CODE = 'pl'
    AVAILABLE_LANGUAGES = ('pl',)
    ```
1. Set contact info
    ```python
    CONTACT_SUBREDDIT = None
    CONTACT_TWITTER = None
    CONTACT_EMAIL = 'kontakt@kodujdlapolski.pl' 
    ``` 
2. Disable middleware responsible for choosing language based on a subddomain:
    ```python
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # 'i18n.middleware.SubdomainLanguageMiddleware',  # disable
        'i18n.middleware.MultipleProxyMiddleware'
    )
    ```
2. Set website title
    ```python
    TITLE = 'The debate' # or
    # LOGO_PATH = 'img/logo-debate.png'  # path relative to the /static/ directory; if no logo is defined then TITLE is used
    ```