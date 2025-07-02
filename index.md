# Exploitation Report

During the past week, the most critical exploitation activity centers on a newly-disclosed Google Chrome zero-day (CVE-2025-6554) that is already being weaponized in the wild, allowing remote code execution via a V8 type-confusion flaw. Concurrently, attackers are abusing Windows’ Mark-of-the-Web (MoTW) logic with a “FileFix” technique to launch malicious JScript without security prompts, while browser-based threats expand through the rogue “FoxyWallet” Firefox add-on and a flaw that lets malicious IDE extensions masquerade as “verified.” Collectively, these campaigns underscore the ongoing shift toward client-side and supply-chain attack surfaces that give adversaries direct access to endpoints and developer environments.

## Active Exploitation Details

### Google Chrome V8 Type-Confusion Zero-Day  
- **Description**: A type-confusion bug in Chrome’s V8 JavaScript engine enables attackers to corrupt memory and execute arbitrary code when a victim visits a specially crafted webpage.  
- **Impact**: Full remote code execution in the browser context, potential sandbox escape, and follow-on compromise of the host system.  
- **Status**: Actively exploited in the wild; Google released out-of-band security updates for all platforms. Users must update to the latest stable channel immediately.  
- **CVE ID**: CVE-2025-6554  

### FileFix Mark-of-the-Web (MoTW) Bypass  
- **Description**: Attackers save malicious webpages as “Webpage, Complete” (`.htm` + folder) files. When users open the local copy, the referenced `.js` file loads from the accompanying resources folder without inheriting the MoTW flag, suppressing security warnings.  
- **Impact**: Silent execution of JScript or other embedded payloads, leading to initial access for malware loaders, infostealers, or ransomware.  
- **Status**: Observed in active phishing/lure campaigns. No dedicated patch; mitigation relies on hardening attachment handling and blocking script execution from untrusted paths.

### Malicious Firefox Extension “FoxyWallet” Abuse  
- **Description**: A rogue browser extension disguised as a cryptocurrency wallet escalates permissions post-installation to exfiltrate credentials and wallet secrets.  
- **Impact**: Theft of crypto assets, session cookies, and sensitive user data; possible lateral movement via synced browser profiles.  
- **Status**: Actively distributed outside Mozilla’s add-on store; users who sideloaded the extension are already compromised. Mozilla is investigating takedown measures.

### IDE Extension Verification Bypass  
- **Description**: Researchers found weaknesses in Visual Studio Code, Visual Studio, IntelliJ IDEA, and Cursor that let malicious extensions spoof “verified publisher” status or sidestep marketplace code-signing requirements.  
- **Impact**: Supply-chain compromise of developer workstations, credential theft, and insertion of backdoors into compiled software.  
- **Status**: Proof-of-concept exploitation demonstrated; threat actors are beginning to weaponize the flaw in targeted dev-focused phishing campaigns. Vendors are reviewing mitigation options; no official patches yet.

### Anthropic MCP Inspector Remote-Code Execution Flaw  
- **Description**: A critical bug in the Model Context Protocol (MCP) Inspector allows attackers to craft malicious context files that trigger arbitrary code when parsed by the MCP tool.  
- **Impact**: Remote code execution on developer machines, enabling theft of proprietary AI models and credentials.  
- **Status**: Publicly disclosed with exploit details. A temporary mitigation has been published by Anthropic; a full patch is pending.

## Affected Systems and Products

- **Google Chrome prior to patched Stable build**  
  - **Platform**: Windows, macOS, Linux, Android, iOS (Chromium-based browsers may also inherit the flaw)

- **Microsoft Edge (Chromium) and other Chromium forks**  
  - **Platform**: Windows, macOS, Linux (pending vendor back-port of Google’s fix)

- **Windows 10 & 11 MoTW mechanism**  
  - **Platform**: All Windows endpoints that allow saving and opening “Webpage, Complete” files

- **Mozilla Firefox with “FoxyWallet” or similar rogue add-ons**  
  - **Platform**: Windows, macOS, Linux, Android (if extension sideloaded)

- **Visual Studio Code, Visual Studio, IntelliJ IDEA, Cursor IDE**  
  - **Platform**: Windows, macOS, Linux developer environments

- **Anthropic MCP Inspector (all released versions)**  
  - **Platform**: Cross-platform developer systems using the AI tooling

## Attack Vectors and Techniques

- **Drive-By Download (V8 Type-Confusion)**  
  - **Vector**: Malicious or compromised websites deliver JavaScript triggering the type-confusion flaw to gain RCE.

- **Saved-HTML “FileFix” Technique**  
  - **Vector**: Phishing emails or chat lures persuade users to save and open an HTML file; linked JScript runs outside MoTW controls.

- **Rogue Browser Extension Sideloading**  
  - **Vector**: Users are enticed to install “FoxyWallet” via social engineering or third-party repositories; the add-on escalates permissions post-install.

- **IDE Marketplace Spoofing**  
  - **Vector**: Adversaries publish malicious extensions that appear “verified,” or deliver them directly in dev-targeted phishing kits, bypassing trust checks.

- **Malicious MCP Context File**  
  - **Vector**: Attackers share poisoned `.mcp` files or GitHub repositories; parsing triggers remote code execution on the analyst’s machine.

## Threat Actor Activities

- **Unknown Chrome Exploit Operators**  
  - **Campaign**: Leveraging CVE-2025-6554 in watering-hole and spear-phishing websites to gain footholds in enterprise networks, with post-exploit C2 observed on VPS infrastructure.

- **Financially Motivated Phishers (FileFix)**  
  - **Campaign**: Distribute “invoice” or “remittance” HTML archives exploiting the MoTW bypass to deploy loaders for infostealers and ransomware.

- **Cryptocurrency-Themed Actors behind “FoxyWallet”**  
  - **Campaign**: Target retail investors and DeFi users; stolen seed phrases are rapidly emptied into mixers to launder gains.

- **Emerging Supply-Chain Groups Targeting Developers**  
  - **Campaign**: Use the IDE verification bypass to implant trojanized dependencies within corporate software pipelines.

- **Opportunistic Threats Eyeing AI Tooling (Anthropic MCP)**  
  - **Campaign**: Share malicious AI context files on developer forums and Discord channels, aiming to compromise organizations experimenting with LLM integrations.

