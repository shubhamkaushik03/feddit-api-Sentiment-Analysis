#Introduction
The process of building a RESTful API using Flask for fetching comments from different sources, performing sentiment analysis on them, and providing the results to users. The API allows users to specify the source of comments (local sample data or an external API), apply time range filters, and sort the results by sentiment polarity.

###prerequisite

**install the dependency using **
  -  _pip install requirement.txt_

**Run the application**
  - python src/app.py

Note: As you given the docker-compose.yml when I run the container so using that I am not able to get the data so I am using sample data to cover the below points and also adding one function accept the apiurl on which bases perform below operation.

  1. identifies if comments on a given subfeddit or category are positive or negative
  2. list of the most recent comments
  3. The unique identifier of the comment
  4. The text of the comment
  5. The polarity score and the classification of the comment (positive, or negative) based on that score.
  6. Filter comments by a specific time range
  7. Sort the results by the comments polarity score

####ENDPOINTS
http://localhost:5000/api/v1/comments?subfeddit=gaming

**To filter by time range:**
http://localhost:5000/api/v1/comments?subfeddit=gaming&time_range=2024-05-15T12:00:00Z,2024-05-15T13:00:00Z

**To sort by polarity score:**
http://localhost:5000/api/v1/comments?subfeddit=gaming&sort_by_polarity=true

**using api endpoint like reddit which running locallly**
http://localhost:5000/api/v1/comments?data_source_api=http://localhost:8080/api/v1/version

![image](https://github.com/shubhamkaushik03/feddit-api-Sentiment-Analysis/assets/93450340/5fc7ca73-9087-4a2d-8b42-8b438ad4ae4a)











