const STACK_DESCRIPTIONS = {
  STANDARD: "Package is neither bulky nor heavy — routed to standard processing.",
  SPECIAL: "Package is bulky or heavy (but not both) — routed to special handling.",
  REJECTED: "Package is both bulky and heavy — rejected from automated sorting.",
};

document.getElementById("sort-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const resultDiv = document.getElementById("result");
  const errorDiv = document.getElementById("error");
  resultDiv.style.display = "none";
  errorDiv.style.display = "none";

  const form = event.target;
  const payload = {
    width: parseFloat(form.width.value),
    height: parseFloat(form.height.value),
    length: parseFloat(form.length.value),
    mass: parseFloat(form.mass.value),
  };

  try {
    const response = await fetch("/sort", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      const data = await response.json();
      document.getElementById("result-stack").textContent = data.stack;
      document.getElementById("result-detail").textContent =
        STACK_DESCRIPTIONS[data.stack] ?? "";
      resultDiv.style.display = "block";
    } else {
      const data = await response.json();
      document.getElementById("error-message").textContent =
        data.detail ?? "An unexpected error occurred.";
      errorDiv.style.display = "block";
    }
  } catch {
    document.getElementById("error-message").textContent =
      "Failed to reach the server. Please try again.";
    errorDiv.style.display = "block";
  }
});
