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
// LOGIN / REGISTER
// -----------------------------
document.getElementById("auth-submit-btn")?.addEventListener("click", async () => {

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Please fill all required fields");
    return;
  }

  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: formData
  });

  const data = await res.json();

  if (res.ok) {
    localStorage.setItem("access_token", data.access_token);
    accessToken = data.access_token;
    showScreen("welcome-screen");
    await loadUserProfile();
  } else {
    alert("Invalid credentials");
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
// RENDER RESULTS (BAR CHART)
// -----------------------------
function renderResults() {

  const labels = Object.keys(resultData.traits);
  const dataValues = Object.values(resultData.traits);

  const ctx = document.getElementById("traitChart");

  if (window.traitChartInstance) {
    window.traitChartInstance.destroy();
  }

  window.traitChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Trait Level',
        data: dataValues
      }]
    },
    options: {
      indexAxis: 'y',
      scales: {
        x: {
          min: 0,
          max: 1
        }
      }
    }
    
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