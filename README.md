# StackOverflowSuggestBot
This project aims to create an automatic tool that suggests solutions to python errors from Stack Overflow

- Project Description:

Developing software free from any syntax and/or compilation errors is a crucial task. 
It is well-known in the software community that this is not always easy to accomplish considering how hard finding and solving errors can be. 
As a fact, most developers face errors while coding and search for solutions on the Internet. This process, of course, requires manual human-effort and delays the production time. 
Our motivation is to reduce this development effort by automating the process of finding and suggesting existing solutions for compilation and syntax errors; thus saving time. 
To do so, we used 298.000 Stackoverflow Python Question-Solution set to train a Doc2Vec model and created 200 manual test data to evaluate our model. 
Finally, our model provided good suggestions with a 59\% rate with a 79\% similarity score. 

Our Jira page link can be found [here](https://cs48000-team1.atlassian.net/jira/software/c/projects/CT/boards/1)\
Final report can be found [here](https://github.com/gokturkYandim98/StackOverflowSuggestBot/blob/main/CS48000_Final_Report.pdf)

- How to Install, Repeat, Replicate, or Reproduce the Results Presented: 

Download the codes from GitHub and open them with Google Colab or Visual Studio. The model will ask and wait for you to ask your question about Python. After taking the input, model will show you another question which is similar to yours and generate Stack Overflow links as explanations to answer your question. If you click on links, you will be directed to Stack Overflow site and will be able to see answers. After this question is done, you can ask another question and repeat this process as much as you need. An example usage is down below:

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Enter your question about python: Google-trans-new throws an error previously working code in Python.

This question sounds similar to yours: python google trans new throwing error code wo...

Links and explanations to answers to this question:

1. https://stackoverflow.com/a/68270197

It seems to be an error from the package google-trans-new that is known and already corriged. (Check this discussion for more information).
A new version of the module with the bugfix hasn’t been released to pip yet. So you have to manually do the modification or wait for the newt version to be released.

2. https://stackoverflow.com/a/69302211

from bs4 import BeautifulSoup

from bs4.formatter import HTMLFormatter

from googletrans import Translator

import requests

translator = Translator()

class UnsortedAttributes(HTMLFormatter):

def attributes(self, tag):

for k, v in tag.attrs.items():

yield k, v

Check this 2 alternatives for Python transtator code:

https://neculaifantanaru.com/en/python-code-text-google-translate-website-translation-beautifulsoup-library.html

or here:

https://neculaifantanaru.com/en/example-google-translate-api-key-python-code-beautifulsoup.html

-----------------------------------------------------------------------------------------------------------------------------------------------------------

or the output can be "We couldn't find any matches"  as our model can not find matches from time to time. But these kinds of outputs (regarding finding a match and not) would indicate that code is working and can be useful for you.
 









