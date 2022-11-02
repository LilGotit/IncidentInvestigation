My program is available either as a Python file or a Jupyter Notebook, both named fireIncidents
The assets\fireIncidents.csv is necessary for operation, and the pandas and matplotlib modules
are required ("pip install pandas" and "pip install matplotlib" commands, respectively.)  

Beginning with an unaltered CSV file downloaded from louisville.gov, the data on fire incidents is
imported into a Pandas dataframe, and a visualization displays the amount of fire injuries per
incident over a dozen year period.

Incidents involving more than one fire injury are filtered out, and the dates are formatted and
concatenated into a Google Search, and the results are written to a text file.

Over the course of this journey with data, I had five requirements to meet with this project:
(1) Read data in, which I performed by downloading openly available government data, using pandas
(2) Manipulate and clean data, which I performed by converting my date column into datetime format
(3) Analyze data, which I performed with my custom function to concatenate Google searches
(4) Visualize data, which I performed with my visualizing function to generate two plots
(5) Interpret data and graphical output, which I performed in my markdown after generating results

I have designated meeting these requirements within the Markdown areas of the related sections.