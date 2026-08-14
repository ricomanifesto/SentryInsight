(() => {
  let theme;
  try { theme = localStorage.getItem("sentryinsight-theme"); } catch {}
  if (theme !== "light" && theme !== "dark") theme = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  document.documentElement.dataset.theme = theme;
})();
