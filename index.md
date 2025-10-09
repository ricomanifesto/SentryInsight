# Exploitation Report

The current threat landscape reveals significant active exploitation across multiple attack vectors, with particular emphasis on widespread botnet operations, WordPress vulnerabilities, and sophisticated malware campaigns. The RondoDox botnet stands out as a major threat, actively targeting 56 different vulnerabilities across more than 30 distinct device types worldwide. Critical WordPress vulnerabilities are being actively exploited, including authentication bypass flaws in the Service Finder theme. Meanwhile, advanced persistent threat actors continue to evolve their tactics, with China-aligned groups deploying sophisticated malware like GOVERSHELL and weaponizing legitimate tools such as the Nezha monitoring platform.

## Active Exploitation Details

### RondoDox Botnet Multi-Vulnerability Campaign
- **Description**: A large-scale botnet operation actively exploiting 56 different n-day vulnerabilities across more than 30 distinct device types, including vulnerabilities first disclosed during Pwn2Own competitions
- **Impact**: Enables attackers to compromise a wide variety of networked devices and systems for botnet recruitment
- **Status**: Currently active with ongoing worldwide attacks targeting multiple vulnerability classes

### WordPress Service Finder Theme Authentication Bypass
- **Description**: Critical security flaw in the Service Finder WordPress theme that allows authentication bypass to gain unauthorized access to any account
- **Impact**: Complete compromise of WordPress sites including administrator account takeover
- **Status**: Actively being exploited by threat actors

### WordPress Sites JavaScript Injection Campaign
- **Description**: Malicious JavaScript injections targeting WordPress sites to redirect users to malicious destinations as part of next-generation ClickFix phishing attacks
- **Impact**: Site visitors redirected to phishing sites and potentially malicious payloads
- **Status**: Active campaign compromising WordPress installations

### Figma MCP Server Remote Code Execution
- **Description**: Vulnerability in the Framelink Figma MCP Server that enables agentic AI compromise leading to remote code execution
- **Impact**: Remote code execution on affected systems with agentic AI integrations
- **Status**: Patch available, organizations urged to update immediately
- **CVE ID**: CVE-2025-53967

## Affected Systems and Products

- **WordPress Sites**: Service Finder theme and general WordPress installations targeted for authentication bypass and JavaScript injection
- **Multiple Device Types**: Over 30 distinct device categories targeted by RondoDox botnet including various IoT and network devices
- **Figma MCP Servers**: Third-party Framelink integration vulnerable to RCE attacks
- **Android Devices**: Russian users targeted by ClayRat spyware through fake WhatsApp and TikTok applications
- **SonicWall Cloud Services**: All cloud backup customers affected by firewall configuration theft
- **AWS Cloud Instances**: Targeted by Crimson Collective for data theft operations

## Attack Vectors and Techniques

- **Botnet Recruitment**: Mass exploitation of 56 different vulnerabilities across diverse device types for botnet expansion
- **Social Engineering**: ClayRat distribution through fake popular applications and Telegram channels
- **Cache Smuggling**: FileFix attack variant uses cache smuggling to bypass security software detection
- **Spear Phishing**: UTA0388 campaigns targeting multiple regions with Go-based implants
- **Cloud Infrastructure Compromise**: Direct targeting of AWS environments for data exfiltration
- **Authentication Bypass**: Direct exploitation of WordPress theme vulnerabilities
- **JavaScript Injection**: Malicious code injection into compromised WordPress sites

## Threat Actor Activities

- **RondoDox Operators**: Conducting worldwide attacks targeting 56 vulnerabilities across 30+ device types in large-scale botnet operations
- **UTA0388 (China-aligned)**: Operating spear-phishing campaigns across North America, Asia, and Europe delivering GOVERSHELL and HealthKick malware variants
- **ClayRat Campaign**: Targeting Russian Android users through sophisticated fake application distribution networks
- **Crimson Collective**: Actively compromising AWS cloud instances for data theft and extortion, recently targeting Red Hat Consulting GitLab instance
- **Chinese APT Groups**: Weaponizing legitimate Nezha monitoring tool to deliver Gh0st RAT malware in new attack waves
- **WordPress Attackers**: Multiple groups exploiting WordPress vulnerabilities for authentication bypass and malicious JavaScript injection
- **Ransomware Cartel**: LockBit, Qilin, and DragonForce forming collaborative partnership to share attack information and resources
- **TwoNet Hacktivists**: Pro-Russian group pivoting from DDoS attacks to critical infrastructure targeting