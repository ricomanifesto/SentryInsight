# Exploitation Report

Critical exploitation activity continues to escalate with CISA confirming active exploitation of FileZen CVE-2026-25108, marking it as a significant threat requiring immediate attention. Additionally, SolarWinds has disclosed four critical vulnerabilities in its Serv-U file transfer software that allow remote code execution with root privileges. The cybersecurity landscape is further complicated by the arrest of a former defense contractor employee who sold eight zero-day exploits to Russian brokers, highlighting insider threats to national security. Meanwhile, the North Korean Lazarus Group has expanded its operations by deploying Medusa ransomware against healthcare organizations and Middle Eastern entities, demonstrating sophisticated nation-state actors' continued evolution in their attack methodologies.

## Active Exploitation Details

### FileZen File Transfer Vulnerability
- **Description**: A security flaw in FileZen file transfer software that has been actively exploited in the wild
- **Impact**: Allows attackers to compromise file transfer operations and potentially gain unauthorized access to systems
- **Status**: Currently being exploited; added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Remote Code Execution Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software enabling remote code execution
- **Impact**: Successful exploitation could result in remote code execution with root privileges, allowing complete system compromise
- **Status**: Recently patched by SolarWinds; patches available

### Defense Contractor Zero-Day Exploits
- **Description**: Eight zero-day vulnerabilities sold by a former L3Harris employee to Russian exploit brokers
- **Impact**: Unknown specific impacts as vulnerability details remain classified for national security reasons
- **Status**: Employee arrested and sentenced; exploits potentially in adversary hands

### GitHub Codespaces RoguePilot Vulnerability
- **Description**: A flaw in GitHub Codespaces that could be exploited to inject malicious Copilot instructions through GitHub issues
- **Impact**: Attackers could seize control of repositories by leaking GITHUB_TOKEN credentials
- **Status**: Vulnerability disclosed; remediation status unclear

## Affected Systems and Products

- **SolarWinds Serv-U 15.5**: File transfer software with four critical remote code execution vulnerabilities
- **FileZen**: File transfer software actively being exploited in the wild
- **GitHub Codespaces**: Development environment vulnerable to malicious Copilot instruction injection
- **L3Harris Defense Systems**: Unspecified systems affected by stolen zero-day exploits
- **Android Mental Health Apps**: 14.7 million installations containing security flaws exposing medical information
- **Central Asian Telecommunications**: Companies in Kyrgyzstan and Tajikistan targeted by UnsolicitedBooker
- **European Financial Institutions**: Targeted by UAC-0050 with spoofed domains and RMS malware
- **U.S. Healthcare Organizations**: Targeted by Lazarus Group using Medusa ransomware

## Attack Vectors and Techniques

- **Social Engineering**: UAC-0050 uses spoofed domains to target European financial institutions
- **Ransomware Deployment**: Lazarus Group employing Medusa ransomware against healthcare and Middle Eastern targets
- **Backdoor Installation**: UnsolicitedBooker deploying LuciDoor and MarsSnake backdoors in telecom networks
- **Phishing Campaigns**: Diesel Vortex targeting freight and logistics organizations across 52 domains
- **Malicious Google Ads**: 1Campaign platform helping threat actors evade detection in advertising networks
- **AI Model Extraction**: Chinese firms using 16 million queries to illegally copy Anthropic's Claude model
- **ATM Jackpotting**: Physical attacks on ATMs causing over $20 million in losses during 2025
- **DDoS Attacks**: Spanish hacktivist groups targeting government ministries and political parties

## Threat Actor Activities

- **Lazarus Group (Diamond Sleet/Pompilus)**: North Korean state-backed group deploying Medusa ransomware against U.S. healthcare and Middle Eastern entities, utilizing Comebacker backdoor, Blindingcan RAT, and Infohook stealer
- **UnsolicitedBooker**: Targeting Central Asian telecommunications companies with LuciDoor and MarsSnake backdoors, expanding from previous Saudi Arabian focus
- **UAC-0050**: Russia-aligned threat actor conducting social engineering attacks against European financial institutions using spoofed domains and RMS malware
- **Diesel Vortex**: Financially motivated group stealing credentials from freight and logistics operators using 52 domains in phishing attacks
- **ShinyHunters**: Extortion gang claiming responsibility for multiple data breaches including Wynn Resorts, CarGurus (12.4 million accounts), and Dutch telecom provider Odido
- **MuddyWater**: Iranian threat group deploying fresh malware strains against organizations in the Middle East and Africa amid rising geopolitical tensions
- **Anonymous Fenix**: Spanish hacktivist group arrested for DDoS attacks against government websites and political institutions
- **Russian Exploit Brokers**: Purchasing zero-day exploits from defense contractor insiders for potential state-sponsored operations