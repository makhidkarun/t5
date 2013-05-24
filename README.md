T5
--

python libraries for parsing and working with traveller5

data, rules, etc

thinking out loud - aiming to make this libraries that can be used
by any python program for working with Traveller5.

t5/survey
 - reading ISS survey data
 - might want a variation of this to use/parse the extended format
   - i.e. second survey data (pg 431)
   - tab delim, json, yaml?
 - function to generate a random sector

t5/system
 - class to hold a mainworld
 - functions to generate a random mainworld
 - description and methods for use in other places (i.e. survey)
 - list/describe trade classifications
 - extend class to hold a system description
  - placing worlds, gas giants, etc
  - describing a full system as well

t5/trade
 - classes to describe tradegoods
 - functions to genearte random tradegoods per TC
 - functions to determine base cost, base price, and ranging in on actual value

webapp setup:

* virtualenv .venv --distribute
* source .venv/bin/activate
* pip install Flask gunicorn
