# Exploitation Report

A critical zero-day vulnerability chain in Microsoft SharePoint is currently being weaponized in the wild by state-sponsored and financially motivated threat actors. First observed on 7 July 2025 and still unpatched at the time of reporting, the flaw allows attackers to execute the “ToolShell” implant, exfiltrate authentication keys, and maintain long-term persistence in on-premises and cloud-connected SharePoint environments. Chinese nation-state operators are leading the campaigns, while Check Point Research and Microsoft telemetry confirm broad, automated probing of Internet-exposed SharePoint servers across multiple sectors worldwide.

## Active Exploitation Details

### Microsoft SharePoint Zero-Day “ToolShell” Vulnerability Chain  
- **Description**: A chain of previously unknown vulnerabilities in Microsoft SharePoint that enables unauthenticated attackers to upload a malicious file, trigger server-side code execution, and deploy the post-exploitation framework “ToolShell.”  
- **Impact**: Full remote code execution on the SharePoint server; credential theft (including Azure AD application keys), establishment of reverse shells, lateral movement into adjoining Windows infrastructure, and long-term persistence through scheduled tasks and modified service binaries.  
- **Status**: Confirmed active exploitation since 7 July 2025. Microsoft has not yet issued a security update; mitigations involve removing public exposure, enforcing strict upload filters, and applying least-privilege configurations.  

## Affected Systems and Products

- **Microsoft SharePoint Server 2016 / 2019 / Subscription Edition**  
  - **Platform**: On-premises Windows Server deployments and hybrid cloud environments integrated with Azure AD  
- **SharePoint-connected Windows Server hosts** (Domain controllers, file servers used for lateral movement)  
  - **Platform**: Windows Server 2019, 2022  

## Attack Vectors and Techniques

- **Unauthenticated File Upload RCE**  
  - **Vector**: Crafted HTTP POST requests to a vulnerable SharePoint endpoint allow the upload of weaponized ASPX pages, which are then executed to run arbitrary PowerShell.  
- **ToolShell Post-Exploitation Framework**  
  - **Vector**: PowerShell-based implant establishes reverse HTTPS beacons, conducts credential harvesting, and registers scheduled tasks for persistence.  
- **Credential & Key Theft**  
  - **Vector**: Extracts Azure AD application keys and on-premises service accounts to facilitate cloud pivoting and long-term tenant access.  

## Threat Actor Activities

- **Actor/Group**: Suspected Chinese state-sponsored cluster (overlaps with APT41 infrastructure)  
  - **Campaign**: Mass exploitation of SharePoint servers to deploy ToolShell, targeting government, defense, and manufacturing organizations on several continents, including newly observed activity in Africa.  

- **Actor/Group**: Financially motivated crimeware operators (unattributed)  
  - **Campaign**: Opportunistic scanning of Internet-facing SharePoint portals, dropping crypto-mining payloads and infostealers after successful RCE.  

