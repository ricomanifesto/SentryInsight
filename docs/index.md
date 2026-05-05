# Exploitation Report

Critical vulnerability exploitation activity is currently dominated by the active exploitation of CVE-2026-22679 in Weaver E-cology enterprise office automation platforms, which has been under attack since March 2026. Additionally, threat actors are weaponizing a critical cPanel authentication bypass vulnerability to target government and managed service provider networks. The threat landscape also includes sophisticated supply chain attacks by North Korean APT groups, widespread phishing campaigns abusing legitimate services, and the emergence of new malware variants targeting both Android and Windows platforms.

## Active Exploitation Details

### Weaver E-cology Remote Code Execution Vulnerability
- **Description**: A critical security vulnerability in Weaver (Fanwei) E-cology enterprise office automation and collaboration platform that allows remote code execution via the debug API
- **Impact**: Attackers can execute arbitrary commands on affected systems, potentially gaining full control of enterprise environments
- **Status**: Actively exploited in the wild since mid-March 2026, with hackers running discovery commands on compromised systems
- **CVE ID**: CVE-2026-22679

### cPanel Authentication Bypass Vulnerability
- **Description**: A critical authentication bypass flaw in cPanel web hosting control panels that allows attackers to bypass authentication mechanisms
- **Impact**: Complete compromise of web hosting environments, affecting potentially millions of websites and hosting accounts
- **Status**: Multiple proof-of-concept exploits have appeared after disclosure, with claims of zero-day activity for at least one month prior to public disclosure

### Copy Fail Linux Privilege Escalation Vulnerability
- **Description**: A Linux security vulnerability that enables local privilege escalation to root access
- **Impact**: Allows attackers to gain complete administrative control over Linux systems
- **Status**: Now being exploited in the wild according to CISA warnings, with proof-of-concept exploits publicly available

### MOVEit Automation Authentication Bypass
- **Description**: A critical authentication bypass vulnerability in Progress Software's MOVEit Automation enterprise managed file transfer application
- **Impact**: Potential unauthorized access to sensitive file transfer systems and data
- **Status**: Recently patched by Progress Software, but represents high-value target for attackers

## Affected Systems and Products

- **Weaver E-cology**: Enterprise office automation and collaboration platforms, particularly affecting organizations using the debug API functionality
- **cPanel**: Web hosting control panel software affecting millions of hosting accounts and websites globally
- **Linux Systems**: Various Linux distributions vulnerable to the "Copy Fail" privilege escalation flaw
- **MOVEit Automation**: Enterprise-grade managed file transfer applications from Progress Software
- **Android Devices**: Targeted by BirdCall malware through compromised gaming platforms
- **Microsoft Phone Link**: Abused by CloudZ malware to intercept SMS messages and one-time passwords
- **PyTorch Lightning**: Machine learning framework package on PyPI compromised with credential-stealing payload

## Attack Vectors and Techniques

- **Supply Chain Attacks**: North Korean APT group ScarCruft compromising video game platforms to distribute BirdCall malware to Android and Windows users
- **Debug API Exploitation**: Direct exploitation of Weaver E-cology debug interfaces to execute remote commands
- **Phishing via Legitimate Services**: Large-scale campaigns abusing Amazon SES to deliver convincing phishing emails that bypass security filters
- **RMM Tool Abuse**: Attackers using SimpleHelp and ScreenConnect remote monitoring tools to maintain persistent access after initial compromise
- **Package Repository Poisoning**: Malicious PyTorch Lightning packages on PyPI designed to steal credentials from development environments
- **Social Engineering**: Tax-themed phishing campaigns targeting organizations in India and Russia using code of conduct lures

## Threat Actor Activities

- **ScarCruft (APT37)**: North Korean state-sponsored group conducting supply chain attacks through gaming platforms, deploying BirdCall backdoor on both Android and Windows systems
- **Silver Fox**: China-based cybercrime group launching tax-themed phishing campaigns targeting over 1,600 organizations in Russia and India, deploying ABCDoor malware, ValleyRAT, and other backdoors
- **Karakurt Ransomware Group**: Russian extortion gang with recent conviction of a Latvian "cold case" negotiator sentenced to 8.5 years in prison
- **ShinyHunters**: Extortion gang claiming responsibility for data breach at educational technology company Instructure
- **Unknown Government Targeting Group**: Previously unknown threat actor specifically targeting government and military entities in Southeast Asia, along with managed service providers using the critical cPanel vulnerability
- **Multi-Vector Phishing Operators**: Coordinated campaign targeting over 80 organizations using legitimate RMM tools for persistent access, active since April 2025