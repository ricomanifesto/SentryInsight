# Exploitation Report

Critical security incidents dominate the current threat landscape, with CISA confirming active exploitation of FileZen CVE-2026-25108 and multiple critical vulnerabilities in SolarWinds Serv-U offering root access to servers. The North Korean Lazarus Group has escalated operations using Medusa ransomware to target U.S. healthcare organizations and Middle Eastern entities, while Russian-backed threat actors APT28 and UAC-0050 conduct sophisticated campaigns against European targets. Notable security concerns include a vulnerability in GitHub Codespaces that could leak authentication tokens, and the compromise of over 600 FortiGate devices by an amateur hacker using AI tools.

## Active Exploitation Details

### FileZen Vulnerability
- **Description**: A recently disclosed vulnerability in FileZen file sharing software that has been added to CISA's Known Exploited Vulnerabilities catalog
- **Impact**: Active exploitation confirmed by CISA with evidence of real-world attacks
- **Status**: Currently being exploited in the wild, patch status unknown from provided information
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Remote Code Execution Flaws
- **Description**: Four critical remote code execution vulnerabilities in SolarWinds Serv-U file transfer software
- **Impact**: Attackers can gain root access to unpatched servers, allowing complete system compromise
- **Status**: Patches available from SolarWinds, but unpatched systems remain vulnerable

### GitHub Codespaces RoguePilot Flaw
- **Description**: A vulnerability in GitHub Codespaces that allows malicious actors to inject Copilot instructions through GitHub issues to seize repository control
- **Impact**: Attackers could leak GITHUB_TOKEN credentials and gain unauthorized access to repositories
- **Status**: Vulnerability disclosed, exploitation potential through AI manipulation

### FortiGate Device Compromise
- **Description**: Mass compromise of over 600 FortiGate firewall devices by an amateur hacker using generative AI tools
- **Impact**: Credential theft and backup access, potentially enabling follow-on ransomware attacks
- **Status**: Active compromise affecting 600+ devices, targeting Russian-speaking regions

## Affected Systems and Products

- **FileZen**: File sharing software currently under active exploitation
- **SolarWinds Serv-U**: File transfer servers vulnerable to remote code execution
- **GitHub Codespaces**: Development environment susceptible to AI-based token leakage
- **FortiGate Firewalls**: 600+ devices compromised for credential and backup theft
- **Android Mental Health Apps**: 14.7 million installations containing security vulnerabilities exposing medical data
- **Classic Microsoft Outlook**: Desktop client experiencing mouse pointer visibility issues

## Attack Vectors and Techniques

- **Social Engineering**: UAC-0050 using spoofed domains and social engineering against European financial institutions
- **Webhook-Based Macro Malware**: APT28 deploying macro-based malware with webhook communication
- **Voice Phishing (Vishing)**: Optimizely breach through voice-based social engineering attacks
- **AI-Enhanced Exploitation**: Amateur hackers leveraging generative AI to compromise enterprise firewalls
- **Ransomware Deployment**: Lazarus Group using Medusa ransomware in healthcare and Middle Eastern targets
- **Malicious Google Ads**: 1Campaign platform helping threat actors evade detection in advertising networks
- **Phishing Campaigns**: Diesel Vortex targeting freight and logistics organizations across 52 domains

## Threat Actor Activities

- **Lazarus Group**: North Korean state-backed group deploying Medusa ransomware against U.S. healthcare organizations and Middle Eastern entities, utilizing Comebacker backdoor, Blindingcan RAT, and Infohook information stealer
- **APT28**: Russian state-sponsored actor targeting Western and Central European entities with webhook-based macro malware campaigns
- **UAC-0050**: Russia-aligned threat actor conducting social engineering attacks against European financial institutions using spoofed domains and RMS malware
- **UnsolicitedBooker**: Threat cluster targeting telecommunications companies in Kyrgyzstan and Tajikistan with LuciDoor and MarsSnake backdoors
- **ShinyHunters**: Extortion gang claiming breaches of Wynn Resorts, CarGurus (12.4 million accounts), and Odido telecommunications provider
- **Diesel Vortex**: Financially motivated group conducting credential theft campaigns against freight and logistics operators in the U.S. and Europe
- **MuddyWater**: Iranian threat group deploying new malware strains against organizations in the Middle East and Africa
- **Anonymous Fenix**: Spanish hacktivist group arrested for DDoS attacks against government ministries and public institutions