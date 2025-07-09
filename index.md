# Exploitation Report

During the past week, exploit activity has centered on Internet-facing infrastructure and supply-chain components, with critical weaponization of a new Citrix NetScaler flaw (“CitrixBleed 2”), an actively exploited zero-day in Microsoft SQL Server, and IoT vulnerabilities leveraged by the emerging RondoDox botnet. Mobile users are also at risk from the Android “TapTrap” permission-bypass technique, while developers face supply-chain threats through a compromised VS Code extension (Ethcode). CISA’s decision to fast-track four additional vulnerabilities into its Known Exploited Vulnerabilities (KEV) catalog underscores the urgency of patching publicly exploited flaws across multiple platforms.

## Active Exploitation Details

### Citrix NetScaler “CitrixBleed 2”
- **Description**: Memory-disclosure and request-smuggling flaw in NetScaler ADC/Gateway appliances, enabling attackers to harvest session tokens and authentication material remotely.  
- **Impact**: Full device compromise, lateral movement into internal networks, potential data theft.  
- **Status**: Proof-of-concept exploits are publicly available; Citrix has issued fixed firmware builds.  
- **CVE ID**: CVE-2025-5777  

### Microsoft SQL Server Zero-Day
- **Description**: Privilege-escalation vulnerability in Microsoft SQL Server disclosed and patched in July 2025 Patch Tuesday. Security researchers confirmed in-the-wild exploitation prior to patch release.  
- **Impact**: Attackers achieving SYSTEM-level execution on Windows hosts running vulnerable SQL Server instances; enables deployment of webshells or ransomware.  
- **Status**: Patched in July 2025 updates; exploitation observed before fixes were distributed.  

### TBK Digital Video Recorder Remote-Code Flaw
- **Description**: Authentication bypass and command-injection weakness in TBK DVR firmware exploited to enlist devices into DDoS botnets.  
- **Impact**: Remote code execution, botnet enrollment, and use of DVR bandwidth for high-volume attacks.  
- **Status**: Exploitation active by the RondoDox botnet; no official vendor patch referenced.  

### Four-Faith Router Command Injection Vulnerability
- **Description**: Improper input validation in web-management interface allows unauthenticated command execution.  
- **Impact**: Router takeover, network pivoting, and incorporation into RondoDox for distributed attacks.  
- **Status**: Active exploitation; remediation guidance not yet published.  

### Android “TapTrap” Permission-Bypass Technique
- **Description**: Tapjacking method abusing UI animation layers to make security prompts invisible, tricking users into granting high-risk permissions.  
- **Impact**: Access to camera, microphone, SMS, and potentially destructive actions (factory reset, app installs).  
- **Status**: Technique observed in the wild; mitigations require OS-level hardening (no discrete patch).  

### Ethcode VS Code Extension Supply-Chain Vulnerability
- **Description**: Maintainer account compromise led to malicious pull request that injected backdoor code into the Ethcode extension used by blockchain developers.  
- **Impact**: Execution of arbitrary code on developer machines, credential theft, and potential compromise of smart-contract projects.  
- **Status**: Malicious version pulled; users must reinstall from a clean repository.  

### Newly Added KEV Catalog Flaws
- **Description**: Four critical vulnerabilities (details redacted by CISA) confirmed exploited against U.S. organizations, spanning network appliances and enterprise software.  
- **Impact**: Remote code execution and privilege escalation depending on specific products.  
- **Status**: Mandatory patch deadlines set for Federal Civilian Executive Branch agencies; exploitation ongoing in the public domain.  

## Affected Systems and Products

- **Citrix NetScaler ADC/Gateway**: All supported builds prior to patched firmware; affects on-prem and cloud appliances  
- **Microsoft SQL Server**: Supported versions prior to July 2025 cumulative updates on Windows Server 2016 – 2022  
- **TBK DVR Series**: Multiple DVR models used in retail and surveillance deployments  
- **Four-Faith Industrial Routers (F-3x/F-9x lines)**: Routers deployed in SCADA and IoT edge environments  
- **Android Smartphones**: Devices running Android 10–14 susceptible to tapjacking UI overlays  
- **VS Code Ethcode Extension**: Versions cloned or installed after the malicious pull request; ~6,000 installations  
- **Multiple Products in CISA KEV List**: Network security appliances and enterprise software identified by CISA as actively exploited  

## Attack Vectors and Techniques

- **Memory-Disclosure & Session-Hijack (CitrixBleed 2)**  
  - **Vector**: Crafted HTTP/HTTPS requests to NetScaler gateway endpoints leak session tokens.

- **Privilege Escalation via SQL Query Abuse (SQL Server Zero-Day)**  
  - **Vector**: Authenticated or chained attacks inject malicious queries to elevate privileges to SYSTEM.

- **Command Injection on Embedded Web UI (TBK/Four-Faith)**  
  - **Vector**: Unsanitized CGI parameters allow shell command execution over HTTP.

- **Tapjacking Animation Overlay (TapTrap)**  
  - **Vector**: Malicious app draws invisible UI layers over system dialogs, hijacking user taps.

- **Malicious Extension Update (Ethcode)**  
  - **Vector**: Compromised GitHub pull request auto-updates developer environments with backdoored code.

- **Proof-of-Concept Publication**  
  - **Vector**: Public PoC scripts lower bar for indiscriminate exploitation, particularly of CitrixBleed 2.

## Threat Actor Activities

- **RondoDox Botnet Operators**  
  - **Campaign**: Exploiting TBK DVR and Four-Faith router flaws to amass a DDoS network targeting service providers.

- **Unknown Threat Actors (CitrixBleed 2)**  
  - **Campaign**: Mass scanning and token-harvesting from exposed NetScaler appliances; goal is credential theft and lateral movement.

- **Unattributed Actors Exploiting SQL Server Zero-Day**  
  - **Campaign**: Targeting self-hosted SQL instances in finance and healthcare to deploy webshells and ransomware.

- **Supply-Chain Intrusion Set (Ethcode)**  
  - **Campaign**: Focused on blockchain developers to siphon wallet credentials and manipulate smart-contract code.

- **Mobile Threat Actors Using TapTrap**  
  - **Campaign**: Distributing repackaged apps on third-party stores to harvest SMS 2FA codes and device data.

- **CISA-Highlighted Actors**  
  - **Campaign**: Ongoing exploitation of four unnamed KEV catalog vulnerabilities across federal and critical infrastructure networks.

- **DragonForce Ransomware Group**  
  - **Campaign**: Used social-engineering foothold at M&S to deploy ransomware, illustrating the tie between credential phishing and vulnerability exploitation post-compromise.

- **Silk Typhoon (China-linked)**  
  - **Campaign**: Historical cyber-espionage; recent arrest may disrupt but not eliminate exploitation operations.