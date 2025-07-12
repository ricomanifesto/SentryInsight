# Exploitation Report

Over the past week, defenders have had to contend with a surge of high-impact exploitation activity targeting edge appliances, widely-used developer tools, consumer IoT, and popular web software. The most critical events center on active weaponization of a pre-authentication SQL-injection flaw in Fortinet FortiWeb, mass exploitation of the new “Citrix Bleed 2” vulnerability in NetScaler ADC/Gateway, and in-the-wild attacks on Wing FTP Server. At the same time, supply-chain compromises against WordPress Gravity Forms and the OpenVSX extension registry demonstrate that attackers continue to favor poisoning software distribution channels. Finally, the “PerfektBlue” Bluetooth RCE chain exposes hundreds of millions of vehicles and embedded devices to 1-click compromise, underscoring the broad attack surface presented by third-party SDKs.

## Active Exploitation Details

### Citrix Bleed 2
- **Description**: Memory-leak vulnerability in Citrix NetScaler ADC and Gateway allowing disclosure of session tokens that can be replayed for full device takeover.
- **Impact**: Remote attackers can hijack authenticated sessions, pivot inside networks, and access sensitive data and applications delivered through the appliance.
- **Status**: Confirmed active exploitation; added to CISA KEV catalog. Patches and mitigation guidance have been released by Citrix.
- **CVE ID**: CVE-2025-5777

### Fortinet FortiWeb Pre-Auth SQL Injection RCE
- **Description**: A pre-authentication SQL-injection flaw enabling arbitrary command execution on FortiWeb web-application firewalls without valid credentials.
- **Impact**: Full remote code execution on the underlying OS, leading to device compromise and potential downstream attacks on protected web assets.
- **Status**: PoC exploit code published publicly; exploitation observed in the wild. Fortinet has issued patches and signatures.
- **CVE ID**: CVE-2025-25257

### Wing FTP Server Remote Code Execution
- **Description**: Maximum-severity vulnerability in Wing FTP Server allowing unauthenticated attackers to execute arbitrary code.
- **Impact**: Complete takeover of Windows and Linux servers hosting the application, data theft, and lateral movement.
- **Status**: Actively exploited according to Huntress telemetry; fixed version available from vendor.
- **CVE ID**: CVE-2025-47812

### WordPress Gravity Forms Supply-Chain Backdoor
- **Description**: Attackers compromised the developer’s infrastructure and injected a PHP backdoor into manual installer ZIP files of the Gravity Forms plugin.
- **Impact**: Sites installing the tampered package grant attackers persistent remote access and the ability to execute arbitrary code within WordPress.
- **Status**: Malicious builds have been pulled; clean packages re-issued. Incident response ongoing.

### PerfektBlue Bluetooth RCE Chain
- **Description**: Four vulnerabilities in OpenSynergy’s BlueSDK stack that can be chained for 1-click remote code execution over Bluetooth.
- **Impact**: Attackers within Bluetooth range can execute code on infotainment systems, potentially access CAN-bus components, or compromise embedded/medical/industrial devices.
- **Status**: No confirmed exploitation yet, but proof-of-concept attack demonstrated. Vendors are releasing firmware updates.

### McHire Weak Administrative Credential Exposure
- **Description**: The McDonald’s McHire chatbot platform was protected by the trivial password “123456,” exposing an internal Kibana interface.
- **Impact**: Unauthenticated access to chat transcripts of ~64 million job applicants, leading to massive PII exposure.
- **Status**: Vulnerability disclosed and remediated; no patch required, credentials rotated.

### OpenVSX Extension Registry Zero-Day
- **Description**: Input-validation flaw in the OpenVSX marketplace that let attackers overwrite any extension and deliver malicious updates to Cursor and Windsurf IDE users.
- **Impact**: Supply-chain compromise of millions of developer machines via automatic extension updates.
- **Status**: Patched; no evidence of mass exploitation, but the vulnerability was exploitable prior to disclosure.

### mcp-remote Command-Injection
- **Description**: Improper argument sanitization in the mcp-remote open-source project allows arbitrary OS command execution.
- **Impact**: Systems running vulnerable builds can be fully compromised through crafted network requests.
- **Status**: Fixed version published; exploitation not yet observed.

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: Appliance builds prior to patched release; all platforms (VPX, MPX, SDX).
- **Fortinet FortiWeb**: Versions before the vendor’s July 2025 updates; physical and virtual appliances.
- **Wing FTP Server**: Windows & Linux deployments prior to 7.3.6.
- **WordPress Gravity Forms**: Manual installer ZIPs downloaded from the official site between compromise window.
- **Vehicles Using OpenSynergy BlueSDK**: Mercedes, Volkswagen, Skoda models; additional industrial, medical, and consumer devices incorporating the SDK.
- **McHire (Paradox.ai) Chatbot Platform**: U.S. deployment storing applicant chats.
- **OpenVSX Marketplace**: All Cursor, Windsurf, and other IDE users pulling extensions before patch.
- **mcp-remote Library**: All versions before the fixed release (437 k+ downloads on GitHub/NPM).

## Attack Vectors and Techniques

- **Session Token Bleed**: Exploiting memory-leak to steal valid session cookies (Citrix Bleed 2).
- **Pre-Auth SQL Injection**: Injecting malicious SQL payloads in HTTP parameters to reach underlying shell (FortiWeb).
- **Unauthenticated Buffer/Logic Flaw RCE**: Direct network exploitation without credentials (Wing FTP Server).
- **Supply-Chain Poisoning**: Tampering with legitimate installer archives or extension repositories (Gravity Forms, OpenVSX).
- **Bluetooth 1-Click RCE (“PerfektBlue”)**: Malicious Bluetooth payload triggers overflow leading to code execution in BlueSDK.
- **Default/Weak Credentials**: Direct access via easily guessable password to internal dashboards (McHire).
- **Command Injection via Unsanitized Arguments**: Crafted requests cause mcp-remote to execute attacker-controlled commands.

## Threat Actor Activities

- **Pay2Key (Iran-linked RaaS)**
  - **Campaign**: Relaunched service with 80 % affiliate profit share, encouraging attacks against U.S. and Israeli organizations.
  - **Activities**: Recruiting on cyber-crime forums, offering turnkey ransomware builds, leveraging initial access brokers.

- **Scattered Spider**
  - **Campaign**: Ongoing data-theft and extortion operations against retail and transportation. Four members arrested in the U.K., temporarily disrupting activity.

- **Unattributed Actors Exploiting Citrix Bleed 2**
  - **Campaign**: Mass scanning and automated token harvesting across exposed NetScaler appliances; rapid lateral movement into internal networks.

- **Unknown Threat Actors Targeting FortiWeb & Wing FTP**
  - **Campaign**: Opportunistic exploitation following PoC releases; deployment of webshells and cryptominers observed by MSSPs.

- **Supply-Chain Intruders (Gravity Forms, OpenVSX)**
  - **Campaign**: Focus on plugin and extension ecosystems to gain developer and CMS footholds; backdoor insertion and C2 beacons embedded in modified packages.

- **PerfektBlue Research Demonstration**
  - **Campaign**: Security researchers showcased 1-click exploit chain; no malicious actor attribution yet, but automotive threat landscape is being reevaluated.

