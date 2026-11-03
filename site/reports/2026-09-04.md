---
schema_version: 2
report_date: 2026-09-04
generated_at: 2026-09-04T11:12:10Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-04/
---
# Exploitation Report

## Executive Summary

Active exploitation campaigns are targeting critical vulnerabilities across WordPress ecosystems, enterprise networking equipment, and widely deployed client software. Over 440,000 exploit attempts have been recorded against Super Forms and Elementor Pro plugins, with CVE-2026-32475 in Elementor Pro actively delivering webshells to compromise WordPress sites. Google has patched an actively exploited V8 type confusion zero-day (CVE-2026-85046) in Chrome, while Cisco has addressed a critical unauthenticated RCE (CVE-2026-20212) affecting ten Nexus 9000 switch models. These incidents demonstrate rapid weaponization of high-severity flaws across both web applications and infrastructure hardware.

Simultaneously, multiple zero-day and undisclosed vulnerabilities are emerging in security and productivity tools. A proof-of-concept for FalconFlank—a privilege escalation in CrowdStrike Falcon Sensor—has been publicly released, while NSO Group's Pegasus spyware leveraged an iMessage zero-click exploit to infect a Serbian activist's iPhone. Plex has issued urgent update advisories for multiple undisclosed flaws across its media server and desktop clients, with CVE identifiers still pending. Threat actors are also abusing legitimate software such as Node.js runtime for malware delivery in targeted campaigns against government, technology, and hospitality sectors since February 2026.

Threat actor activity shows increased sophistication in both automated and targeted operations. The Shai-Hulud infostealer worm has expanded its credential-harvesting scope to 469 locations across developer environments, CI/CD pipelines, and AI tool configurations. The "Phantom Deal" campaign conducts detailed reconnaissance for business email compromise via fake M&A scenarios, while an RMM phishing operation spanning 46 countries now targets the United States as its primary victim. Supply chain compromise of Coder's registry infrastructure delivered malicious Terraform modules, and the BraZetsu framework commercializes access to compromised Windows hosts through an Initial Access Broker marketplace model.

## Active Exploitation Details

