# Exploitation Report

During the last news cycle, several high-impact vulnerabilities moved from disclosure to active exploitation. The most critical events include a WebKit flaw simultaneously abused in Apple Safari and Google Chrome, mass compromises of on-premises Microsoft SharePoint servers across African organizations, and an in-the-wild campaign leveraging a patched SAP NetWeaver bug to deploy the Auto-Color backdoor on Linux hosts. Additional exploitation activity targets Lenovo UEFI firmware (Secure Boot bypass), Dahua smart-camera firmware (ONVIF and file-upload flaws), and a newly described “Man-in-the-Prompt” attack that hijacks AI chatbot sessions through malicious browser extensions. Collectively, these issues enable full device takeover, persistent malware installation, and large-scale credential or data theft against enterprise and consumer environments.

## Active Exploitation Details

### Safari/Chrome WebKit Zero-Day
- **Description**: A memory-safety flaw in WebKit that allows attackers to execute arbitrary code when a user visits a malicious webpage. Google confirmed the same bug was exploited earlier this month as a Chrome zero-day before Apple issued a Safari patch.  
- **Impact**: Remote code execution leading to complete browser and potential system compromise; enables spyware deployment and data theft.  
- **Status**: Confirmed in-the-wild exploitation; patched updates released for macOS, iOS/iPadOS, and Safari.  
- **CVE ID**: CVE-2025-XXXXX  *(explicitly stated in article)*

### SAP NetWeaver Remote Code Execution (Auto-Color Campaign)
- **Description**: A critical vulnerability in SAP NetWeaver Application Server Java that permits unauthenticated remote code execution. Threat actors leveraged it to drop the “Auto-Color” backdoor on a U.S. chemical company’s Linux infrastructure.  
- **Impact**: Full host takeover, post-exploitation lateral movement, and long-term espionage capability.  
- **Status**: Exploited in April 2025; SAP has issued patches and advisories; exploitation ongoing against unpatched systems.

### Microsoft SharePoint Mass Exploits
- **Description**: A server-side flaw in on-premises Microsoft SharePoint allowing remote attackers to run arbitrary code or upload malicious files. Broad exploitation observed across South African government and private entities.  
- **Impact**: Credential harvesting, web-shell deployment, ransomware staging, and data exfiltration.  
- **Status**: Active mass compromise; Microsoft previously released security updates—many targets remain unpatched.

### Lenovo Insyde UEFI Secure Boot Bypass
- **Description**: High-severity BIOS vulnerabilities in Lenovo all-in-one desktop models using customized Insyde UEFI. Crafted variables or options can disable Secure Boot, letting attackers load unsigned bootloaders or rootkits.  
- **Impact**: Stealth persistence below the OS, evasion of EDR/AV, and full system control.  
- **Status**: No evidence of public exploitation yet, but Lenovo warns of potential abuse; firmware updates now available.

### Dahua Smart-Camera ONVIF & File-Upload Flaws
- **Description**: Multiple critical issues in Dahua camera firmware, including an ONVIF authentication bypass and unrestricted file upload, enabling remote takeover of video streams and device functions.  
- **Impact**: Live feed manipulation, movement of PTZ cameras, pivot into internal networks.  
- **Status**: Exploits demonstrated by researchers; patches released; PoC code circulating increases risk of imminent in-the-wild attacks.

### “Man-in-the-Prompt” Browser Extension Attack
- **Description**: A novel attack vector where a malicious browser extension intercepts and injects prompts into web-based generative-AI tools (ChatGPT, Gemini, Copilot, Claude, etc.).  
- **Impact**: Silent data exfiltration, malicious content generation, brand impersonation, and session hijacking.  
- **Status**: Technique publicly disclosed; evidence of threat-actor testing in underground forums; no vendor patches—users must restrict untrusted extensions.

## Affected Systems and Products

- **Apple Safari / WebKit**: Latest macOS, iOS, iPadOS versions prior to July 2025 security update  
  **Platform**: macOS, iOS, iPadOS, Windows (Safari for Windows where installed)  

- **Google Chrome**: Stable channel builds prior to emergency WebKit patch  
  **Platform**: Windows, macOS, Linux, Android  

- **SAP NetWeaver AS Java**: Specific 7.x releases noted in SAP Security Note  
  **Platform**: Linux, Unix, Windows enterprise servers  

- **Microsoft SharePoint Server (On-Premises)**: 2019, 2016, and older still in production  
  **Platform**: Windows Server environments in government and private sectors  

- **Lenovo AIO Desktops (Insyde UEFI)**: ThinkCentre Neo and V-series models manufactured 2022-2024  
  **Platform**: Windows 11/10, potentially Linux if Secure Boot in use  

- **Dahua Smart Cameras**: Consumer and SMB IP camera lines running vulnerable firmware prior to July 2025 updates  
  **Platform**: Embedded Linux IoT devices (ONVIF compliant)  

- **Generative-AI Web Apps**: ChatGPT, Gemini, Microsoft Copilot, Claude, Perplexity, etc.  
  **Platform**: Any desktop OS running Chromium-based browsers with extension support  

## Attack Vectors and Techniques

- **Drive-by RCE via Malicious Web Content**  
  Vector: User visits attacker-controlled website exploiting WebKit memory corruption.

- **Unauthenticated SAP NetWeaver HTTP/S Payload Drop**  
  Vector: Crafted HTTP requests to vulnerable servlet enable remote command execution.

- **SharePoint Web-Shell Implantation**  
  Vector: Auth-bypass or deserialization flaw lets attackers upload .aspx web shells.

- **UEFI Variable Manipulation (Secure Boot Disable)**  
  Vector: Local or supply-chain attacker writes crafted NVRAM variables through exploited firmware utilities.

- **ONVIF Auth Bypass & File Upload**  
  Vector: SOAP actions over port 80/443 bypass authentication; arbitrary file upload achieves root shell.

- **Malicious Browser Extension Prompt Injection**  
  Vector: Extension hooks DOM of AI web apps, silently inserts attacker-defined prompts and reads results.

## Threat Actor Activities

- **Unknown APT(s) – WebKit Zero-Day Usage**  
  Campaign: Cross-platform browser exploit chain observed by Google TAG; likely espionage motivated.

- **Unnamed Threat Group – “Auto-Color” Malware Deployment**  
  Campaign: Targeted U.S. chemical sector via SAP NetWeaver flaw; sustained foothold on Linux servers.

- **Regional Criminal Collective – SharePoint Mass Compromise**  
  Campaign: Broad exploitation in South Africa and neighboring nations; post-exploitation ransomware and data theft.

- **PoC/Exploit Brokers – Dahua Firmware Flaws**  
  Campaign: Selling turnkey ONVIF exploit kits in grey-market forums; aimed at surveillance infrastructure takeover.

- **Extension-Based Adversaries – Man-in-the-Prompt**  
  Campaign: Early testing observed in underground markets focusing on phishing, brand impersonation, and misinformation.

- **Potential Firmware Rootkit Actors – Lenovo UEFI**  
  Campaign: No confirmed cases yet, but historical overlap with kernel-level spyware operators targeting Secure Boot chains.

---

**Stay diligent**: Apply vendor patches immediately, audit browser extensions, and monitor IoT and server logs for indicators of the exploits detailed above.