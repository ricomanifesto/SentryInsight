# Exploitation Report

Over the past week, threat activity has centered on critical client-side attack surfaces—most notably web browsers and Windows desktop workflows. Google patched a new Chrome zero-day (CVE-2025-6554) that was already being weaponized in the wild, while a novel “FileFix” technique is actively bypassing Windows Mark-of-the-Web (MoTW) protections to execute JScript payloads. Concurrently, the China-linked “Silver Fox” group is abusing DLL sideloading in a targeted Taiwanese campaign to deliver a customized Gh0stRAT variant, and a rogue Firefox add-on dubbed “FoxyWallet” is siphoning credentials after evading Mozilla’s security vetting. These exploits collectively highlight continued attacker focus on endpoint compromise through socially-engineered payload delivery, browser zero-days, and trust-abuse of signed/verified components.

## Active Exploitation Details

### Google Chrome V8 Out-of-Bounds Write
- **Description**: Memory corruption flaw in the V8 JavaScript engine enabling arbitrary code execution when processing crafted HTML/JS.
- **Impact**: Full takeover of the victim’s browsing session, potential remote code execution at the browser or underlying OS level.
- **Status**: Exploits observed in the wild; Google released emergency updates for all channels.
- **CVE ID**: CVE-2025-6554

### Windows “FileFix” Mark-of-the-Web Bypass
- **Description**: Attackers save malicious webpages locally, leveraging the `filefix://` scheme to load external JScript without inheriting the MoTW security marker.
- **Impact**: Silent execution of scripts that would normally be blocked or trigger SmartScreen warnings, leading to malware installation or further exploitation.
- **Status**: Technique actively used in phishing campaigns; no dedicated patch yet—mitigations rely on hardening attachment handling policies.

### DLL Sideloading in Silver Fox DeepSeek Campaign
- **Description**: Legitimate installers (masquerading as DeepSeek LLM setup files) load a tampered DLL that, in turn, launches a Gh0stRAT variant.
- **Impact**: Stealthy remote control of compromised Windows hosts, data exfiltration, and persistent access.
- **Status**: Ongoing targeted exploitation against Taiwanese entities; defenders must remove vulnerable binaries or enforce application-control policies.

### “FoxyWallet” Malicious Firefox Extension
- **Description**: Trojanized WebExtension posing as a cryptocurrency wallet; abuses extension APIs to harvest browsing data, credentials, and clipboard contents.
- **Impact**: Account takeover, theft of cryptocurrency assets, and broader credential compromise.
- **Status**: Extension observed in live attacks and subsequently removed from the Mozilla Add-ons store; users must manually verify removal.

## Affected Systems and Products

- **Google Chrome (≤ latest unpatched builds prior to July 2025)**  
  **Platform**: Windows, macOS, Linux, Android, ChromeOS

- **Microsoft Windows 10 & 11 (all builds)**  
  **Platform**: Desktop environments where users save and open HTML files

- **Legitimate DeepSeek Installer Packages & Associated DLLs**  
  **Platform**: Windows endpoints in Taiwanese organizations

- **Mozilla Firefox with “FoxyWallet” Add-on Installed**  
  **Platform**: Windows, macOS, Linux

## Attack Vectors and Techniques

- **Browser Zero-Day Exploitation**  
  **Vector**: Drive-by download or malicious site triggering V8 memory corruption (CVE-2025-6554)

- **Mark-of-the-Web Evasion (“FileFix”)**  
  **Vector**: Phishing email delivers zipped/saved HTML that references external JScript via `filefix://` URI

- **DLL Sideloading**  
  **Vector**: Victim executes a trojanized installer that loads a malicious DLL located in the same directory

- **Malicious Browser Extension Abuse**  
  **Vector**: Users persuaded to install “FoxyWallet,” which is then automatically updated with spying code

## Threat Actor Activities

- **Silver Fox**  
  **Campaign**: Targets Taiwanese entities with DeepSeek-themed lures; delivers Gh0stRAT through DLL sideloading; objectives include espionage and persistent access.

- **Unknown Chrome Zero-Day Operators**  
  **Campaign**: Drive-by exploitation of CVE-2025-6554 against undisclosed high-value targets; likely financially motivated or espionage-focused.

- **Scattered Spider (Mentioned in Qantas Incident)**  
  **Campaign**: Broader aviation-sector intrusions; no specific vulnerability exploitation disclosed but part of same threat landscape.

- **Unidentified Threat Actor Behind “FoxyWallet”**  
  **Campaign**: Credential harvesting and crypto theft through rogue Firefox extension distributed via phishing and third-party sites.

- **FileFix Phishers**  
  **Campaign**: Mass-mail distribution of weaponized HTML archives to bypass MoTW and execute JScript payloads leading to commodity malware drops.