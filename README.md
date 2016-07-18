[![Build Status](https://travis-ci.org/sansaralab/shiva.svg?branch=master)](https://travis-ci.org/sansaralab/shiva)  [![Coverage Status](https://coveralls.io/repos/github/sansaralab/shiva/badge.svg?branch=master)](https://coveralls.io/github/sansaralab/shiva?branch=master)  [![Code Climate](https://codeclimate.com/github/sansaralab/shiva/badges/gpa.svg)](https://codeclimate.com/github/sansaralab/shiva) [![Documentation Status](https://readthedocs.org/projects/sansaralab-shiva/badge/?version=latest)](http://sansaralab-shiva.readthedocs.io/en/latest/?badge=latest)  [![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](http://www.apache.org/licenses/LICENSE-2.0.html)

# Shiva
Tool for tracking users, firing hooks (send request or run js on front) based on user's actions.
It is possible to define very flexible triggers. Also it is possible to attach any identifying information to user like email.

It's like triggered emails, but for everything and with superpower!

Group for discussions - [https://groups.google.com/forum/#!forum/sansara-lab-shiva](https://groups.google.com/forum/#!forum/sansara-lab-shiva)

## Cases:
- Fire external endpoint when users with emails ends with "@megamailhost.net" do not appear on the site more than a week.
- Execute custom js code every time when users with phone number that starts with "+1" click anywhere on the site.
- Do something only for users come from Twitter.
- Сongratulate all users who have birthday today via alert or something else.
