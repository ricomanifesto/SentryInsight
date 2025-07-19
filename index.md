# Exploitation Report

Over the last week, threat actors have sharply escalated their use of zero-day and recently patched vulnerabilities to gain initial access, with particular focus on enterprise file-sharing platforms, VPN appliances, and publicly exposed developer ecosystems. The most critical activity revolves around the new CrushFTP authentication-bypass flaw (CVE-2025-54309), which is being weaponized for full administrative takeover of servers. Concurrently, unpatched Ivanti Connect Secure and Policy Secure gateways are being breached to deploy the new MDifyLoader malware and in-memory Cobalt Strike beacons, while supply-chain manipulation of Arch Linux AUR packages has been leveraged to implant the CHAOS RAT on Linux endpoints. Government and enterprise Microsoft 365 tenants face credential-harvesting campaigns attributed to APT28, and a novel “PoisonSeed” phishing technique is enabling adversaries to sidestep FIDO-based MFA protections. Collectively, these exploits highlight the continued premium placed on remote, zero-click, or social-engineering attack surfaces that yield high-privilege access across diverse environments.

## Active Exploitation Details

### CrushFTP Web Interface Authentication Bypass
- **Description**: A zero-day flaw in CrushFTP’s web management interface allows unauthenticated attackers to forge session data and gain full administrative control.
- **Impact**: Complete takeover of the file-sharing server, exfiltration or destruction of hosted data, and ability to pivot into internal networks.
- **Status**: Actively exploited in the wild; vendor has issued emergency updates and mitigations.
- **CVE ID**: CVE-2025-54309

### Ivanti Connect Secure / Policy Secure Zero-Days
- **Description**: Multiple previously unknown vulnerabilities in Ivanti VPN appliances enable unauthenticated remote code execution, facilitating the drop of a custom loader dubbed “MDifyLoader,” which then injects Cobalt Strike into memory.
- **Impact**: Persistent foothold on perimeter devices, lateral movement, and post-exploitation command-and-control via encrypted channels.
- **Status**: Exploits observed in active campaigns; Ivanti has released patches and interim mitigations.

### Arch Linux AUR Supply-Chain Poisoning
- **Description**: Three malicious packages were uploaded to the Arch User Repository with post-install scripts that fetch and execute the CHAOS remote-access trojan.
- **Impact**: Remote command execution, data theft, and potential lateral movement on developer workstations and production servers.
- **Status**: Malicious packages removed; users must audit and reinstall clean versions.

### Microsoft 365 “Authentic Antics” Credential Theft
- **Description**: A stealthy malware framework that injects malicious device identities and tokens to siphon credentials from Microsoft 365 tenants, evading standard detection.
- **Impact**: Account takeover, email exfiltration, and long-term espionage activity within cloud environments.
- **Status**: Ongoing exploitation attributed to APT28; Microsoft and UK NCSC have issued detection guidance.

### “PoisonSeed” FIDO-Bypass Phishing
- **Description**: Attackers present victims with a fraudulent QR code during MFA that proxies authentication to steal session cookies, thus bypassing FIDO-based hardware keys.
- **Impact**: Compromise of accounts previously protected by strong MFA, enabling full access to corporate resources.
- **Status**: Active campaigns observed; relies on user interaction rather than software patching.

### Unauthenticated MCP Server Exposure
- **Description**: Nearly 2,000 servers running the Multi-Compute Platform (MCP) for agentic AI were found with authentication disabled, granting unfettered remote control.
- **Impact**: Attackers can manipulate AI agents, harvest data, or repurpose compute resources for malicious tasks.
- **Status**: Wide-scale exposure persists; mitigation requires administrators to enable built-in authentication controls.

## Affected Systems and Products

- **CrushFTP Server (v10–v12)**  
  Platform: Windows, Linux, macOS

- **Ivanti Connect Secure & Policy Secure Gateways**  
  Platform: Purpose-built VPN appliances and virtual editions

- **Arch Linux AUR Packages – “sysupdate-helper”, “jupiter-wm”, “vpnstreamer”**  
  Platform: Arch Linux endpoints using affected community packages

- **Microsoft 365 Tenants (Government, Defense, Critical Infrastructure)**  
  Platform: Cloud (Azure AD / Entra ID)

- **Enterprise Accounts Using FIDO2/U2F Security Keys**  
  Platform: Web-based SSO portals and SaaS apps

- **MCP (Multi-Compute Platform) Agentic AI Servers**  
  Platform: Cloud-hosted or on-prem Linux servers running MCP without authentication

## Attack Vectors and Techniques

- **Session Forgery / Auth-Bypass**  
  Vector: Crafted HTTP requests to CrushFTP web interface

- **Unauthenticated Remote Code Execution**  
  Vector: Exploitation of Ivanti VPN web components to write and execute MDifyLoader

- **Malicious Package Installation**  
  Vector: Users installing trojanized Arch Linux AUR packages with post-install scripts

- **Token & Device Identity Hijacking**  
  Vector: Authentic Antics malware manipulating Microsoft 365 OAuth tokens

- **QR-Code MFA Phishing**  
  Vector: Social-engineering victims into scanning attacker-controlled QR codes that proxy authentication flows

- **Open Management API Abuse**  
  Vector: Direct unauthenticated API calls to exposed MCP servers

## Threat Actor Activities

- **Unknown (CrushFTP Intrusions)**  
  Campaign: Rapid opportunistic scanning and exploitation of public CrushFTP instances for data theft and foothold creation

- **Unattributed Operators (Ivanti Zero-Day Exploits)**  
  Campaign: Delivery of MDifyLoader → Cobalt Strike beacons, targeting corporate VPN infrastructure

- **Supply-Chain Threat Actor (Arch Linux AUR)**  
  Campaign: Poisoned packages uploaded to developer repository to distribute CHAOS RAT

- **APT28 / Fancy Bear (Authentic Antics)**  
  Campaign: Espionage against governmental Microsoft 365 environments, focusing on credential theft and inbox surveillance

- **PoisonSeed Group**  
  Campaign: MFA-bypass phishing leveraging QR codes to compromise FIDO-protected enterprise accounts

- **Opportunistic Attackers (MCP Exposure)**  
  Campaign: Mass scanning for unauthenticated MCP servers to gain control of AI workloads and underlying infrastructure