# Exploitation Report

A surge of browser-focused attacks dominates the current threat landscape. A newly discovered zero-day in Google Chrome is being weaponized in the wild for remote code execution, while adversaries are simultaneously abusing Firefox’s extension ecosystem through over 40 rogue “FoxyWallet” add-ons that exfiltrate cryptocurrency secrets. On the Windows side, the emergent “FileFix” attack chain is actively bypassing Mark-of-the-Web (MoTW) protections to run JScript payloads, and a critical flaw in Anthropic’s Model Context Protocol (MCP) Inspector project exposes developer workstations to remote compromise. These incidents underscore attackers’ preference for initial-access vectors that require minimal user interaction and demonstrate the continued importance of rapid patching and layered browser defenses.

## Active Exploitation Details

### Google Chrome Zero-Day Memory Corruption Vulnerability
- **Description**: A high-severity memory corruption flaw in Chrome’s rendering engine allows a crafted webpage to trigger out-of-bounds memory access, leading to arbitrary code execution within the browser context.  
- **Impact**: Full takeover of the browser process, sandbox escape chaining, potential installation of additional malware.  
- **Status**: Confirmed to be exploited in the wild. Google has released an emergency update for all desktop and mobile channels; users must upgrade to the latest stable build immediately.  

### FileFix Mark-of-the-Web Bypass
- **Description**: The “FileFix” attack chain leverages browser behavior when saving HTML content. By convincing a victim to save and rename a malicious file, attackers remove MoTW metadata, allowing embedded JScript to execute without SmartScreen or Protected View warnings.  
- **Impact**: Silent execution of scripts, deployment of loaders/RATs, and full user-level compromise on Windows systems.  
- **Status**: Actively exploited through social-engineering lures; no official patch, but Microsoft recommends Group Policy to block dangerous file types and enhanced Attack Surface Reduction (ASR) rules.  

### Firefox “FoxyWallet” Malicious Extension Abuse
- **Description**: Over 40 counterfeit Firefox add-ons masquerade as legitimate crypto-wallets (e.g., MetaMask, Coinbase) to siphon seed phrases and private keys. Attackers exploit gaps in Mozilla’s add-on verification rather than a code vulnerability in Firefox itself.  
- **Impact**: Immediate theft of cryptocurrency holdings and sensitive user data once the extension is installed.  
- **Status**: Ongoing; extensions have been removed from the store, but installed copies persist until manually deleted by users.  

### Anthropic MCP Inspector Remote Code Execution Flaw
- **Description**: A critical security weakness in the open-source MCP Inspector utility allows hostile servers to deliver malicious payloads that execute with the privileges of the developer running the tool.  
- **Impact**: Remote execution on developer machines, unauthorized access to source code, and lateral movement into corporate networks.  
- **Status**: Exploitable conditions confirmed; a patched version has been released by Anthropic. Security researchers have observed proof-of-concept exploitation but no large-scale campaigns yet.  

## Affected Systems and Products

- **Google Chrome (all channels)**: Windows, macOS, Linux, Android – versions prior to the latest emergency release  
- **Mozilla Firefox with compromised add-ons**: Desktop versions on Windows, macOS, Linux  
- **Microsoft Windows 10 / 11**: Any edition where users save malicious HTML files (FileFix chain)  
- **Anthropic MCP Inspector ≤ vulnerable release**: Developer workstations on Windows, Linux, macOS  

## Attack Vectors and Techniques

- **Drive-By Download (Chrome Zero-Day)**  
  - **Vector**: Visiting a booby-trapped website triggers the memory corruption exploit and drops secondary payloads.  

- **Malicious Add-on Installation (FoxyWallet)**  
  - **Vector**: Users are lured via phishing or search-engine ads to install fake wallet extensions from the official Firefox Add-ons Store.  

- **MoTW Evasion via File Renaming (FileFix)**  
  - **Vector**: Social engineering emails instruct victims to save a web page then rename the file, stripping security metadata and allowing JScript execution.  

- **Supply-Chain Abuse of Developer Tooling (Anthropic MCP)**  
  - **Vector**: Attacker-controlled servers send crafted context data that exploits the MCP Inspector flaw during AI model debugging sessions.  

## Threat Actor Activities

- **Unknown Chrome Exploit Operators**  
  - **Campaign**: Exploit kit infrastructure delivering the Chrome zero-day to broad audiences; targeting appears opportunistic across geographies.  

- **Crypto-Theft Group behind “FoxyWallet”**  
  - **Campaign**: Mass-scale credential harvesting of cryptocurrency wallets; infrastructure rotates domains and extension IDs to evade takedowns.  

- **FileFix Social-Engineering Operators**  
  - **Campaign**: Phishing emails themed around invoice processing and HR documents; observed dropping remote-access trojans and info-stealers.  

- **Suspected Silver Fox APT**  
  - **Campaign**: Separate Taiwanese intrusion leveraging DLL sideloading and Gh0stRAT delivery; uses DeepSeek LLM installer lure (no direct CVE, but notable activity).  

- **TA829 & UNK_GreenSec Collaboration**  
  - **Campaign**: Shared C2 infrastructure disseminating RomCom RAT and TransferLoader malware, illustrating convergence among financially motivated groups.  

- **Bulletproof Hosting – Aeza Group**  
  - **Activity**: Recently sanctioned Russian provider hosting ransomware and infostealer infrastructure, facilitating rapid weaponization of the above exploits.  

Stay vigilant by applying vendor patches promptly, removing untrusted browser extensions, tightening Windows scripting policies, and monitoring outbound traffic for anomalous C2 beacons.