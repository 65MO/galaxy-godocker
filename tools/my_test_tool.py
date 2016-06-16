
#!/usr/bin/env python
"""
Testing tool 
"""

import string
import sys

if __name__ == "__main__":
    name = None
    age = 0
    try:
        name = sys.argv[1]
        age = str(sys.argv[2])
        if int(age) >40:
           sys.stderr.write('sorry, too old!)
           sys.exit(10)
        msg = name + age
        sys.stdout.write(msg)
    except:
        sys.stderr.write(msg)
        sys.exit(100)
