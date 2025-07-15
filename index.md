# Exploitation Report

The past week’s activity underscores an aggressive shift toward supply-chain compromise, firmware tampering, and cloud-hosted command-and-control. North Korean operators poisoned the npm ecosystem with dozens of weaponized packages that sideload the new XORIndex loader, while the Interlock ransomware group rolled out a “FileFix” delivery chain to silently implant a PHP-based RAT. Separate campaigns leveraged malformed Android APKs, malicious VSCode extensions, and insecure AWS Lambda functions to gain covert access to developer workstations and government networks. Of particular concern is a Secure Boot-bypass flaw in Gigabyte UEFI firmware and critical weaknesses in Kigen eSIM cards that put billions of IoT devices at risk. Hyper-volumetric DDoS attacks exploiting the HTTP/2 Rapid Reset weakness also reached a record 7.3 Tbps, indicating that denial-of-service tactics remain a favored method for large-scale disruption.

## Active Exploitation Details

### Gigabyte UEFI Secure Boot Bypass
- **Description**: Multiple Gigabyte motherboard firmware images allow unsigned or tampered bootloaders to execute before the OS, effectively disabling Secure Boot protections.  
- **Impact**: Attackers can install stealthy bootkits that survive OS reinstallation, remain invisible to endpoint security, and provide full system persistence.  
- **Status**: Exploitation observed in the wild; Gigabyte is expected to release updated UEFI images, but many systems remain unpatched.

### Kigen eUICC / eSIM Remote Profile Takeover
- **Description**: Design flaws in Kigen’s eSIM cards allow unauthorized over-the-air profile provisioning and key extraction.  
- **Impact**: Enables SIM cloning, interception of SMS-based multi-factor authentication, remote device tracking, and massive IoT disruption.  
- **Status**: Active proof-of-concept exploitation reported. Mitigations involve carrier-side validation and firmware updates to affected eUICC cards.

### XORIndex Malicious npm Packages
- **Description**: 67 trojanized npm packages embed the XORIndex malware loader, triggered during post-install scripts on developer machines.  
- **Impact**: Steals source code, environment variables, and credentials; establishes persistence for follow-on implants.  
- **Status**: Packages have been removed from the registry, but cloned mirrors and cached copies continue to circulate.

### FileFix Delivery Chain (Interlock RAT)
- **Description**: Interlock ransomware actors weaponized a “FileFix” technique that abuses specially crafted file associations to drop a new PHP-based RAT.  
- **Impact**: Provides remote shell access, lateral movement, and data encryption capabilities prior to ransom demands.  
- **Status**: Ongoing; no vendor patch required—defenders must block suspicious file types and harden email/web gateways.

### HazyBeacon AWS Lambda Abuse
- **Description**: State-sponsored operators deploy the HazyBeacon backdoor, which communicates over legitimate AWS Lambda and S3 APIs to blend C2 traffic with benign cloud noise.  
- **Impact**: Covert exfiltration of diplomatic documents and persistent access in Southeast Asian government networks.  
- **Status**: Campaign active; mitigation requires inspection of cloud service logs and tighter IAM controls.

### Diskstation NAS Ransomware Intrusions
- **Description**: The Romanian “Diskstation” gang brute-forces or exploits exposed NAS management interfaces, encrypting storage for extortion.  
- **Impact**: Business-critical file servers rendered inaccessible, leading to operational paralysis.  
- **Status**: Law-enforcement takedown disrupted infrastructure, but residual infections persist on unpatched NAS devices.

### Konfety Android Malformed APK
- **Description**: A new Konfety variant hides malicious payloads in APKs with corrupt ZIP headers, bypassing automated scanners and many AV engines.  
- **Impact**: Grants full device control, credential theft, and espionage functions on compromised smartphones.  
- **Status**: Seen in third-party app stores; Google Play Protect updates underway.

### Malicious VSCode Extension in Cursor IDE
- **Description**: A fake extension for the Cursor AI-enabled IDE installs remote-access tools and infostealers during IDE startup.  
- **Impact**: Led to at least one confirmed theft of $500 K in cryptocurrency wallets; also harvests SSH keys and API tokens.  
- **Status**: Extension repository entry removed; users must manually audit extensions and revoke stolen keys.

