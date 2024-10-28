<p align="center">
<a href="https://t.me/rktechnoindians"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>


# Bug Bounty


<p align="center"> 
<a href="https://t.me/rktechnoindians"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=𝐅𝐫𝐢𝐝𝐚-𝐓𝐨𝐨𝐥𝐬+𝐢𝐧+𝐓𝐞𝐫𝐦𝐮𝐱" /></a>
 </p>

<p align="center">
<a href="https://t.me/rktechnoindians"><img src="https://s10.gifyu.com/images/SrIwA.gif"></a>
</p>


Install
-------

**Bug Bounty**

    $ python3 -m pip install BugBounty

or

    $ git clone https://github.com/Technoindian/BugBounty
    $ cd BugBounty
    $ python3 -m pip install -r requirements.txt
    $ python3 setup.py install


Usage
-----

**Bug Bounty**

Scan only when using the website quota you want to scan

`--mode -f (File_Path)`

    $ BugBounty -f subdomain.txt

`--mode -c (cidr/ip-range)`

    BugBounty -c 127.0.0.1/24

`--mode -f & -c for -p (Port)`

    BugBounty -f subdomain.txt --p 443
    
    BugBounty -f subdomain.txt --p 80 443 53

`--mode http & https`

    BugBounty -f subdomain.txt -http
    
`--mode -m (Methods) (GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE)`

    BugBounty -f subdomain.txt -m GET

`--mode in -c & -f for -t (timeout) -T (Thareds) -o (Output)`

    BugBounty -f subdomain.txt -t 3
    BugBounty -f subdomain.txt -T 100
    BugBounty -f subdomain.txt -o /sdcard/other_result.txt
    
<!-- -->

    BugBounty -f subdomain.txt -p 80 443 -m GET -t 3 -T 100
    BugBounty -c 127.0.0.1/24 -p 80 443 -m GET -t 3 -T 100


**Bug Bounty (Other Features)**


`--mode -i (IP) (Host/Domain to IPV4 & IPV6 IP Convert)`

    BugBounty -i crazyegg.com
    
`--mode -tls (TLS Version/Cipher Connection Check )`

    BugBounty -tls crazyegg.com

`--mode -rr (RESPONSE) (Host/Domain/IP to Header Response)`

    BugBounty -rr crazyegg.com

`--mode -r (REVERSE) (Reverse IP LookUp)`

    BugBounty -r crazyegg.com

`--mode -op (OpenPort) (Host/Domain/IP to Open Port)`

    BugBounty -op crazyegg.com
    
    
Updating
--------

    python3 -m pip install --upgrade BugBounty


Note
----

## 🇮🇳 Welcome By Techno India 🇮🇳

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindians)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/RK_TECHNO_INDIA)
</p>
