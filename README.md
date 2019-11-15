# Phishing Site Detection
- web extension to obtain url and indicate state of current site
- extension sends url to back end server
- server has a custom crawler for scraping starting from source urls
- extracts html and url based features prior to performing classification

This readme file provides instructions to run three parts of the project.
Assumption: run on Ubuntu 18.04 and has least the configuration of the VM.

Preliminary preparations:
- change directory data 'cd  crawler/data'
- run sh setup_db.sh   to install mongodb
- install packages in requirements.txt
- pip3 install -r requirements.txt

Part 1. The crawler.
- This section demonstrates our custom crawler. Running it shows crawled sites being saved into the database.
- change directory to src 'cd crawler/src'
- python3 demo.py --crawl True

Part 2. The prediction.
- This section extracts features from websites in real-time. It take a URL, extracts features from it in real-time and returns a prediction. The prediction is sent to the Web Extension to warn the user.
- change directory to src 'cd crawler/src'
- python3 demo.py --predict True --url https://google.com
- check demo.py for URLs to try.

Part 3. The results.
This section demonstrates the results obtained from our CSV features.
- change directory to results 'cd results'
- Included files:
- The '*.csv' files contains the extracted features.
- run 'python3 test.py'. It will produce results using all features. Shows the accuracy vs depth of tree plot in 'num_tree_acc.png'. It also saves the fraction of links at a distance of 1 from the root classified as phishing by our model in 'fraction_links_phishing.csv'.
- run 'python3 test_html_only.py' will produce results using only HTML features.

Outputs:
- 'accuracy.csv' containing accuracy for different classifiers using all features.
- Shows the accuracy vs depth of tree plot in 'num_tree_acc.png'.
- It also saves the fraction of links at a distance of 1 from the root classified as phishing by our model in 'action_links_phishing.csv'.

HTML only:
- run 'python3 test_html_only.py'
Outputs:
- 'accuracy_html_only.csv' containing accuracy for different classifiers using only HTML features.
