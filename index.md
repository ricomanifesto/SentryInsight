# Exploitation Report

A surge of high-impact exploitation activity is unfolding across multiple layers of the technology stack. Threat actors are concurrently abusing an authenticated-bypass zero-day in CrushFTP (CVE-2025-54309), leveraging still-unpatched flaws in Ivanti Connect Secure and Policy Secure gateways, and weaponising software-supply chains by hijacking popular JavaScript “linter” libraries as well as Arch Linux AUR packages to deliver remote-access malware. In parallel, the “PoisonSeed” phishing operation is dismantling FIDO2 protections by downgrading WebAuthn authentication flows, while Russia-linked APT28 is exfiltrating Microsoft 365 credentials with its newly attributed “Authentic Antics” malware. Collectively, these campaigns enable full server takeover, credential theft, and covert persistence inside enterprise environments, underscoring the need for immediate patching, package integrity validation, and hardened MFA roll-outs.

## Active Exploitation Details

### CrushFTP Web Interface Admin Bypass  
- **Description**: A zero-day flaw in CrushFTP’s web interface allows crafted HTTP requests to bypass authentication controls and gain administrative privileges.  
- **Impact**: Full administrative takeover, arbitrary file read/write, and potential lateral movement across networks hosting vulnerable instances.  
- **Status**: Actively exploited in the wild; vendor shipped emergency patches and upgrade instructions.  
- **CVE ID**: CVE-2025-54309  

### Ivanti Connect Secure / Policy Secure Zero-Days  
- **Description**: Two newly discovered vulnerabilities in the gateway’s web components enable attackers to chain an authentication-bypass with a command-injection, achieving remote code execution without valid credentials.  
- **Impact**: Deployment of MDifyLoader malware followed by in-memory Cobalt Strike beacons, facilitating persistence, data exfiltration, and later movement.  
- **Status**: Exploits observed in active campaigns; interim mitigations available while formal patches are pending.  

### FIDO2 MFA Downgrade (“PoisonSeed”)  
- **Description**: The campaign abuses WebAuthn’s cross-device sign-in feature to coerce victims into scanning a malicious QR code that downgrades FIDO2 security-key authentication to a less secure mechanism the attacker can relay.  
- **Impact**: Account takeover on cloud services protected by FIDO2 keys, defeating phishing-resistant MFA.  
- **Status**: Ongoing phishing waves; no vendor patch applicable—mitigations focus on user awareness and enforcing security-key-only flows.  

### npm Linter Package Hijacking  
- **Description**: Maintainer accounts for “eslint-config-prettier” and “eslint-plugin-prettier” were compromised via targeted phishing, and malicious versions were published that fetch secondary payloads at install-time.  
- **Impact**: Supply-chain malware deployment on developer workstations and CI/CD environments, leading to credential theft and potential backdoor insertion into downstream projects.  
- **Status**: Malicious versions yanked by npm; clean releases restored. Users must audit dependency trees and rotate secrets.  

### Arch Linux AUR Chaos RAT Packages  
- **Description**: Three malicious AUR packages were uploaded that executed install-time scripts to drop the CHAOS remote-access trojan on Linux hosts.  
- **Impact**: Full remote control of affected systems, including file exfiltration and command execution.  
- **Status**: Packages removed from AUR; impacted users advised to reinstall from trusted sources and purge malicious artifacts.  

### “Authentic Antics” Microsoft 365 Credential Theft  
- **Description**: APT28’s malware leverages malicious OAuth applications and stealthy HTTP beacons to harvest Microsoft 365 credentials from targeted organisations.  
- **Impact**: Access to mailboxes, SharePoint data, and potential impersonation within supply chains.  
- **Status**: Active espionage operation; defenders urged to audit OAuth consent and enforce conditional access policies.  

## Affected Systems and Products

- **CrushFTP Server 9.x / 10.x**  
  - **Platform**: Cross-platform Java server (Windows, Linux, macOS)

- **Ivanti Connect Secure & Policy Secure VPN Gateways**  
  - **Platform**: Proprietary network appliances (all firmware prior to forthcoming patch)

- **WebAuthn-enabled SaaS & Identity Platforms using FIDO2 Keys**  
  - **Platform**: Browser-based cross-device sign-in workflows (Windows, macOS, Linux, Mobile)

- **npm Packages “eslint-config-prettier” (v9.0.0 series) and “eslint-plugin-prettier” (compromised build)**  
  - **Platform**: Node.js development environments, CI/CD pipelines

- **Arch Linux AUR – three malicious community packages (names redacted by Arch advisory)**  
  - **Platform**: Arch Linux distributions utilizing the affected AUR helpers

- **Microsoft 365 Tenants (Exchange Online, SharePoint, OneDrive)**  
  - **Platform**: Cloud SaaS

## Attack Vectors and Techniques

- **Zero-Day Exploitation (CrushFTP, Ivanti)**  
  - **Vector**: Direct HTTP(S) requests to vulnerable web interfaces, bypassing auth and invoking command injection.

- **Supply-Chain Package Poisoning (npm, AUR)**  
  - **Vector**: Compromised maintainer credentials → malicious package publish → automatic installation scripts download payloads.

- **MFA Downgrade Phishing (PoisonSeed)**  
  - **Vector**: Email delivers HTML page with QR code → user scans on mobile → WebAuthn cross-device channel abused to request weaker auth.

- **OAuth Application Abuse (Authentic Antics)**  
  - **Vector**: Victim consents to rogue Azure AD app → app retrieves refresh tokens → covert API calls harvest mailbox contents.

- **In-Memory Post-Exploit Tooling (MDifyLoader & Cobalt Strike)**  
  - **Vector**: Loader reflectively injects beacon into process memory, evading disk-based detection.

## Threat Actor Activities

- **PoisonSeed Operators**  
  - **Campaign**: Large-scale phishing targeting enterprise FIDO2 deployments; focuses on Microsoft and Google account ecosystems.

- **Unknown Supply-Chain Actor (npm incident)**  
  - **Campaign**: Maintainer impersonation via phishing, rapid publication of malware-laden releases, aiming at developer environments.

- **Malicious AUR Contributor(s)**  
  - **Campaign**: Uploaded trojanised packages to infect Arch Linux users with Chaos RAT for botnet expansion.

- **Unidentified Actor Exploiting CrushFTP**  
  - **Campaign**: Opportunistic mass scanning of port-exposed CrushFTP instances followed by privilege escalation and data theft.

- **UNG0002**  
  - **Campaign**: Parallel LNK/RAT operations in China, Hong Kong, and Pakistan; leverages commodity RATs for espionage.

- **APT28 (Fancy Bear, Russian GRU)**  
  - **Campaign**: “Authentic Antics” attacks on government and defence sectors to steal Microsoft 365 credentials, maintain long-term access, and exfiltrate sensitive documents.

- **Post-Exploitation Operators (Ivanti)**  
  - **Campaign**: Use of MDifyLoader and Cobalt Strike to pivot from compromised VPN gateways into internal networks, indicating possible ransomware preparation or espionage.

---

**End of Report**