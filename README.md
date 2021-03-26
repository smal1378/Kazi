# Kazi
##### Map of Kazi farm

This project is created just for fun, and some personal uses.
It also presents how do I code, and what can my team do. Just to get a job later.

Telegram: t.me/smal1378



#
##### Views Available:

    home_view (home.html):
        - maps: a list countaining five "Map" object, current page maps.
        - page: presenting current page number.
        - total_pages: presenting all pages count.
        - user: containg name of user or None.
    login_view (already_login.html):
        - user: username of currently logged in user
    login_view (login.html):
        - error: 0 means no error, if 1: invalid user or pass
    login_view (bad_request.html):
        no context passed to, this page is used to show bad request.

#
##### Models Available:

    Map:
        - name: string presenting name of Map.
        - user: "user" presenting creator of Map.
        - current_water: integer presenting current ongoing water.
        - time_created: time of creation.
        - notes: string presenting some info about Map.
        - s: integer presenting surface of Map, in hektars.