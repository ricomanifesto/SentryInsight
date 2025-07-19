# Exploitation Report

During the past week, security researchers observed intensified exploitation of enterprise-facing software and cloud authentication workflows. The most critical activity centers on two zero-day chains in Ivanti Connect Secure appliances and a newly disclosed credential-exposure flaw (CVE-2025-48927) in the TeleMessage “SGNL” secure-messaging clone of Signal. Both issues are already leveraged in the wild to drop post-exploitation loaders or harvest passwords at scale. Simultaneously, Russia-linked APT28 is abusing Microsoft 365 OAuth flows with a custom malware dubbed “Authentic Antics,” while a threat actor tracked as PoisonSeed is bypassing FIDO-based MFA through QR-code social engineering. These campaigns collectively highlight attackers’ preference for identity compromise and edge-device exploitation to obtain initial access and maintain persistence.

## Active Exploitation Details

### TeleMessage SGNL Credential-Exposure Vulnerability
- **Description**: A server-side flaw in TeleMessage’s SGNL application allows unauthenticated retrieval of usernames, plaintext or hashed passwords, and additional sensitive account metadata via crafted API queries.  
- **Impact**: Attackers can harvest credentials in bulk, enabling lateral movement into corporate messaging infrastructure and associated single-sign-on (SSO) environments.  
- **Status**: Public exploit code observed; mass scanning activity is underway while the vendor has issued an emergency patch.  
- **CVE ID**: CVE-2025-48927  

### Ivanti Connect Secure / Policy Secure Zero-Day Chain
- **Description**: Two previously unknown vulnerabilities in Ivanti VPN gateways permit remote code execution that injects the “MDifyLoader” malware, which in turn side-loads an in-memory instance of Cobalt Strike Beacon.  
- **Impact**: Full device compromise, credential theft, network pivoting, and command-and-control inside segmented environments.  
- **Status**: Actively exploited prior to patch release; Ivanti has published fixes and mitigations, but unpatched devices remain vulnerable.  

### Microsoft 365 “Authentic Antics” OAuth Abuse
- **Description**: APT28 deploys a bespoke malware framework that registers rogue OAuth applications within Azure Entra ID, then silently steals Microsoft 365 authentication tokens and mailbox data without triggering conventional MFA challenges.  
- **Impact**: Persistent access to Exchange Online, SharePoint, and Teams; exfiltration of emails and files; potential for internal phishing.  
- **Status**: Active espionage operations confirmed; Microsoft guidance focuses on app-consent hygiene and conditional-access hardening.  

### PoisonSeed QR-Code MFA Bypass
- **Description**: The PoisonSeed actor replaces standard MFA prompts with attacker-controlled QR codes that phish session cookies, effectively circumventing FIDO/WebAuthn hardware keys.  
- **Impact**: Account takeover even in environments mandating phishing-resistant MFA.  
- **Status**: In-the-wild campaigns targeting remote workforce portals; mitigation involves out-of-band verification of login requests and disabling fallback QR authentication where possible.  

## Affected Systems and Products

- **TeleMessage SGNL**: All on-prem and cloud deployments prior to the emergency hotfix  
  - **Platform**: Linux-based application servers and hosted SaaS environment  

- **Ivanti Connect Secure / Policy Secure Gateways**: 9.x and 22.x firmware branches before latest patches  
  - **Platform**: Purpose-built VPN/SSL gateway appliances (virtual and hardware)  

- **Microsoft 365 & Azure Entra ID Tenants**: Organizations permitting user or admin consent to third-party OAuth apps  
  - **Platform**: Cloud (SaaS) – Exchange Online, SharePoint Online, Teams, Graph API  

- **Enterprise MFA Implementations Using FIDO/WebAuthn with Optional QR Enrollment**  
  - **Platform**: Web portals, VPN logins, SSO providers (Okta, Duo, Azure AD)  

## Attack Vectors and Techniques

- **Mass Internet Scanning & API Enumeration**  
  - **Vector**: Automated queries against exposed SGNL endpoints to dump credential stores.

- **SSL-VPN Edge Exploitation & Malware Side-Loading**  
  - **Vector**: Crafted HTTP requests trigger zero-day flaws on Ivanti gateways; shell access is used to deploy MDifyLoader, which side-loads Cobalt Strike in memory.

- **OAuth Application Impersonation**  
  - **Vector**: Rogue Azure apps obtain admin consent or exploit misconfigured consent settings, generating long-lived refresh tokens for Microsoft 365.

- **QR-Code-Based Phishing (MFA Relay)**  
  - **Vector**: Victims scan malicious QR codes presented during spoofed login flows; session cookies are proxied to the attacker, bypassing hardware-bound FIDO keys.

- **LNK Shortcut Malware Delivery (UNG0002 auxiliary activity)**  
  - **Vector**: Weaponized Windows shortcut files execute RAT payloads when icons are clicked, facilitating initial access in regional espionage campaigns.

## Threat Actor Activities

- **APT28 (Fancy Bear / GRU)**  
  - **Campaign**: “Authentic Antics” – targeting government and defense organizations to harvest Microsoft 365 credentials via OAuth abuse.

- **PoisonSeed**  
  - **Campaign**: QR-code MFA bypass attacks against global corporate users operating remotely, emphasizing identity compromise.

- **Unknown Cluster Exploiting Ivanti Zero-Days**  
  - **Campaign**: Drops MDifyLoader and Cobalt Strike to establish footholds in enterprise networks, chiefly in North America and Europe.

- **Internet-Wide Opportunists**  
  - **Campaign**: Automated exploitation of CVE-2025-48927 in TeleMessage SGNL, aiming to build credential databases for resale or follow-on intrusions.

- **UNG0002**  
  - **Campaign**: Twin espionage operations in China, Hong Kong, and Pakistan using malicious LNK files and multiple RAT families for surveillance and data theft.

