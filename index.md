# Exploitation Report

A spike in high-impact exploitation is underway across both enterprise and developer ecosystems. Threat actors are abusing a zero-day in CrushFTP (CVE-2025-54309) to seize administrative access to file-sharing servers, leveraging fresh Ivanti Connect Secure / Policy Secure flaws to implant in-memory Cobalt Strike beacons, hijacking popular JavaScript and Arch Linux packages for malware delivery, and side-stepping FIDO2 security keys in sophisticated phishing operations (“PoisonSeed”). Government–linked actors such as Russia’s APT28 are simultaneously harvesting Microsoft 365 credentials with the newly outed “Authentic Antics” malware. The activity demonstrates an aggressive focus on supply-chain compromise, MFA downgrades, and remote-access edge appliances—targets that provide rapid lateral movement and data exfiltration opportunities.

## Active Exploitation Details

### CrushFTP Administrative Access Zero-Day
- **Description**: A vulnerability in CrushFTP’s web interface allows unauthenticated attackers to escalate privileges and obtain full administrative control.
- **Impact**: Complete server takeover, file theft, user impersonation, and potential pivoting into internal networks.
- **Status**: Actively exploited in the wild; vendor released emergency patches and mitigation guidance.
- **CVE ID**: CVE-2025-54309

### Ivanti Connect Secure / Policy Secure Zero-Days
- **Description**: Newly identified flaws enable attackers to bypass authentication, write files, and execute code on Ivanti VPN gateways.
- **Impact**: Deployment of “MDifyLoader” malware followed by in-memory Cobalt Strike, granting persistent network access and command-and-control.
- **Status**: Exploitation observed prior to public disclosure; patches and work-arounds have been issued.

### WebAuthn Cross-Device MFA Downgrade (“PoisonSeed”)
- **Description**: Attackers coerce victims into scanning a QR code that invokes WebAuthn’s cross-device sign-in, downgrading FIDO2 hardware-key authentication to a push notification the attacker controls.
- **Impact**: Account compromise despite hardware security keys; enables Business Email Compromise (BEC) and data theft.
- **Status**: Ongoing phishing campaign; no software patch required—mitigations focus on user awareness and policy hardening.

### npm Package Hijacking (eslint-config-prettier & eslint-plugin-prettier)
- **Description**: Maintainer accounts were phished, and the packages were republished to download additional payloads during `npm install`.
- **Impact**: Supply-chain malware delivery to any CI/CD pipeline or workstation that resolves the compromised versions.
- **Status**: Malicious versions removed; clean releases restored. Users must audit dependencies and rotate secrets.

### Arch Linux AUR Malicious Packages (chaotic-aur, connman-ui, libpaf)
- **Description**: Three AUR uploads executed install scripts that retrieved and ran the CHAOS RAT.
- **Impact**: Remote command execution, data exfiltration, and system surveillance on affected Linux hosts.
- **Status**: Packages pulled from AUR; users instructed to validate systems for RAT artifacts and revoke exposed credentials.

### “Authentic Antics” Microsoft 365 Credential Harvester
- **Description**: Malware attributed to APT28 steals session cookies and token material from Microsoft 365 to maintain clandestine cloud access.
- **Impact**: Long-term espionage, email theft, and potential manipulation of cloud resources.
- **Status**: Active campaign; Microsoft and UK NCSC published indicators and remediation steps.

### MCP Server Authentication Bypass (Configuration Flaw)
- **Description**: Management Control Protocol (MCP) servers operate with optional authentication, leaving ~2,000 instances openly accessible.
- **Impact**: Unrestricted administrative commands enable takeover of agentic-AI infrastructures and data manipulation.
- **Status**: Issue remains largely unremediated—operators must enable authentication and network segmentation.

## Affected Systems and Products

- **CrushFTP (v11 and prior)**  
  Platform: Windows, macOS, Linux file-sharing servers  

- **Ivanti Connect Secure / Policy Secure Gateways (various 2024–2025 builds)**  
  Platform: Hardened Linux appliances at network edge  

- **WebAuthn-enabled SaaS (Microsoft 365, Google Workspace, Okta, etc.)**  
  Platform: Any OS/browser supporting FIDO2 hardware keys  

- **eslint-config-prettier & eslint-plugin-prettier (npm versions 9.0.0–9.0.2)**  
  Platform: Node.js development and CI environments  

- **Arch Linux systems using AUR helpers (affected packages: chaotic-aur, connman-ui, libpaf)**  
  Platform: x86_64 / ARM Linux  

- **Microsoft 365 Tenants targeted by “Authentic Antics”**  
  Platform: Cloud SaaS; Windows/macOS endpoints for token theft  

- **Public MCP Servers with authentication disabled**  
  Platform: Linux/UNIX servers running agentic-AI back-ends  

## Attack Vectors and Techniques

- **Web Interface Admin Bypass**  
  Vector: Crafted HTTP requests to CrushFTP API endpoints  

- **VPN Appliance Auth Bypass & File Write**  
  Vector: Chained HTTP requests exploiting new Ivanti flaws  

- **MFA Downgrade via QR-Based Phishing**  
  Vector: Social-engineering emails lead to fake login portal rendering WebAuthn cross-device QR  

- **Dependency Confusion / Package Takeover**  
  Vector: Compromised maintainer credentials allow malicious npm publish; install hooks download binaries  

- **AUR Malicious `prepare()` and `install()` Scripts**  
  Vector: Execution during `makepkg` pulls CHAOS RAT from attacker-controlled URL  

- **Session Cookie & OAuth Token Theft**  
  Vector: “Authentic Antics” implants inject into browser processes and exfiltrate tokens  

- **Unauthenticated MCP Command Execution**  
  Vector: Direct TCP connections to MCP service on default port with no credential challenge  

## Threat Actor Activities

- **PoisonSeed Operators**  
  Campaign: Large-scale enterprise phishing targeting FIDO2 users; focus on finance and tech firms  

- **Unknown CrushFTP Exploiters**  
  Campaign: Rapid smash-and-grab file exfiltration; servers observed beaconing to multiple C2 nodes  

- **MDifyLoader Group**  
  Campaign: Uses Ivanti zero-days to plant loaders and Cobalt Strike; post-exploitation aims at credential dumping  

- **APT28 (Fancy Bear) / GRU**  
  Campaign: “Authentic Antics” espionage, targeting government and defense entities for Microsoft 365 intel  

- **npm Supply-Chain Actor**  
  Campaign: Spear-phished maintainer, weaponized linter packages; telemetry shows thousands of global downloads in 48 hours  

- **AUR Chaos RAT Actor**  
  Campaign: Opportunistic; sought persistence on hobbyist and research Linux systems  

- **UNG0002**  
  Campaign: Parallel LNK-based intrusions in China, Hong Kong, Pakistan leveraging RATs and staging servers for espionage  

- **Unknown MCP Scanners**  
  Campaign: Internet-wide sweeps issuing agentic-AI control commands; motivations range from crypto-mining to sabotage  

