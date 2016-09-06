char_list = 'abcdefghijklmnopqrstuvwxyz'
db_loc = './somefolder/crypted.db'
max_chars = 6



from pysqlcipher import dbapi2 as sqlite
import sys

complete_list = []
for current in xrange(max_chars):
    a = [i for i in char_list]
    for y in xrange(current):
        a = [x+i for i in char_list for x in a]
    complete_list = complete_list+a

conn = sqlite.connect(db_loc)
c = conn.cursor()

counter = 0

for st in complete_list:
    counter += 1
    if counter%50 == 0:
        print counter

    c.execute("PRAGMA key='" + st + "'")
    try:
        c.execute('''create table test (test text)''')
        print "key is '" + st + "'"
        sys.exit()
    except:
        pass