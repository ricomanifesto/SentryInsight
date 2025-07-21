# Exploitation Report

A wave of highly coordinated attacks is currently leveraging multiple zero-day and recently patched vulnerabilities to compromise enterprise infrastructure worldwide. Most notable is an on-going exploitation campaign dubbed “ToolShell,” which is abusing two remote-code-execution flaws in Microsoft SharePoint Server (CVE-2025-53770 and CVE-2025-53771). The intrusions have already hit U.S. government agencies and numerous private-sector organizations, prompting an emergency, out-of-band patch cycle from Microsoft. Simultaneously, more than 1,000 Internet-facing CrushFTP instances are under active hijack attempts through a critical authentication-bypass bug that grants full administrator access. These activities are accompanied by sophisticated social-engineering tactics—such as PoisonSeed’s QR-code phishing that downgrades FIDO protections—and mass web-cryptojacking operations compromising thousands of sites. The combination of server-side RCEs and innovative credential-theft techniques underscores the urgent need for rapid patching, rigorous hardening, and continuous monitoring across all exposed assets.

## Active Exploitation Details

### SharePoint ‘ToolShell’ Remote Code Execution
- **Description**: A server-side RCE vulnerability in Microsoft SharePoint that allows attackers to execute arbitrary code via crafted API requests, frequently dropping a post-exploitation toolkit referred to as “ToolShell.”  
- **Impact**: Full takeover of SharePoint servers, lateral movement into internal networks, data theft, and the ability to deploy persistent web shells.  
- **Status**: Actively exploited in global attacks; Microsoft issued emergency fixes for SharePoint Server 2019 and 2022. SharePoint 2016 remains vulnerable pending further guidance.  
- **CVE ID**: CVE-2025-53770  

### SharePoint Secondary RCE Vulnerability
- **Description**: A distinct RCE flaw in SharePoint exposed alongside CVE-2025-53770, enabling execution of malicious code through improper input validation in SharePoint’s workflow components.  
- **Impact**: Same level of server compromise as the primary ToolShell bug, often chained for privilege escalation and broader persistence.  
- **Status**: Confirmed in active exploitation; patched in the same out-of-band update cycle released on July 20.  
- **CVE ID**: CVE-2025-53771  

### CrushFTP Administrative Hijack Vulnerability
- **Description**: A critical security bug in CrushFTP that lets remote attackers bypass authentication and seize administrative control of the web interface using specially crafted requests.  
- **Impact**: Attackers obtain full admin privileges, exfiltrate hosted data, upload malicious files, and pivot deeper into the victim environment.  
- **Status**: Ongoing mass exploitation with more than 1,000 vulnerable servers detected online; vendor patches are available and urgently recommended.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019 / 2022 (fully on-prem or hybrid)**  
  - **Platform**: Windows Server installations hosting SharePoint farms  
- **Microsoft SharePoint Server 2016**  
  - **Platform**: Windows Server; currently lacks official fix—mitigations only  
- **CrushFTP Server versions prior to latest hotfix**  
  - **Platform**: Cross-platform (Windows, Linux, macOS) deployments exposed to the Internet  

## Attack Vectors and Techniques

- **Crafted SharePoint API Requests**  
  - **Vector**: HTTP/S calls to vulnerable SharePoint `_layouts` endpoints inject malicious payloads that spawn `cmd.exe` or PowerShell, installing “ToolShell.”  
- **Authentication Bypass via Path Manipulation (CrushFTP)**  
  - **Vector**: Manipulated web requests exploit insufficient path sanitization to hijack active admin sessions without credentials.  
- **QR-Code Phishing & Cross-Device Sign-In Abuse (PoisonSeed)**  
  - **Vector**: Victims scan attacker-generated QR codes, downgrading FIDO protections and approving rogue sign-in requests on secondary devices.  
- **Stealth JavaScript WebSocket Cryptojacking**  
  - **Vector**: Injected obfuscated JS initiates WebSocket tunnels to mining pools, covertly using visitor CPU cycles across 3,500 compromised sites.  

## Threat Actor Activities

- **Unknown ToolShell Operators**  
  - **Campaign**: Systematic exploitation of SharePoint zero-days targeting U.S. government entities and global enterprises; deployment of custom post-exploitation toolkit; emphasis on persistence and credential dumping.  
- **PoisonSeed Group**  
  - **Campaign**: QR-code phishing attacks focused on bypassing hardware-based FIDO keys, primarily aiming at corporate users reliant on passwordless authentication.  
- **Cryptojacking Syndicate (Unnamed)**  
  - **Campaign**: Mass compromise of over 3,500 websites to embed JavaScript miners, leveraging WebSocket evasion to maintain low detection profiles.  

**Bold, immediate action**—including patch application, exposure reduction, and enhanced monitoring—is essential to disrupt these active exploitation waves before they escalate further.