# Exploitation Report

The past week’s telemetry and open-source reporting highlight renewed, in-the-wild exploitation attempts against Progress MOVEit Transfer instances, with adversaries mass-scanning the Internet to revive last year’s supply-chain ransomware playbook. While several other critical vulnerabilities were disclosed—most notably two unauthenticated RCE bugs in Cisco Identity Services Engine (ISE) and a default-credential flaw impacting 689 Brother printer models—the MOVEit SQL-injection chain remains the only issue confirmed to be under active attack. Concurrently, state-aligned and financially motivated actors are abusing living-off-the-land features (Microsoft 365 Direct Send, Microsoft ClickOnce) and fake-software websites to deliver bespoke RATs and rootkits, underscoring the growing blend of social engineering and post-exploitation toolsets instead of pure n-day vulnerability abuse.

## Active Exploitation Details

### Progress MOVEit Transfer SQL-Injection Chain
- **Description**: A set of SQL-injection vulnerabilities in Progress MOVEit Transfer that allow unauthenticated attackers to execute arbitrary SQL statements, achieve remote code execution, and exfiltrate stored files.  
- **Impact**: Full compromise of MOVEit instances, lateral movement into connected storage back-ends, and large-scale data theft leading to extortion and ransomware deployment.  
- **Status**: GreyNoise and other sensors report a surge in automated scanning beginning 27 May 2025, indicating renewed, widespread exploitation attempts. Patches are available from Progress; unpatched servers remain highly vulnerable.  
<!-- No CVE line because the article did not enumerate specific CVE IDs -->

## Affected Systems and Products

- **Progress MOVEit Transfer**  
  - Versions prior to the latest security hotfix (on-prem and cloud)  
  - Platform: Windows Server deployments exposed to the Internet  

- **Cisco Identity Services Engine (ISE) & ISE-Passive Identity Connector (ISE-PIC)**  
  - Versions prior to Cisco’s June 2025 security update that fixes two max-severity RCE flaws  
  - Platform: Virtual appliances and hardware appliances on corporate networks  

- **Brother Printers (689 models)**  
  - Firmware shipped with predictable default administrative passwords  
  - Platform: Network-attached printers in enterprise and SMB environments  

- **Open VSX Registry (open-vsx.org)**  
  - Supply-chain registry for VS Code extensions before the recent patch  
  - Platform: Cloud service used by developer IDEs  

- **Microsoft 365 Tenants**  
  - Any tenant where “Direct Send” is enabled without additional mail-flow controls  
  - Platform: Microsoft Exchange Online  

- **Windows Endpoints**  
  - Systems leveraging Microsoft ClickOnce deployments without application control  
  - Platform: Windows 10/11 in enterprise environments  

## Attack Vectors and Techniques

- **Automated Internet Scanning**  
  - Vector: Mass scanning for MOVEit Transfer endpoints on ports 80/443, followed by scripted SQL injection.  

- **Phishing via Microsoft 365 Direct Send**  
  - Vector: Attackers authenticate to compromised accounts and use “smtp.office365.com” to deliver emails that bypass secure-email gateways by appearing as internal traffic.  

- **ClickOnce Abuse (“OneClik” Campaign)**  
  - Vector: Malicious `*.application` files hosted on attacker-controlled domains trigger silent installation of Golang backdoors once a user clicks a link.  

- **Fake Software Distribution Sites (Silver Fox)**  
  - Vector: Look-alike domains serving trojanized installers (WPS Office, Sogou, DeepSeek) that side-load the Sainbox RAT and a BYOVD-style Hidden rootkit.  

- **Default-Credential Harvesting (Brother Printers)**  
  - Vector: Remote attackers generate predictable admin passwords based on printer serials, enabling full device takeover across the network.  

## Threat Actor Activities

- **Silver Fox (PRC-linked)**  
  - Campaign: Fake-software websites distributing Sainbox RAT and Hidden rootkit to Chinese-language users; likely initial foothold for espionage.  

- **OneClik Operators (Energy-Sector Targeting)**  
  - Campaign: Phishing emails weaponizing ClickOnce to deploy custom Golang backdoors inside power-generation and oil-service firms across EMEA.  

- **Unnamed Actors Reviving MOVEit Exploits**  
  - Campaign: Surge in scanning for MOVEit Transfer; objective presumed data theft and ransomware similar to 2023 Cl0p operations. Targeting unpatched public-facing servers worldwide.  

- **Cyber Criminal Clusters in Africa-Focused Campaigns**  
  - Campaign: Leveraging open-source post-exploitation frameworks to infiltrate financial institutions in at least nine African nations; rely on credential phishing and commodity RATs post-intrusion.  

- **APT35 (Iran)**  
  - Campaign: AI-augmented spear-phishing against Israeli tech analysts; uses lure documents but no current exploitation of software flaws observed—focus on credential theft and social engineering.  

---

By prioritizing remediation of exposed MOVEit Transfer servers, applying Cisco’s latest patches, disabling unnecessary Microsoft 365 “Direct Send” pathways, and rotating default credentials on embedded devices, defenders can significantly reduce risk from the most pressing exploitation trends outlined above.