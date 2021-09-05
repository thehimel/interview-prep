# Security

## What is 'defense in depth'?

- https://www.cloudflare.com/de-de/learning/security/glossary/what-is-defense-in-depth/

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

