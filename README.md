## <center> ***Cultural Health Moments*** 
<center>A Search Analysis During Times of Heightened Awareness To Identify Potential Interception Points With Digital Health Consumers.</center>
<br>
<center><img src="Assets/DigitalHealth.jpg" width=600/></center>

* ***Vision:*** Understanding how cultural health moments impact health consumers’ digital search behavior, and if this provides insight into potential interception points relating to disease-state awareness, education, symptoms, diagnosis, and/or treatment.
<br>
<br>
* ***Issue:*** During high-profile health moments (ex. – the cancer-related deaths of Chadwick Boseman and Eddie Van Halen, or the cancer diagnosis of Jimmy Carter or Rush Limbaugh) digital health consumers’ initial search queries are typically surface-level search (ex. – scandal, wealth, career highlights, spouse, etc.), but the search behavior shifts to awareness, signs, symptoms, and introspection over time. Understanding that time horizon when the shift occurs and what common topical trends exist  may provide opportunities to engage by leveraging naturally occurring awareness and search.
<br>
<br>
* ***Method:*** <br>

> 1. Examination of publicly available search data as related to high-profile disease state diagnosis and/or deaths. 

> 2. Develop an interactive Cultural Health Moment tool that allows the user to enter a High Profile Person (HPP) name, the Chronic Condition (CC), important dates (up to 2 dates) and they can visualize the search trend demand interest overtime, related quiries (and topics) and interest per region.

The Project is going to make use of the Google Search Trends via PyTrends (which is an unofficial Google Trends API). Google Trends => is a tool by Google that analyzes the popularity (demand, interest overtime) of top search queries in Google Search across various regions, subjects and languages. The website uses graphs to compare the search volume of different queries over time. PyTrends inturn is a Python library/module/API that Allows simple interface for automated downloading of reports from Google Trends. <br>
<br>
The data/reports from Google Trends is given as relative popularity and not the actual search volume. <br> <br>
From [Google Trends]("https://support.google.com/trends/answer/4365533?hl=en") =>
"*Google Trends normalizes search data to make (search demand) comparisons between terms easier. Search results are normalized to the time and location of a query by the following process:*"

> 1. Each data point is divided by the total searches of the geography and time range it represents to compare relative popularity. Otherwise, places with the most search volume would always be ranked highest.

> 2. The resulting numbers are then scaled on a range of 0 to 100 based on a topic’s proportion to all searches on all topics.

> 3. Different regions that show the same search interest for a term don't always have the same total search volumes.

* ***Potential Output:*** Identifying a window of heightened awareness and interest among digital health consumers and the general public caused by cultural health moments. The insight can be used within strategic campaign development for advocacy groups (for example, American Cancer Society), health insurance companies  (Aetna,Cigna, Blue Cross), and/or healthcare companies.