# Exploitation Report

Over the last week, defenders observed a sharp rise in active exploitation across enterprise software, authentication flows, and open-source supply chains. A zero-day in CrushFTP (CVE-2025-54309) is being mass-exploited to seize administrative control of file-sharing servers, while two never-before-seen Ivanti Connect Secure flaws are enabling in-memory Cobalt Strike beacons via the new “MDifyLoader” malware. Concurrently, the “PoisonSeed” campaign is abusing WebAuthn’s cross-device sign-in feature to downgrade FIDO2 hardware key workflows, effectively nullifying phishing-resistant MFA. Attackers also hijacked popular npm linter packages and several Arch Linux AUR packages, weaponizing the open-source ecosystem to deliver malware. Finally, almost 2,000 MCP servers were found exposed with no authentication, underscoring persistent misconfiguration risks. Collectively, these events highlight an aggressive threat landscape targeting both infrastructure software and the human layer of defense.

## Active Exploitation Details

### CrushFTP Web Interface Authentication Bypass
- **Description**: A logic flaw in the CrushFTP web interface allows remote, unauthenticated attackers to bypass login controls and obtain full administrative privileges.  
- **Impact**: Complete takeover of the file-sharing server, exfiltration of stored data, and deployment of additional malware or ransomware.  
- **Status**: Confirmed in-the-wild exploitation; vendor has released patched builds and mitigation guidance.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure Zero-Day Chain
- **Description**: Two previously unknown vulnerabilities in Ivanti Connect Secure / Policy Secure gateways are being chained to execute “MDifyLoader,” which in turn injects Cobalt Strike into memory. Attacks occur pre-authentication over HTTPS.  
- **Impact**: Remote code execution, establishment of persistent backdoors, and lateral movement into internal networks.  
- **Status**: Actively exploited; Ivanti has shipped emergency patches and recommends immediate upgrade or appliance isolation.  

### FIDO2 MFA Downgrade via WebAuthn Cross-Device Flow (PoisonSeed)
- **Description**: PoisonSeed phishers present a QR code that triggers WebAuthn’s cross-device sign-in, coercing victims to approve a secondary (non-FIDO2) push notification. This downgrades authentication strength and bypasses hardware security keys.  
- **Impact**: Full account compromise despite FIDO2 enrollment, enabling email, cloud, or SaaS takeover.  
- **Status**: Ongoing campaign; no vendor patch—users must scrutinize unexpected cross-device prompts and enforce strict FIDO2-only policies.  

### npm Linter Package Account Takeover
- **Description**: Threat actors phished maintainers of “eslint-config-prettier” and “eslint-plugin-prettier,” publishing tainted versions that download and execute malware during post-install scripts.  
- **Impact**: Developers and CI pipelines integrating the packages suffer credential theft and workstation compromise.  
- **Status**: Malicious versions were detected and yanked; clean releases re-published. Users must audit dependency trees and reinstall trusted versions.  

### Malicious Arch Linux AUR Packages Delivering Chaos RAT
- **Description**: Three newly-submitted Arch User Repository packages masqueraded as legitimate utilities but silently installed the CHAOS remote access trojan.  
- **Impact**: Remote control of infected Linux hosts, data theft, and potential participation in botnets.  
- **Status**: Packages removed from AUR; impacted users advised to rebuild systems from trusted sources.  

### Unauthenticated MCP Server Exposure
- **Description**: MCP (agentic AI orchestration) servers default to optional authentication; approximately 2,000 instances were found publicly accessible with no controls in place.  
- **Impact**: Anyone on the internet can issue commands, manipulate AI agents, exfiltrate data, or weaponize compute resources.  
- **Status**: Exploitation confirmed in the wild; administrators must enable authentication and restrict network access immediately.  

## Affected Systems and Products

- **CrushFTP**: Versions prior to the vendor’s latest hotfix; all OS platforms  
- **Ivanti Connect Secure / Policy Secure**: All supported firmware builds prior to emergency patches; physical and virtual appliances  
- **WebAuthn Cross-Device Sign-In**: Chrome, Edge, and other browsers supporting the feature on Windows, macOS, Linux, Android, iOS  
- **eslint-config-prettier & eslint-plugin-prettier (npm)**: Compromised releases published 2025-07-XX  
- **Arch Linux AUR Packages (3 malicious entries)**: All Linux distributions installing from AUR  
- **MCP Servers**: Self-hosted agentic AI infrastructures where authentication remains disabled  

## Attack Vectors and Techniques

- **Authentication Downgrade Phishing**: QR-code–based social engineering forces users into weaker MFA flows.  
- **Pre-Auth Remote Code Execution**: Direct exploitation of web interfaces (CrushFTP, Ivanti) without valid credentials.  
- **Supply-Chain Package Poisoning**: Hijacked maintainer accounts publish malicious updates (npm, AUR).  
- **In-Memory Beacon Injection**: MDifyLoader decrypts and runs Cobalt Strike payloads entirely in RAM to evade disk forensics.  
- **Unauthenticated API Abuse**: Open MCP endpoints allow arbitrary command execution and configuration changes.  

## Threat Actor Activities

- **PoisonSeed**: Conducting large-scale phishing aimed at enterprise users with FIDO2 keys; targets include corporate email and cloud portals.  
- **Unknown Supply-Chain Actor**: Hijacked popular npm linter libraries; goal appears to be broad malware distribution to developer environments.  
- **Chaos RAT Operators**: Leveraged Arch Linux AUR to infiltrate Linux users and build a cross-platform botnet.  
- **Unattributed CrushFTP Exploiters**: Rapid mass-scanning and exploitation of vulnerable servers globally, likely for data theft and ransomware staging.  
- **MDifyLoader Group**: Using Ivanti zero-days to implant Cobalt Strike in government and enterprise networks across multiple regions.  
- **APT28 (Fancy Bear)**: Running “Authentic Antics” malware to harvest Microsoft 365 credentials, primarily against UK entities, leveraging spear-phishing and malicious OAuth apps.  
- **Opportunistic MCP Abusers**: Grey-hat and criminal actors enumerating and commandeering unsecured MCP servers for AI-enabled tasks and resource hijacking.  

**End of Report**