# Exploitation Report

Recent investigations reveal a sharp uptick in sophisticated, real-world exploitation of zero-day and recently disclosed vulnerabilities. The most critical activity involves Paragon’s Graphite spyware weaponizing an undisclosed Apple iOS zero-click flaw against European journalists, and the Stealth Falcon APT actively abusing a Windows WebDAV remote-code-execution (RCE) zero-day to deliver malware to government and defense targets in the Middle East and North Africa. In parallel, bootkit operators continue to leverage a Secure Boot bypass to persist at the firmware layer, while large-scale password-spraying and brute-force campaigns hammer Microsoft Entra ID and Apache Tomcat instances. These attacks illustrate well-resourced adversaries combining zero-day exploitation, living-off-the-land tools, and credential-based intrusion techniques to gain covert access across mobile, cloud, and on-prem environments.

## Active Exploitation Details

### iOS Zero-Click Vulnerability Leveraged by Graphite Spyware
- **Description**: A previously unknown flaw in Apple iOS enables remote code execution on targeted devices without user interaction (zero-click). Paragon’s Graphite platform delivers the exploit via malicious iMessage payloads, silently installing full-featured surveillance tooling.  
- **Impact**: Complete device compromise, microphone and camera activation, file exfiltration, real-time tracking, and encrypted communications interception.  
- **Status**: Confirmed in-the-wild exploitation against at least two European journalists. Apple has issued mitigations in recent iOS security updates.

### Windows WebDAV Remote Code Execution Zero-Day
- **Description**: A flaw in Microsoft’s Web-Distributed Authoring and Versioning (WebDAV) service allows remote attackers to craft malicious requests that execute arbitrary code in the context of the Windows Client/Server Runtime, bypassing standard user privileges.  
- **Impact**: Initial access and malware deployment on fully patched Windows 10/11 and Server systems; facilitates follow-on credential theft and lateral movement.  
- **Status**: Actively exploited since March 2025 by the Stealth Falcon APT; Microsoft has not yet issued a comprehensive patch, workarounds focus on disabling WebClient service and blocking outbound WebDAV traffic.

### UEFI Secure Boot Bypass Exploited by Bootkit Malware
- **Description**: A vulnerability in Windows’ Secure Boot implementation permits threat actors to load a maliciously signed bootloader during system start-up, subverting early-boot protections.  
- **Impact**: Persistent, kernel-level control resistant to OS reinstallation; enables deployment of advanced bootkits (e.g., BlackLotus variants) that disable security products and decrypt BitLocker volumes.  
- **Status**: In-the-wild exploitation continues; Microsoft released an out-of-band patch and updated revocation lists, but full remediation requires firmware and OS updates plus policy enforcement.

## Affected Systems and Products

- **Apple iPhone/iPad (iOS 16/17 prior to latest Rapid Security Response)**  
  - **Platform**: iOS mobile devices targeted via iMessage.

- **Microsoft Windows 10/11 & Windows Server (WebDAV enabled)**  
  - **Platform**: Desktop and server systems; all architectures with WebClient service active.

- **Windows PCs with Secure Boot enabled but not yet updated with latest revocation list**  
  - **Platform**: Consumer and enterprise Windows devices, including Windows 11 24H2.

- **Microsoft Entra ID (formerly Azure AD) tenant accounts**  
  - **Platform**: Cloud identity platform affected by password-spraying attacks.

- **Apache Tomcat 9.x/10.x with exposed Manager interface**  
  - **Platform**: On-prem and cloud-hosted Java application servers.

- **GitLab Community & Enterprise Editions < 17.x (pre-patch)**  
  - **Platform**: Self-hosted DevSecOps platforms vulnerable to newly patched auth bypass flaws.

## Attack Vectors and Techniques

- **Zero-Click iMessage Exploit Chain**  
  - **Vector**: Malformed iMessage attachment triggers memory corruption, downloading Graphite payloads with no user interaction.

- **Malicious WebDAV Request RCE**  
  - **Vector**: Weaponized .url or .lnk files force the OS to reach out to attacker-controlled WebDAV share, leading to arbitrary code execution.

- **Secure Boot Bootloader Substitution**  
  - **Vector**: Adversaries load a rogue, signed bootloader during startup, establishing boot-level persistence before the OS trust chain initializes.

- **Password-Spraying with TeamFiltration**  
  - **Vector**: High-volume authentication attempts against Microsoft Entra ID using common and default passwords, throttling evasion via distributed IP pools.

- **Tomcat Manager Brute-Force**  
  - **Vector**: Automated credential stuffing against `/manager/html` endpoints from hundreds of rotating IP addresses.

- **LLM Guardrail Evasion – TokenBreak**  
  - **Vector**: Single-character perturbations bypass large-language-model moderation filters to produce disallowed content.

- **Smartwatch “SmartAttack” Ultrasonic Exfiltration**  
  - **Vector**: Air-gapped PCs modulate data into ultrasonic signals decoded by nearby wearable devices.

## Threat Actor Activities

- **Stealth Falcon (APT)**  
  - **Campaign**: WebDAV zero-day exploitation since March 2025 targeting defense and government entities in Turkey, Qatar, Egypt, and Jordan; drops bespoke backdoors and credential harvesters.

- **Unattributed Operator Using Paragon Graphite**  
  - **Campaign**: Surveillance operation against European investigative journalists, leveraging iOS zero-click chain for prolonged monitoring.

- **Bootkit Operators / BlackLotus Lineage**  
  - **Campaign**: Ongoing deployment of Secure Boot-bypass malware for espionage and credential theft across unpatched Windows fleets.

- **Unknown Cluster (TeamFiltration Abuse)**  
  - **Campaign**: Global Microsoft Entra ID credential-based attacks against 80,000+ accounts across hundreds of organizations; objective appears to be cloud account takeover.

- **Fog Ransomware Group**  
  - **Campaign**: Uses Syteca employee-monitoring software, PsExec, and open-source tools for encryption operations; no novel CVE exploitation observed but highlights living-off-the-land methodology.

- **Former Black Basta Affiliates**  
  - **Campaign**: 2025 intrusions leveraging Microsoft Teams phishing and custom Python scripts for foothold and lateral movement in North-American manufacturing firms.

- **Distributed Tomcat Brute-Force Botnet**  
  - **Campaign**: Mass scanning and credential stuffing aimed at deploying webshells for crypto-mining and lateral movement.

---

**Note**: Organizations should apply vendor patches immediately, disable unused services (e.g., WebDAV), enforce multi-factor authentication across cloud identities, and monitor for anomalous bootloader modifications and unsolicited iMessage traffic to mitigate current exploitation waves.