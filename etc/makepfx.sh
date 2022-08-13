#!/bin/sh
#
# Read cert.pem and ca.pem, and create signercert.pfx.
#


cat cert.pem ca.pem \
 | openssl pkcs12 -export \
     -inkey privkey.pem -password "pass:" -out signercert.pfx
chgrp www signercert.pfx
chmod 640 signercert.pfx


