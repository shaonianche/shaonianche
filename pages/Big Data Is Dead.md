title:: Big Data Is Dead
author:: [[Jordan Tigani]]
full-title:: "Big Data Is Dead"
type:: [[Readwise]]
category:: [[articles]]
url:: https://motherduck.com/blog/big-data-is-dead/

- [[Readwise]] [[2023-02-09]]
	- Most people don’t have that much data ([View Highlight](https://read.readwise.io/read/01grtk938behqdtb9vfn4k99h1))
	- Customer data sizes followed a power-law distribution. The largest customer had double the storage of the next largest customer, the next largest customer had half of that, etc. So while there were customers with hundreds of petabytes of data, the sizes trailed off very quickly. There were many thousands of customers who paid less than $10 a month for storage, which is half a terabyte. Among customers who were using the service heavily, the median data storage size was much less than 100 GB. ([View Highlight](https://read.readwise.io/read/01grtk9jmbwsmz0y8a8g1sr1gg))
	- The general feedback we got talking to folks in the industry was that 100 GB was the right order of magnitude for a data warehouse. This is where we focused a lot of our efforts in benchmarking. ([View Highlight](https://read.readwise.io/read/01grtkae059sew8c67c9hyhjfn))
	- The storage bias in separation of storage and compute. ([View Highlight](https://read.readwise.io/read/01grtkbdp4s6mtxdas0yee82y7))
- New highlights added [[2023-02-09]] at 5:10 PM
	- Very often when a data warehousing customer moves from an environment where they didn’t have separation of storage and compute into one where they do have it, their storage usage grows tremendously, but their compute needs tend to not really change. ([View Highlight](https://read.readwise.io/read/01grtknqvm5yk2j05jz86dxkz5))
	- People look at the last hour, or the last day, or the last week’s worth of data. Smaller tables tend to be queried more frequently, giant tables more selectively. ([View Highlight](https://read.readwise.io/read/01grtksw9jpqbc3xywd5xx7zet))