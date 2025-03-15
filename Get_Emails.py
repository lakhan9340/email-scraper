{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "20ac9556-98f6-429d-b9bd-8d6279661c7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (1.30.0)\n",
      "Requirement already satisfied: selenium in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (4.26.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (7.0.1)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (2.1.4)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (4.9.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: urllib3<3,>=1.26 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from urllib3[socks]<3,>=1.26->selenium) (2.0.7)\n",
      "Requirement already satisfied: trio~=0.17 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from selenium) (0.26.0)\n",
      "Requirement already satisfied: trio-websocket~=0.9 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from selenium) (0.11.1)\n",
      "Requirement already satisfied: certifi>=2021.10.8 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from selenium) (2024.2.2)\n",
      "Requirement already satisfied: websocket-client~=1.8 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from selenium) (1.8.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.17.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: attrs>=23.2.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (23.2.0)\n",
      "Requirement already satisfied: sortedcontainers in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (2.4.0)\n",
      "Requirement already satisfied: outcome in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
      "Requirement already satisfied: sniffio>=1.3.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.3.0)\n",
      "Requirement already satisfied: cffi>=1.14 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.16.0)\n",
      "Requirement already satisfied: wsproto>=0.14 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
      "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.21)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: h11<1,>=0.9.0 in c:\\users\\mr.jadam\\anaconda3\\lib\\site-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b21007d1-9b98-473a-8937-5c790e1e3b3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-15 19:04:21.033 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\MR.Jadam\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "import streamlit as st\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "\n",
    "# Streamlit setup\n",
    "st.title(\"Email Scraper from Web Page\")\n",
    "st.write(\"This app scrapes email addresses from a webpage.\")\n",
    "\n",
    "# User input for the website URL\n",
    "url = st.text_input(\"Enter the URL to scrape\", \"https://www.intefai.com/\")\n",
    "\n",
    "# Selenium setup\n",
    "chrome_options = Options()\n",
    "chrome_options.add_argument(\"--headless\")  # Run Chrome in headless mode\n",
    "chrome_options.add_argument(\"--window-size=1920,1080\")\n",
    "chrome_driver_path = r\"D:\\IntefAI downloads\\Chrome Driver\\chromedriver-win64\\chromedriver.exe\"  # Update the path if necessary\n",
    "service = Service(chrome_driver_path)\n",
    "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
    "\n",
    "# Fetch the page source of the given URL\n",
    "driver.get(url)\n",
    "page_source = driver.page_source\n",
    "\n",
    "# Regular expression to extract emails\n",
    "EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])'''\n",
    "\n",
    "# Find all emails in the page source\n",
    "list_of_emails = [re_match.group() for re_match in re.finditer(EMAIL_REGEX, page_source)]\n",
    "\n",
    "# Display the emails in the Streamlit app\n",
    "if list_of_emails:\n",
    "    st.subheader(\"Found Emails:\")\n",
    "    for i, email in enumerate(list_of_emails):\n",
    "        st.write(f\"{i+1}. {email}\")\n",
    "else:\n",
    "    st.write(\"No emails found on the page.\")\n",
    "\n",
    "# Close the driver after scraping\n",
    "driver.quit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e41ec142-42e3-4dd7-934a-bf520837dbfc",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2376161928.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[3], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run your_script_name.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run your_script_name.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb1cab00-7058-4114-8fb7-02dcdb89b122",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
