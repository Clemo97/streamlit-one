import requests
from selectolax.parser import HTMLParser
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Create a Streamlit app
st.title("VLR.GG Events")

# List of regions to scrape
regions = ["north-america", "europe", "brazil", "korea", "japan", "latin-america", "oceania", "mena"]

# Initialize a dictionary to store events for each region
events_regions = {}

# Loop through the regions and scrape events
for region in regions:
    # Fetch the HTML data from the URL
    url = f"https://www.vlr.gg/events/{region}"
    html = requests.get(url).text
    parser = HTMLParser(html)

    # Find all the event items in the HTML code
    event_items = parser.css("a.event-item")

    # Initialize a list to store events for the current region
    events = []

    # Loop through the event items and extract the data
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

    # Store the events for the current region in the dictionary
    events_regions[region] = events

# Create a vertical bar graph to show the total number of events for each region
region_names = [region.capitalize() for region in regions]
event_counts = [len(events) for events in events_regions.values()]

# Create a figure and axis for the bar graph
fig, ax = plt.subplots()
ax.bar(region_names, event_counts)
ax.set_xlabel("Region")
ax.set_ylabel("Total Number of Events")
ax.set_title("Total Events by Region")
plt.xticks(rotation=45)

# Create a pie chart based on the event counts
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(event_counts, labels=region_names, autopct='%1.1f%%', startangle=140)
ax_pie.set_title("Distribution of Events by Region")

# Display the bar graph and the pie chart using st.pyplot()
st.pyplot(fig)
st.pyplot(fig_pie)

# Display the extracted data for each region
for region, events in events_regions.items():
    st.subheader(f"{region.capitalize()} Events")
    st.table(events)


import requests
from selectolax.parser import HTMLParser
import streamlit as st
import pandas as pd
import plost

# Create a Streamlit app
st.title("VLR.GG Events")

# List of regions to scrape
regions = ["north-america", "europe", "brazil", "korea", "japan", "latin-america", "oceania", "mena"]

# Initialize a dictionary to store event counts for each region
event_counts = {}

# Loop through the regions and scrape events
for region in regions:
    # Fetch the HTML data from the URL
    url = f"https://www.vlr.gg/events/{region}"
    html = requests.get(url).text
    parser = HTMLParser(html)

    # Find all the event items in the HTML code
    event_items = parser.css("a.event-item")

    # Count the number of events for the current region
    event_counts[region] = len(event_items)

# Create a DataFrame from event counts
df = pd.DataFrame({'Region': list(event_counts.keys()), 'Event Count': list(event_counts.values())})

# Display the bar chart showing the total number of events for each region
st.bar_chart(df.set_index('Region'))

# Display the pie chart using plost.pie_chart
plost.pie_chart(data=df, theta='Event Count', color='Region', title="Event Distribution by Region")


# Read the content of an external Python file (e.g., myfile.py)
with open('myfile.py', 'r') as file:
    python_code = file.read()

# Create a Streamlit app
st.title("Python Code")

# Display the content of the file in a st.code block
st.code(python_code, language="python")