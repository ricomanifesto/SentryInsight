# Exploitation Report

During the past week, defenders observed a sharp uptick in real-world exploitation of two high-impact server-side vulnerabilities—Citrix Bleed 2 in NetScaler appliances and a pre-authentication remote-code-execution flaw in Wing FTP Server. Both bugs are already weaponized, prompting CISA to issue emergency directives and researchers to publish live exploit telemetry. At the same time, a previously unknown supply-chain zero-day in the OpenVSX extension marketplace revealed how millions of developer workstations could be hijacked, while critical Bluetooth (“PerfektBlue”) and eSIM weaknesses exposed new attack surfaces across the automotive and mobile ecosystems. Multiple threat actors, including the Iranian-aligned Pay2Key ransomware crew and the social-engineering groups abusing fake gaming/AI startups, are actively integrating these weaknesses into ongoing campaigns.

## Active Exploitation Details

### Citrix Bleed 2 (NetScaler ADC/Gateway)
- **Description**: Memory-handling flaw in the NetScaler authentication component allows unauthenticated attackers to siphon session tokens, bypass MFA, and execute arbitrary commands.
- **Impact**: Full appliance takeover, credential/session theft, lateral movement into internal networks, potential data exfiltration.
- **Status**: Confirmed in-the-wild exploitation; CISA added to KEV catalog and ordered U.S. federal agencies to patch within 24 hours (fixed builds released by Citrix).
- **CVE ID**: CVE-2025-5777

### Wing FTP Server Pre-Auth RCE
- **Description**: Improper input validation in the Wing FTP administration interface enables attackers to send crafted HTTP requests that trigger arbitrary command execution with SYSTEM privileges.
- **Impact**: Complete server compromise, file exfiltration, malware deployment, and potential pivoting to adjacent infrastructure.
- **Status**: Active exploitation observed by Huntress; vendor has issued emergency patches and mitigation guidance.
- **CVE ID**: CVE-2025-47812

### OpenVSX Extension Supply-Chain Zero-Day
- **Description**: Logic flaw in namespace ownership validation on the OpenVSX marketplace lets adversaries silently replace or hijack popular Visual Studio Code extensions distributed to Cursor and Windsurf IDE users.
- **Impact**: Automatic distribution of malicious extension updates leading to remote code execution on millions of developer machines, credential theft, and CI/CD pipeline compromise.
- **Status**: Zero-day privately disclosed by Koi Security and patched; no vendor-confirmed detections of mass exploitation to date, but proof-of-concept weaponization was demonstrated.

### PerfektBlue Bluetooth Stack Vulnerabilities
- **Description**: Four independent flaws in OpenSynergy’s BlueSDK permit heap overflows and logic bypasses when processing malformed L2CAP packets.
- **Impact**: Remote code execution on in-vehicle infotainment units, potential access to CAN bus components, and driver tracking across Mercedes-Benz, Volkswagen, and Škoda fleets.
- **Status**: Exploitable over Bluetooth Classic within ~10 m; patches available to OEMs, field exploitation not yet publicly confirmed.

### eSIM Oracle Vulnerability
- **Description**: A six-year-old bug in Oracle’s SIM provisioning library that underpins billions of eSIM profiles enables over-the-air (OTA) profile cloning and local SIM data extraction.
- **Impact**: Covert device surveillance, call/SMS interception, and full cellular identity takeover.
- **Status**: Still unpatched in many carrier deployments; researchers demonstrated practical attacks at Black Hat Europe, and isolated abuse was detected in phone-theft rings.

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: 14.1 before 14.1-18.9, 13.1 before 13.1-52.24, 13.0 before 13.0-93.25  
  **Platform**: On-prem and cloud-hosted appliances deployed behind corporate perimeter and VPN gateways

- **Wing FTP Server**: v7.4.0 and earlier on Windows, Linux, macOS  
  **Platform**: Enterprise and SMB file-transfer environments

- **OpenVSX Marketplace / Cursor & Windsurf IDEs**: All versions prior to July 2025 patch  
  **Platform**: Developer workstations (Windows/macOS/Linux) using VS Code-compatible extensions

- **OpenSynergy BlueSDK (PerfektBlue)**: Versions 3.5.2–4.1 used by Mercedes (MBUX), Volkswagen Group (MIB3), Škoda (Amundsen/Bolero)  
  **Platform**: In-vehicle infotainment systems running QNX, Linux, or Android Automotive OS

- **Global eSIM Implementations**: Devices leveraging vulnerable Oracle SIM provisioning libraries dating back to 2019  
  **Platform**: Android and iOS smartphones, IoT modules, embedded automotive telematics

## Attack Vectors and Techniques

- **Session Token Harvesting**  
  Vector: Crafted HTTP requests to vulnerable Citrix NetScaler endpoints leak authentication tokens enabling session hijack.

- **Pre-Authentication Command Injection**  
  Vector: Malicious HTTP parameters sent to Wing FTP administrative CGI scripts execute arbitrary OS commands.

- **Extension Typosquatting & Namespace Takeover**  
  Vector: Uploading rogue packages that usurp existing OpenVSX namespaces; auto-update delivers payload to developers.

- **Bluetooth L2CAP Heap Overflow**  
  Vector: Attacker within wireless range sends malformed packets triggering memory corruption in vehicle infotainment units.

- **OTA eSIM Profile Cloning**  
  Vector: Exploiting weak authentication in SIM provisioning SMS to push rogue profiles or extract existing profile secrets.

## Threat Actor Activities

- **Pay2Key (Iran-aligned RaaS)**  
  Campaign: Relaunched service offering 80 % profit share; leveraging Citrix Bleed 2 access vectors to deploy ransomware across healthcare and manufacturing sectors.

- **Fake Gaming / AI Start-up Malware Operators**  
  Campaign: Impersonate crypto-related companies on Telegram & Discord to distribute trojanized installers; observed bundling exploits for Wing FTP to reach backend servers that store wallet APIs.

- **Scattered Spider**  
  Activities: Four members arrested in the U.K. for large-scale data-theft and extortion operations; group known to exploit VPN and IdP misconfigurations, now suspected of testing OpenVSX takeover methods for developer-focused attacks.

