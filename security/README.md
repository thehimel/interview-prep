# Security

## What is 'defense in depth'?

- https://www.cloudflare.com/de-de/learning/security/glossary/what-is-defense-in-depth/
- Enforcing security in multiple layers. It is also referred as `layered security`.

## OWASP Top Ten

- https://owasp.org/www-project-top-ten/
- Group 1
  - Broken Authentication
  - Broken Access Control
  - Sensitive Data Exposure
- Group 2
  - Injection
  - Cross-Site Scripting (XSS)
  - XML External Entities (XXE)
- Group 3
  - Security Misconfiguration
  - Insecure Deserialization
  - Using Components with Known Vulnerabilities
  - Insufficient Logging & Monitoring

## CSRF vs. XSS

- https://security.stackexchange.com/questions/138987/difference-between-xss-and-csrf
- In a cross-site request forgery attack, the attacker tries to force/trick you into making a request which you did not
intend. This could be sending you a link that makes you involuntarily change your password. A malicious link could look
like that: `https://security.stackexchange.com/account?new_password=abc123`
- In a cross-site scripting attack, the attacker makes you involuntarily execute client-side code, most likely JS.
A typical reflected XSS attacking attempt could look like this:
`https://security.stackexchange.com/search?q="><script>alert(document.cookie)</script>`
- https://www.cloudflare.com/learning/security/threats/cross-site-scripting/

## How does Cross-Site Request Forgery Work?

- https://www.cloudflare.com/learning/security/threats/cross-site-request-forgery/

## What is cross-site scripting (XSS)?

- https://portswigger.net/web-security/cross-site-scripting
- Attacker inserts malicious code in the client side to perform evil activities i.e. steal session token.

## What are common web app security vulnerabilities? And how to overcome them?

- https://www.cloudflare.com/learning/security/what-is-web-application-security/

## What is an on-path attacker?

- https://www.cloudflare.com/learning/security/threats/on-path-attack/
- This is often referred to as a Man-in-the-middle (MITM) attack.
- On-path attackers place themselves between two devices (often a web browser and a web server) and intercept or modify
communications between the two. The attackers can then collect information as well as impersonate either of the two
agents. In addition to websites, these attacks can target email communications, DNS lookups, and public Wi-Fi networks.
Typical targets of on-path attackers include SaaS businesses, ecommerce businesses, and users of financial apps.
- You can think of an on-path attacker like a rogue postal worker who sits in a post office and intercepts letters
written between two people. This postal worker can read private messages and even edit the contents of those letters
before passing them along to their intended recipients.
- https://www.professormesser.com/security-plus/sy0-601/sy0-601-video/on-path-attacks/
- [On-Path Attacks - SY0-601 CompTIA Security+ : 1.4](https://www.youtube.com/watch?v=pY20_7l8AKc)

### What are ways to protect against on-path attackers?

- SSL/TLS, IPSec, VPN, etc.

## What is the global DNS hijacking threat?

- https://www.cloudflare.com/learning/security/global-dns-hijacking-threat/
- The attacker takes control of the DNS admin and redirects the traffic of the original site to a dummy site and
steals users' credentials when they log in to the fake site.
- Solution: DNS Providers should enforce 2FA.

## What is BGP hijacking?

- https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/
- Attacker tells that it has a shorter path to a set of IPs and the BGP router forwards the traffic through forged AS.

## What is a zero-day exploit?

- https://www.cloudflare.com/learning/security/threats/zero-day-exploit/
- Attacker exploits a known vulnerability. Organization has zero-day to resolve the issue once known.

## What is swatting?

- https://www.cloudflare.com/learning/security/glossary/what-is-swatting/
- Keeping some criminal footprint in victim's area presence, and then call the law enforcement authority.

## What is doxing?

- https://www.cloudflare.com/learning/security/glossary/what-is-swatting/
- Doxing (or doxxing) is the practice of researching someone’s personal information such as identity, address, and phone
number for the purpose of sharing that information publicly. The goal of doxing is to disrupt the victim’s privacy.

## What is a KRACK attack?

- https://www.cloudflare.com/learning/security/what-is-a-krack-attack/

## What is Meltdown/Spectre?

- https://www.cloudflare.com/learning/security/threats/meltdown-spectre/
- Vulnerabilities found in Intel, AMD, Apple, and ARM processor chips.
- Solution: Replacement of processor or OS Patch.

## What is a malicious payload?

- https://www.cloudflare.com/learning/security/glossary/malicious-payload/
- Attacker sends the victim a payload that once executed causes harm to the victim.


## What is a firewall?

- https://www.cloudflare.com/learning/security/what-is-a-firewall/
- A software between the internet and the trusted network.

## What is a next-generation firewall (NGFW)?

- https://www.cloudflare.com/learning/security/what-is-next-generation-firewall-ngfw/
- Enhanced, secured, and more powerful firewall.
- Uses Deep Packet Inspection (DPI).

## What are packet filtering and deep packet inspection (DPI)?

- https://www.cloudflare.com/learning/security/what-is-next-generation-firewall-ngfw/
- Packet filtering uses only the packet header for inspection, but DPI uses both header and body.

## What is HTTPS inspection?

- https://www.cloudflare.com/learning/security/what-is-https-inspection/
- Decrypting HTTPS traffic to block malicious activity by impersonating client and server like `MITM` attack.

## What is threat intelligence in cyber-security?

- https://www.cloudflare.com/learning/security/glossary/what-is-threat-intelligence/
- The practice of distributing the information about the potential attacks an organization may face and how to detect
and stop those attacks.

## What is threat modeling?

- https://www.csoonline.com/article/3537370/threat-modeling-explained-a-process-for-anticipating-cyber-attacks.html
- Threat modeling is a structured process through which IT pros can identify potential security threats and
vulnerabilities, quantify the seriousness, and prioritize techniques to mitigate attack and protect IT resources.

## Top 10 Most Common Types of Cyber-Attacks

- https://blog.netwrix.com/2018/05/15/top-10-most-common-types-of-cyber-attacks/

## What happens in a TLS handshake?

- https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/
