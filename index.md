# Exploitation Report

During the last week, browser-based zero-days and creative security‐control bypasses have dominated exploitation activity. Attackers are actively leveraging a newly discovered Google Chrome zero-day, abusing Windows’ Mark-of-the-Web (MoTW) logic with a “FileFix” technique that executes unsigned JScript, and slipping malicious extensions past “verified publisher” checks in popular IDEs such as Visual Studio Code. In parallel, a critical remote–code-execution flaw in Anthropic’s MCP Inspector tool has been disclosed, and multiple campaigns show advanced social-engineering—callback phishing with weaponized PDFs, large-scale AI-generated fake login pages, and DLL side-loading against Taiwanese entities. Bulletproof hosting from the sanctioned Aeza Group continues to enable ransomware crews, while threat actors like Scattered Spider, Silver Fox, TA829, and UNK_GreenSec expand targeting across aviation, government, and enterprise sectors.

## Active Exploitation Details

### Google Chrome Zero-Day Rendering Vulnerability  
- **Description**: A flaw in Chrome’s rendering engine allows malicious web content to trigger out-of-bounds memory access, leading to arbitrary code execution in the browser context.  
- **Impact**: Full takeover of the browser session, sandbox escape potential, credential theft, and follow-on malware delivery.  
- **Status**: Confirmed exploitation in the wild; Google has released an emergency update for desktop and mobile channels.  
- **CVE ID**: CVE-2024-XXXX  

### “FileFix” Mark-of-the-Web Bypass (Windows)  
- **Description**: Attackers save weaponized HTML pages locally; when users open them, Windows fails to propagate MoTW metadata to embedded files, enabling unsigned `.jse` / `.js` execution without SmartScreen warnings.  
- **Impact**: Stealth execution of scripts that install backdoors or ransomware, bypassing a key desktop protection control.  
- **Status**: Technique observed in active campaigns; Microsoft has not yet issued a dedicated patch, but mitigation guidance is available.  

### IDE Verified-Publisher Spoofing Weakness  
- **Description**: Weaknesses in the extension-verification pipelines of Visual Studio Code, Visual Studio, IntelliJ IDEA, and Cursor allow attackers to impersonate “verified” publishers and distribute trojanized extensions.  
- **Impact**: Remote code execution on developer workstations, supply-chain insertion of backdoors, credential and source-code theft.  
- **Status**: Proof-of-concept exploit and in-the-wild abuse reported; vendors are rolling out back-end validation improvements and urging users to audit installed extensions.  

### Anthropic MCP Inspector Remote-Code-Execution Vulnerability  
- **Description**: A critical flaw in the Model Context Protocol (MCP) Inspector project lets crafted payloads break out of the inspection sandbox and execute arbitrary commands on host machines.  
- **Impact**: Full system compromise of developer or build-pipeline hosts running MCP Inspector, enabling lateral movement into sensitive AI research environments.  
- **Status**: Public disclosure with patches and work-arounds released; exploitation attempts detected in the wild targeting exposed CI/CD runners.  

## Affected Systems and Products

- **Google Chrome (<= latest pre-patch build)**  
  Platform: Windows, macOS, Linux, Android, iOS  
- **Microsoft Windows 10 & 11 (all builds)**  
  Platform: Desktop environments where users save and reopen HTML files  
- **Visual Studio Code, Visual Studio, IntelliJ IDEA, Cursor (current releases)**  
  Platform: Windows, macOS, Linux developer workstations  
- **Anthropic MCP Inspector (all versions prior to the July hot-fix)**  
  Platform: Developer laptops, build servers, CI/CD pipelines  
- **Mozilla Firefox (users installing “FoxyWallet” extension)**  
  Platform: Windows, macOS, Linux browsers, especially cryptocurrency users  

## Attack Vectors and Techniques

- **Drive-by Compromise via Browser Zero-Day**  
  Vector: Malicious or compromised websites deliver exploit kits that abuse the Chrome rendering vulnerability.  

- **Local-File “FileFix” Exploit**  
  Vector: Phishing emails or Slack/Teams messages deliver ZIP archives with saved HTML pages; opening the page sideloads JScript payloads without MoTW warnings.  

- **Malicious IDE Extension Deployment**  
  Vector: Attackers publish trojanized extensions to official marketplaces under spoofed verified identities; automatic updates push payloads to developers.  

- **Callback Phishing with Weaponized PDFs**  
  Vector: PDFs impersonating Microsoft, DocuSign, and other brands lure targets into calling attacker-controlled numbers where social engineers deliver remote-access tools.  

- **AI-Generated Phishing Pages (Vercel v0 Abuse)**  
  Vector: Threat actors rapidly spin up convincing login portals, host them on free sub-domains, and distribute links via SMS and email.  

- **DLL Side-Loading (Silver Fox / DeepSeek Lure)**  
  Vector: Fake installers place benign executables that load malicious DLLs (Gh0stRAT variant) from the same directory.  

## Threat Actor Activities

- **Scattered Spider**  
  Campaign: Ongoing intrusions into aviation; leveraged social-engineering and cloud-identity abuse to breach Qantas third-party platform, accessing customer data.  

- **Silver Fox**  
  Campaign: Targeted Taiwanese organizations using DeepSeek AI installer lures; delivered Gh0stRAT through DLL side-loading, focusing on espionage.  

- **TA829 & UNK_GreenSec**  
  Campaign: Shared infrastructure distributing RomCom RAT and TransferLoader malware against North-American and European enterprises via phishing.  

- **Bulletproof Hosting – Aeza Group**  
  Activity: Provided resilient infrastructure for ransomware actors and infostealer operators; now sanctioned by OFAC, but still observed hosting C2 nodes.  

- **North Korean IT Worker Scheme**  
  Activity: Thousands of DPRK nationals masquerading as freelance developers inside US companies; laundering funds and siphoning sensitive intellectual property.  

- **Unknown Chrome Zero-Day Exploitation Crew**  
  Activity: Exploiting CVE-2024-XXXX across high-traffic news and entertainment sites to distribute spyware targeting government and corporate employees.  

- **Callback Phish Operators (“PDF Callback” group)**  
  Activity: Brand-impersonation via PDFs; persuading victims to initiate phone calls where remote-support tools are installed for data exfiltration and business-email compromise.  

- **FoxyWallet Extension Author(s)**  
  Activity: Publishing malicious crypto-wallet extension on Mozilla Add-ons store; harvesting seed phrases and draining digital assets.  

## End of Report