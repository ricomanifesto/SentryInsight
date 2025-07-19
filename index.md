# Exploitation Report

The most significant exploitation activity observed this cycle is the active weaponization of a zero-day in CrushFTP (CVE-2025-54309) that grants remote administrative access through the product’s web interface. Simultaneously, fresh zero-days in Ivanti Connect Secure/Policy Secure are being abused to deploy MDifyLoader and in-memory Cobalt Strike beacons against enterprise VPN gateways. Supply-chain compromises remain rampant: two extremely popular npm linter packages and multiple Arch Linux AUR packages were hijacked to deliver steganographically-packed malware (including CHAOS RAT). Nation-state operators continue to innovate, with APT28’s newly-attributed “Authentic Antics” malware harvesting Microsoft 365 credentials and the “PoisonSeed” actor bypassing FIDO-based MFA with QR-code phishing. These campaigns collectively underscore the critical need for immediate patching, package integrity monitoring, and robust phishing defenses.

## Active Exploitation Details

### CrushFTP Web Interface Administrative Bypass
- **Description**: A zero-day flaw that lets unauthenticated attackers gain administrative rights via the CrushFTP web interface.  
- **Impact**: Full takeover of the file-transfer server, exfiltration or tampering with stored files, and lateral movement inside corporate networks.  
- **Status**: Exploited in the wild; emergency patches and work-arounds released by the vendor.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Days
- **Description**: Multiple previously unknown vulnerabilities in Ivanti’s VPN and NAC appliances leveraged to plant MDifyLoader, which in turn launches in-memory Cobalt Strike payloads.  
- **Impact**: Stealthy remote code execution on perimeter devices, credential theft, and foothold for long-term espionage.  
- **Status**: Confirmed active exploitation; Ivanti has issued patches and mitigations.  

### npm “eslint-config-prettier” & “eslint-plugin-prettier” Package Hijack
- **Description**: Maintainer accounts were phished, enabling attackers to publish trojanized package versions that download secondary payloads during install scripts.  
- **Impact**: Developers unknowingly execute malware during `npm install`, leading to workstation compromise or CI/CD pipeline intrusion.  
- **Status**: Malicious versions removed from npm; clean releases re-published.  

### Arch Linux AUR Chaos RAT Campaign
- **Description**: Three malicious AUR packages were crafted to fetch and execute the CHAOS remote-access trojan on Linux endpoints.  
- **Impact**: Full remote control of affected systems, data theft, and potential pivot into production servers.  
- **Status**: Packages taken down by Arch Linux maintainers; users advised to audit and rebuild affected hosts.  

### “Authentic Antics” Microsoft 365 Credential Stealing Malware
- **Description**: A stealthy implant attributed to APT28 that impersonates Microsoft authentication flows to exfiltrate session cookies and access tokens.  
- **Impact**: Covert access to corporate mailboxes, SharePoint sites, and Teams chats for espionage.  
- **Status**: Active; Microsoft and the UK-NCSC have issued detection guidance.  

### “PoisonSeed” QR-Code MFA Bypass
- **Description**: Phishing kit serving victims a spoofed MFA page with a QR code that relays authentication to attackers, effectively bypassing FIDO security keys.  
- **Impact**: Account takeover even where hardware-based 2FA is enforced.  
- **Status**: Campaigns observed targeting remote workers; no vendor patch applicable—requires user awareness and phishing-resistant MFA.  

## Affected Systems and Products

- **CrushFTP Server**: Versions 10 and earlier exposed via public web interface  
- **Ivanti Connect Secure & Policy Secure**: All firmware builds prior to emergency July 2025 fixes  
- **eslint-config-prettier / eslint-plugin-prettier**: Compromised npm releases 9.1.0–9.1.2  
- **Arch Linux AUR**: Malicious packages `ruby-bitwarden`, `libbpf`, `jsox` (July 2025 uploads)  
- **Microsoft 365 Tenants**: Outlook, SharePoint, and Teams users targeted by “Authentic Antics”  
- **Enterprise Workstations & Mobile Devices**: Users subjected to “PoisonSeed” QR-code phishing  

## Attack Vectors and Techniques

- **Web-Interface Admin Bypass**  
  - **Vector**: Direct HTTP(S) requests exploiting logic flaws in CrushFTP’s session management.  

- **VPN Appliance RCE via Zero-Day**  
  - **Vector**: Crafted HTTPS requests to Ivanti ICS/IPS portals resulting in shell access and loader deployment.  

- **Malicious Package Installation (npm/AUR)**  
  - **Vector**: `postinstall` scripts and PKGBUILD hooks execute obfuscated shell commands to pull remote binaries.  

- **Steganographic Payload Delivery**  
  - **Vector**: Malware hidden inside seemingly benign image or configuration files retrieved by trojanized packages.  

- **QR-Code MFA Relay Phishing**  
  - **Vector**: Victims scan attacker-controlled QR codes presented as part of an “extra authentication step,” forwarding session tokens.  

- **Cloud Token Exfiltration**  
  - **Vector**: “Authentic Antics” intercepts Azure AD refresh tokens via malicious OAuth applications and custom DLL loaders.  

## Threat Actor Activities

- **Unknown Actor (CrushFTP)**  
  - **Campaign**: Opportunistic mass scanning of exposed FTP servers; objective is data theft and foothold for ransomware.  

- **Unattributed Group leveraging Ivanti zero-days**  
  - **Campaign**: MDifyLoader distribution; post-exploitation uses Cobalt Strike for lateral movement in corporate networks.  

- **Supply-Chain Intruder (npm)**  
  - **Campaign**: Targeted phishing against package maintainers; focus on developer environments and CI/CD infiltration.  

- **Chaos RAT Operator**  
  - **Campaign**: Insertion of trojanized AUR packages; goal is to build a Linux botnet for crypto-mining and DDoS.  

- **APT28 (Fancy Bear)**  
  - **Campaign**: “Authentic Antics” espionage against Western diplomatic and defense sectors; harvests Microsoft 365 data.  

- **“PoisonSeed”**  
  - **Campaign**: Remote-workforce credential harvesting; industries targeted include finance, healthcare, and tech SaaS providers.  

