## carrot

'carrot' is a my first attempt at a search engine. It's pretty bad but looks quite nice. The implementation is really chaotic because I just hacked it together in a day.


### screenshots

#### landing page
![homepage.png](images/landing.png)

#### The results page

![results.png](images/results.png)

### future

* at some point I'll use data structures to speed up search. The current method is linear.
* there's no NLP in use - queries like "how do I..." aren't interpreted by the engine.
* you can use regular expressions to search more precisely. Need to make this more robust to prevent ReDoS attacks.
* need to add a page ranking scheme, e.g. PageRank or lexical-distance based.
* sometimes, duplicate results are returned, fix this.
* need to implement pagination on results page.
