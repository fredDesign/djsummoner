djsummoner
==========

This is a site that contains a deck printing app for the game [Summoner Wars](http://www.plaidhatgames.com/games/summoner-wars)
by [Plaid Hat Games](http://www.plaidhatgames.com/). Cards are entered in the admin, then associated with a deck. Each deck can then
be printed by selecting it from a web page.

This project also serves to test the 'domain object' concept. That is, the models will be restricted to database logic, and views
will interact with an intermediary object that controls the non-database, application specific logic. This is intended to make 
logic more isolated, and make testing easier and faster, since (hypothetically) there are no database connections necessary in
the tests.
