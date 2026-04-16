
console.log("script.js loaded successfully");


const API_BASE = "http://127.0.0.1:8000";

let accessToken = localStorage.getItem("access_token");
let isRegisterMode = false;

// Assessment state
let questions = [];
let answers = [];
let currentQuestionIndex = 0;
let selectedOption = null;
let resultData = null;
let selectedAnswersMap = {};

// FitCheck state
let fitcheckDomains = [];
let fitcheckQuestions = [];
let fitcheckCurrentIndex = 0;
let selectedFitcheckDomain = null;
let fitcheckAnswersMap = {};
let selectedFitcheckOption = null;

// Explore state
let exploreDomains = [];
let currentExploreDomain = null;

// -----------------------------
// HELPERS
// -----------------------------
function showScreen(id) {
  document.querySelectorAll(".screen").forEach((s) => s.classList.remove("active"));

  const el = document.getElementById(id);
  if (el) el.classList.add("active");

  const profileBtn = document.getElementById("profile-btn");
  const homeBtn = document.getElementById("home-btn");
  const profileMenu = document.getElementById("profile-menu");
  const pageIndicator = document.getElementById("page-indicator");

  const isLoggedIn = !!accessToken;
  const isAuthScreen = id === "auth-screen";

  if (profileMenu) {
    profileMenu.classList.add("hidden");
  }

  if (isLoggedIn && !isAuthScreen) {
    profileBtn?.classList.remove("hidden");
    homeBtn?.classList.remove("hidden");
    pageIndicator?.classList.remove("hidden");
  } else {
    profileBtn?.classList.add("hidden");
    homeBtn?.classList.add("hidden");
    pageIndicator?.classList.add("hidden");
  }

  updatePageIndicator(id);
  updateHomeButtonState(id);
}

function updatePageIndicator(screenId) {
  const pageIndicator = document.getElementById("page-indicator");
  if (!pageIndicator) return;

  const labels = {
    "welcome-screen": "Dashboard",
    "question-screen": "Dashboard / Assessment",
    "submit-screen": "Dashboard / Assessment / Submit",
    "loading-screen": "Processing",
    "results-screen": "Dashboard / Assessment / Results",
    "fitcheck-domain-screen": "Dashboard / Fit Check",
    "fitcheck-chat-screen": "Dashboard / Fit Check / Questions",
    "fitcheck-result-screen": "Dashboard / Fit Check / Result",
    "explore-screen": "Dashboard / Explore Domains"
  };

  if (screenId === "auth-screen" || !accessToken) {
    pageIndicator.classList.add("hidden");
    pageIndicator.innerText = "";
    return;
  }

  pageIndicator.classList.remove("hidden");
  pageIndicator.innerText = labels[screenId] || "CareerForge AI";
}

function updateHomeButtonState(screenId) {
  const homeBtn = document.getElementById("home-btn");
  if (!homeBtn) return;

  const isHome = screenId === "welcome-screen";

  homeBtn.disabled = isHome;
  homeBtn.classList.toggle("home-active", isHome);
  homeBtn.setAttribute(
    "aria-label",
    isHome ? "You are already on dashboard" : "Go to dashboard"
  );
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.innerText = value;
}

