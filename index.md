# Exploitation Report

An intense wave of exploitation activity is unfolding across several widely-used enterprise platforms. The most urgent development is Microsoft’s disclosure of multiple SharePoint zero-days, including the actively exploited “ToolShell” flaw (CVE-2025-53770), which attackers are leveraging to gain remote code-execution inside government and corporate environments. Simultaneously, over a thousand Internet-facing CrushFTP servers are being hijacked through a critical authentication-bypass bug that hands over full admin control. Google Chrome, NVIDIA’s developer toolkit, and ExpressVPN’s Windows client all received emergency fixes after in-the-wild abuses or real-world exposure scenarios were uncovered. These exploits are being weaponized by state-aligned groups such as China’s APT41 and Iran-linked operators deploying DCHSpy malware, underscoring the heightened risk to unpatched systems.

## Active Exploitation Details

### SharePoint “ToolShell” Remote Code Execution
- **Description**: A zero-day vulnerability in Microsoft SharePoint that allows attackers to execute arbitrary PowerShell commands (“ToolShell”) via specially crafted API requests.  
- **Impact**: Full remote code-execution on SharePoint servers, permitting installation of web shells, lateral movement, and data exfiltration.  
- **Status**: Actively exploited in the wild; Microsoft released an out-of-band patch.  
- **CVE ID**: CVE-2025-53770  

### SharePoint Server Emergency Zero-Day (July 20 Patch)
- **Description**: Another SharePointServer flaw disclosed by Microsoft in an emergency update that attackers are using to compromise organizations before patch deployment.  
- **Impact**: Allows privilege escalation and takeover of SharePoint farms, enabling credential theft and access to hosted documents.  
- **Status**: Exploitation observed; patches issued for recent SharePoint versions, while 2016 builds remain at heightened risk.  

### CrushFTP Administrative Hijack Vulnerability
- **Description**: A critical flaw in CrushFTP that lets unauthenticated attackers bypass login controls and seize admin access to the web interface.  
- **Impact**: Complete takeover of file-transfer servers, exposure or alteration of corporate data, and installation of malicious plugins.  
- **Status**: More than 1,000 vulnerable instances are currently being hijacked; a vendor patch is available.  

### Google Chrome Zero-Day Exploit
- **Description**: A high-severity vulnerability in Chrome being exploited to escape the browser sandbox.  
- **Impact**: Attackers can execute code on the underlying OS after a user visits a malicious site.  
- **Status**: Google has pushed a security update; exploitation was confirmed before the fix.  

### NVIDIA Toolkit Remote Code Execution
- **Description**: A vulnerability in NVIDIA’s developer toolkit that allows remote execution of code through malicious project files or network calls.  
- **Impact**: Compromise of developer workstations and potential pivot into build environments.  
- **Status**: Active exploitation observed; patches have been released by NVIDIA.  

### ExpressVPN RDP Traffic Leak
- **Description**: A flaw in ExpressVPN’s Windows client caused Remote Desktop Protocol traffic to bypass the VPN tunnel, revealing users’ real IP addresses.  
- **Impact**: De-anonymisation of users, enabling tracking or geo-location of sensitive RDP sessions.  
- **Status**: Fixed in the latest Windows client update; users must upgrade to regain full tunnel protection.  

## Affected Systems and Products

- **Microsoft SharePoint Server (2016, 2019, Subscription Edition, Online)**  
  Platform: Windows Server on-prem & cloud deployments  

- **CrushFTP (multiple versions prior to latest hotfix)**  
  Platform: Cross-platform Java application on Windows, Linux, macOS  

- **Google Chrome (desktop builds prior to emergency channel release)**  
  Platform: Windows, macOS, Linux  

- **NVIDIA Developer Toolkit (affected toolkit versions before vendor patch)**  
  Platform: Windows and Linux developer workstations  

- **ExpressVPN Windows Client (builds preceding the current patched release)**  
  Platform: Windows 10/11 endpoints  

## Attack Vectors and Techniques

- **Web-Shell Deployment via SharePoint API Abuse**  
  Vector: Crafted HTTP requests exploit SharePoint parsing logic to invoke PowerShell (“ToolShell”).  

- **Authentication Bypass over HTTP/S on CrushFTP**  
  Vector: Manipulated session tokens or path traversal grants direct access to `/WebInterface/`.  

- **Browser Exploit / Sandbox Escape**  
  Vector: Malicious JavaScript embedded in webpages triggers the Chrome zero-day to break out of the renderer process.  

- **Malicious Project File Execution in NVIDIA Toolkit**  
  Vector: Weaponised project files trigger vulnerable parsing routines, leading to RCE on import.  

- **VPN Tunnel Evasion**  
  Vector: RDP traffic defaults to the physical NIC due to routing flaw, exposing real IP addresses despite active VPN tunnel.  

## Threat Actor Activities

- **APT41 (China-Linked)**  
  Campaign: Targeted espionage against African government IT infrastructure, leveraging hard-coded internal hostnames and likely piggy-backing on unpatched enterprise software (including SharePoint).  

- **Iranian MOIS-Aligned Operators**  
  Campaign: Distribution of “DCHSpy” Android malware disguised as VPN applications to surveil dissidents; infrastructure overlaps observed with previous state campaigns.  

- **Unnamed Actors Exploiting SharePoint ‘ToolShell’**  
  Campaign: Broad intrusion set targeting U.S. government agencies and private sector networks by chaining the SharePoint zero-day with post-exploitation tooling.  

- **CrushFTP Hijackers**  
  Campaign: Opportunistic mass scanning of Internet-exposed CrushFTP servers, followed by admin takeover and data exfiltration.  

