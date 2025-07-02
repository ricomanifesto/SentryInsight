# Exploitation Report

The most critical exploitation activity this cycle centers on a new Google Chrome zero-day that is already being weaponized in the wild to gain arbitrary code-execution on fully-patched desktop systems. Concurrently, adversaries are bypassing Windows Mark-of-the-Web protections with a “FileFix” attack to run JScript payloads without user warnings, while researchers have disclosed a remote-code execution flaw in Anthropic’s Model Context Protocol that threatens developer workstations. These developments are unfolding alongside rapid abuse of AI tooling (Vercel v0) to mass-produce convincing phishing sites, malicious Firefox extensions targeting crypto users, and DLL-sideloading campaigns attributed to the “Silver Fox” threat actor against Taiwanese entities.

## Active Exploitation Details

### Google Chrome V8 Type-Confusion Zero-Day
- **Description**: A memory-safety flaw in Chrome’s V8 JavaScript engine that permits type confusion, leading to out-of-bounds memory access and arbitrary code execution in the browser context.  
- **Impact**: Full takeover of the renderer process that can be chained with sandbox escapes for system compromise; drive-by download and watering-hole attacks reported.  
- **Status**: Actively exploited in the wild; emergency patches released via stable channel updates for Windows, macOS, and Linux.  
- **CVE ID**: CVE-2025-6554  

### Windows Mark-of-the-Web Bypass (“FileFix” Attack)
- **Description**: Attackers save malicious webpages as “Web Archive” (MHT/HTML) files. When the file is opened locally, Windows fails to propagate the MOTW alternate data stream to embedded JScript, allowing silent execution.  
- **Impact**: Execution of scripts without SmartScreen or Protected-View prompts, enabling malware installation, credential theft, and lateral movement.  
- **Status**: Observed in active campaigns; no formal patch yet. Mitigations include blocking saved-webpage file types and enforcing Attachment Manager policies.

### Anthropic MCP Inspector Remote Code Execution Vulnerability
- **Description**: Unsanitized file-path handling in the Model Context Protocol (MCP) Inspector allows remote attackers to craft payloads that trigger arbitrary command execution on the analyst’s machine when a malicious model context is inspected.  
- **Impact**: Compromise of developer workstations, lateral movement into CI/CD pipelines, and potential poisoning of AI model artifacts.  
- **Status**: Patch released by Anthropic; exploitation considered plausible and demonstration exploits were shown at disclosure.

## Affected Systems and Products

- **Google Chrome (pre-stable-channel patch builds)**  
  - **Platform**: Windows, macOS, Linux desktop editions

- **Microsoft Windows (all supported versions)**  
  - **Platform**: Desktop and server environments susceptible to MOTW bypass with local file execution

- **Anthropic MCP Inspector (open-source builds prior to latest commit)**  
  - **Platform**: Developer machines on Windows, macOS, and Linux

- **Mozilla Firefox users with “FoxyWallet” extension installed**  
  - **Platform**: Multi-platform Firefox browsers, primarily targeting cryptocurrency holders

- **Taiwanese organizations running DeepSeek LLM installer packages**  
  - **Platform**: Windows systems leveraged for DLL sideloading (Gh0stRAT payload)

## Attack Vectors and Techniques

- **Drive-By Browser Exploitation**  
  - **Vector**: Compromised or malicious sites deliver exploit for CVE-2025-6554 to execute code in the Chrome renderer.

- **Mark-of-the-Web Circumvention (FileFix)**  
  - **Vector**: Malicious MHT/HTML files bypass MOTW, executing JScript without security prompts.

- **Malicious Extension Abuse**  
  - **Technique**: “FoxyWallet” masquerades as a crypto-wallet manager, requesting excessive permissions, exfiltrating seed phrases and private keys.  
  - **Vector**: Users tricked into installation via phishing sites and forum posts.

- **AI-Generated Phishing Infrastructure**  
  - **Technique**: Vercel v0 generative AI rapidly creates cloned login pages with correct CSS/branding.  
  - **Vector**: Mass-phishing email campaigns embed links to these convincing pages.

- **DLL Sideloading**  
  - **Technique**: “Silver Fox” packages malicious DLLs with a trojanized DeepSeek installer; legitimate executable sideloads the DLL to launch Gh0stRAT.  
  - **Vector**: Spear-phishing attachments and staged download links.

- **IDE Extension Verification Bypass**  
  - **Technique**: Malicious Visual Studio Code extensions spoof “Verified Publisher” status to evade scrutiny and run arbitrary code at install time.  
  - **Vector**: VS Code marketplace entries and GitHub repositories.

## Threat Actor Activities

- **Unknown Phishing Collective**  
  - **Campaign**: Weaponizing Vercel v0 to scale creation of fake login portals targeting Office 365, Google Workspace, and Okta tenants.

- **Silver Fox**  
  - **Campaign**: Taiwan-focused operation delivering Gh0stRAT via DeepSeek LLM installer lure; uses DLL sideloading and encrypted C2 channels.

- **Scattered Spider**  
  - **Campaign**: Aviation-sector breaches including Qantas third-party data compromise; relies on SIM-swap–enabled social engineering and MFA fatigue tactics.

- **TA829 & UNK_GreenSec**  
  - **Campaign**: Shared infrastructure distributing RomCom RAT and TransferLoader malware against enterprise targets in North America and Europe.

- **Cryptocurrency-Focused Actor (“FoxyWallet” operator)**  
  - **Campaign**: Malicious Firefox extension harvesting wallet credentials, primarily targeting retail crypto traders.

- **North Korean IT Worker Networks**  
  - **Campaign**: Covert employment schemes within U.S. tech firms; proceeds funneled to DPRK missile programs. Recent DoJ takedown seized 29 “laptop farms.”

- **Aeza Group (Bulletproof Hosting)**  
  - **Campaign**: Infrastructure provider facilitating ransomware and infostealer C2 servers; now sanctioned by U.S. Treasury.

