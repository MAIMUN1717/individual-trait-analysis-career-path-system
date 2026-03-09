const API_BASE = "http://localhost:8000";

let accessToken = localStorage.getItem("access_token");
let questions = [];
let answers = [];
let currentQuestionIndex = 0;
let selectedOption = null;
let resultData = null;
let isRegisterMode = false;

// -----------------------------
// Screen switch helper
// -----------------------------
function showScreen(id) {
  document.querySelectorAll(".screen").forEach(s => s.classList.remove("active"));
  const el = document.getElementById(id);
  if (el) el.classList.add("active");
}

// -----------------------------
// LOAD PROFILE + RESULTS
// -----------------------------
async function loadUserProfile() {

  if (!accessToken) return;

  try {
    const profileRes = await fetch(`${API_BASE}/profile`, {
      headers: { "Authorization": `Bearer ${accessToken}` }
    });

    if (!profileRes.ok) return;

    const user = await profileRes.json();

    const nameEl = document.getElementById("profile-name");
    const emailEl = document.getElementById("profile-email");

    if (nameEl) nameEl.innerText = user.name;
    if (emailEl) emailEl.innerText = user.email;

    const resultsRes = await fetch(`${API_BASE}/my-results`, {
      headers: { "Authorization": `Bearer ${accessToken}` }
    });

    if (!resultsRes.ok) return;

    const results = await resultsRes.json();
    const container = document.getElementById("previous-results");

    if (!container) return;

    container.innerHTML = "";

    if (results.length === 0) {
      container.innerHTML = "<p>No previous results</p>";
      return;
    }

    results.forEach(r => {
      const div = document.createElement("div");
      div.style.padding = "6px 0";
      div.style.borderBottom = "1px solid #eee";
      div.innerHTML = `
        <strong>${r.top_role}</strong><br>
        <small>Score: ${(r.top_score * 100).toFixed(1)}%</small>
      `;
      container.appendChild(div);
    });

  } catch (err) {
    console.error("Profile load error:", err);
  }
}

// -----------------------------
// AUTO AUTH CHECK
// -----------------------------
window.onload = async () => {

  const profileBtn = document.getElementById("profile-btn");

  if (!accessToken) {
    showScreen("auth-screen");
    if (profileBtn) profileBtn.classList.add("hidden");
    return;
  }

  showScreen("welcome-screen");

  if (profileBtn) profileBtn.classList.remove("hidden");

  await loadUserProfile();
};

// -----------------------------
// PROFILE MENU TOGGLE
// -----------------------------
const profileBtn = document.getElementById("profile-btn");
const profileMenu = document.getElementById("profile-menu");

if (profileBtn && profileMenu) {

  profileBtn.addEventListener("click", () => {
    profileMenu.classList.toggle("hidden");
  });

  // Close menu if clicking outside
  document.addEventListener("click", (e) => {
    if (!profileBtn.contains(e.target) && !profileMenu.contains(e.target)) {
      profileMenu.classList.add("hidden");
    }
  });
}

// -----------------------------
// AUTH TOGGLE (Login <-> Register)
// -----------------------------
const authTitle = document.getElementById("auth-title");
const toggleAuth = document.getElementById("toggle-auth");
const nameField = document.getElementById("name-field");
const authBtn = document.getElementById("auth-submit-btn");

if (toggleAuth) {
  toggleAuth.addEventListener("click", () => {
    isRegisterMode = !isRegisterMode;

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
  });
}

// -----------------------------
// LOGIN / REGISTER HANDLER
// -----------------------------
authBtn?.addEventListener("click", async () => {

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const name = document.getElementById("name-field").value.trim();

  if (!email || !password) {
    alert("Please fill required fields");
    return;
  }

  try {

    if (isRegisterMode) {

      if (!name) {
        alert("Please enter your full name");
        return;
      }

      const registerRes = await fetch(`${API_BASE}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name,
          email: email,
          password: password
        })
      });

      if (!registerRes.ok) {
        const err = await registerRes.json();
        alert(err.detail || "Registration failed");
        return;
      }

      alert("Registration successful. Please login.");
      isRegisterMode = false;
      authTitle.innerText = "Login";
      nameField.style.display = "none";
      authBtn.innerText = "Login";
      toggleAuth.innerText = "Don't have an account? Register";
      return;

    } else {

      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", password);

      const loginRes = await fetch(`${API_BASE}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData
      });

      const data = await loginRes.json();

      if (!loginRes.ok) {
        alert("Invalid credentials");
        return;
      }

      localStorage.setItem("access_token", data.access_token);
      accessToken = data.access_token;

      document.getElementById("profile-btn")?.classList.remove("hidden");

      showScreen("welcome-screen");
      await loadUserProfile();
    }

  } catch (err) {
    console.error("Auth error:", err);
    alert("Something went wrong.");
  }

});

