# Exploitation Report

During the last week, defender telemetry and government advisories show a marked rise in successful attacks that bypass traditional perimeter controls by targeting infrastructure firmware and edge devices.  The most critical activity centers on the ongoing exploitation of an American Megatrends (AMI) MegaRAC Baseboard Management Controller (BMC) flaw that lets unauthenticated attackers hijack and even brick servers.  CISA simultaneously added three vulnerabilities – in AMI MegaRAC, legacy D-Link DIR-859 home routers, and Fortinet FortiOS – to its Known Exploited Vulnerabilities (KEV) catalogue, confirming they are being abused in the wild.  These server- and network-level compromises are being paired with novel social-engineering vectors such as Microsoft 365 “Direct Send” abuse and the rapidly growing “ClickFix/FileFix” CAPTCHA-bait tactic, illustrating the broadening attack surface defenders must now monitor.

## Active Exploitation Details

### AMI MegaRAC BMC Firmware Vulnerability
- **Description**: A maximum-severity flaw in AMI’s MegaRAC Baseboard Management Controller firmware allows remote, unauthenticated access to the BMC via management interfaces (IPMI/Redfish), enabling arbitrary code execution and firmware overwrite.  
- **Impact**: Full remote takeover of server hardware, installation of persistent malware, or permanent denial-of-service by bricking the motherboard.  
- **Status**: CISA reports confirmed, widespread exploitation; AMI has issued fixes to OEMs, but patch adoption remains slow across data centers.  

### D-Link DIR-859 Router Command Injection
- **Description**: An unauthenticated command-injection vulnerability in the web-management interface permits attackers to run shell commands by sending specially crafted HTTP requests.  
- **Impact**: Complete router compromise leading to traffic redirection, network eavesdropping, or enlistment in botnets.  
- **Status**: Listed in CISA KEV as actively exploited.  Product is end-of-life; no vendor patch is expected, so mitigation requires device replacement or isolation.  

### Fortinet FortiOS Edge Device Vulnerability
- **Description**: A high-severity flaw in FortiOS (commonly exposed through SSL VPN) lets remote attackers bypass authentication and execute arbitrary code or commands on FortiGate appliances.  
- **Impact**: Firewall takeover, network infiltration, lateral movement, and data exfiltration.  
- **Status**: Active exploitation confirmed by CISA; Fortinet has shipped patched firmware versions and urges immediate upgrade.  

## Affected Systems and Products

- **AMI MegaRAC BMC**: Multiple server OEMs (Dell EMC, HPE, Lenovo, Supermicro, Gigabyte) shipping MegaRAC-based firmware across x86 and ARM servers.  
- **D-Link DIR-859 Router**: All hardware revisions; firmware is no longer maintained.  
- **Fortinet FortiOS**: Impacted 7.x and 6.x branches on FortiGate, FortiProxy, and FortiSwitchManager appliances prior to vendor-specified fixed builds.

## Attack Vectors and Techniques

- **BMC Network Exploitation**  
  - **Vector**: Direct IPMI/Redfish access over management networks or exposed public IPs.  
  - **Technique**: Unauthenticated API calls to trigger arbitrary firmware reads/writes and command execution.  

- **HTTP Command Injection on Routers**  
  - **Vector**: WAN-facing web interface for DIR-859.  
  - **Technique**: Crafted GET/POST parameters injecting system commands executed with root privileges.  

- **SSL VPN Device Exploit**  
  - **Vector**: Internet-exposed FortiGate SSL VPN portal.  
  - **Technique**: Malformed requests that bypass authentication checks, followed by payload upload for root shell access.  

- **Microsoft 365 “Direct Send” Phishing Abuse**  
  - **Vector**: Direct Send feature allows SMTP relay from tenant IPs.  
  - **Technique**: Threat actors send phishing emails appearing as internal users, bypassing SPF/DKIM inspection.  

- **ClickFix/FileFix CAPTCHA Social Engineering**  
  - **Vector**: Malicious websites mimicking CAPTCHA verification.  
  - **Technique**: Fake CAPTCHA forces victim to download “FileFix/ClickFix” loaders that install backdoors.  517 % jump in observed campaigns H2 2024 → H1 2025.  

- **Authenticode Signature Stuffing**  
  - **Vector**: Modified ConnectWise ScreenConnect installers signed with legitimate certificates.  
  - **Technique**: Attackers embed malicious payloads inside untouched Authenticode signature sections, maintaining valid digital signatures.  

## Threat Actor Activities

- **Unknown Infrastructure Intrusion Sets**  
  - **Campaign**: Mass scanning and exploitation of AMI MegaRAC BMCs to obtain persistent, hardware-level access across hosting providers and enterprises.  

- **Botnet Operators & IoT Malware Authors**  
  - **Campaign**: Leveraging DIR-859 command injection to conscript abandoned home routers into DDoS botnets and residential proxy networks.  

- **Multiple APT & Cyber-criminal Groups**  
  - **Campaign**: Chaining FortiOS exploits with social-engineering footholds to infiltrate corporate networks, especially in finance and insurance sectors.  

- **Scattered Spider**  
  - **Activities**: Continues sophisticated multi-factor authentication bypass and SIM-swap techniques while expanding targeting from retail to U.S. insurance firms.  

- **Iran-Linked APT35 / Charming Kitten**  
  - **Activities**: AI-assisted spear-phishing against Israeli cybersecurity experts; uses generative-text lures but currently no new CVEs abused.  

- **IntelBroker (Individual Criminal Actor)**  
  - **Activities**: Charged for data-theft campaigns exploiting weakly secured APIs and misconfigurations across multiple organizations, causing $25 million in damages.  

---

Security teams should prioritize firmware-level visibility, accelerate patch cycles for edge devices, and harden email and web controls against evolving social-engineering techniques that now accompany device exploits.