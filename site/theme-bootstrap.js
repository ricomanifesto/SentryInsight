(() => {
  let theme = "light";
  try {
    const savedTheme = localStorage.getItem("sentryinsight-theme");
    if (savedTheme === "light" || savedTheme === "dark") theme = savedTheme;
  } catch {}
  document.documentElement.dataset.theme = theme;
})();
