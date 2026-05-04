# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms through various attack vectors. Most notably, CISA has added CVE-2026-31431, a Linux root access vulnerability, to its Known Exploited Vulnerabilities catalog due to active exploitation in the wild. Simultaneously, a critical cPanel flaw tracked as CVE-2026-41940 is being mass-exploited in "Sorry" ransomware campaigns, demonstrating the rapid weaponization of newly disclosed vulnerabilities. Additional threats include sophisticated supply chain attacks targeting CI/CD pipelines through poisoned Ruby Gems and Go modules, large-scale phishing operations leveraging Google AppSheet to compromise Facebook accounts, and automated OAuth abuse campaigns targeting Azure environments.

## Active Exploitation Details

### Linux Root Access Vulnerability
- **Description**: Recently disclosed security flaw affecting various Linux distributions that allows attackers to gain root-level access to compromised systems
- **Impact**: Complete system compromise with administrative privileges, enabling full control over affected Linux machines
- **Status**: Actively exploited in the wild; CISA has added to Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-31431

### Critical cPanel Security Flaw
- **Description**: Newly disclosed critical vulnerability in cPanel web hosting control panel software being exploited for ransomware deployment
- **Impact**: Website compromise and data encryption through "Sorry" ransomware attacks
- **Status**: Mass exploitation currently underway against vulnerable cPanel installations
- **CVE ID**: CVE-2026-41940

### Supply Chain Attacks on CI/CD Pipelines
- **Description**: Malicious packages distributed through Ruby Gems and Go module repositories targeting continuous integration environments
- **Impact**: Credential theft, GitHub Actions tampering, and compromise of software development infrastructure
- **Status**: Active campaign using sleeper packages to deploy subsequent malicious payloads

### Google AppSheet Phishing Relay
- **Description**: Vietnamese-linked operation using Google AppSheet as a phishing relay platform to distribute credential harvesting campaigns
- **Impact**: Compromise of over 30,000 Facebook accounts through sophisticated phishing infrastructure
- **Status**: Ongoing large-scale operation targeting social media credentials

## Affected Systems and Products

- **Linux Distributions**: Various distributions vulnerable to root access exploitation
- **cPanel Hosting Platforms**: Web hosting environments running vulnerable cPanel versions
- **Ruby Development Environments**: CI/CD pipelines using Ruby Gems package manager
- **Go Development Infrastructure**: Systems utilizing Go modules in build processes
- **Facebook Accounts**: Social media users targeted through AppSheet-based phishing
- **Azure Environments**: Microsoft cloud platforms targeted by automated OAuth abuse
- **Telegram Mini Apps**: Mobile applications distributed through Telegram's Mini App feature
- **SAP Development Packages**: npm packages for SAP's cloud application development ecosystem

## Attack Vectors and Techniques

- **Privilege Escalation**: Linux root access exploitation for system compromise
- **Web Application Exploitation**: cPanel vulnerability abuse for ransomware deployment
- **Supply Chain Poisoning**: Malicious package distribution through legitimate repositories
- **Phishing-as-a-Service**: Google AppSheet platform abuse for credential harvesting
- **OAuth Manipulation**: Automated consent abuse targeting Azure Single Sign-On systems
- **Vishing Operations**: Voice phishing combined with SSO abuse for rapid SaaS environment compromise
- **Mobile Malware Distribution**: Telegram Mini Apps used for Android malware deployment
- **Package Repository Compromise**: TeamPCP's "Mini Shai-Hulud" attacks targeting SAP ecosystems

## Threat Actor Activities

- **ShinyHunters**: Claimed responsibility for Instructure data breach affecting educational technology platform
- **Vietnamese Threat Actors**: Operating large-scale Facebook account compromise campaign through Google AppSheet
- **Sorry Ransomware Group**: Mass exploitation of cPanel vulnerabilities for data encryption attacks
- **TeamPCP**: Supply chain attacks targeting SAP development packages with compromised npm modules
- **China-Linked Espionage Groups**: Targeting Asian governments, NATO states, journalists, and activists
- **North Korean Actors**: Responsible for 76% of all cryptocurrency stolen in 2026 through historic heist operations
- **ConsentFix v3 Operators**: Automated OAuth abuse campaigns circulating on underground hacker forums
- **BlackCat Ransomware Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware attacks