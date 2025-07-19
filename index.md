# Exploitation Report

Threat hunters observed a sharp uptick in zero-day exploitation and credential-theft campaigns this week. The most critical developments are the active abuse of CVE-2025-54309 in CrushFTP servers, mass Internet scanning for CVE-2025-48927 in the TeleMessage SGNL secure-messaging platform, and weaponisation of still-unpatched Ivanti Connect Secure zero-days to deliver the new “MDifyLoader” malware and in-memory Cobalt Strike beacons. Parallel supply-chain and social-engineering activity—malicious Arch Linux AUR packages, GRU-backed “Authentic Antics” Microsoft 365 malware, and the novel “PoisonSeed” QR-code MFA bypass—expand adversaries’ reach across Linux, Microsoft 365, and multi-factor authentication ecosystems.

## Active Exploitation Details

### CrushFTP Web-Interface Authentication Bypass  
- **Description**: A logic flaw in CrushFTP’s web administration interface allows an unauthenticated attacker to craft a request that hijacks an administrator’s session, granting full control of the managed file-transfer server.  
- **Impact**: Administrative takeover, arbitrary file upload/download, remote code execution, and lateral movement into connected storage or internal networks.  
- **Status**: Confirmed zero-day exploitation in the wild; vendor has released fixed builds and urges immediate upgrades.  
- **CVE ID**: CVE-2025-54309  

### TeleMessage SGNL Credential Exposure  
- **Description**: Improper authentication on an API endpoint of the SGNL enterprise messaging application permits attackers to retrieve clear-text usernames, passwords, and configuration data by sending crafted requests.  
- **Impact**: Full account compromise, credential stuffing against corporate SSO, and potential interception of supposedly secure communications.  
- **Status**: Large-scale Internet scans and exploitation attempts detected; patches and updated Docker images are available from the vendor.  
- **CVE ID**: CVE-2025-48927  

### Ivanti Connect Secure / Policy Secure Zero-Days  
- **Description**: A chained authentication-bypass and command-injection pair in Ivanti VPN gateways is being leveraged to drop “MDifyLoader,” which injects Cobalt Strike beacons directly into memory to evade disk-based detection.  
- **Impact**: Pre-authentication remote code execution, persistent foothold on perimeter VPN devices, credential harvesting, and post-exploitation pivoting.  
- **Status**: Actively exploited before public disclosure; emergency mitigation guidance and patched firmware images have been issued.  

## Affected Systems and Products

- **CrushFTP Managed File Transfer Server**: Versions prior to the hot-fix releases published 24 hours after disclosure  
- **TeleMessage SGNL**: All on-prem and Docker deployments running vulnerable API component builds prior to the vendor’s July patch  
- **Ivanti Connect Secure / Policy Secure / ZTA Gateways**: All supported hardware and virtual appliances until patched firmware is applied  
- **Arch Linux AUR**: Malicious “adbutils”, “fabric-base”, and “miniconda-pytorch” packages (now removed)  
- **Microsoft 365 Tenants**: Any organisation targeted by APT28’s “Authentic Antics” malware chain  
- **Linux Workstations & Servers**: Systems where users built the compromised AUR packages or where Chaos RAT subsequently deployed  

## Attack Vectors and Techniques

- **Web-Admin Session Riding (CrushFTP)**  
  - **Vector**: Crafted HTTP requests that manipulate session tokens to impersonate an admin without credentials.  

- **Unauthenticated API Scraping (TeleMessage SGNL)**  
  - **Vector**: Direct requests to misconfigured API endpoint returning credential objects in JSON.  

- **Auth-Bypass + Command-Injection Chain (Ivanti)**  
  - **Vector**: Pre-auth path traversal to reach an internal endpoint, followed by shell-command injection that fetches MDifyLoader.  

- **Supply-Chain Typosquatting (Arch AUR)**  
  - **Vector**: Upload of look-alike packages that execute post-install scripts to drop Chaos RAT.  

- **QR-Code MFA Phishing (“PoisonSeed”)**  
  - **Vector**: Phishing pages serving a QR code which, once scanned, proxies the MFA session and sidesteps FIDO-based keys.  

## Threat Actor Activities

- **APT28 / Fancy Bear (Russian GRU)**  
  - **Campaign**: “Authentic Antics” – custom malware exfiltrating Microsoft 365 credentials, targeting UK and NATO-aligned organisations.  

- **Unknown CrushFTP Exploiters**  
  - **Campaign**: Opportunistic mass scanning and server hijacking for data exfiltration and potential ransomware deployment.  

- **TeleMessage SGNL Scanners**  
  - **Campaign**: Broad Internet sweeps originating from multiple VPS providers to harvest credentials for sale or follow-on intrusions.  

- **“PoisonSeed” Operators**  
  - **Campaign**: Spear-phishing against enterprise users, delivering QR-code–based MFA bypass to hijack sessions.  

- **UNG0002**  
  - **Campaign**: Twin espionage operations in China, Hong Kong, and Pakistan using malicious LNK files and RAT payloads for long-term surveillance.  

- **AUR Chaos RAT Maintainer(s)**  
  - **Campaign**: Supply-chain compromise of Arch Linux AUR to deploy remote-access malware onto developer workstations.  

- **Ivanti Zero-Day Exploitation Cluster (attribution pending)**  
  - **Campaign**: Deployment of MDifyLoader and Cobalt Strike for covert persistence on VPN appliances and subsequent network intrusion.