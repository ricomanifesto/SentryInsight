# Exploitation Report

Critical exploitation activity is currently dominated by several actively exploited vulnerabilities across enterprise infrastructure and development platforms. The most significant threat involves CVE-2026-35616, a critical FortiClient Enterprise Management Server vulnerability being actively exploited in the wild, prompting Fortinet to release emergency patches. Additionally, CVE-2025-55182 (React2Shell) is being leveraged in large-scale automated credential theft campaigns targeting Next.js applications. North Korean threat actors continue sophisticated supply chain attacks, including the $285 million Drift cryptocurrency exchange compromise and social engineering campaigns targeting npm package maintainers. Multiple threat groups are also exploiting OAuth-based phishing techniques and deploying persistent implants through malicious npm packages.

## Active Exploitation Details

### FortiClient EMS Critical Vulnerability
- **Description**: Critical security flaw in Fortinet's FortiClient Enterprise Management Server that enables remote code execution
- **Impact**: Complete system compromise allowing attackers to gain administrative access to enterprise management infrastructure
- **Status**: Actively exploited in the wild; emergency patches released by Fortinet
- **CVE ID**: CVE-2026-35616

### React2Shell Vulnerability in Next.js Applications
- **Description**: Server-side request forgery vulnerability in Next.js applications that enables remote code execution
- **Impact**: Automated credential theft and system compromise through large-scale campaigns
- **Status**: Actively exploited in automated attacks targeting vulnerable Next.js applications
- **CVE ID**: CVE-2025-55182

### DarkSword iOS Vulnerability
- **Description**: Severe mobile operating system vulnerability affecting iOS devices
- **Impact**: Complete iOS device compromise enabling persistent access and data extraction
- **Status**: Patched by Apple in iOS 18 in an unprecedented move to address older iOS versions

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Critical vulnerability affecting enterprise management infrastructure
- **Next.js Applications**: Web applications vulnerable to React2Shell exploitation for credential theft
- **iOS Devices**: Mobile devices running older iOS versions affected by DarkSword exploit
- **npm Package Registry**: 36 malicious packages disguised as Strapi CMS plugins targeting Redis and PostgreSQL
- **Axios npm Package**: Popular HTTP client library compromised through social engineering
- **Drift Cryptocurrency Exchange**: Solana-based DEX platform compromised for $285 million theft

## Attack Vectors and Techniques

- **Social Engineering**: Sophisticated multi-month campaigns targeting software maintainers with fake Microsoft Teams error scenarios
- **Supply Chain Attacks**: Malicious npm packages and compromised legitimate packages for persistent implant deployment
- **OAuth Device Code Phishing**: Attacks surged 37x leveraging OAuth 2.0 Device Authorization Grant flow for account hijacking
- **Cookie-Controlled Web Shells**: PHP-based web shells using HTTP cookies as control channels on Linux servers
- **QR Code Phishing**: Traffic violation scams utilizing QR codes to redirect victims to credential harvesting sites
- **Durable Nonce Attacks**: Advanced cryptocurrency theft techniques targeting blockchain transaction mechanisms

## Threat Actor Activities

- **UNC1069 (North Korean)**: Orchestrated social engineering campaign against Axios npm package maintainer leading to supply chain compromise
- **DPRK-Linked Groups**: Conducted six-month social engineering operation culminating in $285 million Drift exchange theft
- **TA416 (China-Linked)**: Targeting European government and diplomatic organizations with PlugX malware and OAuth-based phishing since mid-2025
- **TeamPCP**: Supply chain attacks affecting European Commission and 30+ EU entities with expanding blast radius
- **Qilin Ransomware**: Claimed responsibility for Die Linke German political party attack with data theft threats
- **ShinyHunters and Lapsus$**: Taking credit for TeamPCP-related breaches amid hacker infighting and attribution confusion