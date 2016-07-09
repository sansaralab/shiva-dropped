[![Build Status](https://travis-ci.org/sansaralab/shiva.svg?branch=master)](https://travis-ci.org/sansaralab/shiva)

# Shiva
Tool for tracking users, firing hooks (send request or run js on front) based on user's actions.
It is possible to define very flexible triggers. Also it is possible to attach any identifying information to user like email.


## Cases:
- Fire external endpoint when users with emails ends with "@megamailhost.net" do not appear on the site more than a week.
- Execute custom js code every time when users with phone number that starts with "+1" click anywhere on the site.
- Do something only for users come from Twitter.
