# Exploitation Report

Microsoft has patched six actively exploited zero-day vulnerabilities as part of its February 2026 Patch Tuesday update, addressing 59 total security flaws across its software portfolio. Simultaneously, multiple sophisticated threat campaigns are actively targeting organizations through advanced malware operations, including North Korean-linked groups using AI-generated content to target cryptocurrency organizations, the emergence of new Linux botnets exploiting legacy kernel vulnerabilities, and surge in information stealer campaigns leveraging social engineering techniques. The threat landscape is further complicated by IoT botnet activities disrupting anonymity networks and cross-platform remote access trojan campaigns targeting critical infrastructure.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities actively exploited in the wild, with three identified as security feature bypass flaws
- **Impact**: Attackers can bypass built-in security protections across multiple Microsoft products, potentially leading to system compromise and privilege escalation
- **Status**: Patches released in February 2026 Patch Tuesday update covering 59 total vulnerabilities

### Legacy Linux Kernel Exploits
- **Description**: SSHStalker botnet leverages legacy Linux kernel vulnerabilities to compromise systems
- **Impact**: Remote code execution and system compromise leading to botnet enrollment
- **Status**: Ongoing exploitation targeting Linux systems with outdated kernels

### SolarWinds Web Help Desk Vulnerabilities
- **Description**: Public-facing SolarWinds WHD instances being actively targeted by attackers
- **Impact**: Unauthorized access to help desk systems and potential lateral movement
- **Status**: Organizations with exposed instances identified as prime targets

## Affected Systems and Products

- **Microsoft Windows**: Windows 10, Windows 11 versions affected by six zero-day vulnerabilities and 53 additional security flaws
- **Microsoft 365**: Admin center experiencing outages affecting business and enterprise subscriptions in North America
- **Linux Systems**: Legacy kernel versions targeted by SSHStalker botnet operations
- **SolarWinds Web Help Desk**: Public-facing instances at high risk of compromise
- **I2P Network**: Anonymity network disrupted by Kimwolf IoT botnet activities
- **Cryptocurrency Platforms**: Windows and macOS systems in cryptocurrency sector targeted by North Korean threat actors

## Attack Vectors and Techniques

- **Social Engineering with ClickFix**: LummaStealer campaigns using fake browser fixes to deliver CastleLoader malware
- **AI-Generated Content**: North Korean actors using AI-generated videos as lures in cryptocurrency targeting campaigns
- **IRC Command-and-Control**: SSHStalker botnet using Internet Relay Chat for C2 communications
- **Cross-Platform RAT Deployment**: APT36 and SideCopy deploying remote access trojans across Windows and Linux environments
- **Fake Software Distribution**: Malicious 7-Zip websites distributing trojanized installers with proxy tools
- **LinkedIn Impersonation**: DPRK operatives using compromised LinkedIn accounts to apply for remote IT positions
- **Legacy Protocol Exploitation**: Continued exploitation of Telnet traffic, particularly prevalent in Asian regions
- **MFA Bypass Techniques**: ZeroDayRAT implementing stalkerware capabilities to bypass multi-factor authentication

## Threat Actor Activities

- **APT36 and SideCopy**: Targeting Indian defense sector and government organizations with cross-platform RAT campaigns
- **UNC1069 (North Korea-linked)**: Sophisticated cryptocurrency sector targeting using AI lures and multi-platform malware
- **SSHStalker Operators**: Linux botnet campaign using IRC protocol for command-and-control operations
- **Kimwolf Botnet**: Large-scale IoT botnet disrupting I2P anonymity network infrastructure
- **DPRK IT Workers**: Using compromised LinkedIn profiles to infiltrate companies through fake job applications
- **LummaStealer Distributors**: Social engineering campaigns leveraging CastleLoader malware for information theft
- **ZeroDayRAT Operators**: Commercial spyware operations targeting individuals with stalkerware capabilities