### CVE-2026-32475 - Elementor Pro WordPress Plugin RCE
- **Description**: A critical vulnerability in the Elementor Pro plugin for WordPress that allows attackers to deliver webshell payloads and execute arbitrary commands on the server.
- **Impact**: Full server compromise via webshell deployment, enabling arbitrary command execution, data theft, and persistence on compromised WordPress sites.
- **Status**: Actively exploited in the wild; patch available in recent Elementor Pro versions.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-32475
- **Reporting**: [The Hacker News — Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws](https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html), [Bleeping Computer — Critical Elementor Pro flaw exploited to take over WordPress sites](https://www.bleepingcomputer.com/news/security/critical-elementor-pro-flaw-exploited-to-take-over-wordpress-sites/)

### CVE-2026-14894 - Super Forms WordPress Plugin File Upload
- **Description**: A missing file type validation vulnerability in Super Forms – Drag & Drop Form Builder that allows unauthenticated attackers to upload files of any type, leading to remote code execution.
- **Impact**: Unauthenticated remote code execution via malicious file upload, enabling complete site takeover and server compromise.
- **Status**: Actively exploited with over 440,000 exploit attempts observed; patch available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-14894
- **Reporting**: [The Hacker News — Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws](https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html)

### CVE-2026-85046 - Chrome V8 Type Confusion Zero-Day
- **Description**: A type confusion bug in V8, Chrome's JavaScript and WebAssembly engine, affecting versions prior to 152.0.7977.82. This zero-day was actively exploited in the wild before patching.
- **Impact**: Remote code execution via crafted web content, allowing attackers to escape the sandbox and compromise the browser and potentially the underlying system.
- **Status**: Actively exploited zero-day; patched in Chrome 152.0.7977.82 released September 2026.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85046
- **Reporting**: [The Hacker News — Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day](https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html)

### CVE-2026-20212 - Cisco Nexus 9000 Unauthenticated RCE
- **Description**: A critical security flaw affecting 10 Silicon One-based Nexus 9000 switches that allows an unauthenticated, remote attacker to execute code as root. Part of a broader IOS XR hardening release bundling 7 umbrella CVEs, two rated 9.8.
- **Impact**: Unauthenticated remote root code execution on core network infrastructure, enabling complete device compromise, network pivoting, and traffic interception.
- **Status**: Patches released by Cisco; no workaround available for any IOS XR version.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **CVE IDs**: CVE-2026-20212
- **Reporting**: [The Hacker News — Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html)

### FalconFlank - CrowdStrike Falcon Sensor Privilege Escalation
- **Description**: A zero-day privilege escalation flaw (dubbed FalconFlank) that abuses the "office malicious macros remediation" feature in CrowdStrike Falcon Sensor. A proof-of-concept has been publicly released by researcher Chaotic Eclipse.
- **Impact**: Local privilege escalation on endpoints running CrowdStrike Falcon Sensor, potentially allowing attackers to bypass security controls and gain SYSTEM-level access.
- **Status**: Zero-day with public PoC; no CVE assigned yet; vendor response pending.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate
- **Reporting**: [The Hacker News — Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)

### Pegasus iMessage Zero-Click Exploit
- **Description**: An iMessage zero-click exploit used to deploy NSO Group's Pegasus spyware on an iPhone belonging to a Serbian student protest movement member, confirmed by Citizen Lab and SHARE Foundation.
- **Impact**: Full device compromise without user interaction, enabling surveillance of communications, location tracking, and data exfiltration.
- **Status**: Actively exploited in targeted attacks; no public patch information available at time of reporting.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: monitor
- **Reporting**: [The Hacker News — Pegasus Zero-Click Spyware Exploit Infects Serbian Student Movement Member's iPhone](https://thehackernews.com/2026/09/pegasus-zero-click-spyware-exploit.html)

### Plex Multiple Undisclosed Security Flaws
- **Description**: Multiple undisclosed security vulnerabilities in Plex Media Server and Plex Desktop clients. Plex has requested CVE identifiers but has not disclosed technical details of the flaws.
- **Impact**: Unspecified security impact; Plex urges immediate updates for all server owners and Desktop users.
- **Status**: Patches available in Plex Media Server 1.43.3 and Plex Desktop 1.115.0; CVE identifiers pending.
- **Severity**: unknown
- **Exploitation Status**: unknown
- **Action**: patch
- **Reporting**: [The Hacker News — Plex Urges Immediate Updates After Patching Multiple Undisclosed Security Flaws](https://thehackernews.com/2026/09/plex-urges-immediate-updates-after.html), [Bleeping Computer — Plex warns users to patch security vulnerabilities immediately](https://www.bleepingcomputer.com/news/security/plex-warns-users-to-patch-security-vulnerabilities-immediately/)

### HPE ArubaOS-CX Critical RCE
- **Description**: A critical vulnerability in the ArubaOS-CX network operating system that could lead to remote code execution. Hewlett Packard Enterprise has released patches.
- **Impact**: Remote code execution on network infrastructure devices running ArubaOS-CX.
- **Status**: Patched by HPE; exploitation status not explicitly confirmed in source.
- **Severity**: critical
- **Exploitation Status**: observed
- **Action**: patch
- **Reporting**: [Bleeping Computer — HPE patches critical ArubaOS-CX remote code execution flaw](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)

## Affected Systems and Products

- **Elementor Pro WordPress Plugin**: Versions prior to the patched release containing fix for CVE-2026-32475; WordPress sites with Elementor Pro installed.
- **Super Forms – Drag & Drop Form Builder WordPress Plugin**: Versions vulnerable to CVE-2026-14894; WordPress sites using the Super Forms plugin.
- **Google Chrome**: Versions prior to 152.0.7977.82 across Windows, macOS, and Linux platforms.
- **Cisco Nexus 9000 Series Switches**: 10 Silicon One-based models including N9K-C9316D-GX, N9K-C9324D-GX2A, N9K-C9324D-GX2B, N9K-C9336C-FX2, N9K-C9348D-GX2A, N9K-C9348D-GX2B, N9K-C9364C-GX, N9K-C9324D-GX2A, N9K-C9324D-GX2B, and N9K-C9316D-GX.
- **Cisco IOS XR**: Multiple versions across Cisco routing platforms; 7 umbrella CVEs addressed in hardening release with no workaround for any version.
- **CrowdStrike Falcon Sensor**: Versions containing the vulnerable "office malicious macros remediation" feature; Windows endpoints with Falcon Sensor deployed.
- **Apple iOS/iMessage**: iPhone devices targeted by NSO Group's Pegasus spyware via zero-click iMessage exploit; specific iOS versions not disclosed.
- **Plex Media Server**: Versions prior to 1.43.3 across all supported platforms (Windows, macOS, Linux, NAS devices).
- **Plex Desktop**: Versions prior to 1.115.0 on Windows and macOS.
- **HPE ArubaOS-CX**: Network switches running vulnerable versions of ArubaOS-CX; specific version details in HPE security advisory.

## Attack Vectors and Techniques

- **Unauthenticated File Upload to RCE**: Attackers exploit missing file type validation in WordPress plugins (Super Forms CVE-2026-14894, Elementor Pro CVE-2026-32475) to upload malicious PHP webshells, achieving remote code execution without authentication.
- **Browser Engine Zero-Day Exploitation**: Type confusion in Chrome's V8 JavaScript engine (CVE-2026-85046) exploited via crafted web content to achieve remote code execution and sandbox escape.
- **Network Device Unauthenticated RCE**: Root-level code execution on Cisco Nexus 9000 switches (CVE-2026-20212) without authentication, enabling infrastructure compromise.
- **Security Agent Privilege Escalation**: Abuse of CrowdStrike Falcon Sensor's "office malicious macros remediation" feature (FalconFlank) for local privilege escalation to SYSTEM.
- **Zero-Click Mobile Exploitation**: iMessage zero-click exploit delivering Pegasus spyware without user interaction, targeting high-value individuals.
- **Living-off-the-Land with Node.js**: Threat actors leverage the trusted Node.js runtime (node.exe) as a malware delivery mechanism, exploiting its legitimate presence and capabilities to evade detection in targeted attacks against government, technology, and hospitality sectors since February 2026.
- **Infostealer Credential Harvesting at Scale**: Shai-Hulud worm variant scans 469 credential locations across developer environments, CI/CD tooling, cloud configurations, and AI tool configs—expanded from 189 paths in earlier variants.
- **Supply Chain Compromise**: Attackers compromised Coder's Cloudflare infrastructure to inject unauthorized registry servers delivering malicious Terraform modules containing credential-stealing code.
- **Business Email Compromise via Social Engineering**: "Phantom Deal" campaign conducts detailed company reconnaissance to craft convincing fake M&A communications targeting midlevel employees for financial fraud.
- **RMM Phishing with Tax-Themed Lures**: Phishing campaign using Remote Monitoring and Management (RMM) tools and Canada Revenue Agency tax form lures, expanded to 46 countries with 45% targeting the United States (601 observed cases).
- **Commercialized Access Brokerage**: BraZetsu malware framework converts compromised Windows hosts into inventoried assets for Initial Access Brokers, featuring a comprehensive toolkit beyond standard infostealer capabilities.

## Threat Actor Activities

- **NSO Group**: Deployed Pegasus spyware via iMessage zero-click exploit against a Serbian student movement member; confirmed by Citizen Lab and SHARE Foundation analysis showing high-confidence indicators of compromise.
- **Shai-Hulud Operators**: Evolved infostealer worm to harvest credentials from 469 locations across developer environments, CI/CD pipelines, cloud configurations, and AI tool configurations—representing a 148% increase from earlier 189-path variants.
- **Phantom Deal Campaign Operators**: Conduct extensive reconnaissance on target companies to execute highly convincing fake merger and acquisition scams, targeting midlevel employees to initiate fraudulent financial transfers.
- **RMM Phishing Campaign Operators**: Run a multi-national phishing operation spanning 46 countries using RMM tools and tax-themed lures (initially CRA forms), with the United States as the top target at 45% of observed activity; 601 cases linked by ANY.RUN research.
- **Coder Registry Compromise Actors**: Compromised Coder's Cloudflare infrastructure to inject malicious registry servers distributing trojanized Terraform modules with credential-stealing payloads—a supply chain attack targeting infrastructure-as-code workflows.
- **BraZetsu Framework Operators/Initial Access Brokers**: Utilize the Python-based BraZetsu malware framework to convert compromised Windows hosts into commercialized inventory for access brokering, providing a master toolkit that goes beyond standard infostealer functionality.
- **Chaotic Eclipse (INFINITE NIGHTMARE/MSNightmare/Nightmare-Eclipse)**: Security researcher who publicly released the FalconFlank proof-of-concept exploit for a zero-day privilege escalation in CrowdStrike Falcon Sensor.
- **Unidentified Actors - WordPress Mass Exploitation**: Conducting large-scale exploitation attempts (440,000+) against Super Forms (CVE-2026-14894) and Elementor Pro (CVE-2026-32475) vulnerabilities across WordPress installations.