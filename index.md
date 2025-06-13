# Exploitation Report

The past week’s threat landscape was dominated by highly targeted zero-click exploits and stealthy boot-level attacks.  Apple urgently patched an iMessage flaw weaponized by Paragon’s “Graphite” spyware to surveil European journalists, while Microsoft rushed fixes for a Secure Boot bypass abused by bootkit malware that can persist below the operating-system layer.  Although still in responsible-disclosure status, researchers also revealed “EchoLeak,” a zero-click prompt-injection flaw that can silently siphon Microsoft 365 Copilot data, underscoring the growing risk surface of AI copilots.  Concurrently, large-scale password-spray campaigns and traffic-distribution scams show attackers broadening their reach with open-source tools and malvertising infrastructure.

## Active Exploitation Details

### Apple iMessage Zero-Click Vulnerability
- **Description**: A flaw in Apple’s Messages framework allowed specially crafted, invisible payloads to execute without user interaction (“zero-click”), delivering Paragon’s Graphite spyware.
- **Impact**: Full device compromise enabling microphone/camera activation, file exfiltration, and continuous tracking of high-value targets.
- **Status**: Actively exploited before Apple’s out-of-band patch; fixes shipped in the latest iOS/iPadOS/macOS security updates and are now available via Software Update.

### Windows Secure Boot Bypass / Bootkit Vulnerability
- **Description**: A Secure Boot weakness let malicious bootloaders evade measurement, enabling unsigned kernel-level code during the early boot chain.
- **Impact**: Attackers achieve pre-OS persistence, disable EDR solutions, and deploy stealthy payloads that survive re-installation.
- **Status**: Exploited by in-the-wild bootkit malware; Microsoft has released emergency patches and updated revocation lists.  Systems require both OS updates and refreshed UEFI DBX revocation to be fully protected.

### “EchoLeak” Zero-Click Copilot Exploit
- **Description**: Researchers showed that crafted prompts embedded in shared content can trigger Microsoft 365 Copilot to exfiltrate internal data to external servers without user clicks or awareness.
- **Impact**: Unauthorized disclosure of emails, documents, and tenant data processed by Copilot, potentially breaching confidentiality obligations.
- **Status**: No confirmed in-the-wild exploitation; Microsoft is rolling out mitigations server-side and preparing client updates.

## Affected Systems and Products

- **Apple iOS / iPadOS / macOS**: All versions prior to the latest rapid-response patch; vulnerable through the Messages component.  
- **Microsoft Windows (multiple releases)**: Systems with Secure Boot enabled but lacking the newest KB and UEFI revocation list.  
- **Microsoft 365 Copilot (cloud service & Microsoft 365 apps)**: All tenants using Copilot prior to Microsoft’s mitigations.  

## Attack Vectors and Techniques

- **Zero-Click Payload Delivery (iMessage)**  
  - **Vector**: Malformed iMessage attachment leveraging the Messages parsing flaw; no user interaction required.

- **Bootkit Installation**  
  - **Vector**: Maliciously signed or tampered bootloader introduced via physical access, phishing-delivered firmware flashing tools, or supply-chain images to bypass Secure Boot validation.

- **Prompt-Injection Data Exfiltration (EchoLeak)**  
  - **Vector**: Embedded natural-language payloads in shared documents/emails automatically processed by Copilot, forcing it to return sensitive data to attacker-controlled endpoints.

- **Password-Spray via TeamFiltration**  
  - **Vector**: Automated authentication attempts against Microsoft Entra ID using recycled credentials and low-frequency spray tactics to evade lockouts.

- **Malvertising with Fake CAPTCHA (AdTech Empire)**  
  - **Vector**: JavaScript CAPTCHA overlays that redirect browsers to disinformation or exploit-kit landing pages once users interact.

## Threat Actor Activities

- **Paragon (Graphite) Spyware Operators**  
  - **Campaign**: Zero-click surveillance of European journalists and civil-society figures; delivers Graphite agent for long-term espionage.

- **Kremlin-Aligned Disinformation Actors**  
  - **Campaign**: Dark Adtech infrastructure leveraging fake CAPTCHA malvertising to bypass content moderation and disseminate propaganda.

- **VexTrio TDS & Affiliates (Help TDS, Disposable TDS)**  
  - **Campaign**: Compromised WordPress sites weaponized to funnel victims toward scams, exploit kits, and credential-harvesting pages.

- **TeamFiltration Operators**  
  - **Campaign**: Global password-spray offensive targeting 80,000+ Microsoft Entra ID accounts across hundreds of organizations for cloud account takeover.

- **Fog Ransomware Group**  
  - **Campaign**: Uses open-source penetration tools and legitimate employee-monitoring software to blend in, encrypt data, and demand payment while evading traditional defenses.

