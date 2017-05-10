#!/usr/bin/python

import sys
import os
import time
import re
import hashlib

start1 = time.time()
for i in range(1, 1000):
  #hash_object = hashlib.sha256()
  #with open("22c1430f2646bbd5.crt") as f:
  #  hash_object.update(f.read())

  #with open("22c1430f2646bbd5.crt", "rb") as f:
  #  for chunk in iter(lambda: f.read(4096), b""):
  #    hash_object.update(chunk)
  #print hash_object.hexdigest()
  sha256 = os.popen('openssl x509 -noout -in 22c1430f2646bbd5.crt -fingerprint -sha256 | sed \'s/://g\' | tr \'[:upper:]\' \'[:lower:]\'').read()
  m = re.search('sha256 fingerprint=(.+)', sha256)
  if m:
    sha256 = m.group(1)
  #sha256_emercoin = 'c6cec35009004e981b44124983873cf88003a705ded5691f57a8915c99aa6414'
  sha256_emercoin = os.popen('openssl verify 22c1430f2646bbd5.crt').read()		
  #sha256_emercoin = os.popen('../emercoin-0.5.0/bin/emercoin-cli name_show ssl:22c1430f2646bbd5').read()
  n = re.search('sha256=(.+)",', sha256_emercoin)
  if n:
    sha256_emercoin = n.group(1)

  if(sha256 == sha256_emercoin):
    print 'Verified'
  else:
    print 'Not Verified'

end1 = time.time()


start2 = time.time()
for i in range(1, 1000):
  sha256 = os.popen('openssl x509 -noout -in 86d6fcd1792c91c6.crt -fingerprint -sha256 | sed \'s/://g\' | tr \'[:upper:]\' \'[:lower:]\'').read()
  m = re.search('sha256 fingerprint=(.+)', sha256)
  if m:
    sha256 = m.group(1)

  sha256_emercoin = os.popen('openssl verify 22c1430f2646bbd5.crt').read()
  #sha256_emercoin = os.popen('../emercoin-0.5.0/bin/emercoin-cli name_show ssl:86d6fcd1792c91c6').read()
  n = re.search('sha256=(.+)",', sha256_emercoin)
  if n:
    sha256_emercoin = n.group(1)

  if(sha256 == sha256_emercoin):
    print 'Verified'
  else:
    print 'Not Verified'


end2 = time.time()


start3 = time.time()
for i in range(1, 1000):
  #os.system('openssl verify -CAfile cert.pem www.google.com.crt')
  os.system('openssl verify -CApath /etc/ssl/certs -CAfile Google\ Internet\ Authority\ G2 www.google.com')
end3 = time.time()



print 'Emercoin Certificate verification - Exists:', (end1 - start1)
print 'Emercoin Certificate verification - Does not exist:',(end2 - start2)
print 'CA Certificate verification:', (end3 - start3)