function escapeHTML(str) {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function prettyTraitLabel(trait) {
  const labels = {
    analytical_reasoning: "Analytical Reasoning",
    problem_framing: "Problem Framing",
    learning_agility: "Learning Agility",
    attention_control: "Attention Control",
    creativity: "Creativity",
    decision_style: "Decision Style",
    pattern_thinking: "Pattern Thinking",
    attention_to_detail: "Attention to Detail",
    curiosity: "Curiosity",
    product_thinking: "Product Thinking",
    systems_thinking: "Systems Thinking",
    optimization: "Optimization",
    technical_interest: "Technical Interest"
  };
  return labels[trait] || trait.replaceAll("_", " ");
}

function interpretTrait(score) {
  if (score < 40) return "Emerging";
  if (score < 60) return "Developing";
  if (score < 80) return "Strong";
  return "Exceptional";
}

function clearAuthFields() {
  const nameField = document.getElementById("name-field");
  const emailField = document.getElementById("email");
  const passwordField = document.getElementById("password");

  if (nameField) nameField.value = "";
  if (emailField) emailField.value = "";
  if (passwordField) passwordField.value = "";

  setPasswordVisibility(false);
}

function setAuthMode(registerMode) {
  const authTitle = document.getElementById("auth-title");
  const toggleAuth = document.getElementById("toggle-auth");
  const nameField = document.getElementById("name-field");
  const authBtn = document.getElementById("auth-submit-btn");

  isRegisterMode = registerMode;

  if (isRegisterMode) {
    authTitle.innerText = "Register";
    nameField.style.display = "block";
    authBtn.innerText = "Register";
    toggleAuth.innerText = "Already have an account? Login";
  } else {
    authTitle.innerText = "Login";
    nameField.style.display = "none";
    authBtn.innerText = "Login";
    toggleAuth.innerText = "Don't have an account? Register";
  }
}

function resetExploreState() {
  currentExploreDomain = null;
  const detail = document.getElementById("explore-detail");
  if (detail) {
    detail.classList.add("hidden");
    detail.innerHTML = "";
  }
}

function resetFitcheckState() {
  fitcheckQuestions = [];
  fitcheckCurrentIndex = 0;
  selectedFitcheckDomain = null;
  fitcheckAnswersMap = {};
  selectedFitcheckOption = null;
}

function showToast(message, type = "info", title = "") {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const icons = {
    success: "✅",
    error: "❌",
    warning: "⚠️",
    info: "ℹ️"
  };

  const defaultTitles = {
    success: "Success",
    error: "Error",
    warning: "Warning",
    info: "Notice"
  };

  const toast = document.createElement("div");
  toast.className = `toast ${type}`;

  toast.innerHTML = `
    <div class="toast-icon">${icons[type] || "ℹ️"}</div>
    <div class="toast-content">
      <div class="toast-title">${escapeHTML(title || defaultTitles[type] || "Notice")}</div>
      <div class="toast-message">${escapeHTML(message)}</div>
    </div>
    <button class="toast-close" type="button" aria-label="Close notification">×</button>
  `;

  container.appendChild(toast);

  const removeToast = () => {
    toast.classList.add("hide");
    setTimeout(() => {
      toast.remove();
    }, 250);
  };

  toast.querySelector(".toast-close")?.addEventListener("click", removeToast);
  setTimeout(removeToast, 3000);
}

function setButtonLoading(button, isLoading, loadingText) {
  if (!button) return;

  if (isLoading) {
    if (!button.dataset.originalText) {
      button.dataset.originalText = button.innerText;
    }
    button.innerText = loadingText;
    button.disabled = true;
  } else {
    button.innerText = button.dataset.originalText || button.innerText;
    button.disabled = false;
  }
}

function setPasswordVisibility(showPassword) {
  const passwordInput = document.getElementById("password");
  const toggleBtn = document.getElementById("toggle-password");
  const toggleIcon = document.getElementById("toggle-password-icon");

  if (!passwordInput || !toggleBtn || !toggleIcon) return;

  passwordInput.type = showPassword ? "text" : "password";
  toggleIcon.innerText = showPassword ? "Hide" : "Show";
  toggleBtn.setAttribute("aria-label", showPassword ? "Hide password" : "Show password");
}

async function apiRequest(endpoint, options = {}) {
  const headers = {
    ...(options.headers || {})
  };

  if (accessToken) {
    headers.Authorization = `Bearer ${accessToken}`;
  }

  const response = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers
  });

  let data = null;
  const contentType = response.headers.get("content-type") || "";

  if (contentType.includes("application/json")) {
    data = await response.json();
  } else {
    const text = await response.text();
    data = text ? { detail: text } : null;
  }

  if (!response.ok) {
    throw new Error(data?.detail || `Request failed: ${response.status}`);
  }

  return data;
}

// -----------------------------
// API LAYER
// -----------------------------
async function getQuestions() {
  return await apiRequest("/questions");
}

async function analyzeAssessment(payload) {
  return await apiRequest("/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });
}

async function getProfile() {
  return await apiRequest("/profile", {
    method: "GET"
  });
}

async function getPreviousResults() {
  return await apiRequest("/my-results", {
    method: "GET"
  });
}

async function registerUser(payload) {
  return await apiRequest("/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });
}

async function loginUser(email, password) {
  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  return await apiRequest("/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    body: formData
  });
}

async function getFitcheckDomains() {
  return await apiRequest("/fit-check/domains", {
    method: "GET"
  });
}

async function startFitcheck(domainId) {
  return await apiRequest("/fit-check/start", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ domain: domainId })
  });
}


async function submitFitcheck(domainId, answersPayload) {
  return await apiRequest("/fit-check/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      domain: domainId,
      answers: answersPayload
    })
  });
}

async function getExploreDomains() {
  return await apiRequest("/explore/domains", {
    method: "GET"
  });
}

async function getExploreDetail(domainId) {
  return await apiRequest(`/explore/${domainId}`, {
    method: "GET"
  });
}

async function expandConcept(domainId, concept) {
  return await apiRequest("/explore/expand", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      domain: domainId,
      concept
    })
  });
}

// -----------------------------
// LOAD PROFILE + RESULTS
// -----------------------------
async function loadUserProfile() {
  if (!accessToken) return;

  try {
    const user = await getProfile();
    const results = await getPreviousResults();

    setText("profile-name", user.name || "User");
    setText("profile-email", user.email || "");

    const container = document.getElementById("previous-results");
    if (!container) return;

    container.innerHTML = "";

    if (!results || results.length === 0) {
      container.innerHTML = "<p>No previous results</p>";
      return;
    }

    results.forEach((r) => {
      const div = document.createElement("div");
      div.style.padding = "8px 0";
      div.style.borderBottom = "1px solid rgba(0,0,0,0.08)";
      div.innerHTML = `
        <strong>${escapeHTML(r.top_role || r.role || "Result")}</strong><br />
        <small>Score: ${((Number(r.top_score || r.fit_score || 0)) * 100).toFixed(1)}%</small>
      `;
      container.appendChild(div);
    });
  } catch (err) {
    console.error("Profile load error:", err);
    showToast(err.message || "Unable to load profile.", "error", "Profile");
  }
}

