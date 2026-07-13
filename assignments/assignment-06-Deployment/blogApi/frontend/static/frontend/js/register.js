//const API_BASE = "https://blogwebapi.pythonanywhere.com/api";

const registerForm = document.getElementById("register-form");
const registerMessage = document.getElementById("register-message");

registerForm.addEventListener("submit", async function (event) {
    event.preventDefault();


    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;


    try {
        const response = await fetch(`${API_BASE}/register/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, email, password }),
            });
        const data = await response.json();

        if (response.ok) {
            registerMessage.textContent = "Account created! Redirecting to login...";
            setTimeout(() => {
                window.location.href = "/login/";
            }, 1500);
            
        } else {
            registerMessage.textContent = "Registration failed: " + JSON.stringify(data);
        }
    } catch (error) {
        registerMessage.textContent = "Something went wrong. Try again.";
        console.error(error);
    }
    
});