# Exploitation Report

Microsoft's January 2026 Patch Tuesday reveals critical exploitation activity with 114 security flaws addressed, including one actively exploited zero-day vulnerability and two additional publicly disclosed zero-days. Simultaneously, threat actors are leveraging sophisticated techniques including DLL side-loading vulnerabilities in the c-ares library, exploiting FortiSIEM critical flaws for unauthenticated remote code execution, and deploying advanced malware frameworks like VoidLink targeting Linux cloud environments. Notable campaigns include PLUGGYAPE malware targeting Ukrainian defense forces and ongoing web skimming operations stealing credit card data from online checkout pages since 2022.

## Active Exploitation Details

### Microsoft Windows Zero-Day Vulnerability
- **Description**: One of three zero-day vulnerabilities in Microsoft's January 2026 security update that has been actively exploited in the wild
- **Impact**: Attackers can exploit this vulnerability to compromise Windows systems, though specific attack outcomes vary based on the vulnerability type
- **Status**: Patched in Microsoft's January 2026 Patch Tuesday update (KB5074109, KB5073455, KB5073724)

### c-ares DLL Side-Loading Vulnerability
- **Description**: A DLL side-loading vulnerability in a legitimate binary associated with the open-source c-ares library
- **Impact**: Allows attackers to bypass security controls and deploy malware while appearing to use legitimate processes
- **Status**: Currently being actively exploited in malware campaigns

### FortiSIEM Critical Remote Code Execution Flaw
- **Description**: A critical security flaw in Fortinet's FortiSIEM product allowing unauthenticated remote code execution
- **Impact**: Enables unauthenticated attackers to achieve complete code execution on vulnerable FortiSIEM instances
- **Status**: Patches released by Fortinet to address the vulnerability

### Node.js async_hooks Stack Overflow Vulnerability
- **Description**: A critical security issue affecting virtually every production Node.js application through the async_hooks module
- **Impact**: Successful exploitation can trigger denial-of-service conditions causing server crashes
- **Status**: Updates released by Node.js to fix the vulnerability

## Affected Systems and Products

- **Microsoft Windows**: All supported Windows operating systems affected by 114 security flaws including three zero-days
- **c-ares Library**: Open-source DNS resolution library vulnerable to DLL side-loading attacks
- **Fortinet FortiSIEM**: Security information and event management platform with critical RCE vulnerability
- **Node.js Applications**: Virtually all production Node.js applications vulnerable to async_hooks stack overflow
- **ServiceNow AI Platform**: Agentic AI implementation with severe vulnerability exposing customer data
- **Linux Cloud Servers**: Targeted by VoidLink malware framework with custom loaders and rootkits
- **Google Chrome Extensions**: Malicious extensions targeting MEXC cryptocurrency exchange API keys
- **Web Payment Systems**: American Express, Diners Club, Discover payment networks targeted by web skimming

## Attack Vectors and Techniques

- **DLL Side-Loading**: Exploitation of legitimate c-ares binaries to load malicious DLLs and bypass security controls
- **Unauthenticated Remote Code Execution**: Direct exploitation of FortiSIEM systems without authentication requirements
- **Web Skimming**: Long-running campaign since January 2022 targeting online checkout pages to steal credit card data
- **Malicious Browser Extensions**: Chrome extensions masquerading as trading tools to steal cryptocurrency API keys
- **Social Engineering**: Charity-themed campaigns targeting Ukrainian defense forces with PLUGGYAPE malware
- **Cloud-Native Malware**: VoidLink framework specifically designed for Linux cloud environments with modular architecture
- **AI Session Hijacking**: "Reprompt" attack method to infiltrate Microsoft Copilot sessions for data exfiltration
- **Python and Cloudflare Abuse**: Legitimate services weaponized to deliver AsyncRAT malware
- **Text File Delivery**: Shadow#Reactor campaign using text-only files to deploy Remcos RAT

## Threat Actor Activities

- **Ukrainian Defense Targeting**: CERT-UA reports attacks between October-December 2025 using PLUGGYAPE malware delivered through Signal and WhatsApp
- **Chinese State Activity**: Increased cyber pressure on Taiwan with 6% rise in attacks on critical infrastructure, averaging 2.63 million attacks daily in 2025
- **Web Skimming Groups**: Long-running campaign active since January 2022 targeting major payment networks with sophisticated card theft operations
- **Cryptocurrency Threat Actors**: Development and deployment of malicious Chrome extensions specifically targeting MEXC exchange users
- **Cloud-Focused Attackers**: Deployment of VoidLink malware framework showing advanced capabilities in Linux cloud environment targeting
- **Healthcare Targeting**: Multiple incidents including Belgian hospital AZ Monica cyberattack and data breaches at Central Maine Healthcare (145,000+ affected) and Monroe University (320,000+ affected)