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

## What are common web app security vulnerabilities? And how to overcome them?

- https://www.cloudflare.com/learning/security/what-is-web-application-security/

