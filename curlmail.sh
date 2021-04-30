#!/bin/sh
curl --ssl-reqd \
--url 'smtps://smtp-relay.sendinblue.com:465' \
--user 'ksaw0011@stud.kea.dk:tHN6AwFK75qanR98' \
--mail-from 'ksaw0011@stud.kea.dk' \
--mail-rcpt 'igax0027@stud.kea.dk' \
--upload-file mail.txt
