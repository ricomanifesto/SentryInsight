# Exploitation Report

Recent threat intelligence highlights a surge in highly targeted exploitation, ranging from a newly disclosed CrushFTP zero-day that grants full administrative access, to multi-stage supply-chain attacks abusing popular npm linter packages. Active campaigns are also downgrading FIDO2 multi-factor authentication, weaponizing fresh Ivanti zero-days to deploy in-memory Cobalt Strike beacons, and seeding Arch Linux AUR packages with Chaos RAT. Notably, Russia-linked APT28 is running Microsoft 365 credential-theft operations, while lax authentication on thousands of MCP servers leaves them wide open for hijacking. These developments underscore the continued attacker focus on authentication bypass, software-supply-chain compromise, and public-facing server vulnerabilities.

## Active Exploitation Details

### CrushFTP Web Interface Zero-Day
- **Description**: A flaw in CrushFTP’s web interface allows remote, unauthenticated attackers to escalate directly to administrative access.  
- **Impact**: Full takeover of file-transfer servers, exfiltration of stored data, and deployment of additional payloads.  
- **Status**: Exploited in the wild; vendor released CrushFTP 11.2.0/10.7.1 and hot-fix patches.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Days
- **Description**: Multiple previously unknown vulnerabilities in the Ivanti VPN and network-access appliances enable code execution that drops the new “MDifyLoader” malware, followed by in-memory Cobalt Strike.  
- **Impact**: Network pivoting, credential theft, lateral movement, and persistent foothold within enterprise environments.  
- **Status**: Actively exploited in the wild; Ivanti has issued emergency mitigation guidance and patches are being rolled out.  

### PoisonSeed FIDO2 Downgrade Phishing
- **Description**: The “PoisonSeed” phishing kit abuses WebAuthn’s cross-device sign-in to trick victims into authenticating a malicious session, effectively downgrading FIDO2 security-key protection to a push-based approval.  
- **Impact**: Account takeover even when hardware security keys are enforced; enables subsequent business-email-compromise (BEC) and data theft.  
- **Status**: Ongoing campaign; no vendor patch required, but security-key user-experience hardening and policy updates are advised.  

### npm Linter Package Hijack
- **Description**: eslint-config-prettier and eslint-plugin-prettier were taken over through credential-phishing of the maintainer. Updated versions act as malware droppers, fetching second-stage payloads at install time.  
- **Impact**: Remote code execution on developer machines, potential CI/CD pipeline compromise, and downstream supply-chain infection.  
- **Status**: Malicious versions yanked from npm; developers must audit caches and lockfiles and pin to safe releases.  

### Arch Linux AUR Chaos RAT Packages
- **Description**: Three malicious AUR packages were uploaded that silently install the Chaos remote-access trojan during build.  
- **Impact**: Backdoor control of affected Linux systems, data exfiltration, and participation in botnet activity.  
- **Status**: Packages removed; users encouraged to verify builds and rotate keys.  

### Authentic Antics – Microsoft 365 Credential-Stealing Malware
- **Description**: Stealthy malware toolkit attributed to APT28 that steals session tokens and credentials from Microsoft 365 tenants, evading traditional detection.  
- **Impact**: Espionage-grade access to corporate mailboxes, SharePoint, and Teams data; potential for further pivoting inside cloud environments.  
- **Status**: Active; Microsoft and the UK NCSC have issued detection signatures and hardening guidance.  

### Unauthenticated MCP Server Exposure
- **Description**: Management servers for the MCP (agentic-AI backbone) ship with authentication set to “optional,” leaving ~2,000 internet-reachable nodes exposed.  
- **Impact**: Complete remote control, model manipulation, and data tampering by any external actor.  
- **Status**: Exploitability is trivial; no patches yet—administrators must manually enable strong authentication and firewall access.  

## Affected Systems and Products

- **CrushFTP**: Versions prior to 11.2.0/10.7.1  
  **Platform**: Windows, Linux, macOS, and other supported server OSes  
- **Ivanti Connect Secure / Policy Secure**: All supported firmware builds prior to emergency patches  
  **Platform**: Network VPN and NAC appliances  
- **WebAuthn / FIDO2 Implementations**: Any web applications relying on cross-device sign-in  
  **Platform**: All major browsers and OSes supporting WebAuthn  
- **eslint-config-prettier & eslint-plugin-prettier (npm)**: Compromised 9.x and 8.x versions published during attack window  
  **Platform**: Node.js development environments, CI/CD systems  
- **Arch Linux AUR Packages**: Specific malicious packages (names redacted by AUR) prior to takedown  
  **Platform**: Arch Linux desktops, servers, and derivatives  
- **Microsoft 365 Tenants**: Organizations using cloud email and collaboration services  
  **Platform**: Azure AD / Entra ID, Office 365 web and desktop clients  
- **MCP Servers**: Public-facing agentic-AI orchestration servers with default configuration  
  **Platform**: Linux and containerized deployments, often cloud-hosted  

## Attack Vectors and Techniques

- **Zero-Day Remote Code Execution (RCE)**  
  Vector: Direct HTTP/S requests to vulnerable CrushFTP and Ivanti web interfaces.

- **Supply-Chain Package Hijacking**  
  Vector: Malicious npm/AUR package versions executed during install or build.

- **MFA Downgrade / WebAuthn Cross-Device Abuse**  
  Vector: Phishing site serves QR code and push notification that leverages cross-device sign-in loophole.

- **In-Memory Post-Exploitation Tooling**  
  Vector: MDifyLoader injects Cobalt Strike beacons to avoid disk artifacts.

- **Cloud Token Theft**  
  Vector: Authentic Antics malware extracts Microsoft 365 refresh tokens and session cookies.

- **Unauthenticated API Exposure**  
  Vector: Open MCP endpoints allow remote procedure calls without credentials.

## Threat Actor Activities

- **PoisonSeed**  
  Campaign: Ongoing phishing operations targeting enterprise users with FIDO2 keys; focuses on credential harvesting and session hijack.

- **APT28 (Fancy Bear)**  
  Campaign: “Authentic Antics” Microsoft 365 espionage; credential theft, mailbox scraping, sustained persistence.

- **Unknown Operators (CrushFTP Zero-Day)**  
  Campaign: Opportunistic server hijacking observed globally; objective appears to be data exfiltration and possible ransomware staging.

- **Unattributed Supply-Chain Actors**  
  Campaign: npm linter package takeover; aims at developer environments to pivot into corporate networks.

- **Threat Cluster Behind MDifyLoader**  
  Campaign: Targets Ivanti appliances to deploy loader and in-memory Cobalt Strike for lateral movement in high-value networks.

- **Malicious Maintainer (Arch Linux AUR)**  
  Campaign: Chaos RAT seeding via community repository; focus on building Linux botnet capabilities.

- **Opportunistic Hackers (MCP Servers)**  
  Campaign: Large-scale scanning and hijacking of unsecured MCP nodes to manipulate AI workloads or harvest sensitive data.

