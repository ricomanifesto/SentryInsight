# Exploitation Report

Ongoing attacks are leveraging multiple enterprise-grade vulnerabilities, headlined by two distinct Microsoft SharePoint zero-days that adversaries are chaining for remote code execution and data theft. One of the flaws remains unpatched, forcing defenders to rely on temporary mitigations while Microsoft races to deliver a fix. Concurrently, threat actors are weaponizing two newly disclosed SysAid ITSM vulnerabilities to hijack privileged administrator sessions inside corporate help-desk environments, and a revamped “Coyote” banking trojan is abusing the Windows UI Automation framework to harvest credentials without triggering traditional security controls. The intersection of these exploits underscores an elevated risk to organizations running exposed collaboration platforms, IT service software, or unmanaged Windows endpoints.

## Active Exploitation Details

### Microsoft SharePoint Zero-Day #1 (Patched)
- **Description**: A remote code execution flaw in SharePoint Server enabling attackers to upload a specially crafted file that is executed in the context of the SharePoint service account.  
- **Impact**: Full server compromise, lateral movement into Microsoft 365 and on-prem AD environments, and exfiltration of stored SharePoint data.  
- **Status**: Confirmed in-the-wild exploitation; Microsoft has issued a security update.  
- **CVE ID**: CVE-2025-XXXXX   <!-- include only if article provided; remove if none -> we'll omit due to unknown -->

### Microsoft SharePoint Zero-Day #2 (Unresolved)
- **Description**: A privilege-escalation vulnerability allowing authenticated users to gain SYSTEM-level privileges on SharePoint servers.  
- **Impact**: Attackers chaining with RCE achieve complete takeover of SharePoint farms, enabling persistence and deployment of web shells.  
- **Status**: Active exploitation reported; no permanent patch released. Microsoft advises disabling vulnerable components and tightening firewall rules.  

### SysAid ITSM Authentication-Bypass & Path-Traversal Flaws
- **Description**: Two separate weaknesses in SysAid’s on-prem IT service management platform—one bypasses authentication controls, the other allows path traversal leading to arbitrary file upload.  
- **Impact**: Unauthenticated attackers can create or hijack administrator accounts, execute malicious code, and pivot to internal assets handled by the help-desk system.  
- **Status**: CISA confirms active exploitation; vendor patches available in latest SysAid release.  

### Windows UI Automation Abuse (Coyote Malware)
- **Description**: The Coyote banking trojan leverages Microsoft’s UI Automation (UIA) accessibility interface to invisibly interact with banking windows, capture credentials, and manipulate transactions.  
- **Impact**: Stealthy theft of banking usernames, passwords, and MFA tokens; bypass of browser-based anti-fraud extensions.  
- **Status**: In-the-wild deployment of new Coyote variant; no vendor patch (abuses legitimate OS functionality). Defenders must rely on behavior-based detection.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2019 / Subscription Edition**  
  - **Platform**: On-prem Windows Server deployments exposed to the Internet or internal users.  

- **SysAid ITSM (on-prem editions prior to latest security release)**  
  - **Platform**: Windows-based and Linux-based servers hosting the SysAid service.  

- **Windows 10 & 11 endpoints (all builds)**  
  - **Platform**: Any workstation where users can be lured to run the Coyote trojan; exploitation occurs post-infection via UI Automation.  

## Attack Vectors and Techniques

- **Malicious File Upload (SharePoint RCE)**  
  - **Vector**: Crafted SharePoint package uploaded through the web interface triggers server-side code execution.  

- **Privilege Escalation via Service Account Manipulation (SharePoint)**  
  - **Vector**: Abuse of vulnerable SharePoint component to escalate from authenticated user to SYSTEM.  

- **Unauthenticated REST/API Calls (SysAid)**  
  - **Vector**: Attacker sends specially formed API requests to create admin accounts, bypassing login checks.  

- **Arbitrary File Upload & Path Traversal (SysAid)**  
  - **Vector**: Crafted paths allow dropping web shells outside the intended upload directory.  

- **UI Automation Hijacking (Coyote)**  
  - **Vector**: Malware hooks UIA event listeners to scrape credentials and issue hidden UI commands.  

- **Kerberoasting**  
  - **Vector**: Attackers request service tickets for vulnerable SPNs, then brute-force encrypted blobs offline to recover service account passwords, facilitating lateral movement.  

## Threat Actor Activities

- **Multiple Chinese Nation-State Groups**  
  - **Campaign**: Coordinated exploitation of both SharePoint zero-days to breach Western government and defense contractors, followed by data exfiltration and credential harvesting.  

- **Unidentified Threat Actors Exploiting SysAid**  
  - **Campaign**: Post-compromise deployment of web shells on help-desk servers, enabling ransomware staging and privilege escalation within enterprise networks.  

- **Coyote Malware Operators (Financially Motivated)**  
  - **Campaign**: Targeting Latin American and European online-banking customers; leveraging UI Automation to bypass anti-fraud controls and perform fraudulent transfers.  

- **Red-Team & Pen-Test Imitators**  
  - **Campaign**: Surge in Kerberoasting usage observed in recent penetration tests, mirroring real-world tactics for privilege escalation inside Active Directory domains.  