// -----------------------------
// RENDER QUESTION
// -----------------------------
function renderQuestion() {
  const q = questions[currentQuestionIndex];
  if (!q) return;

  setText("question-number", `Question ${currentQuestionIndex + 1} of ${questions.length}`);

  const answeredCount = Object.keys(selectedAnswersMap).length;
  const progressPercent = questions.length ? (answeredCount / questions.length) * 100 : 0;

  document.getElementById("progress-fill").style.width = `${progressPercent}%`;
  setText("progress", `${Math.round(progressPercent)}% COMPLETE`);
  setText("question-text", q.text);

  const container = document.getElementById("options-container");
  container.innerHTML = "";

  selectedOption =
    selectedAnswersMap[currentQuestionIndex] !== undefined
      ? selectedAnswersMap[currentQuestionIndex]
      : null;

  q.options.forEach((opt, i) => {
    const div = document.createElement("div");
    div.className = "option";
    div.innerText = opt;

    if (selectedOption === i) {
      div.classList.add("selected");
    }

    div.onclick = () => {
      document
        .querySelectorAll("#options-container .option")
        .forEach((o) => o.classList.remove("selected"));

      div.classList.add("selected");
      selectedOption = i;
      selectedAnswersMap[currentQuestionIndex] = i;

      const updatedAnsweredCount = Object.keys(selectedAnswersMap).length;
      const updatedProgressPercent = questions.length
        ? (updatedAnsweredCount / questions.length) * 100
        : 0;

      document.getElementById("progress-fill").style.width = `${updatedProgressPercent}%`;
      setText("progress", `${Math.round(updatedProgressPercent)}% COMPLETE`);
    };

    container.appendChild(div);
  });

  const prevBtn = document.getElementById("prev-btn");
  if (prevBtn) {
    prevBtn.disabled = currentQuestionIndex === 0;
    prevBtn.style.opacity = currentQuestionIndex === 0 ? "0.5" : "1";
    prevBtn.style.cursor = currentQuestionIndex === 0 ? "not-allowed" : "pointer";
  }
}

function goToNextQuestion() {
  if (selectedOption === null) {
    showToast("Please select an option before continuing.", "warning", "Assessment");
    return;
  }

  selectedAnswersMap[currentQuestionIndex] = selectedOption;

  if (currentQuestionIndex < questions.length - 1) {
    currentQuestionIndex++;
    renderQuestion();
  } else {
    answers = questions.map((q, index) => ({
      question_id: q.id,
      selected_option: selectedAnswersMap[index]
    }));
    showScreen("submit-screen");
  }
}

function parseFeedback(feedbackText) {
  const sections = {
    strengths: "",
    weaknesses: "",
    advice: "",
    projects: ""
  };

  const lines = feedbackText.split("\n");
  let current = "";

  lines.forEach(line => {
    const lower = line.toLowerCase();

    if (lower.includes("strength")) current = "strengths";
    else if (lower.includes("weakness")) current = "weaknesses";
    else if (lower.includes("advice")) current = "advice";
    else if (lower.includes("project")) current = "projects";
    else if (current) sections[current] += line + "\n";
  });

  return sections;
}  

