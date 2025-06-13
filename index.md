# Exploitation Report

Over the last week researchers observed a sharp rise in zero-click and authentication-bypass exploits that require no user interaction and provide attackers with immediate, high-value access. Two headline-grabbing flaws dominate: “EchoLeak,” a newly disclosed Microsoft 365 Copilot weakness that silently exfiltrates tenant data, and a still-unnamed iOS zero-click chain abused by Paragon’s Graphite spyware against European journalists. At the same time, enterprise software is being hammered — Trend Micro shipped out-of-band fixes for pre-authentication remote-code-execution bugs already weaponized in the wild, while GitLab hurried to close an account-takeover gap that researchers proved can be exploited to hijack CI/CD pipelines. Finally, continuing password-spray and malvertising campaigns show that threat actors are pairing these vulnerabilities with creative tradecraft to maximize impact across cloud, mobile, and on-prem environments.

## Active Exploitation Details

### EchoLeak Zero-Click Copilot Data Exfiltration
- **Description**: A zero-click prompt-injection flaw in Microsoft 365 Copilot that lets an attacker embed specially crafted HTML/JavaScript which forces Copilot to replay private chat or document content to a remote endpoint.
- **Impact**: Complete theft of sensitive tenant data (emails, Teams chats, SharePoint files) without end-user interaction; bypasses Microsoft’s content-moderation safeguards.
- **Status**: Publicly disclosed with proof-of-concept; Microsoft issued server-side mitigations but a definitive patch is still pending.

### Graphite Spyware iOS Zero-Click Exploit
- **Description**: An exploit chain delivered via iMessage that installs Paragon’s “Graphite” spyware on fully patched iPhones with no user action, leveraging undocumented iOS vulnerabilities to gain kernel-level access.
- **Impact**: Total compromise of device, including microphone, camera, keychain, and messaging data; persistence through reboots.
- **Status**: Actively used in the wild against journalists; Apple has released emergency security updates for supported iOS versions.

### Trend Micro Apex Central & Endpoint Encryption Pre-Auth RCE / Auth Bypass
- **Description**: Multiple web-console flaws allowing unauthenticated attackers to upload malicious files or bypass login checks, culminating in remote code execution under SYSTEM on Windows deployments or root on Linux appliances.
- **Impact**: Full takeover of security-management infrastructure, leading to lateral movement and tampering with endpoint-protection policies.
- **Status**: Exploits spotted in honeypots before the patch release; Trend Micro pushed critical updates and urges immediate installation.

### GitLab Account-Takeover & Pipeline Injection Flaws
- **Description**: Missing authentication checks on specific API endpoints permit attackers to reset passwords or inject jobs into CI/CD pipelines, effectively hijacking user accounts and artifact repositories.
- **Impact**: Source-code theft, supply-chain poisoning, and privilege escalation within self-hosted and GitLab-SaaS environments.
- **Status**: Fixed in GitLab 17.x, 16.11.x, and 16.10.x; exploitation observed in targeted attacks against DevOps teams.

### Windows Secure-Boot Bypass Used by Bootkit Malware
- **Description**: A vulnerability in Windows bootloader signature validation enables maliciously signed bootloaders to execute, allowing attackers to install stealth bootkits that survive OS reinstalls.
- **Impact**: Kernel-mode persistence, EDR evasion, and full system compromise.
- **Status**: Microsoft released an emergency Windows 11 24H2 update; active exploitation reported by incident-response teams investigating recent ransomware intrusions.

## Affected Systems and Products

- **Microsoft 365 Copilot**: All tenants using Copilot across Microsoft 365 services  
  **Platform**: Cloud (Microsoft SaaS)  
- **Apple iPhone / iPad**: iOS/iPadOS 15 – 17 prior to latest Rapid Security Response  
  **Platform**: Mobile (iOS)  
- **Trend Micro Apex Central**: On-prem versions 2019 HF6 and below, SaaS build prior to June 2025  
  **Platform**: Windows & Linux server appliances  
- **Trend Micro Endpoint Encryption PolicyServer**: Versions before 3.1.0 Build 2540  
  **Platform**: Windows Server  
- **GitLab Community & Enterprise Edition**: 17.0.0 and earlier, 16.11.3 and earlier, 16.10.6 and earlier  
  **Platform**: Linux (self-hosted) & GitLab-SaaS  
- **Microsoft Windows**: Windows 11 24H2 (all editions prior to KB5039703)  
  **Platform**: Desktop & Server (UEFI Secure Boot)  

## Attack Vectors and Techniques

- **Zero-Click Prompt Injection**  
  - **Vector**: Malicious HTML/JavaScript embedded in emails or documents triggers Copilot to send data to attacker-controlled domains.
- **iMessage Zero-Click Exploit Chain**  
  - **Vector**: Specially crafted multimedia messages exploiting memory-corruption in CoreGraphics and kernel privilege-escalation bugs.
- **Pre-Authentication RCE via File Upload**  
  - **Vector**: Direct HTTP POST to Trend Micro management console with a crafted archive that is automatically unpacked and executed.
- **Authentication Bypass API Abuse**  
  - **Vector**: Manipulation of GitLab password reset and project-import endpoints lacking token validation.
- **Secure-Boot Bypass Bootkit**  
  - **Vector**: Replacement of legitimate bootloader with a maliciously signed binary that passes signature checks.
- **Password-Spraying with TeamFiltration**  
  - **Vector**: Slow-rate authentication attempts against Microsoft Entra ID leveraging open-source tooling to evade lockout thresholds.
- **Malvertising via Fake CAPTCHA**  
  - **Vector**: Ad-network iframes masquerading as CAPTCHA challenges inject click-jacking and tracking scripts to distribute disinformation.

## Threat Actor Activities

- **Kremlin-Linked Disinformation Operators**  
  - **Campaign**: Use of fake CAPTCHA malvertising to bypass social-media moderation and disseminate propaganda across ad exchanges.
- **Paragon-Backed Operators (Graphite Spyware)**  
  - **Campaign**: Highly targeted surveillance of investigative journalists in Europe via iOS zero-click exploits.
- **Unidentified Cloud Threat Actors (EchoLeak)**  
  - **Campaign**: Early testing and small-scale data-harvesting against Microsoft 365 tenants, focusing on legal and financial firms.
- **Former Black Basta Affiliates**  
  - **Campaign**: Email-bombing and Microsoft Teams phishing for initial access, followed by ransomware deployment.
- **Fog Ransomware Group**  
  - **Campaign**: Leverages Syteca employee-monitoring software plus open-source tooling to move laterally and exfiltrate data before encryption.
- **TeamFiltration Operators**  
  - **Campaign**: Global password-spray attacks against 80,000+ Microsoft Entra ID accounts across 800 organizations, aiming for cloud account takeover.