### Basic Preliminaries
- Get required Acorn components running as described in `/esit-migrate/README.md`.

- Make sure you have python3 installed on your machine.

- Add a `.env` file to `esit-migrate/src` with the following variables.

```
UW_EMAIL=<MYNETID@uw.edu>
UW_NETID=<MYNETID>
UW_PASSWORD=<MYNETID_PASSWORD>
```

- Update `esit-migrate/src/bin` with a new chromedriver as needed. As of this writing, the chromedriver there is 88.0.4324.96. Current drivers are [here](https://chromedriver.chromium.org/downloads). 

### Run an Automated Referral with Selenium

- From `esit-migrate/src/` run 

```
python3 authomate_referral.py
```

**The above script performs the following tasks**

1. Uses selenium to log into the development environment. 

2. Uses selenium to enter a referral (hard coded for now). 

3. Attempts to scrape cookies from the "manually" entered referral and make a post (NOTE: This last step is currently resulting in a 401). 
