My project began with an ambitious thought: Fires injuring more than one person would have
an exponentially increased likelihood of online documentation. This thesis was tested by
parsing an unaltered government data file involving fire responses from data.louisville.gov, 
isolating incidents with multiple injuries, and concatenating a Google search to seek an
accompanying news report.

The resulting program is available either as a Python file or a Jupyter Notebook, both named
fireIncidents. The assets/fireIncidents.csv file is necessary for operation, and the pandas and 
matplotlib modules are required ("pip install pandas" and "pip install matplotlib" commands,
respectively).  

Beginning with an unaltered CSV file downloaded from louisville.gov (assets/fireIncidents.csv),
the data on fire incidents is imported into a Pandas dataframe, and a visualization displays the
amount of fire injuries per incident over a dozen year period.

Incidents involving more than one fire injury are filtered out, the dates are formatted for
visualization and re-formatted into a string to concatenate into a Google Search, and the results are
written to a CSV file (googleSearches.csv) in an Excel-friendly hyperlink format.

Over the course of this journey with data, I had five requirements to meet with this project:
(1) Read data in, which I performed by downloading openly available government data, using pandas
(2) Manipulate and clean data, which I performed by converting my date column into datetime format
(3) Analyze data, which I performed with my custom function to concatenate Google searches
(4) Visualize data, which I performed with my visualizing function to generate two plots
(5) Interpret data and graphical output, which I performed in my markdown after generating results

I have designated meeting these requirements within the Markdown areas of the related sections.

While I overestimated my efficiency, and my program ultimately underperformed, I'm quite pleased
with how much I learned through failure. I have used Git, iterated through CSV files, created
graphs with data, crafted custom functions, and made my mistakes into teachable moments for myself.
