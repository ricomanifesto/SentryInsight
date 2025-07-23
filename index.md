# Exploitation Report

Ongoing, in-the-wild exploitation of two critical Microsoft SharePoint Server flaws (CVE-2025-49704 and CVE-2025-49706) dominates the current threat landscape. U.S. CISA has issued an emergency directive placing both bugs on its Known Exploited Vulnerabilities catalog after Microsoft and independent researchers confirmed successful compromises of Internet-facing SharePoint servers. Microsoft has attributed the activity to multiple Chinese nation-state operators (Linen Typhoon, Violet Typhoon, and an additional unnamed group), while Dark Reading notes a wider “feeding frenzy” among criminal actors now weaponizing the same bugs. Concurrently, financially-motivated malware crews—including the resurging Lumma infostealer gang and operators of the Coyote banking trojan—are leveraging novel abuse of Windows features (e.g., UI Automation) for post-exploit data theft, and Interlock ransomware affiliates continue to intensify double-extortion operations. Rapid patching and immediate threat-hunting on SharePoint estates are therefore paramount.

## Active Exploitation Details

### Microsoft SharePoint Server Remote Code Execution – CVE-2025-49704
- **Description**: A remote code execution flaw in on-premises Microsoft SharePoint Server allowing unauthenticated attackers to execute arbitrary code by sending crafted requests to vulnerable endpoints.
- **Impact**: Full compromise of SharePoint sites, lateral movement into connected networks, and potential data exfiltration or deployment of ransomware.
- **Status**: Actively exploited in the wild; emergency patches released by Microsoft and mandated by CISA.
- **CVE ID**: CVE-2025-49704

### Microsoft SharePoint Server Privilege Escalation – CVE-2025-49706
- **Description**: A privilege-escalation vulnerability enabling authenticated low-privilege users (or code running under compromised service accounts) to obtain SYSTEM-level permissions on SharePoint hosts.
- **Impact**: Elevation to administrative control, facilitating deployment of additional payloads or disabling security controls after initial RCE.
- **Status**: Confirmed live exploitation alongside CVE-2025-49704; fixes available from Microsoft and required under CISA’s KEV mandate.
- **CVE ID**: CVE-2025-49706

### Windows UI Automation Framework Abuse
- **Description**: Coyote banking-trojan operators abuse Microsoft’s legitimate UI Automation accessibility interface to programmatically detect when victims visit banking or cryptocurrency sites, bypassing traditional DOM-based detection.
- **Impact**: Targeted credential harvesting and session hijacking without relying on browser exploits, reducing detection by security tools.
- **Status**: Observed in active campaigns; no patch (abuse of legitimate feature). Mitigations include hardening application whitelisting and behavioral monitoring.

## Affected Systems and Products

- **Microsoft SharePoint Server 2019/2016/Subscription Edition**  
  - **Platform**: On-premises Windows Server installations exposed to the Internet  
- **Microsoft Windows (all supported desktop & server builds)**  
  - **Platform**: UI Automation abuse affects any Windows environment where the trojan executes  
- **Enterprise endpoints running unpatched Microsoft Office ecosystems**  
  - **Platform**: Targeted for subsequent lateral movement after initial SharePoint compromise  

## Attack Vectors and Techniques

- **Crafted SharePoint HTTP Request RCE**  
  - **Vector**: Unauthenticated call to vulnerable SharePoint API endpoint triggers deserialization leading to code execution.  
- **Privilege Escalation via SharePoint Service Misconfiguration**  
  - **Vector**: Malicious payload leverages CVE-2025-49706 to move from service context to SYSTEM.  
- **Living-off-the-Land Abuse of UI Automation**  
  - **Vector**: Malware invokes UIA APIs to enumerate window titles and DOM elements, stealing credentials when banking portals are detected.  
- **Post-Exploit Malware Deployment**  
  - **Vector**: Threat actors drop Lumma or Coyote loaders, then exfiltrate data or deploy Interlock ransomware for double-extortion.  

## Threat Actor Activities

- **Linen Typhoon (China)**  
  - **Campaign**: Coordinated exploitation of SharePoint servers since 7 July 2025 for espionage and credential theft.  
- **Violet Typhoon (China)**  
  - **Campaign**: Parallel operations focusing on governmental and defense contractors’ SharePoint sites, implanting custom web-shells.  
- **Third Chinese Nation-State Group (unnamed)**  
  - **Campaign**: Observed by Dark Reading scanning for the same SharePoint endpoints, expanding target scope to education and manufacturing.  
- **Lumma Infostealer Operators**  
  - **Campaign**: Reconstituted infrastructure after May takedown; pivoting off compromised SharePoint machines to mass-exfiltrate browser tokens.  
- **Coyote Banking-Trojan Operators**  
  - **Campaign**: New variant integrates UI Automation spying, primarily targeting Latin-American financial institutions.  
- **Interlock Ransomware Affiliates**  
  - **Campaign**: Surge in double-extortion incidents, leveraging credentials obtained via SharePoint breaches or infostealer logs to gain initial foothold.