// -----------------------------
// LOGOUT
// -----------------------------
document.getElementById("logout-btn")?.addEventListener("click", () => {
  localStorage.removeItem("access_token");
  accessToken = null;

  document.getElementById("profile-btn")?.classList.add("hidden");
  document.getElementById("profile-menu")?.classList.add("hidden");

  showScreen("auth-screen");
});

// -----------------------------
// START ASSESSMENT
// -----------------------------
document.getElementById("start-btn")?.addEventListener("click", async () => {

  if (!accessToken) {
    alert("Please login first");
    showScreen("auth-screen");
    return;
  }

  const res = await fetch(`${API_BASE}/questions`);
  questions = await res.json();
  answers = [];
  currentQuestionIndex = 0;
  showScreen("question-screen");
  renderQuestion();
});

// -----------------------------
// RENDER QUESTION
// -----------------------------
function renderQuestion() {

  const q = questions[currentQuestionIndex];
  const progressPercent = ((currentQuestionIndex + 1) / questions.length) * 100;

  document.getElementById("progress-fill").style.width = progressPercent + "%";
  document.getElementById("question-text").innerText = q.text;
  document.getElementById("progress").innerText =
    Math.round(progressPercent) + "% COMPLETE";

  const container = document.getElementById("options-container");
  container.innerHTML = "";
  selectedOption = null;

  q.options.forEach((opt, i) => {
    const div = document.createElement("div");
    div.className = "option";
    div.innerText = opt;
    div.onclick = () => {
      document.querySelectorAll(".option").forEach(o => o.classList.remove("selected"));
      div.classList.add("selected");
      selectedOption = i;
    };
    container.appendChild(div);
  });
}

// -----------------------------
// NEXT BUTTON
// -----------------------------
document.getElementById("next-btn")?.addEventListener("click", () => {

  if (selectedOption === null) return alert("Please select an option");

  answers.push({
    question_id: questions[currentQuestionIndex].id,
    selected_option: selectedOption
  });

  currentQuestionIndex++;

  if (currentQuestionIndex < questions.length) {
    renderQuestion();
  } else {
    showScreen("submit-screen");
  }
});