// -----------------------------
// RENDER RESULTS
// -----------------------------
function renderResults() {
  if (!resultData) return;

  const domainTitle = document.getElementById("domain-title");
  const domainNames = {
    ai_data: "AI / Data Science",
    software_engineering: "Software Engineering",
    cloud_devops: "Cloud & DevOps",
    cybersecurity: "Cybersecurity",
    product_design: "Product & Product Strategy"
  };

  if (domainTitle && resultData.domain) {
    const prettyDomain = domainNames[resultData.domain] || resultData.domain;
    domainTitle.innerText = `Detected Career Domain: ${prettyDomain}`;
  }

  const labels = Object.keys(resultData.traits || {});
  const dataValues = Object.values(resultData.traits || {}).map((v) => Number(v) * 100);
  const chartLabels = labels.map((trait) => prettyTraitLabel(trait));
  const ctx = document.getElementById("traitChart");

  if (window.traitChartInstance) {
    window.traitChartInstance.destroy();
  }

  window.traitChartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: chartLabels,
      datasets: [
        {
          label: "Trait Profile",
          data: dataValues,
          backgroundColor: [
            "rgba(135, 206, 235, 0.85)",
            "rgba(255, 160, 122, 0.85)",
            "rgba(144, 238, 144, 0.85)",
            "rgba(100, 149, 237, 0.85)",
            "rgba(255, 218, 185, 0.85)",
            "rgba(176, 224, 230, 0.85)"
          ],
          borderColor: [
            "rgba(135, 206, 235, 1)",
            "rgba(255, 160, 122, 1)",
            "rgba(144, 238, 144, 1)",
            "rgba(100, 149, 237, 1)",
            "rgba(255, 218, 185, 1)",
            "rgba(176, 224, 230, 1)"
          ],
          borderWidth: 1,
          borderRadius: 8,
          barThickness: 24
        }
      ]
    },
    options: {
      indexAxis: "y",
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        x: {
          min: 0,
          max: 100,
          ticks: {
            stepSize: 10,
            callback: function (value) {
              return value + "%";
            }
          },
          grid: {
            color: "rgba(0,0,0,0.08)"
          }
        },
        y: {
          grid: {
            display: false
          }
        }
      }
    }
  });

  const traitList = document.getElementById("trait-list");
  if (traitList) {
    traitList.innerHTML = "";

    labels.forEach((trait, i) => {
      const percent = Number(dataValues[i]).toFixed(1);
      const div = document.createElement("div");
      div.innerHTML = `<strong>${prettyTraitLabel(trait)}</strong>: ${percent}% (${interpretTrait(Number(percent))})`;
      traitList.appendChild(div);
    });
  }

  const rolesContainer = document.getElementById("roles-container");
  rolesContainer.innerHTML = "";

  if (!resultData.recommendations || resultData.recommendations.length === 0) {
    rolesContainer.innerHTML = "<p>No recommendations available.</p>";
  } else {
    resultData.recommendations.slice(0, 3).forEach((roleObj) => {
      const percent = (Number(roleObj.fit_score) * 100).toFixed(1);
      const div = document.createElement("div");
      div.className = "role-card";
      div.innerHTML = `
        <h3>🎯 ${escapeHTML(roleObj.role)}</h3>
        <p><strong>Match Score:</strong> ${percent}%</p>
      `;
      rolesContainer.appendChild(div);
    });
  }

  const aiSection = document.getElementById("ai-section");
  const aiRoleContainer = document.getElementById("ai-role-analysis");
  const aiSkillPlan = document.getElementById("ai-skill-plan");

  if (resultData.ai_role_analysis || resultData.ai_skill_plan) {
    aiRoleContainer.innerHTML = "";

    if (resultData.ai_role_analysis) {
      resultData.ai_role_analysis.forEach((item) => {
        const block = document.createElement("div");
        block.className = "ai-card";
        block.innerHTML = `
          <div class="ai-header">▶️ ${escapeHTML(item.role)}</div>
          <div class="ai-body hidden">
            <pre>${escapeHTML(item.analysis)}</pre>
          </div>
        `;

        const header = block.querySelector(".ai-header");
        const body = block.querySelector(".ai-body");

        header.addEventListener("click", () => {
          body.classList.toggle("hidden");
          header.innerText = body.classList.contains("hidden")
            ? `▶️ ${item.role}`
            : `▼ ${item.role}`;
        });

        aiRoleContainer.appendChild(block);
      });
    }

    if (aiSkillPlan && resultData.ai_skill_plan) {
      aiSkillPlan.innerText = resultData.ai_skill_plan;
    }

    aiSection.classList.remove("hidden");
  } else {
    aiSection.classList.add("hidden");
  }
}

// -----------------------------
// FITCHECK
// -----------------------------
function renderFitcheckDomainList() {
  const container = document.getElementById("fitcheck-domain-list");
  container.innerHTML = "";

  fitcheckDomains.forEach((domain) => {
    const div = document.createElement("div");
    div.className = "domain-card";
    div.innerHTML = `
      <h3>${escapeHTML(domain)}</h3>
      <p>Start a focused psychometric fit check for this domain.</p>
      <button>Start Fit Check</button>
    `;

    div.querySelector("button").addEventListener("click", async () => {
      try {
        selectedFitcheckDomain = { id: domain, name: domain };
        const data = await startFitcheck(domain);
        fitcheckQuestions = data.questions || [];
        fitcheckCurrentIndex = 0;
        fitcheckAnswersMap = {};
        selectedFitcheckOption = null;

        if (!fitcheckQuestions.length) {
          showToast("No Fit Check questions available for this domain.", "warning", "FitCheck");
          return;
        }

        renderFitcheckQuestion();
        showScreen("fitcheck-chat-screen");
      } catch (err) {
        showToast(err.message || "Unable to start FitCheck.", "error", "FitCheck");
      }
    });

    container.appendChild(div);
  });
}

