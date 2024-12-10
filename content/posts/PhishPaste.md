---
title: PhishPaste
date: 2024-12-04
draft: false
tags:
  - gophish
categories: Reference
---

Phishpaste is a tool used to copy landing pages, sending profiles, and email templates between users in gophish
1. set $DATABASE_URL `export DATABASE_URL='<<gophishdbuser>>:<<gophishdbpwd>>@(<<IPADDRESS>>:3306)/gophish?charset=utf8&parseTime=True&loc=UTC'`
2. change to the gophish directory `cd /root/gophish/`
3. List gophish users `go run phishpaste.go --list-users`
4. Copy data `go run phishpaste.go --source <<sourceuser>> --destination <<destinationuser>> --email-templates --landing-pages --sending-profiles`

![Image Description](/images/PhishPaste-20241210134632470.webp)