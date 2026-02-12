# Exploitation Report

The cybersecurity landscape is currently experiencing significant exploitation activity, with Microsoft releasing patches for six actively exploited zero-day vulnerabilities in their February 2026 Patch Tuesday update. Concurrently, threat actors are leveraging sophisticated social engineering techniques, including AI-generated content and the ClickFix method, to deliver malware across multiple platforms. Notable campaigns include North Korean UNC1069 targeting cryptocurrency firms with cross-platform malware, supply chain attacks through compromised Outlook add-ins that have stolen over 4,000 Microsoft credentials, and the emergence of new botnets like SSHStalker exploiting legacy Linux kernel vulnerabilities.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerabilities
- **Description**: Six zero-day vulnerabilities across Microsoft's software ecosystem, including three security feature bypass flaws and multiple other critical vulnerabilities
- **Impact**: Attackers can bypass built-in security protections in Microsoft products and potentially achieve elevated privileges or system compromise
- **Status**: Actively exploited in the wild; patches released in February 2026 Patch Tuesday

### Windows 11 Notepad Remote Code Execution
- **Description**: A vulnerability in Windows 11 Notepad that allows remote code execution through specially crafted Markdown links
- **Impact**: Attackers can execute local or remote programs when users click malicious Markdown links
- **Status**: Fixed by Microsoft in recent updates

### Legacy Linux Kernel Exploits
- **Description**: Multiple legacy kernel vulnerabilities being exploited by the SSHStalker botnet to compromise Linux systems
- **Impact**: Complete system compromise allowing botnet enrollment and remote control via IRC communications
- **Status**: Actively exploited against unpatched legacy systems

## Affected Systems and Products

- **Microsoft Windows**: Windows 10 and Windows 11 systems affected by zero-day vulnerabilities and Notepad RCE flaw
- **Microsoft Outlook**: Email clients compromised through malicious add-ins distributed via Microsoft Store
- **Linux Systems**: Legacy kernel versions vulnerable to SSHStalker botnet exploitation
- **macOS Systems**: Targeted by North Korean UNC1069 campaigns with custom malware
- **Cryptocurrency Platforms**: Web3 companies and crypto firms targeted by sophisticated social engineering campaigns
- **SolarWinds Web Help Desk**: Internet-exposed instances targeted for exploitation
- **7-Zip Users**: Victims of fake distribution sites serving trojanized installers

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: Malicious campaigns using fake error messages to trick users into executing malware payloads
- **AI-Generated Content**: Use of deepfakes and AI-generated videos in social engineering campaigns targeting crypto sector
- **Supply Chain Attacks**: Compromise of legitimate software distribution channels and Microsoft Store add-ins
- **IRC Command and Control**: Old-school IRC protocol used by SSHStalker botnet for stealthy communications
- **Markdown Link Exploitation**: Specially crafted Markdown links used to trigger code execution in Windows Notepad
- **Legitimate Tool Abuse**: Employee monitoring software and remote support tools used for persistence and evasion
- **MFA Bypass Techniques**: ZeroDayRAT and similar tools capable of intercepting SMS codes and bypassing multi-factor authentication

## Threat Actor Activities

- **UNC1069 (North Korea)**: Conducting cross-platform campaigns against cryptocurrency organizations using AI-generated lures and custom macOS/Windows malware
- **APT36 and SideCopy**: Launching coordinated campaigns against Indian defense and government entities with cross-platform remote access trojans
- **Crazy Ransomware Gang**: Abusing legitimate employee monitoring tools and remote support software for persistence and network preparation
- **SSHStalker Operators**: Deploying Linux botnet using IRC communications and exploiting legacy kernel vulnerabilities
- **JokerOTP Sellers**: Cybercriminals offering MFA bypass tools for credential theft and account takeover attacks
- **Supply Chain Attackers**: Compromising legitimate software distribution channels including Microsoft Store add-ins and popular archive tools