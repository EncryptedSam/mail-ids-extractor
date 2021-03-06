# Mail Ids Extractor

In a nutshell, it extracts e-mail ids from a given website and feeds them into an Excel Sheet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

Libraries you need to install before you even execute the extractor.py script.
```
beautifulsoup4==4.7.1
bs4==0.0.1
lxml==4.3.2
requests==2.21.0
soupsieve==1.8
urllib3==1.24.1
xlrd==1.2.0
xlwt==1.3.0
```

### Downloading

You can download the project files by clicking on "Clone or download" > "Download ZIP".

### Installing

#### Step 1

Unzip the downloaded file and cd into the folder on your "Terminal or Command prompt" where you've downloaded it.

Example:
```
cd D:\FOLDER-CONTAINING-PROJECT-FILES\
```
```
D:\FOLDER-CONTAINING-PROJECT-FILES>
```

#### Step 2

Execute the command below on you Command "Prompt or Terminal" to download and install the libraries on your local machine with the help of "pip". Make sure that [Python3](https://www.python.org/downloads/) and [Pip3](https://pypi.org/project/pip/) are installed on you local machine.

```
pip install -r requirements.txt --no-index
```
## Before running the tests

### Create text file

Before you even start executing the extractor.py script, you need to create a text file with any name for example "urlist.txt" in the same folder which contains downloaded files and fill it with website urls line by line as shown in the picture below.

![](Images/img_4.PNG)

## Running the tests

To run the tests, steps below have to be followed.

#### Step 1

Executing the extractor.py

![](Images/img_1.PNG)

Hit enter after entering the command above.

#### Step 2

Entering the text file name along with extension (.txt) which contains website links line by line.

![](Images/img_2.PNG)

Hit enter after entering the input file name.

#### Step 3

Enter the desired name for your Excel Sheet with extension (.xls).

![](Images/img_3.PNG)

Hit enter after entering the desired output file name for output.

## Result Time

After execution of the program you should see the output file in the same directory with the name demo.xls.

![](Images/img_5.PNG)

and the image below is the output of demo.xls, the final result.

![](Images/sketch-1552549620231.png)

## Built With

* [Python](https://www.python.org/downloads/) - For setting up the Python Environment on you local machine
* [beautifulsoup4==4.7.1](https://pypi.org/project/beautifulsoup4/) - BeautifulSoup Librariy is used for parsing the HTML file
* [lxml==4.3.2](https://pypi.org/project/lxml/) - Pythonic XML processing library
* [requests==2.21.0](https://pypi.org/project/requests/) - Allows you to send http/https requests
* [urllib3==1.24.1](https://pypi.org/project/urllib3/) - Used for parsing the URL
* [xlwt==1.3.0](https://pypi.org/project/xlwt/) - To generate Excel shpreadsheet file

## Disclaimer

Web scraping and crawling aren't illegal by themselves. After all, you could scrape or crawl your own website, without a hitch. - [Rami Essaid](https://resources.distilnetworks.com/all-blog-posts/is-web-scraping-illegal-depends-on-what-the-meaning-of-the-word-is-is)

## Developer

* [**Sampath Kumar Ajjapaga**](https://github.com/EncryptedSam) 
