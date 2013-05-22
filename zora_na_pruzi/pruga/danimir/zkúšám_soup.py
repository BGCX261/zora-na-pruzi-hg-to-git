#!/usr/bin/env python3
# Copyright (c) 2012 медвед медведович медведев <gazda@xtrip.net>

'''
Hen je program, který ...
'''

import sqlsoup
    
db = sqlsoup.SQLSoup('postgresql+pypostgresql://golf:marihuana@localhost:5432/zemjemjerka')

db.schema = "osm"

def main():
    '''
    zahájí běh programu
    '''
#    print(db.execute("SELECT 1"))
    for user in db.users.order_by(db.users.name).all():
        print(user)
#    users = db.users.all()
#    users.sort()
#    print(users)
    


if __name__ == '__main__':

    print(__doc__)

    main()



