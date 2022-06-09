# StackOverflowSuggestBot
This project aims to create an automatic tool that suggests solutions to python errors from Stack Overflow


Developing software free from any syntax and/or compilation errors is a crucial task. 
It is well-known in the software community that this is not always easy to accomplish considering how hard finding and solving errors can be. 
As a fact, most developers face errors while coding and search for solutions on the Internet. This process, of course, requires manual human-effort and delays the production time. 
Our motivation is to reduce this development effort by automating the process of finding and suggesting existing solutions for compilation and syntax errors; thus saving time. 
To do so, we used 298.000 Stackoverflow Python Question-Solution set to train a Doc2Vec model and created 200 manual test data to evaluate our model. 
Finally, our model provided good suggestions with 59\% rate with a 79\% similarity score. 


[Jira Page Link:](https://cs48000-team1.atlassian.net/jira/software/c/projects/CT/boards/1)
