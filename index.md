# Exploitation Report

Recent threat-hunting telemetry and public-source intelligence reveal a surge in active exploitation of edge appliances and client browsers. Threat actors are leveraging a newly released public exploit chain to compromise Fortinet FortiWeb devices, abusing an undisclosed zero-day in fully-patched SonicWall SMA 100 series appliances, and weaponising Google Chrome’s latest sandbox-escape flaw (CVE-2025-6558). Successful intrusions grant remote code execution, persistent root-level access, and client-side takeover, underscoring the urgency of patching internet-facing infrastructure and endpoint browsers immediately.

## Active Exploitation Details

### Fortinet FortiWeb Remote Code Execution
- **Description**: A pre-authentication RCE vulnerability in the FortiWeb web application firewall allows unauthenticated attackers to run arbitrary system commands by sending crafted HTTP requests. A proof-of-concept exploit was published shortly after the vendor released a patch.  
- **Impact**: Full device takeover, web-shell deployment, lateral movement into protected networks, and data exfiltration.  
- **Status**: Actively exploited in the wild; multiple FortiWeb instances observed with web shells. Patch has been released by Fortinet.  

### SonicWall SMA 100 Series OVERSTEP Rootkit Vector
- **Description**: UNC6148 is exploiting an undisclosed flaw in end-of-life yet fully-patched SonicWall SMA 100 VPN appliances to gain root access and implant the custom OVERSTEP kernel-mode rootkit alongside an ELF backdoor named STEPIN.  
- **Impact**: Persistent root-level access, credential theft from memory, pivoting into internal networks, and command-and-control beacons that survive firmware reboots.  
- **Status**: Confirmed active exploitation; no vendor patch available because affected models are end-of-life. Mitigations require device replacement or network isolation.  

### Google Chrome Sandbox Escape
- **Description**: Type-confusion flaw in Chrome’s V8 engine that allows a renderer-process compromise to break out of the sandbox and execute code on the host.  
- **Impact**: Drive-by compromise of Windows, macOS, and Linux endpoints leading to spyware installation or additional malware payloads.  
- **Status**: Zero-day actively exploited before patch release. Google issued an emergency update (Chrome 125.0.6422.112) that fixes the flaw.  
- **CVE ID**: CVE-2025-6558  

## Affected Systems and Products

- **Fortinet FortiWeb**: All 7.x and 6.x branches prior to the vendor’s June 2025 security release  
  - **Platform**: Dedicated WAF appliance (physical and virtual)

- **SonicWall SMA 100 / 100-FW / 200 / 210** (end-of-life hardware running latest available firmware)  
  - **Platform**: Linux-based SSL-VPN gateway

- **Google Chrome** < 125.0.6422.112 on Windows, macOS, Linux, and ChromeOS  
  - **Platform**: Desktop browsers; affects Electron and other Chromium-embedded frameworks until they upstream the patch

## Attack Vectors and Techniques

- **HTTP Deserialization RCE**  
  - **Vector**: Unauthenticated HTTP POST to vulnerable FortiWeb endpoint carrying malicious payload that triggers command execution.

- **Firmware Logic Bypass & Rootkit Deployment**  
  - **Vector**: UNC6148 abuses unknown logic flaw in SonicWall SMA authentication stack, uploads STEPIN payload, and installs OVERSTEP rootkit via modified init scripts.

- **Drive-By Browser Exploit Chain**  
  - **Vector**: Malicious or compromised websites serve specially crafted JavaScript that triggers V8 type-confusion, escapes sandbox by abusing inter-process communication, then drops stage-2 binaries.

## Threat Actor Activities

- **UNC6148**  
  - **Campaign**: Ongoing operation against defence, telecom, and tech organisations in North America and Europe. Uses OVERSTEP for stealth persistence and exfiltrates configuration files, SSH keys, and VPN credentials from SMA 100 appliances.

- **Unattributed Threat Actors** (FortiWeb)  
  - **Campaign**: Mass scanning of internet-facing FortiWeb WAFs, automatic web-shell planting, and monetisation via access brokerage on dark-web forums.

- **Unknown Chromium Exploit Broker**  
  - **Campaign**: Limited-scope, likely financially motivated or state-sponsored operation distributing CVE-2025-6558 exploit through malvertising and spear-phishing documents embedding browser WebView components.

