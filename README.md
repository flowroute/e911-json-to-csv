# e911-json-to-csv

## WIP Dockerized JSON to CSV Python App with a GUI

**Topics**

*   [Requirements](#requirements)
*   [Installation](#installation)
*   [Usage](#usage)

Download all E911 records from your account and write them to a CSV using this Python GUI app. This E911 JSON to CSV app runs on Python 2.7 and leverages the classic Tkinter module for the GUI that you will be interacting with. It has been tested on `Ubuntu 16.04` and `macOS High Sierra 10.13.4`. 


* * *
Requirements
------------

*   Flowroute [API credentials](https://manage.flowroute.com/accounts/preferences/api/)
*   [Python](https://www.python.org/downloads/): `Python 2 >=2.7.9`

* * *
Installation
------------

1. First, start a shell session and clone the Python GUI app:
    * via HTTPS: `git clone https://github.com/flowroute/e911-json-to-csv.git`

    * via SSH: `git@github.com:flowroute/e911-json-to-csv.git`

2. Switch to the newly-created `e911-json-to-csv` directory. 

3. If you are running Python 2.7, skip this step and see [Usage](#usage) below. To confirm which version of Python you are running on a Mac, run the following:

`python --version`

If you do not have Python 2.7, see [Python 2.7.0 Release](https://www.python.org/download/releases/2.7/) or set up a [virtual environment for Python 2.7](https://virtualenv.pypa.io/).



* * *
Usage
------------

Tkinter is Python's de-facto standard GUI (Graphical User Interface) package, yet I have only heard of it yesterday. I like the simplicity and I can see why it continues to be supported and is considered a minor tradition of the Python world. To systematically check for Tkinter support on your machine, see [Checking your Tkinter support] (https://wiki.python.org/moin/TkInter) on the Python wiki Tkinter page. If you encounter a module or package not found error, refer to Installing Packages [https://packaging.python.org/tutorials/installing-packages/] in the Python Packaging User Guide to learn more about different ways to install Python packages.


### Run the app locally

With all installation requirements out of the way, simply run the following:

`python json2csv.py`

This should pop up a small window which will require your Flowroute API Access Key or `username`, Secret Key or `password`, and Output File or `path` to write your CSV file to. Since I'm lazy, I ran the following optional step:

#### Set and source environment variables

To learn more about setting environment variables, see [How To Read and Set Environmental and Shell Variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps). In a pinch, you can create an `fr_env.sh` file in the same directory and add the following lines:

```bash
export FR_ACCESS_KEY=<YOUR_FR_ACCESS_KEY>
export FR_SECRET_KEY=<YOUR_FR_SECRET_KEY>
export FR_CSV_OUTPUT=/path/to/e911.csv
```

Source the file as follows:
`. fr_env.sh`

Then run json2csv.py as shown above. With your credentials auto-populated like shown in the screenshot below, click Write CSV to write the file to the path that you specified. 

![python-e911-csv.png](https://github.com/flowroute/e911-to-csv/blob/master/images/python-3911-csv.png?raw=true)

To review the CSV file that has been downloaded to the path that you specified, open the file. That's it! Start doing your data magic. 
