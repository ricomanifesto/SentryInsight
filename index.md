# Exploitation Report

Across several high-profile incidents this week, attackers are capitalising on zero-click flaws and long-standing web-application weaknesses to gain initial access and quietly exfiltrate data. The most critical activity includes a newly disclosed “EchoLeak” zero-click vulnerability in Microsoft 365 Copilot that enables cross-tenant data theft without user interaction, a still-unpatched iOS exploit chain abused by the Graphite spyware platform against journalists, large-scale abuse of vulnerable WordPress plug-ins in the VexTrio fake-CAPTCHA ad-fraud operation, and ongoing weaponisation of a Secure Boot bypass (CVE-2023-24932) leveraged by bootkit malware. These campaigns highlight continued interest in supply-chain positions, AI assistants, and low-friction social-engineering tunnels that require little or no victim input.

## Active Exploitation Details

### EchoLeak Zero-Click Copilot Vulnerability  
- **Description**: A logic flaw in Microsoft 365 Copilot allows crafted prompt-injection payloads to traverse trust boundaries and silently return other users’ or tenants’ data to the attacker. The attack is entirely “zero-click,” requiring no interaction from the victim once the malicious prompt is processed by the Copilot service.  
- **Impact**: Theft of sensitive Microsoft 365 content (e-mails, files, chat data), exposure of proprietary or regulated information, and possible compliance violations across multi-tenant environments.  
- **Status**: Actively demonstrated by researchers with proof-of-concept code; Microsoft has acknowledged the issue and is rolling out mitigations, but a comprehensive patch is not yet generally available.  

### Apple iOS Zero-Click Exploit Used by Graphite Spyware  
- **Description**: An undisclosed iMessage-based exploit chain delivers the Graphite spyware platform to fully patched iOS devices. The payload is installed without any user action, leveraging memory-corruption and sandbox-escape primitives to obtain root privileges and persistence.  
- **Impact**: Complete device compromise, microphone and camera activation, credential theft, message interception, geolocation tracking, and encrypted data exfiltration.  
- **Status**: Confirmed in-the-wild attacks against at least two European journalists; Apple has released emergency security updates, but details remain redacted to prevent further exploitation.  

### WordPress Plug-in Injection Flaws in VexTrio/Fake-CAPTCHA Campaigns  
- **Description**: Multiple outdated or poorly maintained WordPress plug-ins (e.g., slider, visual-builder, and statistics components) are being mass-exploited to inject malicious JavaScript that inserts fake CAPTCHA pages. These pages redirect users through Traffic Distribution Systems (TDS) controlled by the VexTrio affiliate network.  
- **Impact**: Drive-by malware delivery (infostealers, loaders), large-scale ad-fraud, SEO poisoning, and covert disinformation distribution.  
- **Status**: Ongoing global exploitation with tens of thousands of compromised sites; patching depends on individual plug-in vendors, many of which have issued fixes that remain widely unapplied.  

### Windows Secure Boot Bypass (BlackLotus Bootkit)  
- **Description**: A vulnerability in the Windows Secure Boot chain allows attackers to load malicious, signed bootloaders that disable security features during system start-up, enabling the BlackLotus UEFI bootkit to persist below the operating system.  
- **Impact**: Ring-0 control, tampering with hypervisor and EDR drivers, evasion of disk-based forensics, lateral-movement staging, and full system takeover.  
- **Status**: Exploited by crime-ware operators in the wild; Microsoft has shipped phased Secure Boot revocation updates, but full protection requires firmware updates and manual configuration steps by administrators.  
- **CVE ID**: CVE-2023-24932  

## Affected Systems and Products

- **Microsoft 365 Copilot**: All tenants and subscriptions where Copilot is enabled; cloud SaaS platform  
- **Apple iOS Devices**: iPhone and iPad running iOS/iPadOS 16 and 17 prior to the latest rapid-security-response patches  
- **WordPress Websites**: Self-hosted WordPress installations using vulnerable third-party plug-ins (Slider Revolution, WP Bakery, Statistics, etc.) on Linux, Windows, or managed-hosting environments  
- **Microsoft Windows**: Windows 10, Windows 11, and Windows Server variants that trust vulnerable bootloaders and have not applied the Secure Boot revocation updates; x86-64 and ARM64 platforms  

## Attack Vectors and Techniques

- **Zero-Click Prompt Injection**: Malicious system/user prompts embedded in Copilot requests force the AI to leak data across tenant boundaries  
- **Zero-Click iMessage Exploit**: Specially crafted iMessage attachments exploit memory corruption to deploy Graphite spyware without user taps  
- **Fake-CAPTCHA TDS Redirection**: Injected JavaScript swaps legitimate navigation flows with CAPTCHA interstitials that funnel victims through VexTrio-controlled ad networks  
- **Secure Boot Bypass via Malicious Bootloader**: Attackers deploy a rogue, signed bootloader to disable security features and stage the BlackLotus bootkit before the OS loads  

## Threat Actor Activities

- **VexTrio / Help TDS / Disposable TDS**  
  - **Campaign**: Monetises compromised WordPress sites and fake CAPTCHA pages to spread malware and conduct large-scale ad-fraud; observed partnership with Kremlin-aligned disinformation operators.  

- **Graphite Spyware Operators (Believed State-Sponsored)**  
  - **Campaign**: Targeted surveillance of European journalists using zero-click iOS exploits; focus on data exfiltration and real-time device monitoring.  

- **BlackLotus Bootkit Affiliates**  
  - **Campaign**: Commodity malware crews bundling the Secure Boot bypass to deploy persistent rootkits and evade EDR on Windows endpoints in both corporate and consumer environments.  

- **Aim Security Research Team**  
  - **Campaign**: Disclosure of EchoLeak; provided proof-of-concept to Microsoft and publicly demonstrated cross-tenant data exposure risks, prompting emergency mitigations.  

