<p align="center">
<a href="https://t.me/rktechnoindians"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>


# Bug Bounty


<p align="center"> 
<a href="https://t.me/rktechnoindians"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=BugBounty" /></a>
 </p>


Install
-------

**Bug Bounty**

    python3 -m pip install BugBounty

Usage
-----

**Bug Bounty**


**Mode -f (File_Path)**

`For One File Only`

    BugBounty -f subdomain.txt
    
`More Then File`

    BugBounty -f subdomain.txt subdomain2.txt subdomain3.txt

**Mode -c (cidr/ip-range)**

`For One CIDR Only`

    BugBounty -c 127.0.0.1/24
    
`More Then CIDR`

    BugBounty -c 127.0.0.1/24 128.0.0.0/24 104.18.25.0/30

**Mode -f & -c for -p (Port)**

`For One Port Only`

    BugBounty -f subdomain.txt --p 443
    
`More Then Port`
    
    BugBounty -f subdomain.txt --p 80 443 53

**Mode http & https**

    BugBounty -f subdomain.txt -http
    
**Mode -m (Methods) (GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE)**

    BugBounty -f subdomain.txt -m GET

**Mode in -c & -f for -t (timeout) -T (Thareds) -o (Output)**

`-t (timeout)`

    BugBounty -f subdomain.txt -t 3
    
`-T (Thareds)`
    
    BugBounty -f subdomain.txt -T 100
    
`-o (Output)`
    
    BugBounty -f subdomain.txt -o /sdcard/other_result.txt
    
`File Scan`

    BugBounty -f subdomain.txt -p 80 443 -m GET -t 3 -T 100
    
`Cidr/IP-Range Scan`
    
    BugBounty -c 127.0.0.1/24 -p 80 443 -m GET -t 3 -T 100

**-m2, (mode2) ➸ Another Scanning Method ( Target Reachable Server )**

`File Scan`

    BugBounty -f subdomain.txt -m2
    
`Cidr/IP-Range Scan`
    
    BugBounty -c 127.0.0.1/24 -m2


Bug Bounty (Other Features)


**Mode -i (IP) (Host/Domain to IPV4 & IPV6 IP Convert)**

    BugBounty -i crazyegg.com
    
**Mode -tls (TLS Version/Cipher Connection Check )**

    BugBounty -tls crazyegg.com

**Mode -rr (RESPONSE) (Host/Domain/IP to Header Response)**

    BugBounty -rr crazyegg.com

**Mode -r (REVERSE) (Reverse IP LookUp)**

    BugBounty -r crazyegg.com

**Mode -op (OpenPort) (Host/Domain/IP to Open Port)**

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
