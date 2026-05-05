# Exploitation Report

The current threat landscape reveals several critical vulnerabilities under active exploitation, with attackers targeting enterprise systems, government networks, and popular platforms. The most concerning activity involves the exploitation of a critical Weaver E-cology vulnerability (CVE-2026-22679) that has been actively exploited since March 2026, alongside a critical cPanel authentication bypass flaw being weaponized against government and MSP networks. Additional threats include supply chain attacks by North Korean groups, sophisticated phishing campaigns leveraging legitimate services, and the emergence of new malware variants targeting mobile and desktop platforms.

## Active Exploitation Details

### Weaver E-cology RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in Weaver (Fanwei) E-cology enterprise office automation platform exploiting a debug API endpoint
- **Impact**: Attackers can execute arbitrary commands and gain full system control, with exploitation being used to run discovery commands on compromised systems
- **Status**: Under active exploitation since mid-March 2026
- **CVE ID**: CVE-2026-22679

### Critical cPanel Authentication Bypass
- **Description**: Authentication bypass vulnerability in cPanel control panel software that allows unauthorized access without proper credentials
- **Impact**: Complete system compromise and control over web hosting environments, affecting millions of users
- **Status**: Multiple proof-of-concept exploits available with claims of zero-day activity for at least one month
- **CVE ID**: Not provided

### Copy Fail Linux Privilege Escalation
- **Description**: Privilege escalation vulnerability affecting Linux systems that allows local attackers to gain root access
- **Impact**: Complete system compromise and root-level access to affected Linux systems
- **Status**: Now being actively exploited in the wild according to CISA warning
- **CVE ID**: Not provided

### MOVEit Automation Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in Progress MOVEit Automation managed file transfer application
- **Impact**: Unauthorized access to sensitive file transfer systems and potential data exfiltration
- **Status**: Recently patched by Progress Software

## Affected Systems and Products

- **Weaver E-cology Platform**: Enterprise office automation and collaboration systems
- **cPanel Control Panels**: Web hosting management systems affecting millions of users
- **Linux Systems**: Various distributions vulnerable to Copy Fail privilege escalation
- **MOVEit Automation**: Enterprise managed file transfer applications
- **Android and Windows Systems**: Targeted by ScarCruft BirdCall malware campaign
- **Microsoft Phone Link**: Abused by CloudZ malware for SMS and OTP theft
- **PyTorch Lightning Package**: Backdoored version on Python Package Index
- **Government Networks**: Southeast Asian government and military entities
- **Managed Service Providers**: Hosting providers and MSP networks

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Compromise of video game platforms to distribute BirdCall malware across Android and Windows systems
- **Phishing Campaigns**: Large-scale credential theft targeting 35,000 users across 26 countries using code of conduct themes
- **RMM Tool Abuse**: Legitimate remote monitoring tools (SimpleHelp and ScreenConnect) used for persistent access in campaigns affecting 80+ organizations
- **Email Service Abuse**: Amazon SES and legitimate email services exploited to bypass security filters in phishing attacks
- **Package Repository Compromise**: Malicious PyTorch Lightning packages on PyPI delivering credential stealers
- **Debug API Exploitation**: Direct exploitation of debug endpoints in enterprise applications
- **Authentication Bypass**: Direct circumvention of authentication mechanisms in critical enterprise software

## Threat Actor Activities

- **ScarCruft (APT37)**: North Korean state-sponsored group conducting supply chain attacks through compromised gaming platforms to deploy BirdCall malware on Android and Windows systems
- **Silver Fox**: China-based cybercrime group deploying ABCDoor malware via tax-themed phishing campaigns targeting organizations in Russia and India with over 1,600 socially engineered messages
- **Karakurt Ransomware Group**: Russian extortion gang with recent arrest of cold case negotiator sentenced to 8.5 years in prison
- **ShinyHunters**: Extortion gang claiming responsibility for Instructure data breach
- **Unknown Southeast Asian Threat Actor**: Targeting government, military entities, and MSPs using weaponized cPanel vulnerability
- **Multi-vector Phishing Operators**: Coordinated campaigns using legitimate RMM tools affecting 80+ organizations since April 2025