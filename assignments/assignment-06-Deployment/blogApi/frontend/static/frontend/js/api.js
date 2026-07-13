const API_BASE = "https://blogwebapi.pythonanywhere.com/api";

function getAccessToken() {
    return localStorage.getItem("access_token");
}

function isLoggedIn() {
    return getAccessToken() !== null;
}

async function apiFetch(path, options = {}) {
    const token = getAccessToken();

    const headers = {
        "Content-Type": "application/json",
        ...options.headers,
    };

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(`${API_BASE}${path}`, {
        ...options,
        headers,
    });

    return response;
}



function updateNav() {
    const loginLink = document.getElementById("nav-login");
    const registerLink = document.getElementById("nav-register");
    const logoutLink = document.getElementById("nav-logout");

    if (isLoggedIn()) {
        loginLink.style.display = "none";
        registerLink.style.display = "none";
        logoutLink.style.display = "inline";

        logoutLink.addEventListener("click", function (event) {
            event.preventDefault();
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            window.location.href = "/login/";
        });
    }
}

updateNav();

function getCurrentUserId() {
    const token = getAccessToken();
    if (!token) return null;

    try {
        const payload = token.split(".")[1];
        const decoded = JSON.parse(atob(payload));
        return decoded.user_id;
    } catch (error) {
        return null;
    }
}
async function getCurrentUser() {
    if (!isLoggedIn()) {
        return null;
    }

    try {
        const response = await apiFetch("/me/");

        if (!response.ok) {
            return null;
        }

        const user = await response.json();

        return user;

    } catch (error) {
        console.error(error);
        return null;
    }
}