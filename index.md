# Exploitation Report

During the past week, defenders observed a sharp uptick in real-world exploitation of network-edge infrastructure and widely-deployed business applications. The most critical activity centers on “CitrixBleed 2,” a new flaw in NetScaler ADC/Gateway appliances now under active attack that enables stealthy session hijacking and long-term persistence. Simultaneously, China-linked actors (“LapDogs”) are operating an established covert mesh of more than 1,000 hacked SOHO routers for espionage operations, and threat hunters note renewed mass scanning of Progress MOVEit Transfer servers, suggesting that last year’s file-transfer vulnerabilities remain a high-value target. These campaigns, combined with continuing abuse of compromised VPN apps and supply-chain-style attacks, underscore the ongoing pivot by both state-aligned and financially-motivated groups toward edge devices and trusted services that sit outside traditional endpoint visibility.

## Active Exploitation Details

### CitrixBleed 2
- **Description**: A critical information-disclosure flaw in NetScaler ADC and NetScaler Gateway that exposes session tokens and authentication data, permitting attackers to hijack valid VPN sessions without credentials. The issue is a logic error similar to, but more evasive than, the original CitrixBleed bug.  
- **Impact**: Full compromise of internal networks reachable through the appliance; enables prolonged, covert access because stolen tokens survive reboots and bypass MFA.  
- **Status**: Actively exploited in the wild; Citrix has issued fixed builds and urges immediate upgrade and token invalidation.  
- **CVE ID**: CVE-2025-5777  

### SOHO Router Exploits (LapDogs Campaign)
- **Description**: A China-linked espionage campaign that compromised over 1,000 small-office/home-office routers by chaining known firmware vulnerabilities and weak credentials to construct a stealth relay infrastructure.  
- **Impact**: Attackers gain root-level control of routers, create VPN tunnels, proxy C2 traffic, and stage intrusions against downstream targets while obscuring attribution.  
- **Status**: Infrastructure fully operational; devices remain backdoored, and no universal vendor patches are available for older end-of-life models.  

### MOVEit Transfer Vulnerability Cluster
- **Description**: Progress MOVEit Transfer file-sharing platform weaknesses previously leveraged in large-scale breaches are again being probed. GreyNoise reports a surge in automated scanning beginning 27 May 2025, indicating renewed exploitation efforts.  
- **Impact**: Successful exploitation provides unauthenticated remote code execution and access to sensitive files frequently containing payroll and HR data.  
- **Status**: Exploitation ongoing against unpatched instances; vendor patches exist and should be applied with post-patch forensics to detect backdoors.  

## Affected Systems and Products

- **NetScaler ADC & NetScaler Gateway**: All builds prior to Citrix’s fixed versions released in June 2025  
  - **Platform**: On-prem appliances and cloud images used for SSL VPN and load-balancing

- **SOHO Routers (multiple vendors/models)**  
  - **Platform**: Home and small-business broadband routers running outdated firmware (many end-of-life)

- **Progress MOVEit Transfer**: Self-hosted and cloud-hosted editions running vulnerable 2023/early-2024 code branches  
  - **Platform**: Windows Server IIS deployments frequently exposed directly to the internet

## Attack Vectors and Techniques

- **Session Token Harvesting (CitrixBleed 2)**  
  - **Vector**: Crafted HTTP requests leak session memory, allowing attackers to replay valid tokens and bypass MFA.

- **Router Takeover via Legacy Firmware**  
  - **Vector**: Combination of credential stuffing, default passwords, and exploitation of outdated web-management flaws to install drop-bear SSH servers and custom VPN daemons.

- **Automated SQL Injection / Deserialization (MOVEit)**  
  - **Vector**: Mass scanning for vulnerable endpoints, exploiting web API parameter flaws to upload web shells, then exfiltrating data over HTTPS.

## Threat Actor Activities

- **LapDogs (China-linked)**  
  - **Campaign**: Maintains a distributed proxy network of hijacked SOHO devices for long-term espionage and staging of intrusions against government and corporate targets worldwide.

- **Unattributed Actors Exploiting CitrixBleed 2**  
  - **Campaign**: Early telemetry shows financially-motivated ransomware affiliates harvesting session tokens to gain footholds in enterprise environments, often preceding data-theft extortion.

- **Multiple Threat Clusters Targeting MOVEit**  
  - **Campaign**: Renewed interest likely driven by past success (e.g., 2023 mass-breaches). Actors are weaponizing automated scanners and re-using prior exploit chains to compromise lagging organizations.

- **Scattered Spider** (contextual)  
  - **Campaign**: While not tied to a new CVE, the group continues cloud-credential theft and destructive “scorched-earth” tactics, highlighting the adversary focus on identity rather than endpoints.

- **Mustang Panda & Silver Fox (China)**  
  - **Campaigns**: Spear-phishing with PUBLOAD/Pubshell malware and fake-software sites delivering Sainbox RAT, respectively; rely on social engineering over n-day exploits.

- **Cyber Fattah (Hacktivist)**  
  - **Campaign**: Data-leak operations against Saudi targets amid regional tensions; illustrates increasing use of opportunistic breaches for ideological messaging.

---

Organizations should prioritize patching NetScaler appliances immediately, audit for suspicious VPN sessions, update or replace end-of-life SOHO hardware, and verify that MOVEit servers are fully current and free of web shells. Continued vigilance on edge devices and identity systems is essential as actors increasingly exploit weaknesses outside the traditional endpoint security perimeter.