# Sentiment-Analyser
This Program will utilise a Twitter API and perform Sentiment analysis on Tweets by using various algorithms.
![Initial Screen](Page1.png)

![Results Screen](Results.png)

# Tech Stack
- Python
- Flask
- HTML/CSS
- Textblob (NLTK and Pattern.en based ML library)
- Google Voice (Speech to Text) Library
- Tweepy (Twitter API)
- Wordcloud (library)
- SqlLite (DB)
- SQLAlchemy (ORM)
- Pytest & Flask-Testing

# The Team
- Preeti
- Dave
- Neil &
- Sundar


# Setting up your Python environment:
-------------------------------------
1. ```virtualenv -p /usr/local/bin/python3 env && source env/bin/activate``` 
2. ```chmod +x pynion_install.sh && ./pynion_install.sh```
3. One time install (if not done already) ```python -m textblob.download_corpora```
4. One time install (if not done already) ```brew install portaudio```
5. To run ```$ ./app.py```

# If you encounter error while running the app:

 - for matplotlib see **"To fix the matplotlib error if you used pip to install"** section
 - for google voice see **"Google Speech to Text Regonition API"** section
 - for Twitter see **"Twitter API Instructions (One Time Process)"** section
 
 - for NLTK/textblob
 > Note: If you encounter CERTIFICATE_VERIFY_FAILED error then from root of your terminal go to 'Applications --> Python 
 > 3.7 directory' using a new terminal window
    ```
    /$ cd cd Applications/Python\ 3.7/
    /Applications/Python 3.7 $ sudo -H ./Install\ Certificates.command
    and return back to the terminal where your step 7 failed and re-issue it.
    ```

# Creating the database
-----------------------
**One time set-up:**
  ```
  python
  >>> from app import init_db, db_session, db
  >>> from app.models import Pynionquery
  >>> init_db()
  >>> q = Pynionquery("Trump")
  >>> db_session.add(q)
  >>> db_session.commit()
  >>> Pynionquery.query.all()
  ```

# Google Speech to Text Regonition API
---------------------------------------
- As an added feature to sentinent analyser we added voice search capability using an existing google API.
- Create a google cloud account and create a account key in JSON format.
- include in your .bash_profile ```export GOOGLE_APPLICATION_CREDENTIALS="~/Projects/Pynion-Sentiment-Analyser/env/KEY.json"```


# To Test & Check for coverage
------------------------------
1. ```pytest -v```
2. ```coverage run /tests/test_basic.py```
3. ```coverage report project/application path/*.py```
4. ```coverage html project/users/*.py```

# Twitter API Instructions (One Time Process)
---------------------------------------------
1. Register with twitter for API keys from https://developer.twitter.com/en.html
2. Ensure you use a new account and not personal twitter account
3. Activate the account, register 'pynion' app (Only after registering an app you will be able to generate keys)
  i. You will be asked to provide justification etc
  ii. Keep github link handy
4. Generate API and Access Token keys
5. From mac terminal (ensure to do this from your virtual env)

```
  Edit your .bash_profile file found in your home directory

  $ cd ~
  $ ls -la
  # find the .bash_profile and edit it
  # using an editor enter
  export API_KEY=**your api key**
  export API_SECRET_KEY=**your api secret key**
  export ACCESS_TOKEN=**your access token**
  export ACCESS_TOKEN_SECRET=**your access token secret**

  # close all terminals and start a new one and do  printenv to check

```
6. In the terminal type ```printenv``` to see if the keys you created are listed. if not you have not created them under your virtualenv
7. The app is available to be accessed within the network hence if you run the app get your ip address from terminal and access it like ```ifconfig | grep inet``` you will find your ip next next to netmask that you can share with colleagues on the same network.

**To fix the matplotlib error if you used pip to install:**
  ```
  cd ~/.matplotlib
  echo "backend: TkAgg" >> matplotlibrc
  ```
