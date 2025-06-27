# Exploitation Report

A surge in critical infrastructure-grade exploits is occurring across firmware, networking, and security platforms.  Most urgent is the ongoing weaponization of a maximum-severity flaw in AMI MegaRAC BMC firmware that allows unauthenticated attackers to seize or permanently brick servers.  CISA has confirmed in-the-wild use of this bug and simultaneously added two other actively exploited issues—one in D-Link DIR-859 routers and another in Fortinet FortiOS—to its Known Exploited Vulnerabilities (KEV) catalog.  Attackers are pairing these exploits with innovative tradecraft, such as abusing Microsoft 365 “Direct Send” to bypass mail filters and the dramatic 517 % rise in “ClickFix/FileFix” CAPTCHA-themed social-engineering lures.  Nation-state actors (Iran’s APT35/Charming Kitten), financially motivated groups (Scattered Spider), and hacktivists (Cyber Fattah) are all leveraging the new capabilities, underscoring an increasingly volatile threat landscape.

## Active Exploitation Details

### AMI MegaRAC BMC Firmware Vulnerability
- **Description**: A maximum-severity flaw in AMI’s MegaRAC Baseboard Management Controller firmware enables unauthenticated remote code execution over the management interface.
- **Impact**: Complete server takeover, deployment of malicious payloads, or permanent “bricking” of hardware through firmware corruption.
- **Status**: Confirmed active exploitation; CISA has added the bug to the KEV catalog.  Firmware patches have been issued to OEMs for downstream distribution.

### D-Link DIR-859 Router Remote Code Execution
- **Description**: A vulnerability in the DIR-859’s web management interface lets remote attackers execute arbitrary commands with root privileges.
- **Impact**: Full device compromise leading to traffic hijacking, botnet enrollment, or lateral movement into internal networks.
- **Status**: Actively exploited in the wild; listed in CISA KEV.  D-Link has released end-of-life mitigation guidance but no comprehensive firmware update.

### Fortinet FortiOS Authentication Bypass / Command Injection
- **Description**: A flaw in FortiOS allows remote, unauthenticated attackers to bypass authentication mechanisms and inject system commands.
- **Impact**: Administrative control of affected firewalls, VPN interception, and the deployment of malware inside protected networks.
- **Status**: Actively exploited according to CISA KEV.  Fortinet has published patched firmware versions and urges immediate upgrade.

### Brother / Fujifilm / Toshiba / Konica Minolta Printer Default-Password Exposure
- **Description**: 742 printer models share an algorithmically predictable default administrator password that can be derived remotely from the device’s serial number.
- **Impact**: Remote takeover of print devices, use as internal pivots, data exfiltration via print queues, or participation in DDoS botnets.
- **Status**: Publicly disclosed; exploitation observed in the wild on internet-exposed printers.  Vendors have issued advisories recommending password changes and firmware updates.

### Microsoft 365 “Direct Send” Abuse
- **Description**: Attackers exploit the built-in “Direct Send” SMTP relay feature to distribute phishing e-mails that appear to originate from legitimate internal users.
- **Impact**: Credential theft, MFA fatigue attacks, and initial foothold for business-e-mail-compromise operations.
- **Status**: Ongoing, large-scale campaign; Microsoft has provided mitigations such as connector restrictions and advanced hunting queries.

### ClickFix / FileFix Social-Engineering Method
- **Description**: A phishing technique that poses fake CAPTCHA or file-repair prompts (“ClickFix” and the newer “FileFix”) to manipulate users into granting access tokens or downloading malware.
- **Impact**: 517 % increase in successful initial access attempts, leading to ransomware deployment or data theft.
- **Status**: Active; no software patch—requires user-awareness training and advanced e-mail filtering.

## Affected Systems and Products

- **AMI MegaRAC BMC Firmware**: Multiple server OEMs using MegaRAC (data center and cloud platforms)  
- **D-Link DIR-859**: All hardware revisions, firmware ≤ latest EOL version  
- **Fortinet FortiOS**: Specific branches 7.x and 6.x (per Fortinet advisory)  
- **Brother, Fujifilm, Toshiba, Konica Minolta Printers**: 689 Brother + 53 multi-vendor models listed in vendor advisory  
- **Microsoft 365 Tenants**: Any tenant with SMTP “Direct Send” enabled via Exchange Online  
- **End-User Workstations & Browsers**: Victims of ClickFix/FileFix social-engineering lures (platform-agnostic)

## Attack Vectors and Techniques

- **Out-of-Band BMC Access**  
  - Vector: IPMI/Redfish ports exposed to management VLAN or internet  
  - Technique: Unauthenticated RCE against MegaRAC firmware

- **Router Web-UI Exploitation**  
  - Vector: HTTP/HTTPS management interface on DIR-859  
  - Technique: Command injection through crafted POST requests

- **Firewall Authentication Bypass**  
  - Vector: Exposed FortiGate SSL-VPN or admin ports  
  - Technique: Crafted requests skipping session validation and injecting shell commands

- **Predictable Default Credentials**  
  - Vector: Printer web configuration pages  
  - Technique: Deriving admin password from serial enumeration and logging in remotely

- **SMTP “Direct Send” Phishing**  
  - Vector: Exchange Online SMTP relay  
  - Technique: Spoofed internal sender without DKIM/DMARC checks

- **CAPTCHA-Themed Lures (ClickFix/FileFix)**  
  - Vector: HTML e-mails or compromised websites  
  - Technique: Fake CAPTCHA → OAuth token theft or malicious executable download

## Threat Actor Activities

- **Cyber Fattah (Hacktivist)**  
  - Campaign: Data-leak operation against Saudi Games, leveraging credential theft and doxing tactics amid regional tensions.

- **APT35 / Charming Kitten (Iran)**  
  - Campaign: AI-assisted spear-phishing targeting Israeli tech and cybersecurity experts; uses tailored lures and cloud-hosted malware.

- **Scattered Spider (UNC3944)**  
  - Campaign: Shift from retail to U.S. insurance sector; employs SIM-swapping, MFA bypass, and living-off-the-land post-exploitation.

- **IntelBroker (Arrested Actor)**  
  - Activities: Orchestrated high-profile breaches and data sales valued at ~$25 M; leveraged forum presence to distribute stolen data.

- **African Financial-Sector Intrusion Set**  
  - Campaign: Uses open-source offensive tools (Quasar, Sliver, Cobalt Strike) for persistent attacks on banks across Africa.

- **Unknown Printer Botnet Operators**  
  - Campaign: Mass scanning and compromise of printers with predictable default passwords for DDoS and spam relay.

**Bold NOTE**: Immediate patching and network-segmentation controls are recommended for all affected firmware and network devices, and defenders should refine e-mail security policies to counter the growing abuse of legitimate cloud features.