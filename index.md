# Exploitation Report

The past week’s threat-hunting telemetry highlights three critical vulnerability-driven attacks: an undisclosed zero-day in SonicWall SMA appliances leveraged to implant the persistent OVERSTEP rootkit, mass exploitation of a freshly patched Fortinet FortiWeb remote-code-execution flaw to install web shells, and an actively abused Google Chrome sandbox-escape (CVE-2025-6558) that Google has now fixed. The SonicWall issue is particularly severe because it compromises fully-patched yet end-of-life devices and provides deep implant-level persistence, while the Fortinet intrusion shows how quickly public proof-of-concept code can be weaponized. The Chrome exploit, already observed in the wild, enables attackers to break out of the browser sandbox across all major desktop platforms. Security teams should prioritize patching, network segmentation, and compromise assessment for the affected products immediately.

## Active Exploitation Details

### SonicWall SMA OVERSTEP Zero-Day
- **Description**: An unidentified vulnerability in SonicWall Secure Mobile Access (SMA) 100 series appliances allows unauthenticated attackers to gain privileged code execution and install the “OVERSTEP” boot-level rootkit, which tamps with the EFI partition to hijack the boot process.  
- **Impact**: Full device takeover, persistence across firmware upgrades and factory resets, lateral movement into protected networks.  
- **Status**: Exploitation confirmed in the wild against fully-patched, end-of-life devices; no official patch is available. SonicWall recommends disconnecting EoL units and migrating to supported platforms.  

### Fortinet FortiWeb Remote Code Execution Flaw
- **Description**: Recently patched RCE vulnerability in Fortinet FortiWeb web application firewalls enables attackers to upload arbitrary files and execute system commands with root privileges via crafted HTTP requests. Public exploit code is circulating.  
- **Impact**: Remote shell access, deployment of persistent web shells, data exfiltration, and potential pivoting to internal assets protected by the WAF.  
- **Status**: Actively exploited in the wild. Fortinet has issued fixes; administrators must update immediately and search for rogue “.jsp” or “.php” files within /data/ and /var/ directories.  

### Google Chrome Sandbox Escape
- **Description**: High-severity use-after-free flaw in the Chrome V8 engine that lets malicious webpages break out of the browser sandbox and execute code on the host operating system.  
- **Impact**: Local code execution, potential full user compromise when chained with additional vulnerabilities or social-engineering.  
- **Status**: Patched in Chrome Stable; exploitation observed prior to the update release. Users should upgrade to the latest version.  
- **CVE ID**: CVE-2025-6558  

## Affected Systems and Products

- **SonicWall Secure Mobile Access 100 Series (SMA 100, 200, 210, 400, 410, 500-v)**  
  - **Platform**: Hardened Linux-based VPN/remote-access appliances (end-of-life firmware builds)  

- **Fortinet FortiWeb (all physical and virtual appliances prior to the July 2025 security release)**  
  - **Platform**: FortiOS-based Web Application Firewall running on dedicated hardware and VM editions  

- **Google Chrome prior to the patched Stable release (Windows, macOS, Linux, ChromeOS)**  
  - **Platform**: Desktop and laptop endpoints running Chromium-based browsers  

## Attack Vectors and Techniques

- **Bootloader Hijacking & Rootkit Installation**  
  - **Vector**: Exploit SonicWall SMA zero-day → overwrite EFI partitions → persist via modified initrd and kernel modules.  

- **Public PoC RCE → Web-Shell Drop**  
  - **Vector**: Send crafted HTTP POST to FortiWeb management interface → upload malicious file → execute command `/bin/sh` → implant web shell.  

- **Browser Sandbox Escape**  
  - **Vector**: Deliver malicious JavaScript through compromised websites or malvertising → trigger use-after-free in V8 → pivot to OS-level payload.  

- **Microsoft Teams Malware Delivery (supporting activity)**  
  - **Vector**: Social-engineering messages with malicious PowerPoint files to sideload Matanbuchus 3.0 on enterprise hosts. *(No underlying Teams CVE involved but noted as an emerging delivery mechanism.)*  

## Threat Actor Activities

- **UNC6148 / Abyss-Linked Operators**  
  - **Campaign**: Deploy OVERSTEP to SonicWall SMA appliances for ransomware staging; observed targeting finance and manufacturing sectors in North America and Europe.  

- **Unattributed FortiWeb Exploiters**  
  - **Campaign**: Opportunistic compromise of internet-facing FortiWeb devices, rapid web-shell deployment, and follow-on credential harvesting.  

- **Unknown Chrome Zero-Day Operators**  
  - **Campaign**: Drive-by download operations using malicious ads and watering-hole sites to compromise end-user desktops before Google’s out-of-band patch.  

Security teams should immediately inventory the listed products, apply vendor patches or mitigations, and hunt for indicators of compromise such as EFI alterations on SonicWall appliances, unexpected web-shell paths on FortiWeb, and suspicious Chrome crash logs associated with V8 engine faults.