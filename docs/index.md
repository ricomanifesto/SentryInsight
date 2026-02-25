# Exploitation Report

Current threat activity reveals a concerning landscape of active vulnerabilities being exploited in the wild, with particular emphasis on zero-day exploits and critical infrastructure targets. Most notably, CISA has confirmed active exploitation of CVE-2026-25108 in FileZen file transfer software, while SolarWinds has urgently patched four critical vulnerabilities in its Serv-U platform that allow remote code execution with root privileges. The threat landscape is further complicated by the illegal sale of eight zero-day exploits from a U.S. defense contractor to Russian brokers, highlighting the sophisticated underground market for advanced exploits. Nation-state actors, particularly the North Korean Lazarus Group, continue leveraging ransomware operations while expanding their targeting scope to healthcare and Middle Eastern organizations.

## Active Exploitation Details

### FileZen Vulnerability
- **Description**: A vulnerability in FileZen file transfer software that is being actively exploited in the wild
- **Impact**: Attackers can compromise file transfer operations and potentially gain unauthorized access to sensitive data transfers
- **Status**: Currently under active exploitation with CISA confirmation
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Critical Vulnerabilities
- **Description**: Four critical security flaws in SolarWinds Serv-U 15.5 file transfer software allowing remote code execution
- **Impact**: Successful exploitation could result in remote code execution with root/administrative privileges on affected servers
- **Status**: Patches have been released by SolarWinds; immediate patching recommended
- **CVE ID**: Not specified in the articles

### GitHub Codespaces RoguePilot Vulnerability
- **Description**: A vulnerability in GitHub Codespaces that could be exploited through malicious Copilot instructions injected via GitHub issues
- **Impact**: Attackers could seize control of repositories by leaking GITHUB_TOKEN credentials through AI-assisted code generation
- **Status**: Vulnerability disclosed and likely patched by GitHub
- **CVE ID**: Not specified in the articles

### Zero-Day Exploits from Defense Contractor
- **Description**: Eight zero-day exploits stolen from L3Harris defense contractor and sold to Russian exploit brokers
- **Impact**: Unknown specific impacts as the nature of the zero-days was not disclosed, but involves critical defense industry vulnerabilities
- **Status**: Perpetrator sentenced to over seven years in prison; exploits likely distributed to hostile actors
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **FileZen File Transfer Software**: Actively exploited vulnerability affecting file transfer operations
- **SolarWinds Serv-U 15.5**: Four critical vulnerabilities allowing root code execution
- **GitHub Codespaces**: AI-assisted development environment vulnerable to token theft
- **L3Harris Defense Systems**: Unspecified systems with eight zero-day vulnerabilities sold to adversaries
- **Mental Health Android Apps**: 14.7 million installations affected by security vulnerabilities exposing medical data
- **ATM Systems**: Increased jackpotting attacks causing over $20 million in losses
- **Windows 11**: KB5077241 update addresses various security improvements including BitLocker enhancements

## Attack Vectors and Techniques

- **File Transfer Exploitation**: Attackers targeting file transfer software to intercept sensitive data transfers
- **Remote Code Execution**: Critical vulnerabilities allowing attackers to execute arbitrary code with elevated privileges
- **AI-Assisted Social Engineering**: Malicious instructions injected into AI coding assistants to leak authentication tokens
- **Zero-Day Marketplace**: Underground trading of advanced exploits between defense contractors and foreign adversaries
- **Ransomware Operations**: Sophisticated campaigns combining multiple malware families for maximum impact
- **Phishing Campaigns**: Targeted attacks against freight and logistics organizations using spoofed domains
- **ATM Jackpotting**: Physical and logical attacks on ATM systems to dispense cash fraudulently
- **Credential Theft**: Rapid network compromise techniques reducing average breach time to 29 minutes

## Threat Actor Activities

- **Lazarus Group (Diamond Sleet/Pompilus)**: North Korean state-backed group now deploying Medusa ransomware against Middle Eastern and U.S. healthcare targets, utilizing Comebacker backdoor, Blindingcan RAT, and Infohook stealer
- **Russian Exploit Brokers**: Sanctioned entities purchasing stolen zero-day exploits from compromised defense contractor employees for potential state-sponsored operations
- **UAC-0050**: Russia-aligned threat actor conducting social engineering attacks against European financial institutions using spoofed domains and RMS malware
- **ShinyHunters Extortion Gang**: Responsible for major data breaches including Wynn Resorts employee data, CarGurus 12.4 million account records, and Dutch telecommunications provider Odido
- **Diesel Vortex**: Financially motivated group targeting freight and logistics operators across the U.S. and Europe through credential theft campaigns
- **UnsolicitedBooker**: Threat cluster targeting Central Asian telecommunications companies in Kyrgyzstan and Tajikistan using LuciDoor and MarsSnake backdoors
- **1Campaign Cybercrime Service**: New platform helping threat actors run persistent malicious Google Ads campaigns while evading security detection