### HTTP/2 Rapid Reset DDoS Exploit
- **Description**: Attackers exploit the “Rapid Reset” weakness in HTTP/2 to amplify DDoS traffic, forcing servers to repeatedly restart streams.  
- **Impact**: Record-breaking 7.3 Tbps floods disrupted finance, SaaS, and telecom providers.  
- **Status**: Cloudflare and other CDN vendors deployed mitigations; origin servers need protocol-level patches or rate-limits.

## Affected Systems and Products

- **Gigabyte AM5 & Intel 700-series Motherboards**: UEFI versions prior to forthcoming vendor patch  
- **Kigen eUICC / eSIM Cards**: M2M, consumer, and IoT profiles across global carriers  
- **Node.js / npm Ecosystem**: Developers installing poisoned packages “classnames-loader”, “react-icons-index”, and related libraries  
- **Windows & Linux Servers**: Targets of Interlock’s FileFix payloads via email attachments and web injects  
- **AWS Cloud Environments**: Misused Lambda, API Gateway, and S3 buckets for HazyBeacon C2  
- **Synology & QNAP NAS Devices**: Internet-exposed admin interfaces without strong authentication  
- **Android 8–14 Devices**: Users sideloading apps from unofficial marketplaces  
- **Cursor IDE (VSCode fork)**: Versions allowing unsigned extension installation  
- **HTTP/2-enabled Web Servers**: Apache, nginx, IIS, and cloud load balancers lacking Rapid Reset mitigations

## Attack Vectors and Techniques

- **Supply-Chain Package Poisoning**: Malicious npm packages execute post-install scripts to drop loaders.  
- **FileFix Association Hijacking**: Crafted files trigger unintended handler execution, silently running payloads.  
- **Malformed APK Packaging**: Corrupt ZIP structures evade antivirus heuristics during Android app installs.  
- **UEFI Bootkit Implantation**: Direct flash modification or DMA attacks inject persistent pre-OS malware.  
- **eSIM Profile Hijack**: Unauthorized SM-DP+ interactions enroll rogue operator profiles.  
- **Cloud-Native C2 (AWS Lambda/S3)**: Beacon traffic tunneled through legitimate cloud API calls.  
- **HTTP/2 Rapid Reset Flooding**: Abusive stream-cancel sequence overwhelms server resources.  
- **Malicious IDE Extension**: Unsigned VSCode add-on abuses IDE privileges for RCE.  
- **Brute-Force / Credential Stuffing**: NAS management panels attacked to deploy ransomware.

## Threat Actor Activities

- **North Korean Contagious Interview Operators**  
  - Planted 67 weaponized npm packages delivering XORIndex; targeting global software developers.

- **Interlock Ransomware Group**  
  - Debuted PHP-based RAT via FileFix; broad industry targeting with web-inject lures.

- **State-Backed HazyBeacon Group (suspected Chinese nexus)**  
  - Intelligence-collection against Southeast Asian government agencies; leverages AWS for stealth.

- **Diskstation Ransomware Gang (Romanian)**  
  - Focused on European SMBs; encrypted NAS appliances until international takedown operation.

- **GLOBAL GROUP RaaS**  
  - Expanding affiliate base with AI-driven negotiation chatbots; victims in Australia, Brazil, EU, and U.S.

- **Konfety Android Operators**  
  - Distributed malformed APKs through third-party stores to steal user data and persist on devices.

- **Unknown Threat Actors Exploiting Gigabyte Firmware**  
  - Implanting UEFI bootkits for long-term espionage and credential theft.

- **Cryptocurrency-Focused Actors via Cursor IDE**  
  - Used malicious VSCode extension to siphon $500 K from a Russian crypto trader; pursuing other high-value wallets.

- **DDoS Botnet Operators**  
  - Leveraged HTTP/2 Rapid Reset to launch 7.3 Tbps floods against finance, telecom, and SaaS infrastructure.

