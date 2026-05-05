# Stuff

Make an entry here with how to run the various code

## import_saepio_data.py

[manage data with DVC](https://dvc.org/doc/start/data-management)

```sh
dvc init
dvc add ./data
```
## BIG IDEAS

Q; Can we teach a machine to write parsers?
https://github.com/rapid7/recog/

Q; Is there a CPE or not?
The identifiers in the HTML data is in the headers. Can we automagically label the headers?

## Step 1: Data Pipeline

Do some parsing.

Dan to give Franklin an API key for a dedicated Saepio instance to pull a subset of data from a unique endpoint.
Dan to explain two type (sever tokens and HTML)
Could trigger an assessment.

1. Server Token Parsing

Group detection: operating system, application

Using `osint_services`

```sh
"Apache/2.4.6 mod_jk/1.2.46 OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16" 
```

operating system
application (apache for example])
version (2.4.6 for example)

```sh
"data": "HTTP/1.1 200 OK\r\nDate: Sat, 30 Apr 2022 23:12:06 GMT\r\nServer: Apache/2.4.6 (CentOS) mod_jk/1.2.46 OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16\r\nStrict-Transport-Security: max-age=60\r\nSet-Cookie: JSESSIONID=C5092D6316AED616CE131439E7FC83FD; Path=/; HttpOnly\r\nContent-Length: 15\r\nCache-Control: max-age=86400, public\r\nContent-Security-Policy: frame-ancestors 'self';\r\nX-Content-Type-Options: nosniff\r\nContent-Type: text/html;charset=ISO-8859-1\r\n\r\n", 
```

Stretch goal, CPE mamming: with a sever token as an input, create parsers that will match the software to CPE

2. Go crazy on HTML data.

key: http object -> html

* The data we need for this is the HTML headers.
* Dan to think about list of stuff to look for.
  * what JS libs are in use
  * are there API keys in the HTML
