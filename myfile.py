
import requests
from selectolax.parser import HTMLParser
import streamlit as st

# Create a Streamlit app
st.title("VLR.GG Events")

# Fetch the HTML data from the URL
url = "https://www.vlr.gg/events/asia-pacific"
html = requests.get(url).text
parser = HTMLParser(html)

# Find all the event items in the HTML code
event_items = parser.css("a.event-item")

# Loop through the event items and extract the data
events = []
for item in event_items:
    href = item.attributes.get('href')
    title = item.css_first("div.event-item-title").text(strip=True)
    status = item.css_first("span.event-item-desc-item-status").text(strip=True)
    prize = item.css_first("div.event-item-desc-item.mod-prize").text(strip=True)
    dates = item.css_first("div.event-item-desc-item.mod-dates").text(strip=True)

    # Get the event URL and extract the dates
    event_url = f"https://www.vlr.gg{href}"

    event = {
        "Title": title,
        "Status": status,
        "Prize": prize,
        "Dates": dates
    }
    events.append(event)

# Display the extracted data in a table
st.table(events)



# Your Python code to execute

# Read the content of an external Python file (e.g., myfile.py)
with open('myfile.py', 'r') as file:
    python_code = file.read()

# Create a Streamlit app
st.title("Display Python Code")

# Display the content of the file in a st.code block
st.code(python_code, language="python")