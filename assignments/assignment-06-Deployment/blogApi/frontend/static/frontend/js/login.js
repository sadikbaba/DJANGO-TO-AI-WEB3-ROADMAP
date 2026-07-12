const API_BASE = "https://blogwebapi.pythonanywhere.com/api";

const loginForm = document.getElementById("login-form");
const loginMessage = document.getElementById("login-message");

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(`${API_BASE}/token/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("access_token", data.access);
            localStorage.setItem("refresh_token", data.refresh);
            loginMessage.textContent = "Login successful! Redirecting...";
            window.location.href = "/";
        } else {
            loginMessage.textContent = "Login failed. Check your username and password.";
        }
    } catch (error) {
        loginMessage.textContent = "Something went wrong. Try again.";
        console.error(error);
    }
});