function renderFitcheckQuestion() {
  const question = fitcheckQuestions[fitcheckCurrentIndex];
  if (!question) return;

  const answeredCount = Object.keys(fitcheckAnswersMap).length;
  const progressPercent = fitcheckQuestions.length
    ? (answeredCount / fitcheckQuestions.length) * 100
    : 0;

  setText("fitcheck-domain-heading", `Fit Check Domain: ${selectedFitcheckDomain?.name || ""}`);

  document.getElementById("fitcheck-progress-fill").style.width = `${progressPercent}%`;
  setText(
    "fitcheck-progress",
    `${fitcheckCurrentIndex + 1} / ${fitcheckQuestions.length} • ${Math.round(progressPercent)}% COMPLETE`
  );
  setText("fitcheck-question-text", question.text);

  const options = [
  { label: "Strongly Agree", value: "Strongly Agree" },
  { label: "Agree", value: "Agree" },
  { label: "Neutral", value: "Neutral" },
  { label: "Disagree", value: "Disagree" },
  { label: "Strongly Disagree", value: "Strongly Disagree" }
];

  selectedFitcheckOption =
    fitcheckAnswersMap[fitcheckCurrentIndex] !== undefined
      ? fitcheckAnswersMap[fitcheckCurrentIndex]
      : null;

  const container = document.getElementById("fitcheck-options");
  container.innerHTML = "";

  options.forEach((opt) => {
    const btn = document.createElement("button");
    btn.className = "likert-btn";
    btn.type = "button";
    btn.innerText = opt.label;

    if (selectedFitcheckOption === opt.value) {
      btn.style.borderColor = "#4a90e2";
    }

    btn.addEventListener("click", () => {
      document
        .querySelectorAll("#fitcheck-options .likert-btn")
        .forEach((b) => (b.style.borderColor = "transparent"));

      btn.style.borderColor = "#4a90e2";
      selectedFitcheckOption = opt.value;
      fitcheckAnswersMap[fitcheckCurrentIndex] = opt.value
        .toLowerCase()
        .replaceAll(" ", "_");

      const updatedAnsweredCount = Object.keys(fitcheckAnswersMap).length;
      const updatedProgressPercent = fitcheckQuestions.length
        ? (updatedAnsweredCount / fitcheckQuestions.length) * 100
        : 0;

      document.getElementById("fitcheck-progress-fill").style.width = `${updatedProgressPercent}%`;
      setText(
        "fitcheck-progress",
        `${fitcheckCurrentIndex + 1} / ${fitcheckQuestions.length} • ${Math.round(updatedProgressPercent)}% COMPLETE`
      );
    });

    container.appendChild(btn);
  });

  const prevBtn = document.getElementById("fitcheck-prev-btn");
  if (prevBtn) {
    prevBtn.disabled = fitcheckCurrentIndex === 0;
    prevBtn.style.opacity = fitcheckCurrentIndex === 0 ? "0.5" : "1";
    prevBtn.style.cursor = fitcheckCurrentIndex === 0 ? "not-allowed" : "pointer";
  }
}

function goToNextFitcheckQuestion() {
  if (selectedFitcheckOption === null) {
    showToast("Please select an option before continuing.", "warning", "Fit Check");
    return;
  }

  fitcheckAnswersMap[fitcheckCurrentIndex] = selectedFitcheckOption;

  if (fitcheckCurrentIndex < fitcheckQuestions.length - 1) {
    fitcheckCurrentIndex++;
    renderFitcheckQuestion();
  } else {
    const fitcheckAnswers = fitcheckQuestions.map((q, index) => ({
     trait: q.trait,
     answer: fitcheckAnswersMap[index]
    }));

    submitFitcheckFlow(fitcheckAnswers);
  }
}

async function submitFitcheckFlow(fitcheckAnswers) {
  const fitcheckNextBtn = document.getElementById("fitcheck-next-btn");
  setButtonLoading(fitcheckNextBtn, true, "Submitting...");

  try {
    showScreen("loading-screen");
    const data = await submitFitcheck(selectedFitcheckDomain.id, fitcheckAnswers);
    renderFitcheckResult(data);
    selectedFitcheckOption = null;
    showScreen("fitcheck-result-screen");
    showToast("Fit Check result generated successfully.", "success", "FitCheck");
  } catch (err) {
    console.error(err);
    showToast(err.message || "Unable to generate Fit Check result.", "error", "FitCheck");
    showScreen("welcome-screen");
  } finally {
    setButtonLoading(fitcheckNextBtn, false);
  }
}

