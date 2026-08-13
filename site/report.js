(() => {
  const root = document.documentElement;
  const themeToggle = document.getElementById("theme-toggle");
  const metadataElement = document.getElementById("report-metadata");
  const copyToast = document.getElementById("copy-toast");

  function readMetadata() {
    if (!metadataElement) return { findings: [] };
    try {
      return JSON.parse(metadataElement.textContent || "{}");
    } catch {
      return { findings: [] };
    }
  }

  function storedTheme() {
    try {
      return localStorage.getItem("sentryinsight-theme");
    } catch {
      return null;
    }
  }

  function saveTheme(theme) {
    try {
      localStorage.setItem("sentryinsight-theme", theme);
    } catch {
      // The selected theme still applies for this page when storage is unavailable.
    }
  }

  function applyTheme(theme) {
    root.dataset.theme = theme;
    if (themeToggle) {
      themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
      themeToggle.textContent = theme === "dark" ? "Light theme" : "Dark theme";
    }
  }

  function showCopyToast(message) {
    if (!copyToast) return;
    copyToast.textContent = message;
    copyToast.hidden = false;
    window.setTimeout(() => {
      copyToast.hidden = true;
    }, 1800);
  }

  async function copyHeadingLink(headingId) {
    const url = `${window.location.origin}${window.location.pathname}#${headingId}`;
    history.replaceState(null, "", `#${headingId}`);
    try {
      await navigator.clipboard.writeText(url);
    } catch {
      // The visible URL and status still make the action useful without clipboard access.
    }
    showCopyToast("Link copied");
  }

  function setupFinding(heading) {
    const disclosure = heading.querySelector(".finding-disclosure");
    const anchor = heading.querySelector(".heading-anchor");
    const icon = heading.querySelector(".disclosure-icon");
    const bodyId = disclosure?.getAttribute("aria-controls");
    const body = bodyId ? document.getElementById(bodyId) : null;
    if (!disclosure || !anchor || !icon || !body) return;

    anchor.addEventListener("click", (event) => {
      event.preventDefault();
      copyHeadingLink(heading.id);
    });
    disclosure.addEventListener("click", () => {
      const expanded = disclosure.getAttribute("aria-expanded") === "true";
      disclosure.setAttribute("aria-expanded", String(!expanded));
      heading.dataset.expanded = String(!expanded);
      body.hidden = expanded;
      icon.textContent = expanded ? "+" : "−";
    });
  }

  function setupFindings() {
    document.querySelectorAll("h3.finding-heading").forEach(setupFinding);
  }

  function enhanceExecutiveSummary() {
    const heading = document.getElementById("executive-summary");
    if (!heading) return;
    const card = document.createElement("section");
    card.className = "executive-summary-card";
    card.setAttribute("aria-labelledby", heading.id);
    const contentNodes = [heading];
    let next = heading.nextSibling;
    while (
      next &&
      !(next.nodeType === Node.ELEMENT_NODE && next.tagName === "H2")
    ) {
      contentNodes.push(next);
      next = next.nextSibling;
    }
    heading.before(card);
    contentNodes.forEach((node) => card.appendChild(node));
  }

  function sanitizeReportContent() {
    const content = document.getElementById("report-content");
    if (!content) return;
    if (!window.DOMPurify) {
      throw new Error("Bundled report sanitizer did not load");
    }
    content.innerHTML = window.DOMPurify.sanitize(content.innerHTML, {
      USE_PROFILES: { html: true },
      ALLOW_DATA_ATTR: true,
      ADD_ATTR: ["target", "rel"],
    });
  }

  function renderAge(metadata) {
    const ageElement = document.getElementById("report-age");
    if (!ageElement || !metadata.generated_at) return;
    const generatedAt = new Date(metadata.generated_at);
    const elapsedMinutes = Math.max(
      0,
      Math.floor((Date.now() - generatedAt.getTime()) / 60000),
    );
    let age = "updated just now";
    if (elapsedMinutes >= 1440) age = `updated ${Math.floor(elapsedMinutes / 1440)}d ago`;
    else if (elapsedMinutes >= 60) age = `updated ${Math.floor(elapsedMinutes / 60)}h ago`;
    else if (elapsedMinutes >= 1) age = `updated ${elapsedMinutes}m ago`;
    ageElement.textContent = ` · ${age}`;
  }

  function setupScrollSpy() {
    if (!("IntersectionObserver" in window)) return;
    const links = [...document.querySelectorAll('nav[aria-label="Report sections"] a')];
    const linksById = new Map();
    for (const link of links) {
      const id = decodeURIComponent(link.hash.slice(1));
      const matching = linksById.get(id) || [];
      matching.push(link);
      linksById.set(id, matching);
    }
    const setCurrent = (id) => {
      links.forEach((link) => link.removeAttribute("aria-current"));
      (linksById.get(id) || []).forEach((link) =>
        link.setAttribute("aria-current", "location"),
      );
    };
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => left.boundingClientRect.top - right.boundingClientRect.top);
        if (visible[0]) setCurrent(visible[0].target.id);
      },
      { rootMargin: "0px 0px -72% 0px", threshold: 0 },
    );
    linksById.forEach((_value, id) => {
      const heading = document.getElementById(id);
      if (heading) observer.observe(heading);
    });
  }

  const metadata = readMetadata();
  const preferredDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  applyTheme(storedTheme() || (preferredDark ? "dark" : "light"));
  themeToggle?.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
    saveTheme(nextTheme);
    applyTheme(nextTheme);
  });
  sanitizeReportContent();
  enhanceExecutiveSummary();
  setupFindings();
  renderAge(metadata);
  setupScrollSpy();
})();
