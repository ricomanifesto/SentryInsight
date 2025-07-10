# Exploitation Report

During the past week, threat intelligence highlights one particularly concerning exploitation wave: the Gold Melody initial-access broker is actively abusing exposed **ASP.NET Machine Keys** to forge authentication cookies and seize footholds inside enterprise environments, selling that access to other threat actors. While several other critical vulnerabilities came to light—such as a container-escape flaw in the **NVIDIA Container Toolkit**, the unpatched Ruckus SmartZone/Virtual SmartZone weaknesses, and a newly-disclosed **ServiceNow “Count(er) Strike”** information-disclosure bug—no confirmed in-the-wild exploitation has been reported for those yet. Security teams should therefore prioritize mitigations for the Gold Melody technique while preparing patches or compensating controls for the other high-impact issues.

## Active Exploitation Details

### Exposed ASP.NET Machine Keys Abuse
- **Description**: Publicly accessible or leaked ASP.NET `machineKey` values allow attackers to generate valid authentication cookies and ViewState data, effectively bypassing login controls.
- **Impact**: Full account takeover, lateral movement, privilege escalation, and the ability to implant web-shells or sell the resulting access on underground markets.
- **Status**: Actively exploited by the Gold Melody initial-access broker. No patch exists for already-leaked keys; mitigation requires regenerating keys, revoking existing cookies, and auditing public repositories for accidental disclosures.

## Affected Systems and Products

- **Microsoft IIS / ASP.NET Applications**  
  - **Platform**: Windows Server environments hosting .NET web apps with misconfigured or leaked `machineKey` settings  

- **NVIDIA Container Toolkit (nvidia-container-toolkit)**  
  - **Platform**: Linux hosts, Docker/Kubernetes environments running GPU-accelerated workloads  

- **Ruckus SmartZone & Virtual SmartZone Controllers, ZoneDirector, Ruckus One, Unleashed**  
  - **Platform**: Network-management appliances and cloud consoles across wired & wireless infrastructures  

- **ServiceNow SaaS Platform (Count(er) Strike flaw)**  
  - **Platform**: All ServiceNow instances where user table ACLs rely on record-level security  

## Attack Vectors and Techniques

- **Machine-Key Cookie Forgery**  
  - **Vector**: Using leaked `machineKey` to sign forged `.ASPXAUTH` cookies and encrypted ViewState blobs, granting instant authenticated sessions.  

- **Container Escape via NVIDIA Toolkit Misconfiguration**  
  - **Vector**: Crafting a malicious container that abuses the toolkit’s `libnvidia-container` path handling, allowing writes to the host filesystem and breakout to host root.  

- **Unauthenticated Enumeration (Count(er) Strike)**  
  - **Vector**: Leveraging ServiceNow’s `sysparm_display_value` and `sysparm_count` parameters to enumerate restricted table rows without required ACL privileges.  

- **Credential Phishing & MFA Relay (reported trend)**  
  - **Vector**: Real-time phishing sites harvest credentials and OTPs, relaying them to legitimate services to bypass traditional authenticator-app-based MFA.  

## Threat Actor Activities

- **Actor/Group**: **Gold Melody (Initial-Access Broker)**  
  - **Campaign**: Exploiting exposed ASP.NET Machine Keys to obtain persistent administrative sessions inside corporate portals, then auctioning that access on dark-web marketplaces. Targets span multiple industries and geographies.

- **Actor/Group**: **DoNot APT**  
  - **Campaign**: Spear-phishing European foreign-affairs ministries with the “LoptikMod” malware family for data exfiltration. While no specific CVE exploitation was detailed, the group demonstrates continued operational expansion.

- **Actor/Group**: **Andariel (North Korea)**  
  - **Campaign**: U.S. Treasury reports the group leveraged fraudulent IT-worker personas to infiltrate companies and deploy custom malware; associated individual Song Kum Hyok has been sanctioned. No new CVE exploitation outlined, but monetization of illicit access remains active.

- **Actor/Group**: **Unknown (Ruckus-focused scanning activity)**  
  - **Campaign**: Researchers observed mass-scanning for Ruckus SmartZone web interfaces following disclosure of the unpatched RCE/privilege-escalation bugs, indicating reconnaissance prior to probable exploitation.

---

Security teams should immediately audit public code repositories and infrastructure-as-code templates for inadvertent exposure of ASP.NET `machineKey` values, rotate these keys, and invalidate all active sessions. Parallel efforts should include reviewing GPU-enabled container deployments, applying available mitigations from NVIDIA, segmenting or isolating Ruckus management interfaces, and adjusting ServiceNow ACL policies to suppress abusive enumeration.