function renderFitcheckResult(data) {
  setText("fit check-domain-title", `Domain: ${selectedFitcheckDomain.name}`);

  const fitPercent = Number(data.fit_score) * 100;
  setText("fit-score-value", `${fitPercent.toFixed(1)}%`);

  const fitScoreBox = document.querySelector(".fit-score-box");
  if (fitScoreBox) {
    fitScoreBox.classList.remove("low-fit", "medium-fit", "high-fit");

    if (fitPercent < 50) {
      fitScoreBox.classList.add("low-fit");
    } else if (fitPercent < 75) {
      fitScoreBox.classList.add("medium-fit");
    } else {
      fitScoreBox.classList.add("high-fit");
    }
  }

  // Traits
  const traitContainer = document.getElementById("fitcheck-traits");
  traitContainer.innerHTML = "";

  Object.entries(data.trait_scores || {}).forEach(([trait, value]) => {
    const percent = (Number(value) * 100).toFixed(1);
    const div = document.createElement("div");
    div.innerHTML = `<strong>${prettyTraitLabel(trait)}</strong>: ${percent}%`;
    traitContainer.appendChild(div);
  });

  // 🔥 FIXED FEEDBACK DISPLAY
  if (typeof data.feedback === "string") {
    const parsed = parseFeedback(data.feedback);

    setText("fit-strengths", parsed.strengths || "-");
    setText("fit-weaknesses", parsed.weaknesses || "-");
    setText("fit-advice", parsed.advice || "-");
    setText("fit-projects", parsed.projects || "-");
  } else {
    setText("fit-strengths", "-");
    setText("fit-weaknesses", "-");
    setText("fit-advice", "-");
    setText("fit-projects", "-");
  }
}
// -----------------------------
// EXPLORE
// -----------------------------
function renderExploreDomainGrid() {
  const grid = document.getElementById("explore-domain-grid");
  grid.innerHTML = "";

  exploreDomains.forEach((domain) => {
    const card = document.createElement("div");
    card.className = "domain-card";
    card.innerHTML = `
      <h3>${escapeHTML(domain.name)}</h3>
      <p>View roadmap, tools, concepts, projects, and resources.</p>
      <button>Open Domain</button>
    `;

    card.querySelector("button").addEventListener("click", async () => {
      try {
        currentExploreDomain = await getExploreDetail(domain.id);
        renderExploreDetail(currentExploreDomain);
      } catch (err) {
        showToast(err.message || "Unable to load domain details.", "error", "Explore");
      }
    });

    grid.appendChild(card);
  });
}

function renderExploreDetail(domain) {
  const detail = document.getElementById("explore-detail");
  if (!domain) return;

  detail.classList.remove("hidden");

  const conceptsHTML = (domain.core_concepts || [])
    .map(
      (concept, index) => `
        <div class="mini-card">
          <h4>${escapeHTML(concept.title)}</h4>
          <p>${escapeHTML(concept.content)}</p>
          <button type="button" class="explain-btn" data-concept-index="${index}">Explain More</button>
          <div class="small-loading hidden" id="concept-loading-${index}">Loading AI explanation...</div>
          <div class="ai-card hidden" id="concept-expand-${index}"></div>
        </div>
      `
    )
    .join("");

  const toolsHTML = (domain.tools || [])
    .map((tool) => `<span class="tag">${escapeHTML(tool)}</span>`)
    .join("");

  const beginnerHTML = (domain.roadmap?.beginner || [])
    .map((item) => `<li>${escapeHTML(item)}</li>`)
    .join("");

  const intermediateHTML = (domain.roadmap?.intermediate || [])
    .map((item) => `<li>${escapeHTML(item)}</li>`)
    .join("");

  const advancedHTML = (domain.roadmap?.advanced || [])
    .map((item) => `<li>${escapeHTML(item)}</li>`)
    .join("");

  const projectsHTML = (domain.projects || [])
    .map(
      (project) => `
        <div class="mini-card">
          <h4>${escapeHTML(project.name)}</h4>
          <p>${escapeHTML(project.description)}</p>
          <p><strong>Steps:</strong></p>
          <ul class="clean-list">
            ${(project.steps || []).map((s) => `<li>${escapeHTML(s)}</li>`).join("")}
          </ul>
          <p><strong>Tech Stack:</strong> ${(project.tech_stack || []).map(escapeHTML).join(", ")}</p>
        </div>
      `
    )
    .join("");

  const interviewHTML = (domain.interview_prep || [])
    .map((item) => `<li>${escapeHTML(item)}</li>`)
    .join("");

  const resourcesHTML = (domain.resources || [])
    .map((item) => `<li>${escapeHTML(item)}</li>`)
    .join("");

  detail.innerHTML = `
    <div class="section-block">
      <h2>${escapeHTML(domain.name)}</h2>
    </div>

    <div class="section-block">
      <h3>Overview</h3>
      <p>${escapeHTML(domain.overview || "")}</p>
    </div>

    <div class="section-block">
      <h3>Why this domain</h3>
      <p>${escapeHTML(domain.why_this_domain || "")}</p>
    </div>

    <div class="section-block">
      <h3>Core Concepts</h3>
      ${conceptsHTML || "<p>No concepts available.</p>"}
    </div>

    <div class="section-block">
      <h3>Tools</h3>
      <div class="tag-list">${toolsHTML || "<p>No tools available.</p>"}</div>
    </div>

    <div class="section-block">
      <h3>Roadmap</h3>
      <div class="feedback-grid">
        <div class="feedback-card">
          <h4>Beginner</h4>
          <ul class="clean-list">${beginnerHTML}</ul>
        </div>
        <div class="feedback-card">
          <h4>Intermediate</h4>
          <ul class="clean-list">${intermediateHTML}</ul>
        </div>
        <div class="feedback-card">
          <h4>Advanced</h4>
          <ul class="clean-list">${advancedHTML}</ul>
        </div>
      </div>
    </div>

    <div class="section-block">
      <h3>Projects</h3>
      ${projectsHTML || "<p>No projects available.</p>"}
    </div>

    <div class="section-block">
      <h3>Interview Prep</h3>
      <ul class="clean-list">${interviewHTML}</ul>
    </div>

    <div class="section-block">
      <h3>Resources</h3>
      <ul class="clean-list">${resourcesHTML}</ul>
    </div>
  `;

  attachExplainMoreHandlers(domain);
}