// -----------------------------
// SUBMIT
// -----------------------------
document.getElementById("submit-btn")?.addEventListener("click", async () => {

  showScreen("loading-screen");

  const res = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${accessToken}`
    },
    body: JSON.stringify({ answers })
  });

  resultData = await res.json();
  showScreen("results-screen");
  renderResults();
});


// -----------------------------
// RENDER RESULTS (BAR CHART + TOP 3 WITH EXPLANATION)
// -----------------------------
function renderResults() {
  const domainTitle = document.getElementById("domain-title");

  if (domainTitle && resultData.domain) {
    const domainNames = {
  ai_data: "AI / Data Science",
  software_engineering: "Software Engineering",
  cloud_devops: "Cloud & DevOps",
  cybersecurity: "Cybersecurity",
  product_design: "Product & Product Strategy"
};

const prettyDomain = domainNames[resultData.domain] || resultData.domain;

domainTitle.innerText = "Detected Career Domain: " + prettyDomain;
  }

  // --------------------
  // Render Trait Chart
  // --------------------
  const labels = Object.keys(resultData.traits);

  // Pretty trait labels
  const traitLabels = {
    analytical_reasoning: "Analytical Reasoning",
    problem_framing: "Problem Framing",
    learning_agility: "Learning Agility",
    attention_control: "Attention Control",
    creativity: "Creativity",
    decision_style: "Decision Style"
  };

  // Psychometric interpretation
  function interpretTrait(score) {

    if (score < 40) return "Emerging";
    if (score < 60) return "Developing";
    if (score < 80) return "Strong";

    return "Exceptional";
  }
  const dataValues = Object.values(resultData.traits).map(v => v * 100);
  const ctx = document.getElementById("traitChart");

  // Destroy old chart if it exists
if (window.traitChartInstance) {
  window.traitChartInstance.destroy();
}

// Create radar chart
window.traitChartInstance = new Chart(ctx, {
  type: 'radar',
  data: {
    labels: labels,
    datasets: [{
      label: 'Trait Profile',
      data: dataValues,
      fill: true,
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgb(54, 162, 235)',
      pointBackgroundColor: 'rgb(54, 162, 235)',
      borderWidth: 2
    }]
  },
  options: {
    scales: {
      r: {
        min: 0,
        max: 100,
        ticks: {
          stepSize: 20
        }
      }
    }
  }
});

// ---------------------
// Render Trait Percentages
// ---------------------
const traitList = document.getElementById("trait-list");

if (traitList) {
  traitList.innerHTML = "";

  labels.forEach((trait, i) => {
    const percent = (dataValues[i]).toFixed(1);

    const div = document.createElement("div");
    const label = traitLabels[trait] || trait;
    const interpretation = interpretTrait(percent);

    div.innerHTML = `<strong>${label}</strong>: ${percent}% (${interpretation})`;

    traitList.appendChild(div);
  });
}

  // --------------------
  // Render Top Roles
  // --------------------
  const rolesContainer = document.getElementById("roles-container");
  rolesContainer.innerHTML = "";

  if (!resultData.recommendations || resultData.recommendations.length === 0) {
    rolesContainer.innerHTML = "<p>No recommendations available.</p>";
    return;
  }

resultData.recommendations.slice(0,3).forEach((roleObj, index) => {
    const percent = (roleObj.fit_score * 100).toFixed(1);

    let explanationHTML = "";

    if (roleObj.explanation && typeof roleObj.explanation === "object") {

      const exp = roleObj.explanation;

      if (exp.summary) {
        explanationHTML += `<p style="margin-top:10px;">${exp.summary}</p>`;
      }

      if (exp.strengths && exp.strengths.length > 0) {
        explanationHTML += `
          <p><strong>Strengths:</strong></p>
          <ul>
            ${exp.strengths.map(s => `<li>${s}</li>`).join("")}
          </ul>
        `;
      }

      if (exp.gaps && exp.gaps.length > 0) {
        explanationHTML += `
          <p><strong>Areas to Improve:</strong></p>
          <ul>
            ${exp.gaps.map(g => `<li>${g}</li>`).join("")}
          </ul>
        `;
      }

      if (exp.growth_suggestions && exp.growth_suggestions.length > 0) {
        explanationHTML += `
          <p><strong>Growth Suggestions:</strong></p>
          <ul>
            ${exp.growth_suggestions.map(gs => `<li>${gs}</li>`).join("")}
          </ul>
        `;
      }

    } else if (typeof roleObj.explanation === "string") {
      explanationHTML = `<p>${roleObj.explanation}</p>`;
    }

    const div = document.createElement("div");
    div.className = "role-card slide-in";

    div.innerHTML = `
      <h3>#${index + 1} ${roleObj.role}</h3>
      <p><strong>Match Score:</strong> ${percent}%</p>
      ${explanationHTML}
    `;

    rolesContainer.appendChild(div);
  });
}
document.addEventListener("DOMContentLoaded", () => {

  const themeBtn = document.getElementById("theme-toggle");

  if (themeBtn) {
    themeBtn.addEventListener("click", () => {

      document.body.classList.toggle("dark-mode");

      // Optional: change icon dynamically
      if (document.body.classList.contains("dark-mode")) {
        themeBtn.innerText = "☀️";
      } else {
        themeBtn.innerText = "🌙";
      }

    });
  }

});

const restartBtn = document.getElementById("restart-btn");

if (restartBtn) {
  restartBtn.addEventListener("click", () => {
    questions = [];
    answers = [];
    currentQuestionIndex = 0;
    selectedOption = null;
    resultData = null;

    if (window.traitChartInstance) {
      window.traitChartInstance.destroy();
    }

    showScreen("welcome-screen");
  });
}