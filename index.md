# Exploitation Report

A surge of browser-based and developer-centric attacks dominates the current threat landscape. Google has patched yet another actively exploited Chrome zero-day (CVE-2025-6554), while adversaries simultaneously abuse Windows’ “Mark of the Web” (MoTW) handling to run unsigned JScript code via the so-called FileFix technique. Developers are also at heightened risk: a critical flaw in Anthropic’s Model Context Protocol (MCP) Inspector enables remote code execution on engineering workstations. Collectively, these exploits provide attackers with direct avenues for initial access, credential theft, and full system compromise across consumer and enterprise environments.

## Active Exploitation Details

### Google Chrome Type-Confusion Zero-Day  
- **Description**: A high-severity type-confusion bug in Chrome’s JavaScript engine that allows arbitrary code execution when processing crafted web content.  
- **Impact**: Remote takeover of the browser, sandbox escape, and potential full host compromise.  
- **Status**: Actively exploited in the wild; emergency patches released for all supported desktop platforms.  
- **CVE ID**: CVE-2025-6554  

### FileFix MoTW Bypass  
- **Description**: Abuse of the way Windows assigns Mark of the Web to files saved from a browser. Attackers embed malicious JScript inside “Web Archive”/HTML files; when the victim double-clicks the file, the script runs without SmartScreen or MoTW warnings.  
- **Impact**: Silent execution of code that installs payloads, downloads additional malware, or exfiltrates data.  
- **Status**: Technique observed in active campaigns; no dedicated patch—mitigation requires hardening file-handling policies and blocking risky extensions.  

### Anthropic MCP Inspector Remote Code Execution  
- **Description**: The open-source MCP Inspector parses untrusted model context data without proper sanitization, permitting injection of commands that execute on the host machine.  
- **Impact**: Full remote code execution on developer endpoints, enabling supply-chain compromise of downstream AI projects.  
- **Status**: Exploit code published; hot-fix available in the project repository.  

### ‘FoxyWallet’ Malicious Firefox Extension  
- **Description**: A rogue browser add-on masquerading as a cryptocurrency wallet. Utilizes legitimate APIs and sideloading loopholes to harvest credentials and seed phrase data.  
- **Impact**: Direct theft of cryptocurrency and browser-stored secrets.  
- **Status**: Extension actively distributed through phishing sites and third-party stores; Mozilla has issued take-down requests.  

## Affected Systems and Products

- **Google Chrome (desktop variants)**  
  - **Platform**: Windows, macOS, Linux prior to the latest stable release containing the emergency fix  

- **Microsoft Windows (10, 11, Server versions)**  
  - **Platform**: All environments where users save and open HTML/HTM/MHT files locally (FileFix attack)  

- **Anthropic MCP Inspector (all pre-patch versions)**  
  - **Platform**: Developer workstations on Windows, macOS, and Linux running the vulnerable Python package  

- **Mozilla Firefox users installing “FoxyWallet”**  
  - **Platform**: Windows, macOS, Linux; extension primarily targets users interacting with cryptocurrency sites  

## Attack Vectors and Techniques

- **Drive-By Browser Exploitation**  
  - **Vector**: Malicious or compromised websites deliver JavaScript that triggers CVE-2025-6554 to execute shellcode in the renderer process.

- **Local File Execution via MoTW Bypass (FileFix)**  
  - **Vector**: Phishing e-mails deliver zipped HTML archives; victims open files believing them benign, bypassing Windows security prompts.

- **Supply-Chain Injection in AI Tooling**  
  - **Vector**: Adversaries craft model context files or pull-requests that exploit MCP Inspector’s parsing flaw to run arbitrary OS commands during analysis.

- **Malicious Extension Sideloading**  
  - **Vector**: Users are lured to install “FoxyWallet” from fake update pages; extension abuses browser storage APIs to extract keys and exfiltrate data over WebSockets.

## Threat Actor Activities

- **Unknown Chrome Exploit Broker(s)**  
  - **Campaign**: Selling or deploying CVE-2025-6554 as part of exploit chains targeting high-value users and enterprise workstations via watering-hole sites.

- **Malware Distributors Leveraging FileFix**  
  - **Campaign**: Wide-scale e-mail phishing distributing archived HTML “invoice” or “resume” files to gain initial foothold in corporate networks.

- **Financially Motivated Actors Behind ‘FoxyWallet’**  
  - **Campaign**: Focused on cryptocurrency theft; observed targeting DeFi and NFT communities through social-media ads and cloned wallet websites.

- **Potential APT Interest in MCP Inspector**  
  - **Campaign**: Security researchers note proof-of-concept exploit circulation on GitHub; high likelihood of adoption by supply-chain attackers seeking developer environments.

