# unfinished warning error about valid


def is_valid_IP(string):
    if string.count('.') == 3 and string.replace('.', '').isdigit():
        slist = string.split('.')
        for i in range(len(slist)):
            if list(slist[i])[0] == '0' or list(slist[i]).pop() == '0':
                return False
            else:
                continue
        return True
    else:
        return False


"""
socket


def is_valid_IP(address):
    import socket
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True
"""

"""
import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))
"""


"""
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))
"""


"""
def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4
"""
