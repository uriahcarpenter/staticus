Staticus
========

This is a sample app to show the usage of mailgun's mail storage API, here's how to set it up for your team.

In this example we use status-updates@mailgun.com for our status list, but you should pick something else like status-updates@mycompany.com

First set up a Mailgun mailing list (something like ``status-updates@mailgun.com`` ).

![](https://raw.github.com/mailgun/staticus/master/assets/make_mailing_list.png)

Then add a route when the matcher is ``match_recipient(status-update@mailgun.com)`` and the action is ``store()``

![](https://raw.github.com/mailgun/staticus/master/assets/make_store_route.png)

Then edit ``staticus.py`` and change the appropriate variables. Set ``API_KEY`` to the API key found in your control panel. ``MY_DOMAIN`` should be the domain of the status list. ``MY_STATUS_LIST`` should be the list you've just made.

From now on you should be able to run ``python staticus.py`` and pull down the most recent status emails from your team.



