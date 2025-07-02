# Exploitation Report

The past week saw a sharp uptick in real-world exploitation against end-user applications and developer tooling. The most critical activity centers on Google Chrome’s newly patched zero-day (CVE-2025-6554) that adversaries are weaponizing for remote code execution, alongside a Windows “FileFix” technique that bypasses Mark-of-the-Web (MoTW) protections to launch JScript without warnings. Threat actors are also abusing DLL sideloading to deploy Gh0stRAT in a Taiwan-focused campaign, exploiting a remote-execution flaw in Anthropic’s Model Context Protocol (MCP) Inspector project, and taking advantage of weak extension-verification logic in multiple IDEs (VS Code, IntelliJ, and others) to ship malicious add-ons. Collectively, these exploits enable initial access, privilege escalation, and persistent footholds across both enterprise and developer environments.

## Active Exploitation Details

### Google Chrome Skia Rendering Engine Type Confusion
- **Description**: Memory-safety issue in Chrome’s Skia graphics library that allows out-of-bounds memory manipulation leading to arbitrary code execution in the browser context.  
- **Impact**: Full remote code execution in the context of the logged-in user; can be chained with sandbox escapes for complete workstation compromise.  
- **Status**: Actively exploited in the wild; Google released emergency updates for Windows, macOS, and Linux stable channels.  
- **CVE ID**: CVE-2025-6554  

### Windows “FileFix” Mark-of-the-Web Bypass
- **Description**: Abuse of how Windows handles “Save Page As” HTML files. Attackers embed JScript inside a locally saved HTML container; Windows fails to preserve the MoTW ADS flag, preventing SmartScreen and script-execution prompts.  
- **Impact**: Silent execution of malicious scripts, leading to malware installation or further payload delivery without user warnings.  
- **Status**: Exploit observed in the wild; no official patch yet, defensive mitigations involve Group Policy adjustments and blocking .js/.hta execution from untrusted paths.  

### Anthropic MCP Inspector Remote Code Execution
- **Description**: Critical flaw in the Model Context Protocol (MCP) Inspector that lets crafted requests escape the sandbox and run arbitrary commands on a developer’s machine.  
- **Impact**: Remote takeover of development workstations, exfiltration of source code, insertion of malicious code into AI workflows.  
- **Status**: Publicly disclosed with proof-of-concept; active exploitation reported by security researchers. Patch/update available in latest GitHub release.  

### IDE Extension Verification Weakness
- **Description**: Logic flaw in Visual Studio Code, Visual Studio, IntelliJ IDEA, and Cursor that allows attackers to masquerade malicious extensions as “verified,” bypassing marketplace trust checks.  
- **Impact**: Installation of backdoored extensions granting code-execution within the IDE, credential theft, and supply-chain insertion.  
- **Status**: Exploits observed in the wild targeting developer environments; vendors are working on enhanced signature validation.  

### DLL Sideloading in Silver Fox / DeepSeek Campaign
- **Description**: Threat actors embed a malicious DLL alongside a legitimate application installer (e.g., DeepSeek LLM installer). When executed, the legitimate binary sideloads the DLL, launching a variant of Gh0stRAT.  
- **Impact**: Stealthy remote administration, screen capture, keylogging, and data exfiltration on targeted Taiwanese systems.  
- **Status**: Ongoing campaign; no vendor patch (abuses legitimate side-loading behavior). Endpoint detection and application whitelisting recommended.  

## Affected Systems and Products

- **Google Chrome (Stable ≤ 125.x)**  
  - **Platform**: Windows, macOS, Linux, ChromeOS

- **Microsoft Windows (10/11 & Server builds)**  
  - **Platform**: Local workstation environments where users save web pages and execute JScript

- **Anthropic MCP Inspector (pre-patched GitHub releases)**  
  - **Platform**: Developer machines running the open-source project on Windows, macOS, and Linux

- **Visual Studio Code, Visual Studio, IntelliJ IDEA, Cursor (all current marketplace versions)**  
  - **Platform**: Cross-platform developer IDE environments

- **DeepSeek LLM Installer bundle (used in Taiwanese organizations)**  
  - **Platform**: Windows endpoints where the trojanized installer is executed

## Attack Vectors and Techniques

- **Drive-By Browser Exploit**  
  - **Vector**: Malicious or compromised websites trigger CVE-2025-6554 in Chrome, leading to RCE without user interaction.

- **Local HTML “FileFix” Exploit**  
  - **Vector**: Phishing emails deliver zipped HTML/JScript bundles; users extract and open the HTML file, which bypasses MoTW and auto-executes scripts.

- **Malicious IDE Extension Injection**  
  - **Vector**: Attackers upload spoofed “verified” extensions to public marketplaces or deliver them through spear-phishing, abusing the verification bypass to gain developer trust.

- **DLL Sideloading**  
  - **Vector**: Legitimate-looking DeepSeek installer drops both EXE and malicious DLL in same directory; Windows Loader prioritizes local DLL, launching Gh0stRAT.

- **Supply-Chain RCE in MCP Inspector**  
  - **Vector**: Crafted network requests or manipulated model context files exploit the Inspector service running locally on developers’ machines.

## Threat Actor Activities

- **Silver Fox**  
  - **Campaign**: Targeting Taiwanese entities with DeepSeek-themed lures, leveraging DLL sideloading to deploy Gh0stRAT for long-term espionage.

- **Unknown Chrome Exploit Operators**  
  - **Campaign**: Weaponizing CVE-2025-6554 in drive-by attacks against global user base; likely crimeware and state-sponsored clusters.

- **Unattributed Actors (FileFix Technique)**  
  - **Campaign**: Mass-phishing waves distributing HTML/JScript bundles that evade MoTW, aiming for initial access and info-stealers.

- **TA829 / UNK_GreenSec**  
  - **Campaign**: Sharing infrastructure for RomCom RAT and TransferLoader deliveries; employing malicious IDE extensions as one of several infection vectors.

- **Scattered Spider**  
  - **Campaign**: Continued intrusions in aviation sector (Qantas disclosure); social-engineering and SIM-swap tactics noted, although no specific CVE exploitation detailed.

- **North Korean IT Worker Operations**  
  - **Campaign**: Infiltration of tech firms to monetize access and exfiltrate intellectual property, occasionally leveraging public IDE extension flaws for persistence.

---

Stay vigilant, apply the latest Chrome updates immediately, audit developer extensions, and harden script-execution policies to mitigate the highlighted threats.