# Exploitation Report

Over the last 48 hours defenders have observed coordinated exploitation of a critical remote-code-execution flaw in the WordPress “Alone” theme and an Apple security bug that was weaponised as part of a wider Chrome zero-day campaign. Both weaknesses are being leveraged for full system compromise: the WordPress issue enables immediate web-server takeover through unauthenticated file uploads, while the Apple flaw allows cross-platform drive-by attacks that ultimately drop arbitrary code on macOS and iOS devices. Concurrently, threat actors such as ShinyHunters and UNC2891 (LightBasin) continue to favour low-tech vectors—voice-phishing and rogue hardware implants—to gain initial access, underlining the breadth of techniques currently in play.

## Active Exploitation Details

### WordPress “Alone” Theme – Unauthenticated Arbitrary File Upload
- **Description**: A logic error in the theme’s file-upload handler lets unauthenticated users upload malicious PHP files outside the intended media directory. Once uploaded, the payload is executed by calling it directly from the web root, granting the attacker remote code execution with the web-server’s privileges.  
- **Impact**: Full site takeover, web-shell deployment, credential theft, installation of additional malware, and potential pivoting into the underlying host.  
- **Status**: Actively exploited in the wild. A patched theme version is available from the vendor’s portal and WordPress marketplaces; administrators must update immediately and remove residual web-shells.  

### Apple Security Flaw Leveraged in Chrome Zero-Day Campaign
- **Description**: A memory-safety issue in Apple’s platform libraries (triggered via malicious web content) enables out-of-bounds memory access that attackers chain with Chrome-specific bugs for sandbox escape and code execution on macOS and iOS.  
- **Impact**: Drive-by compromise of Apple devices browsing attacker-controlled or compromised sites, leading to spyware installation and persistent access.  
- **Status**: Patched by Apple across macOS, iOS, iPadOS, and Safari. Exploitation was detected before the patch release; users must apply the latest updates.  

## Affected Systems and Products

- **WordPress “Alone” Theme**  
  - **Platform**: Self-hosted WordPress CMS (PHP) – vulnerable in all versions prior to the vendor’s latest security release.
- **Apple macOS & iOS Devices**  
  - **Platform**: macOS Sonoma/Ventura, iOS & iPadOS current and recent LTS versions running Safari or any Chromium-based browser using the vulnerable libraries.

## Attack Vectors and Techniques

- **Unauthenticated File Upload (WordPress)**  
  - **Vector**: Direct HTTP POST to the theme’s vulnerable endpoint (`/wp-admin/admin-ajax.php` action parameter) carrying a renamed PHP payload.
- **Drive-By Web Exploit (Apple/Chrome Campaign)**  
  - **Vector**: Malicious or compromised websites deliver crafted media or JavaScript that triggers the memory-safety flaw, followed by a secondary Chrome escape.  
- **Voice Phishing (Salesforce Hijack)**  
  - **Vector**: Social-engineering calls convince employees to provide single-sign-on tokens or MFA codes, allowing attackers to extract Salesforce customer data.
- **Physical Hardware Implant (UNC2891 Bank Attack)**  
  - **Vector**: A 4G-enabled Raspberry Pi smuggled onto the internal network acts as a reverse tunnel, bypassing perimeter controls.

## Threat Actor Activities

- **ShinyHunters**  
  - **Campaign**: Voice-phishing operation targeting corporate Salesforce tenants at Qantas, Allianz Life, LVMH, and Adidas to exfiltrate customer data and extort payment.  
- **UNC2891 / LightBasin**  
  - **Campaign**: Offensive insertion of 4G-equipped Raspberry Pi devices inside a financial institution’s LAN to facilitate an attempted ATM cash-out scheme.  
- **Unknown WordPress Botnet Operators**  
  - **Campaign**: Mass-scanning and exploitation of the “Alone” theme flaw, followed by automated web-shell deployment and SEO spam or malware drops.  
- **Chromium Zero-Day Exploit Operators**  
  - **Campaign**: Highly targeted watering-hole attacks aimed at users of macOS/iOS devices to deploy surveillance tooling before Apple’s out-of-band patch release.

