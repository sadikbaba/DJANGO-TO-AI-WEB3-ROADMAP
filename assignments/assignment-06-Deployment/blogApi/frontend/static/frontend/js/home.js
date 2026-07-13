async function loadCategories() {
    const select = document.getElementById("category");

    try {
        const response = await apiFetch("/categories/");
        const data = await response.json();

        select.innerHTML = "";

        if (data.results.length === 0) {
            select.innerHTML = '<option value="">No categories yet</option>';
            return;
        }

        data.results.forEach(function (category) {
            const option = document.createElement("option");
            option.value = category.id;
            option.textContent = category.name;
            select.appendChild(option);
        });

    } catch (error) {
        select.innerHTML = '<option value="">Could not load categories</option>';
        console.error(error);
    }
}

function setupAutoResizeTextarea() {
    const textarea = document.getElementById("content");

    if (!textarea) {
        return;
    }

    textarea.addEventListener("input", function () {
        this.style.height = "auto";
        this.style.height = this.scrollHeight + "px";
    });
}

function setupCreatePostForm() {
    const section = document.getElementById("create-post-section");
    const form = document.getElementById("create-post-form");
    const message = document.getElementById("create-post-message");

    if (!isLoggedIn()) {
        return;
    }

    section.style.display = "block";
    loadCategories();

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;
        const category = document.getElementById("category").value;

        try {
            const response = await apiFetch("/posts/", {
                method: "POST",
                body: JSON.stringify({ title, content, category }),
            });

            const data = await response.json();

            if (response.ok) {
                message.textContent = "Post created!";
                form.reset();
                loadPosts();
            } else {
                message.textContent = "Failed: " + JSON.stringify(data);
            }
        } catch (error) {
            message.textContent = "Something went wrong.";
            console.error(error);
        }
    });
}



setupCreatePostForm();
setupAutoResizeTextarea();

async function loadPosts() {
    const container = document.getElementById("posts-container");

    try {
        const response = await apiFetch("/posts/");
        const data = await response.json();

        if (!response.ok) {
            container.innerHTML = "<p>Could not load posts.</p>";
            return;
        }

        const posts = data.results;

        if (posts.length === 0) {
            container.innerHTML = "<p>No posts yet.</p>";
            return;
        }

        container.innerHTML = "";

        posts.forEach(function (post) {
            const postElement = document.createElement("div");
            postElement.classList.add("post");

            postElement.innerHTML = `
                <div class="post-card">

                    <div class="post-header">
                        <h3>${post.title}</h3>
                        <p class="post-meta">
                            By ${post.author} in ${post.category_name}
                        </p>
                    </div>

                    <div class="post-body">
                        <p>${post.content}</p>
                    </div>

                    <div class="post-footer">
                    </div>

                </div>
            `;

             if (isLoggedIn() && String(post.author_id) === String(getCurrentUserId())) {
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", async function () {
            const confirmed = confirm("Delete this post?");
            if (!confirmed) return;

            const response = await apiFetch(`/posts/${post.id}/`, {
                method: "DELETE",
            });

            if (response.ok) {
                loadPosts();
            } else {
                alert("Could not delete post.");
            }
        });

        postElement.appendChild(deleteButton);
    }

            container.appendChild(postElement);
        });

    } catch (error) {
        container.innerHTML = "<p>Something went wrong loading posts.</p>";
        console.error(error);
    }
}

loadPosts();