function attachExplainMoreHandlers(domain) {
  const buttons = document.querySelectorAll(".explain-btn");

  buttons.forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (btn.dataset.loading === "true") return;

      btn.dataset.loading = "true";
      btn.disabled = true;
      btn.innerText = "Generating...";

      const index = btn.getAttribute("data-concept-index");
      const concept = domain.core_concepts[index];

      const loadingEl = document.getElementById(`concept-loading-${index}`);
      const outputEl = document.getElementById(`concept-expand-${index}`);

      loadingEl.classList.remove("hidden");
      outputEl.classList.add("hidden");
      outputEl.innerHTML = "";

      try {
        const response = await expandConcept(domain.id, concept.title);
        loadingEl.classList.add("hidden");
        outputEl.classList.remove("hidden");
        outputEl.innerText = response?.data?.explanation || "No explanation available.";
      } catch (err) {
        loadingEl.classList.add("hidden");
        outputEl.classList.remove("hidden");
        outputEl.innerText = err.message || "Unable to load explanation.";
      } finally {
        btn.dataset.loading = "false";
        btn.disabled = false;
        btn.innerText = "Explain More";
      }
    });
  });
}

// -----------------------------
// DOM READY
// -----------------------------
document.addEventListener("DOMContentLoaded", async () => {
  const profileBtn = document.getElementById("profile-btn");
  const profileMenu = document.getElementById("profile-menu");
  const themeBtn = document.getElementById("theme-toggle");
  const homeBtn = document.getElementById("home-btn");
  const toggleAuth = document.getElementById("toggle-auth");
  const authBtn = document.getElementById("auth-submit-btn");
  const togglePasswordBtn = document.getElementById("toggle-password");
  const passwordField = document.getElementById("password");
  const submitAssessmentBtn = document.getElementById("submit-btn");

  accessToken = localStorage.getItem("access_token");

  // Profile menu
  if (profileBtn && profileMenu) {

  profileBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    profileMenu.classList.toggle("hidden");
  });

  profileMenu.addEventListener("click", (e) => {
    e.stopPropagation();
  });

  document.addEventListener("click", () => {
    profileMenu.classList.add("hidden");
  });

}

  // Theme toggle
  const savedTheme = localStorage.getItem("theme_mode");
  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
    if (themeBtn) themeBtn.innerText = "☀️";
  }

  themeBtn?.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
      themeBtn.innerText = "☀️";
      localStorage.setItem("theme_mode", "dark");
    } else {
      themeBtn.innerText = "🌙";
      localStorage.setItem("theme_mode", "light");
    }
  });

  // Show / Hide password
  togglePasswordBtn?.addEventListener("click", () => {
    const showPassword = passwordField?.type === "password";
    setPasswordVisibility(showPassword);
  });

  passwordField?.addEventListener("blur", () => {
    if (!passwordField.value) {
      setPasswordVisibility(false);
    }
  });

  // Auth toggle
  toggleAuth?.addEventListener("click", () => {
    clearAuthFields();
    setAuthMode(!isRegisterMode);
  });

  // Enter key submit
  document.getElementById("email")?.addEventListener("keydown", (e) => {
    if (e.key === "Enter") authBtn?.click();
  });

  passwordField?.addEventListener("keydown", (e) => {
    if (e.key === "Enter") authBtn?.click();
  });

  document.getElementById("name-field")?.addEventListener("keydown", (e) => {
    if (e.key === "Enter") authBtn?.click();
  });

  // Login / Register
  authBtn?.addEventListener("click", async () => {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const name = document.getElementById("name-field").value.trim();

    if (!email || !password) {
      showToast("Please fill in email and password.", "warning", "Required Fields");
      return;
    }

    try {
      if (isRegisterMode) {
        if (!name) {
          showToast("Please enter your full name.", "warning", "Required Fields");
          return;
        }

        setButtonLoading(authBtn, true, "Registering...");
        await registerUser({ name, email, password });
        showToast("Registration successful. Please login.", "success", "Account Created");

        clearAuthFields();
        document.getElementById("email").value = email;
        setAuthMode(false);
        return;
      }

      setButtonLoading(authBtn, true, "Logging in...");
      const data = await loginUser(email, password);

      if (!data?.access_token) {
        throw new Error("Token not received from login API");
      }

      localStorage.setItem("access_token", data.access_token);
      accessToken = data.access_token;

      clearAuthFields();
      showScreen("welcome-screen");
      await loadUserProfile();
      showToast("Login successful. Welcome back!", "success", "Welcome");
    } catch (err) {
      showToast(err.message || "Something went wrong.", "error", "Authentication");
    } finally {
      setButtonLoading(authBtn, false);
    }
  });

  // Logout
  document.getElementById("logout-btn")?.addEventListener("click", () => {
    localStorage.removeItem("access_token");
    accessToken = null;

    resetExploreState();
    resetFitcheckState();
    clearAuthFields();
    setAuthMode(false);
    showToast("You have been logged out successfully.", "success", "Logout");
    showScreen("auth-screen");
  });

  // Home button
  homeBtn?.addEventListener("click", () => {
    if (homeBtn.disabled) return;
    resetExploreState();
    showScreen("welcome-screen");
  });

  document.getElementById("back-home-from-submit")?.addEventListener("click", () => {
    showScreen("welcome-screen");
  });

  document.getElementById("back-fitcheck-to-domain")?.addEventListener("click", () => {
    fitcheckCurrentIndex = 0;
    fitcheckAnswersMap = {};
    selectedFitcheckOption = null;
    showScreen("fitcheck-domain-screen");
  });

  // Assessment
  document.getElementById("start-btn")?.addEventListener("click", async () => {
    if (!accessToken) {
      showToast("Please login first to start the assessment.", "warning", "Login Required");
      showScreen("auth-screen");
      return;
    }

    try {
      questions = await getQuestions();
      answers = [];
      currentQuestionIndex = 0;
      selectedOption = null;
      selectedAnswersMap = {};

      if (!questions.length) {
        showToast("No assessment questions available.", "warning", "Assessment");
        return;
      }

      showScreen("question-screen");
      renderQuestion();
    } catch (err) {
      showToast(err.message || "Unable to load assessment questions.", "error", "Assessment");
    }
  });

  document.getElementById("next-btn")?.addEventListener("click", goToNextQuestion);

  document.getElementById("prev-btn")?.addEventListener("click", () => {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex--;
      renderQuestion();
    }
  });

  submitAssessmentBtn?.addEventListener("click", async () => {
    setButtonLoading(submitAssessmentBtn, true, "Submitting...");
    showToast("Submitting your assessment for analysis...", "info", "Assessment");
    showScreen("loading-screen");

    try {
      resultData = await analyzeAssessment({ answers });

      if (!resultData) {
        throw new Error("No results received");
      }

      showScreen("results-screen");
      renderResults();
    } catch (err) {
      console.error(err);
      showToast(err.message || "Something went wrong while generating results.", "error", "Assessment");
      showScreen("welcome-screen");
    } finally {
      setButtonLoading(submitAssessmentBtn, false);
    }
  });

  document.getElementById("restart-btn")?.addEventListener("click", () => {
    questions = [];
    answers = [];
    currentQuestionIndex = 0;
    selectedOption = null;
    resultData = null;
    selectedAnswersMap = {};

    if (window.traitChartInstance) {
      window.traitChartInstance.destroy();
      window.traitChartInstance = null;
    }

    showScreen("welcome-screen");
  });

  // FitCheck
  document.getElementById("open-fitcheck-btn")?.addEventListener("click", async () => {
    if (!accessToken) {
      showToast("Please login first to open FitCheck.", "warning", "Login Required");
      showScreen("auth-screen");
      return;
    }

    try {
      const fitcheckData = await getFitcheckDomains();
      fitcheckDomains = fitcheckData.domains || [];
      if (!fitcheckDomains.length) {
        showToast("No domains available.", "warning", "FitCheck");
        return;
      }

      renderFitcheckDomainList();
      showScreen("fitcheck-domain-screen");
    } catch (err) {
      showToast(err.message || "Unable to load Fit Check domains.", "error", "FitCheck");
    }
  });

  document.getElementById("fitcheck-next-btn")?.addEventListener("click", goToNextFitcheckQuestion);

  document.getElementById("fitcheck-prev-btn")?.addEventListener("click", () => {
    if (fitcheckCurrentIndex > 0) {
      fitcheckCurrentIndex--;
      renderFitcheckQuestion();
    }
  });

  // Explore
  document.getElementById("open-explore-btn")?.addEventListener("click", async () => {
    if (!accessToken) {
      showToast("Please login first to explore domains.", "warning", "Login Required");
      showScreen("auth-screen");
      return;
    }

    try {
      exploreDomains = await getExploreDomains();

      if (!exploreDomains.length) {
        showToast("No domains available.", "warning", "Explore");
        return;
      }

      renderExploreDomainGrid();
      document.getElementById("explore-detail").classList.add("hidden");
      showScreen("explore-screen");
    } catch (err) {
      showToast(err.message || "Unable to load domains.", "error", "Explore");
    }
  });
    if (accessToken) {
    showScreen("welcome-screen");
    loadUserProfile();
  } else {
    showScreen("auth-screen");
    clearAuthFields();
    setAuthMode(false);
  }
});
