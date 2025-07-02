# Exploitation Report

A surge of browser-focused exploits is dominating the current threat landscape. Google has released an emergency patch for a Chrome zero-day (CVE-2025-6554) that is already leveraged in targeted attacks for remote code execution. Simultaneously, attackers continue to abuse Windows features such as Mark-of-the-Web (MoTW) to deploy payloads without user prompts, and are sideloading malicious DLLs by masquerading as legitimate installers in a newly observed campaign against Taiwanese organizations. Malicious Firefox extensions like “FoxyWallet” further illustrate how browser ecosystems remain a lucrative entry point for threat actors. Collectively, these exploits enable initial access, persistence, and data exfiltration across enterprise environments and highlight the need for rapid patching and hardened application controls.

## Active Exploitation Details

### Chrome Zero-Day in V8 JavaScript Engine
- **Description**: A memory-management flaw in Chrome’s V8 engine allows a crafted web page to achieve out-of-bounds memory manipulation leading to arbitrary code execution in the context of the browser.
- **Impact**: Full compromise of the browser, potential sandbox escape, and follow-on malware deployment.
- **Status**: Actively exploited in the wild; Google released an emergency update for all desktop channels.
- **CVE ID**: CVE-2025-6554

### FileFix Mark-of-the-Web (MoTW) Bypass
- **Description**: Attackers deliver malicious HTML files that, when saved locally, are processed by Windows as “FileFix” items. This bypasses MoTW security prompts and enables embedded JScript execution without SmartScreen or Protected View warnings.
- **Impact**: Silent execution of scripts leading to malware installation, credential harvesting, or further lateral movement.
- **Status**: Attack observed in the wild; no specific patch yet—organizations must rely on content filtering and hardening.

### DLL Sideloading via “DeepSeek” Installer (Gh0stRAT Variant)
- **Description**: The Silver Fox threat group distributes a fake DeepSeek LLM installer bundle that drops a legitimate executable alongside a malicious DLL. The executable sideloads the DLL, launching a customized Gh0stRAT payload.
- **Impact**: Remote access, data theft, and persistent foothold within Taiwanese government and technology networks.
- **Status**: Campaign ongoing; mitigation requires application control and DLL search-order hardening.

### Malicious “FoxyWallet” Firefox Extension
- **Description**: A rogue browser extension posing as a cryptocurrency wallet requests excessive permissions, injects scripts into visited pages, and exfiltrates wallet credentials and session cookies.
- **Impact**: Theft of digital assets, account takeover, and broader credential compromise.
- **Status**: Extension actively circulated outside the official add-on store; Mozilla has issued takedown notices but side-loading remains possible.

## Affected Systems and Products

- **Google Chrome**: All desktop versions prior to the emergency patch (stable channel July 2025)  
  **Platform**: Windows, macOS, Linux, ChromeOS

- **Microsoft Windows**: MoTW handling across Windows 10 and Windows 11 (all supported builds)  
  **Platform**: Desktop endpoints; attack triggered through Edge, Chrome, or any browser that saves HTML files

- **DeepSeek LLM Installer (Trojanized)**: Unsigned installer packages distributed via phishing sites and spear-phishing emails  
  **Platform**: Windows endpoints in Taiwanese organizations

- **Mozilla Firefox** with “FoxyWallet” or similarly crafted extensions  
  **Platform**: Windows, macOS, Linux—any system where the extension is side-loaded

## Attack Vectors and Techniques

- **Use-After-Free Exploit**: Malicious JavaScript triggers memory corruption in Chrome’s V8 engine, granting arbitrary code execution.
- **Mark-of-the-Web Bypass via FileFix**: Attackers exploit how Windows treats saved HTML to run JScript without security warnings.
- **DLL Sideloading**: Legitimate binaries load malicious DLLs placed in the same directory, bypassing signature checks.
- **Malicious Browser Extension**: Threat actors distribute side-loaded add-ons requesting high privileges to harvest data and inject code.

## Threat Actor Activities

- **Silver Fox**  
  - **Campaign**: Targeted spear-phishing of Taiwanese entities using DeepSeek-themed lures. Employs DLL sideloading to deploy a Gh0stRAT variant for long-term espionage.

- **Unnamed Chrome Exploit Operators**  
  - **Campaign**: Drive-by compromise of high-value users and IT administrators via weaponized websites exploiting CVE-2025-6554.

- **FileFix Attackers**  
  - **Campaign**: Mass-mailing campaigns delivering weaponized HTML attachments that silently execute JScript payloads.

- **FoxyWallet Extension Distributor**  
  - **Campaign**: Cryptocurrency-focused theft by propagating malicious Firefox extensions on social media, forums, and cloned wallet sites.

These concurrent exploitation efforts underscore the importance of immediate browser patching, vigilant attachment handling, and strict control over third-party binaries and extensions.